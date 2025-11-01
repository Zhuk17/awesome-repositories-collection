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
    'zh-CN': 'Simplified Chinese (简体中文)',
    'es': 'Spanish (Español)'
}

# Маппинг языков для argostranslate (использует стандартные коды ISO)
ARGOS_LANGUAGE_MAP = {
    'en': 'en',
    'ru': 'ru',
    'zh-CN': 'zh',  # argostranslate использует 'zh' для китайского
    'es': 'es'
}

README_FILES = {
    'en': 'README.md',
    'ru': 'README.ru.md',
    'zh-CN': 'README.zh-CN.md',
    'es': 'README.es.md'
}

# Публичные LibreTranslate серверы (fallback)
LIBRETRANSLATE_SERVERS = [
    'https://translate.argosopentech.com',
    'https://libretranslate.de',
]

def install_argos_language_pair(from_code: str, to_code: str) -> bool:
    """Устанавливает языковую пару для argostranslate"""
    try:
        # Проверяем, не установлена ли уже пара
        installed_languages = argostranslate.translate.get_installed_languages()
        if any(lang.code == to_code for lang in installed_languages):
            print(f"   ✓ Языковая пара {from_code} → {to_code} уже установлена")
            return True
        
        print(f"   📦 Установка языковой пары: {from_code} → {to_code}")
        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        
        package_to_install = next(
            (pkg for pkg in available_packages 
             if pkg.from_code == from_code and pkg.to_code == to_code),
            None
        )
        
        if package_to_install:
            argostranslate.package.install_from_path(package_to_install.download())
            print(f"   ✅ Языковая пара {from_code} → {to_code} успешно установлена")
            return True
        else:
            print(f"   ⚠️  Языковая пара {from_code} → {to_code} не найдена в доступных пакетах")
            return False
    except Exception as e:
        print(f"   ⚠️  Ошибка установки {from_code} → {to_code}: {e}")
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
        'zh-CN': 'zh',
        'es': 'es'
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
    Использует устойчивые к переводу плейсхолдеры (только латиница и цифры)
    
    Returns:
        Tuple (protected_text, placeholders_dict)
    """
    placeholders = {}
    protected_text = text
    counter = 0
    
    # Используем UUID-подобные плейсхолдеры, которые точно не будут переведены
    # Формат: XA1234B, XC5678D и т.д. - переводчик не будет их переводить
    
    # Защищаем code blocks (самый приоритетный - они могут содержать всё)
    code_block_pattern = r'```[\s\S]*?```'
    matches = list(re.finditer(code_block_pattern, protected_text))
    for match in reversed(matches):  # Обратный порядок чтобы не сдвигались индексы
        placeholder = f"XA{str(counter).zfill(4)}B"
        placeholders[placeholder] = match.group(0)
        start, end = match.span()
        protected_text = protected_text[:start] + placeholder + protected_text[end:]
        counter += 1
    
    # Защищаем ссылки [text](url) - более специфичный паттерн
    link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    matches = list(re.finditer(link_pattern, protected_text))
    for match in reversed(matches):
        placeholder = f"XC{str(counter).zfill(4)}D"
        placeholders[placeholder] = match.group(0)
        start, end = match.span()
        protected_text = protected_text[:start] + placeholder + protected_text[end:]
        counter += 1
    
    # Защищаем inline code (но не внутри code blocks)
    inline_code_pattern = r'(?<!`)`([^`\n]+)`(?!`)'
    matches = list(re.finditer(inline_code_pattern, protected_text))
    for match in reversed(matches):
        placeholder = f"XE{str(counter).zfill(4)}F"
        placeholders[placeholder] = match.group(0)
        start, end = match.span()
        protected_text = protected_text[:start] + placeholder + protected_text[end:]
        counter += 1
    
    # Защищаем URLs (но не внутри ссылок или code blocks)
    url_pattern = r'(?<!\]\()https?://[^\s\)<>]+'
    matches = list(re.finditer(url_pattern, protected_text))
    for match in reversed(matches):
        placeholder = f"XG{str(counter).zfill(4)}H"
        placeholders[placeholder] = match.group(0)
        start, end = match.span()
        protected_text = protected_text[:start] + placeholder + protected_text[end:]
        counter += 1
    
    # Защищаем HTML теги и атрибуты
    html_pattern = r'<[^>]+>'
    matches = list(re.finditer(html_pattern, protected_text))
    for match in reversed(matches):
        placeholder = f"XI{str(counter).zfill(4)}J"
        placeholders[placeholder] = match.group(0)
        start, end = match.span()
        protected_text = protected_text[:start] + placeholder + protected_text[end:]
        counter += 1
    
    return protected_text, placeholders

def restore_technical_elements(translated_text: str, placeholders: dict[str, str]) -> str:
    """Восстанавливает технические элементы после перевода"""
    result = translated_text
    
    # Восстанавливаем в порядке убывания длины оригиналов
    # (чтобы более длинные не конфликтовали с короткими)
    sorted_placeholders = sorted(placeholders.items(), key=lambda x: -len(x[0]))
    
    for placeholder, original in sorted_placeholders:
        # Пытаемся найти точное совпадение
        if placeholder in result:
            result = result.replace(placeholder, original)
            continue
        
        # Извлекаем номер из плейсхолдера (например, XA1234B -> 1234)
        num_match = re.search(r'\d+', placeholder)
        if not num_match:
            continue
        
        placeholder_num = num_match.group()
        placeholder_prefix = placeholder[:2]  # XA, XC, XE и т.д.
        placeholder_suffix = placeholder[-1]   # B, D, F и т.д.
        
        # Пробуем различные варианты искажения
        patterns = [
            # Точное совпадение
            placeholder,
            # С пробелами: XA 1234 B, XA1234 B, XA 1234B
            f"{placeholder_prefix}\\s*{placeholder_num}\\s*{placeholder_suffix}",
            f"{placeholder_prefix}{placeholder_num}\\s+{placeholder_suffix}",
            f"{placeholder_prefix}\\s+{placeholder_num}{placeholder_suffix}",
            # Разделено: X A 1234 B
            f"{placeholder_prefix[0]}\\s*{placeholder_prefix[1]}\\s*{placeholder_num}\\s*{placeholder_suffix}",
            # Разные регистры
            placeholder.upper(),
            placeholder.lower(),
            # Без префикса/суффикса: 1234, A1234, 1234B
            placeholder_num,
            f"{placeholder_prefix[1]}{placeholder_num}",
            f"{placeholder_num}{placeholder_suffix}",
        ]
        
        found = False
        for pattern in patterns:
            # Ищем все совпадения
            matches = list(re.finditer(pattern, result, re.IGNORECASE))
            if matches:
                # Заменяем все совпадения на оригинал
                # Но только если это действительно наш плейсхолдер (проверяем номер)
                for match in reversed(matches):
                    matched_text = match.group()
                    # Проверяем, что в совпадении есть наш номер
                    if placeholder_num in matched_text:
                        start, end = match.span()
                        result = result[:start] + original + result[end:]
                        found = True
        
        if not found:
            # Последняя попытка - поиск по номеру с контекстом
            # Ищем паттерн где есть наш номер в правильном формате
            context_pattern = rf'\b{placeholder_prefix[0]}[A-Za-z]?\s*{placeholder_num}\s*[A-Za-z]?\b'
            matches = list(re.finditer(context_pattern, result))
            if matches and len(matches) <= len(placeholders):  # Не заменяем слишком много
                # Берем первое совпадение с таким номером
                match = matches[0]
                start, end = match.span()
                result = result[:start] + original + result[end:]
            else:
                print(f"   ⚠️  Не удалось восстановить плейсхолдер {placeholder} (оригинал: {original[:50]}...)")
    
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
        target_langs = ['ru', 'zh-CN', 'es']
    
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
    targets_str = os.getenv('TARGET_LANGS', 'ru,zh-CN,es')
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

