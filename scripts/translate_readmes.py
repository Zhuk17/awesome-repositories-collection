#!/usr/bin/env python3
"""
Автоматическая синхронизация переводов README файлов
Использует бесплатные переводчики: argostranslate (локальные модели) и LibreTranslate API
"""

import os
import sys
import re
import time
from pathlib import Path
from typing import Optional

# Пытаемся импортировать argostranslate (основной метод)
try:
    import argostranslate.package
    import argostranslate.translate
    ARGOS_AVAILABLE = True
except ImportError:
    ARGOS_AVAILABLE = False

# Fallback на requests для API методов
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

# Конфигурация языков
LANGUAGE_CODES = {
    'en': 'English',
    'ru': 'Russian (Русский)',
    'zh-CN': 'Simplified Chinese (简体中文)'
}

# Маппинг языков для argostranslate (использует стандартные коды ISO)
ARGOS_LANGUAGE_MAP = {
    'en': 'en',
    'ru': 'ru',
    'zh-CN': 'zh'  # argostranslate использует 'zh' для китайского
}

README_FILES = {
    'en': 'README.md',
    'ru': 'README.ru.md',
    'zh-CN': 'README.zh-CN.md'
}

# Публичные LibreTranslate серверы (fallback)
LIBRETRANSLATE_SERVERS = [
    'https://translate.argosopentech.com',
    'https://libretranslate.de',
]

def install_argos_language_pair(from_code: str, to_code: str) -> bool:
    """Устанавливает языковую пару для argostranslate"""
    try:
        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        
        package_to_install = next(
            (pkg for pkg in available_packages 
             if pkg.from_code == from_code and pkg.to_code == to_code),
            None
        )
        
        if package_to_install:
            print(f"   📦 Установка языковой пары: {from_code} → {to_code}")
            argostranslate.package.install_from_path(package_to_install.download())
            return True
        else:
            print(f"   ⚠️  Языковая пара {from_code} → {to_code} не найдена")
            return False
    except Exception as e:
        print(f"   ⚠️  Ошибка установки: {e}")
        return False

def translate_with_argos(text: str, target_lang: str, source_lang: str = 'en') -> Optional[str]:
    """Переводит текст с помощью argostranslate (локальные модели)"""
    if not ARGOS_AVAILABLE:
        return None
    
    try:
        from_code = ARGOS_LANGUAGE_MAP.get(source_lang, source_lang)
        to_code = ARGOS_LANGUAGE_MAP.get(target_lang, target_lang)
        
        # Защищаем технические элементы перед переводом
        protected_text, placeholders = protect_technical_elements(text)
        
        # Устанавливаем языковую пару если её нет
        try:
            translated = argostranslate.translate.translate(protected_text, from_code, to_code)
        except Exception:
            # Пытаемся установить языковую пару
            if install_argos_language_pair(from_code, to_code):
                translated = argostranslate.translate.translate(protected_text, from_code, to_code)
            else:
                return None
        
        # Восстанавливаем технические элементы
        result = restore_technical_elements(translated, placeholders)
        return result
    except Exception as e:
        print(f"   ⚠️  Ошибка argostranslate: {e}")
        return None

def translate_with_libretranslate(text: str, target_lang: str, source_lang: str = 'en') -> Optional[str]:
    """Переводит текст с помощью LibreTranslate API (fallback)"""
    if not REQUESTS_AVAILABLE:
        return None
    
    # Маппинг для LibreTranslate
    libretranslate_map = {
        'en': 'en',
        'ru': 'ru',
        'zh-CN': 'zh'
    }
    
    from_code = libretranslate_map.get(source_lang, source_lang)
    to_code = libretranslate_map.get(target_lang, target_lang)
    
    # Защищаем технические элементы перед переводом
    protected_text, placeholders = protect_technical_elements(text)
    
    for server in LIBRETRANSLATE_SERVERS:
        try:
            print(f"   🌐 Попытка через LibreTranslate: {server}")
            response = requests.post(
                f"{server}/translate",
                json={
                    "q": protected_text,
                    "source": from_code,
                    "target": to_code,
                    "format": "text"
                },
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                translated = result.get("translatedText", "")
                if translated:
                    # Восстанавливаем технические элементы
                    result_text = restore_technical_elements(translated, placeholders)
                    print(f"   ✅ Перевод получен через LibreTranslate")
                    return result_text
            else:
                print(f"   ⚠️  Сервер {server} вернул код {response.status_code}")
        except Exception as e:
            print(f"   ⚠️  Ошибка {server}: {e}")
            continue
    
    return None

def protect_technical_elements(text: str):
    """
    Защищает технические элементы от перевода, заменяя их плейсхолдерами
    
    Returns:
        Tuple (protected_text, placeholders_dict)
    """
    placeholders = {}
    protected_text = text
    counter = 0
    
    # Защищаем code blocks (самый приоритетный - они могут содержать всё)
    code_block_pattern = r'```[\s\S]*?```'
    for match in re.finditer(code_block_pattern, protected_text):
        placeholder = f"__CODEBLOCK_{counter}__"
        placeholders[placeholder] = match.group(0)
        protected_text = protected_text.replace(match.group(0), placeholder, 1)
        counter += 1
    
    # Защищаем ссылки [text](url)
    link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    for match in re.finditer(link_pattern, protected_text):
        placeholder = f"__LINK_{counter}__"
        placeholders[placeholder] = match.group(0)
        protected_text = protected_text.replace(match.group(0), placeholder, 1)
        counter += 1
    
    # Защищаем inline code
    inline_code_pattern = r'`[^`\n]+`'
    for match in re.finditer(inline_code_pattern, protected_text):
        placeholder = f"__INLINECODE_{counter}__"
        placeholders[placeholder] = match.group(0)
        protected_text = protected_text.replace(match.group(0), placeholder, 1)
        counter += 1
    
    # Защищаем URLs
    url_pattern = r'https?://[^\s\)]+'
    for match in re.finditer(url_pattern, protected_text):
        placeholder = f"__URL_{counter}__"
        placeholders[placeholder] = match.group(0)
        protected_text = protected_text.replace(match.group(0), placeholder, 1)
        counter += 1
    
    return protected_text, placeholders

def restore_technical_elements(translated_text: str, placeholders: dict[str, str]) -> str:
    """Восстанавливает технические элементы после перевода"""
    result = translated_text
    # Восстанавливаем в обратном порядке приоритета
    for placeholder, original in placeholders.items():
        result = result.replace(placeholder, original)
    return result

def translate_text(text: str, target_language: str, source_language: str = 'en') -> Optional[str]:
    """
    Переводит текст используя бесплатные переводчики
    Пробует argostranslate -> LibreTranslate API
    
    Args:
        text: Исходный текст для перевода
        target_language: Целевой язык (en, ru, zh-CN)
        source_language: Исходный язык (по умолчанию en)
    
    Returns:
        Переведенный текст или None в случае ошибки
    """
    print(f"   🔄 Начало перевода...")
    
    # Метод 1: argostranslate (локальные модели, самый быстрый)
    if ARGOS_AVAILABLE:
        print(f"   📚 Попытка перевода через argostranslate...")
        translated = translate_with_argos(text, target_language, source_language)
        if translated:
            print(f"   ✅ Перевод получен через argostranslate ({len(translated)} символов)")
            return translated
    
    # Метод 2: LibreTranslate API (fallback)
    if REQUESTS_AVAILABLE:
        print(f"   🌐 Попытка перевода через LibreTranslate API...")
        translated = translate_with_libretranslate(text, target_language, source_language)
        if translated:
            print(f"   ✅ Перевод получен через LibreTranslate ({len(translated)} символов)")
            return translated
    
    print(f"   ❌ Все методы перевода не удались")
    return None

def sync_translations(source_lang='en', target_langs=None):
    """
    Синхронизирует переводы README файлов
    
    Args:
        source_lang: Исходный язык (по умолчанию en)
        target_langs: Список целевых языков (по умолчанию ['ru', 'zh-CN'])
    
    Returns:
        True если успешно, False в случае ошибки
    """
    if target_langs is None:
        target_langs = ['ru', 'zh-CN']
    
    # Определяем корневую директорию репозитория
    repo_root = Path(__file__).parent.parent
    source_file = repo_root / README_FILES[source_lang]
    
    if not source_file.exists():
        print(f"❌ Ошибка: Файл {source_file} не найден")
        return False
    
    print(f"\n📖 Читаем исходный файл: {source_file}")
    with open(source_file, 'r', encoding='utf-8') as f:
        source_text = f.read()
    
    print(f"   Размер: {len(source_text)} символов")
    
    success_count = 0
    
    for target_lang in target_langs:
        if target_lang == source_lang:
            print(f"\n⏭️  Пропуск {target_lang} (совпадает с исходным языком)")
            continue
        
        target_file = repo_root / README_FILES[target_lang]
        
        print(f"\n🌍 Перевод на {LANGUAGE_CODES[target_lang]}...")
        print(f"   Целевой файл: {target_file}")
        
        translated = translate_text(source_text, target_lang, source_lang)
        
        if translated:
            print(f"   💾 Сохранение перевода...")
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(translated)
            print(f"   ✅ Успешно создан {target_file}")
            success_count += 1
        else:
            print(f"   ❌ Ошибка перевода для {target_lang}")
    
    print(f"\n{'='*60}")
    print(f"📊 Результаты: {success_count}/{len(target_langs)} переводов выполнено")
    
    return success_count > 0

if __name__ == '__main__':
    print("="*60)
    print("🌍 Система автоматического перевода README")
    print("="*60)
    
    # Определяем параметры из переменных окружения
    source = os.getenv('SOURCE_LANG', 'en')
    targets_str = os.getenv('TARGET_LANGS', 'ru,zh-CN')
    targets = [t.strip() for t in targets_str.split(',') if t.strip()]
    
    print(f"\n📋 Конфигурация:")
    print(f"   Исходный язык: {LANGUAGE_CODES.get(source, source)}")
    print(f"   Целевые языки: {', '.join([LANGUAGE_CODES.get(t, t) for t in targets])}")
    
    # Проверка доступности переводчиков
    if not ARGOS_AVAILABLE and not REQUESTS_AVAILABLE:
        print("\n❌ КРИТИЧЕСКАЯ ОШИБКА: Нет доступных методов перевода!")
        print("   Установите зависимости:")
        print("   pip install argostranslate requests")
        sys.exit(1)
    
    # Информируем о доступных методах
    methods = []
    if ARGOS_AVAILABLE:
        methods.append("argostranslate (локальные модели)")
    if REQUESTS_AVAILABLE:
        methods.append("LibreTranslate API (публичные серверы)")
    print(f"\n🔧 Доступные методы перевода: {', '.join(methods)}")
    
    # Запуск синхронизации
    success = sync_translations(source, targets)
    
    if success:
        print("\n✨ Все переводы успешно завершены!")
        sys.exit(0)
    else:
        print("\n❌ Произошли ошибки при переводе")
        sys.exit(1)

