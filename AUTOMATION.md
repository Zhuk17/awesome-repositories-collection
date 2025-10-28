# Автоматизация переводов / Translation Automation

## Обзор / Overview

Этот репозиторий включает автоматическую систему синхронизации переводов README файлов на несколько языков (английский, русский, китайский). Система работает через GitHub Actions и использует AI для машинного перевода.

This repository includes an automated translation synchronization system for README files across multiple languages (English, Russian, Chinese). The system works via GitHub Actions and uses AI for machine translation.

## Архитектура / Architecture

### Компоненты / Components

1. **GitHub Actions Workflow** (`.github/workflows/auto-translate-readmes.yml`)
   - Автоматически запускается при изменении README файлов
   - Может быть запущен вручную через workflow_dispatch
   - Включает встроенный Python скрипт для перевода

2. **Python Translation Script** (встроенный в workflow / embedded in workflow)
   - Использует OpenAI API или Anthropic API
   - Сохраняет markdown форматирование
   - Не переводит технические термины, ссылки и теги

## Настройка / Setup

### 1. Добавление API ключей / Adding API Keys

Добавьте секреты в настройках репозитория:

Add secrets in repository settings:

```
Settings → Secrets and variables → Actions → New repository secret
```

**Необходимые секреты / Required secrets:**

- `OPENAI_API_KEY` - ключ OpenAI API (для GPT-4)
- `ANTHROPIC_API_KEY` - ключ Anthropic API (опционально, для Claude)

### 2. Настройка разрешений / Setting Permissions

Убедитесь, что GitHub Actions имеет права на запись:

Ensure GitHub Actions has write permissions:

```
Settings → Actions → General → Workflow permissions → Read and write permissions
```

## Использование / Usage

### Автоматический запуск / Automatic Trigger

Workflow автоматически запускается при:

The workflow automatically triggers when:

- Изменении любого из следующих файлов / Changes to any of these files:
  - `README.md`
  - `README.ru.md`
  - `README.zh-CN.md`
  - `ci_cd/README.md`
  - `telegram/README.md`
  - `video_utils/README.md`

### Ручной запуск / Manual Trigger

Для ручного запуска перевода:

To manually trigger translation:

1. Перейдите в **Actions** → **Auto-Translate READMEs**
2. Нажмите **Run workflow**
3. Выберите параметры:
   - **Source language**: исходный язык (en/ru/zh-CN)
   - **Target languages**: целевые языки через запятую (en,ru,zh-CN)
4. Нажмите **Run workflow**

## Локальное использование / Local Usage

Для локального запуска перевода:

To run translation locally:

### 1. Установка зависимостей / Install dependencies

```bash
pip install openai anthropic requests python-dotenv pyyaml
```

### 2. Создание .env файла / Create .env file

```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

### 3. Извлечение скрипта / Extract the script

Скрипт встроен в workflow файл. Для извлечения:

The script is embedded in the workflow file. To extract:

```bash
# Создать директорию для скриптов
mkdir -p scripts

# Скопировать Python код из секции workflow (между EOF маркерами)
# Copy the Python code from the workflow section (between EOF markers)
```

Или создайте `scripts/translate_readmes.py` вручную с содержимым из workflow файла.

Or create `scripts/translate_readmes.py` manually with content from the workflow file.

### 4. Запуск / Run

```bash
# Перевести с английского на русский и китайский
# Translate from English to Russian and Chinese
export SOURCE_LANG=en
export TARGET_LANGS=ru,zh-CN
python scripts/translate_readmes.py

# Или указать другой исходный язык
# Or specify different source language
export SOURCE_LANG=ru
export TARGET_LANGS=en,zh-CN
python scripts/translate_readmes.py
```

## Конфигурация / Configuration

### Добавление новых языков / Adding New Languages

Для добавления поддержки нового языка:

To add support for a new language:

1. Обновите `LANGUAGE_CODES` в Python скрипте
2. Добавьте соответствие в `README_FILES`
3. Обновите `workflow_dispatch.inputs.source_language.options` в workflow

### Модель перевода / Translation Model

По умолчанию используется `gpt-4-turbo-preview`. Для изменения модели отредактируйте параметр `model` в функции `translate_text()`.

By default, `gpt-4-turbo-preview` is used. To change the model, edit the `model` parameter in the `translate_text()` function.

## Правила перевода / Translation Rules

Скрипт следует следующим правилам:

The script follows these rules:

### Не переводится / Not Translated:
- URLs и ссылки / URLs and links
- Имена репозиториев GitHub / GitHub repository names
- Блоки кода и технические команды / Code blocks and technical commands
- Пути к файлам / File paths and filenames
- Теги (например, `*Tags: Python, AI, Docker*`)

### Переводится / Translated:
- Текстовые описания / Text descriptions
- Заголовки и названия / Headers and titles
- Обычные параграфы / Regular paragraphs

## Устранение неполадок / Troubleshooting

### Workflow не запускается / Workflow doesn't trigger

1. Проверьте разрешения Actions / Check Actions permissions
2. Убедитесь, что изменения коммитятся в `main` ветку / Ensure changes are committed to `main` branch
3. Проверьте пути в `on.push.paths` / Check paths in `on.push.paths`

### Ошибки API / API Errors

1. Проверьте наличие API ключей в секретах / Check API keys in secrets
2. Убедитесь, что ключи активны и имеют квоту / Ensure keys are active and have quota
3. Проверьте логи workflow для деталей / Check workflow logs for details

### Неправильный перевод / Incorrect Translation

1. Проверьте prompt в функции `translate_text()` / Check prompt in `translate_text()` function
2. Настройте параметр `temperature` (ниже = более детерминированно) / Adjust `temperature` parameter (lower = more deterministic)
3. Попробуйте другую модель / Try a different model

## Примеры / Examples

### Пример 1: Обновление основного README

Example 1: Updating main README

```bash
# Редактируем README.md на английском
# Edit README.md in English
vim README.md

# Коммитим изменения
# Commit changes
git add README.md
git commit -m "Update README with new features"
git push origin main

# Workflow автоматически создаст переводы
# Workflow will automatically create translations
```

### Пример 2: Ручной перевод с русского

Example 2: Manual translation from Russian

```bash
# Редактируем README.ru.md
# Edit README.ru.md
vim README.ru.md
git add README.ru.md
git commit -m "Обновление русской версии"
git push origin main

# В GitHub Actions:
# In GitHub Actions:
# Actions → Auto-Translate READMEs → Run workflow
# Source language: ru
# Target languages: en,zh-CN
```

## Лучшие практики / Best Practices

1. **Редактируйте один исходный файл** / **Edit one source file**
   - Выберите основной язык (обычно английский)
   - Дайте автоматизации создавать другие версии

2. **Проверяйте переводы** / **Review translations**
   - AI переводы могут требовать корректировки
   - Проверьте технические термины

3. **Используйте workflow_dispatch** / **Use workflow_dispatch**
   - Для явного контроля над процессом перевода
   - Когда нужно перевести с нестандартного языка

4. **Мониторьте квоты API** / **Monitor API quotas**
   - Следите за использованием OpenAI API
   - Настройте уведомления о лимитах

## Дополнительные ресурсы / Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Markdown Guide](https://www.markdownguide.org/)

## Поддержка / Support

Для вопросов и проблем:

For questions and issues:

- Создайте issue в репозитории / Create an issue in the repository
- Проверьте логи GitHub Actions / Check GitHub Actions logs
- Обратитесь к документации API / Refer to API documentation
