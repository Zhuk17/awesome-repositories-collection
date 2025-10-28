# Коллекция полезных репозиториев ⚡
> Тщательно подобранный список полезных инструментов разработки и утилит
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Языки / Languages / 语言
- [English](README.md)
- [Русский](README.ru.md)
- [简体中文](README.zh-CN.md)

---

## Содержание
- [Навигация по файлам](#навигация-по-файлам)
- [Поиск и замена](#поиск-и-замена)
- [Системный мониторинг](#системный-мониторинг)
- [Сеть](#сеть)
- [Инструменты разработки](#инструменты-разработки)
  - [Git](#git)
  - [Редакторы кода](#редакторы-кода)
  - [Отладка](#отладка)
  - [Производительность](#производительность)
- [Docker / Cloud / Storage](#docker--cloud--storage)
- [IDE / Cloud / Automation](#ide--cloud--automation)
- [Education](#education)
- [Security / OSINT](#security--osint)
- [Другие полезные коллекции](#другие-полезные-коллекции)
- [Папка тезисов (theses)](#папка-тезисов-theses)
- [Как внести вклад](#как-внести-вклад)

> Примечание по автогенерации: описания в локализованных README могут частично генерироваться автоматически на основе англоязычной версии. Пожалуйста, сообщайте об ошибках перевода в Issues.

---

## Навигация по файлам
- **[fzf](https://github.com/junegunn/fzf)** — нечеткий поиск для командной строки.
- **[fd](https://github.com/sharkdp/fd)** — простая, быстрая и удобная альтернатива команде `find`.
- **[exa](https://github.com/ogham/exa)** — современная замена `ls` с улучшенными возможностями.
- **[bat](https://github.com/sharkdp/bat)** — клон `cat` с подсветкой синтаксиса и интеграцией с git.

## Поиск и замена
- **[ripgrep](https://github.com/BurntSushi/ripgrep)** — сверхбыстрый поиск текста по файлам.
- **[ag](https://github.com/ggreer/the_silver_searcher)** — The Silver Searcher, быстрая утилита поиска по коду.
- **[sd](https://github.com/chmln/sd)** — интуитивный инструмент поиска и замены.

## Системный мониторинг
- **[htop](https://github.com/htop-dev/htop)** — интерактивный просмотрщик процессов.
- **[glances](https://github.com/nicolargo/glances)** — кросс‑платформенный инструмент мониторинга системы.
- **[bottom](https://github.com/ClementTsang/bottom)** — графический монитор процессов и системы в терминале.
- **[ncdu](https://dev.yorhel.nl/ncdu)** — анализатор использования дискового пространства.

## Сеть
- **[httpie](https://github.com/httpie/httpie)** — удобный HTTP‑клиент для тестирования API.
- **[curlie](https://github.com/rs/curlie)** — curl с улучшенным интерфейсом httpie.
- **[dog](https://github.com/ogham/dog)** — современная альтернатива DNS‑клиенту dig.
- **[mitmproxy](https://github.com/mitmproxy/mitmproxy)** — интерактивный HTTPS‑прокси для отладки трафика.

## Инструменты разработки
### Git
- **[lazygit](https://github.com/jesseduffield/lazygit)** — TUI‑клиент для git с быстрыми операциями.
- **[git-extras](https://github.com/tj/git-extras)** — набор полезных команд поверх git.

### Редакторы кода
- **[Helix](https://github.com/helix-editor/helix)** — модальный редактор с LSP из коробки.
- **[Neovim](https://github.com/neovim/neovim)** — современный Vim с расширяемой архитектурой.

### Отладка
- **[dlv](https://github.com/go-delve/delve)** — отладчик для Go.
- **[lldb](https://github.com/llvm/llvm-project)** — мощный отладчик из экосистемы LLVM.

### Производительность
- **[hyperfine](https://github.com/sharkdp/hyperfine)** — бенчмаркинг CLI‑команд.
- **[flamegraph](https://github.com/brendangregg/FlameGraph)** — построение flame‑графов профилирования.

## Docker / Cloud / Storage
- **[docker-compose](https://github.com/docker/compose)** — оркестрация многоконтейнерных приложений Docker.
- **[lazydocker](https://github.com/jesseduffield/lazydocker)** — TUI для управления Docker и Docker Compose.
- **[kubectl‑ns/kubectl‑ctx](https://github.com/ahmetb/kubectx)** — быстрые переключатели контекстов и пространств имён Kubernetes.
- **[k9s](https://github.com/derailed/k9s)** — TUI‑интерфейс для кластеров Kubernetes.
- **[Rclone](https://github.com/rclone/rclone)** — синхронизация и бэкапы в облачные хранилища.
- **[minio](https://github.com/minio/minio)** — S3‑совместимое объектное хранилище с открытым кодом.

Пример добавления:
```markdown
- **[lazydocker](https://github.com/jesseduffield/lazydocker)** — TUI для Docker/Compose: просмотр контейнеров, логов, перезапуск, инспект в один клик.
```

## IDE / Cloud / Automation
- **[Cursor](https://github.com/getcursor/cursor)** — IDE с интеграцией ИИ‑ассистентов.
- **[OpenVSX/VS Code](https://github.com/microsoft/vscode)** — расширяемая IDE с экосистемой расширений.
- **[DevPod](https://github.com/loft-sh/devpod)** — dev‑окружения в контейнерах/клауде по шаблонам.
- **[Taskfile](https://github.com/go-task/task)** — удобный таск‑раннер на YAML.
- **[Just](https://github.com/casey/just)** — рецепты команд как Make, но проще.

Пример описания:
```markdown
- **[Taskfile](https://github.com/go-task/task)** — декларативные задачи: кроссплатформенность, переменные, включения, параллельный запуск.
```

## Education
- **[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp)** — интерактивные курсы по веб‑разработке.
- **[OSSU CS](https://github.com/ossu/computer-science)** — программа CS с открытыми курсами.
- **[System Design Primer](https://github.com/donnemartin/system-design-primer)** — база по системному дизайну.
- **[Missing Semester](https://github.com/missing-semester/missing-semester)** — практические инструменты и навыки для разработчиков.

Пример добавления курса:
```markdown
- **[OSSU CS](https://github.com/ossu/computer-science)** — дорожная карта CS: математика, алгоритмы, ОС, сети, проекты.
```

## Security / OSINT
- **[awesome-security](https://github.com/sbilly/awesome-security)** — обзор инструментов и ресурсов по безопасности.
- **[OSINT Framework](https://github.com/lockfale/osint-framework)** — каталог источников разведданных из открытых источников.
- **[Trivy](https://github.com/aquasecurity/trivy)** — сканер уязвимостей контейнеров/образов/IaC.
- **[gitleaks](https://github.com/gitleaks/gitleaks)** — поиск секретов в репозиториях.

Пример описания инструмента:
```markdown
- **[Trivy](https://github.com/aquasecurity/trivy)** — сканирование образов, файловых систем и репозиториев; отчёты в форматах SARIF/JSON.
```

## Другие полезные коллекции
- **[awesome](https://github.com/sindresorhus/awesome)** — главная коллекция «awesome‑списков».
- **[awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted)** — приложения для самостоятельного хостинга.
- **[awesome-CLI](https://github.com/agarrharr/awesome-cli-apps)** — подборка CLI‑утилит.

---

## Папка тезисов (theses)
Вместо раздела в README существует отдельная папка `theses/` с краткими тезисами по темам и репозиториям (конспекты, заметки, сравнения). В конце основного текста размещается ссылка на папку тезисов:

- Папка: [`theses/`](./theses/)
- Пример файла тезисов: `theses/docker-basics.md`

Формат тезисов:
```markdown
# Тема
- Короткие пункты по сути
- Ссылки на исходные репозитории
- Мини‑сравнения и best practices
```

---

## Как внести вклад
- Добавляйте новые репозитории через PR, придерживаясь формата: `- **[name](url)** — краткое русское описание.`
- Для новых категорий сначала создайте раздел в обоих README (EN/RU), затем добавьте элементы.
- При переводе ориентируйтесь на английскую версию. Разрешена умеренная автогенерация описаний, но обязательно проверяйте смысл и корректность ссылок.
- Примеры см. в разделах: добавления для Docker/Cloud/Storage, IDE/Cloud/Automation, Education, Security/OSINT.
