# 🚀 Awesome Repositories Collection ⚡

<p align="center">
  <a href="README.md">🇬🇧 English</a> •
  <a href="README.ru.md">🇷🇺 Русский</a> •
  <a href="README.zh-CN.md">🇨🇳 简体中文</a>
</p>

<p align="center">
  <img src="https://awesome.re/badge.svg" alt="Awesome">
  <img src="https://img.shields.io/github/license/cheesewhe/awesome-repositories-collection" alt="License">
  <img src="https://img.shields.io/github/stars/cheesewhe/awesome-repositories-collection" alt="Stars">
</p>

---

## 📖 Overview

> A carefully curated multilingual collection of essential tools, utilities, and technical resources for developers, system administrators, and researchers.

This repository brings together battle-tested open-source projects spanning **development tools**, **AI/ML**, **system monitoring**, **security**, **containerization**, and **automation**. Each tool is selected based on active maintenance, clear documentation, and real-world applicability.

### 📊 Repository Statistics

- **275+** curated tools and resources
- **19** main categories
- **3** language translations (English, Russian, Chinese)
- **100%** open-source tools

---

[⬆ Back to Top](#-awesome-repositories-collection-)

## 📋 Table of Contents

- [File Navigation](#-file-navigation)
- [Search & Replace](#-search--replace)
- [System Monitoring](#-system-monitoring)
- [Networking](#-networking)
- [Development Tools](#-development-tools)
  - [Git Tools](#git-tools)
  - [Code Editors](#code-editors)
  - [Debugging](#debugging)
  - [Performance](#performance)
- [Docker & Cloud](#-docker--cloud)
  - [Databases](#databases)
  - [Web Development](#web-development)
- [IDE & Automation](#-ide--automation)
  - [Business & Enterprise](#business--enterprise)
- [AI & Machine Learning](#-ai--machine-learning)
- [CI/CD](#-cicd)
- [Video Processing](#-video-processing)
- [3D Vision & Scanning](#-3d-vision--scanning)
- [Industrial Automation & SCADA](#-industrial-automation--scada)
- [CAD & BIM Design](#-cad--bim-design)
- [Security & OSINT](#-security--osint)
- [Education](#-education)
- [Geographic Information Systems](#geographic-information-systems)
- [Other Collections](#-other-awesome-collections)
- [Research & Theses](#-research--theses)
- [Project Ideas](#project-ideas-collection)
- [Contributing](#-contributing)

---

## 📂 File Navigation

Essential tools for exploring and navigating your filesystem efficiently.

- **[fzf](https://github.com/junegunn/fzf)** — Command-line fuzzy finder with interactive interface. Integrates seamlessly with shell history, file search, and vim/neovim for lightning-fast navigation.
- **[fd](https://github.com/sharkdp/fd)** — Simple, fast, and user-friendly alternative to `find`. Supports parallel execution, ignore patterns, and smart case sensitivity.
- **[exa](https://github.com/ogham/exa)** — Modern replacement for `ls` with git integration, tree view, and color-coded file types for enhanced readability.
- **[bat](https://github.com/sharkdp/bat)** — Cat clone with syntax highlighting, git integration, and automatic paging. Perfect for quickly viewing code files in the terminal.
- **[lsd](https://github.com/lsd-rs/lsd)** — Next-generation `ls` command with icons, colors, and tree view. Written in Rust for blazing performance.
- **[ranger](https://github.com/ranger/ranger)** — Vi-inspired file manager with three-column layout, file previews, and extensive customization options.
- **[qView](https://github.com/jurplel/qView)** — Minimalist and fast image viewer for desktop. Lightweight with keyboard navigation, supports all major image formats.
- **[cloudcmd](https://github.com/coderaiser/cloudcmd)** — Web-based file manager with integrated console and editor. Access and manage files remotely through a browser interface.
- **[Flameshot](https://github.com/flameshot-org/flameshot)** — Powerful screenshot tool with annotation capabilities. Capture, annotate, and share screenshots with built-in image editor.
- **[CopyQ](https://github.com/hluk/CopyQ)** — Advanced clipboard manager with searchable history. Store and organize clipboard entries with tags, notes, and scripting support.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 🔍 Search & Replace

Powerful tools for searching through codebases and performing bulk text operations.

- **[ripgrep](https://github.com/BurntSushi/ripgrep)** — Ultra-fast recursive search tool that respects .gitignore by default. Outperforms grep, ag, and other alternatives on large codebases.
- **[ag (The Silver Searcher)](https://github.com/ggreer/the_silver_searcher)** — Code-searching tool optimized for developers. Faster than ack, with smart defaults for ignoring VCS directories.
- **[sd](https://github.com/chmln/sd)** — Intuitive find-and-replace CLI tool with regex support. Safer and more ergonomic than `sed` for everyday use.
- **[ast-grep](https://github.com/ast-grep/ast-grep)** — Structural code search and refactoring tool. Search code by AST patterns instead of regex for more precise results.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 📊 System Monitoring

Track system resources, processes, and performance metrics in real-time.

- **[htop](https://github.com/htop-dev/htop)** — Interactive process viewer for Unix systems. Color-coded display with mouse support and customizable columns.
- **[btop](https://github.com/aristocratos/btop)** — Resource monitor with beautiful UI showing CPU, memory, disk, network, and process information. Modern C++ implementation with themes.
- **[glances](https://github.com/nicolargo/glances)** — Cross-platform monitoring tool written in Python. Exports data to various formats and supports client-server mode.
- **[ncdu](https://dev.yorhel.nl/ncdu)** — NCurses-based disk usage analyzer. Quickly find what's consuming disk space with an intuitive interface.
- **[bottom](https://github.com/ClementTsang/bottom)** — Graphical process/system monitor inspired by gtop and gotop. Customizable widgets with cross-platform support.
- **[ctop](https://github.com/bcicen/ctop)** — Top-like interface for container metrics. Monitor Docker containers in real-time with resource usage stats.
- **[Performa](https://github.com/jhuckaby/Performa)** — Server monitoring with custom metrics. Real-time performance tracking with configurable alerts and dashboards.
- **[resources](https://github.com/nokyan/resources)** — System resource monitor for CPU, GPU, and NPU. Lightweight tool showing detailed hardware utilization.
- **[Umami](https://github.com/umami-software/umami)** — Privacy-focused web analytics. Self-hosted alternative to Google Analytics with GDPR compliance.
- **[Healthchecks](https://github.com/healthchecks/healthchecks)** — Cron job monitoring service. Get alerts when scheduled tasks fail or don't run on time.
- **[coroot](https://github.com/coroot/coroot)** — Infrastructure monitoring and APM analysis. Identify performance bottlenecks and optimize application delivery.
- **[Grafana Loki](https://github.com/grafana/loki)** — Log aggregation system inspired by Prometheus. Highly efficient log storage and querying with Grafana integration for centralized logging.
- **[PowerToys](https://github.com/microsoft/PowerToys)** — Windows utilities for power users. Collection of tools to extend Windows functionality with shortcuts, color picker, and more.
- **[starship](https://github.com/starship/starship)** — Minimalist cross-shell prompt. Fast and customizable prompt for any shell with git status, jobs, and directory info.
- **[Quick Look](https://github.com/QL-Win/QuickLook)** — Instant file preview for Windows. Press spacebar to preview files without opening applications.

### Geographic Information Systems

Tools for geospatial data analysis and mapping.

- **[QGIS](https://www.qgis.org/)** — Geographic Information System. Professional GIS software for geospatial data analysis, cartography, and spatial data management.
- **[Lychee Slicer](https://github.com/LycheeSlicer/LycheeSlicer)** — 3D printing slicer software. Prepare 3D models for printing with advanced slicing algorithms.
- **[Gisia](https://github.com/gisia-io/gisia)** — Self-hosted DevOps platform with CI/CD and infrastructure monitoring. Complete DevOps solution in one platform.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 🌐 Networking

Tools for testing APIs, debugging network traffic, and managing connections.

- **[httpie](https://github.com/httpie/cli)** — User-friendly HTTP client for testing APIs. Expressive syntax with syntax highlighting and JSON support out of the box.
- **[curlie](https://github.com/rs/curlie)** — Modern curl with httpie-like interface. Combines curl's power with httpie's user-friendly syntax.
- **[dog](https://github.com/ogham/dog)** — Modern DNS client with colored output and support for DNS-over-HTTPS. Better alternative to `dig` with clearer output.
- **[mitmproxy](https://github.com/mitmproxy/mitmproxy)** — Interactive HTTPS proxy for penetration testers and developers. Inspect, modify, and replay HTTP/HTTPS traffic.
- **[ngrok](https://github.com/inconshreveable/ngrok)** — Reverse proxy for creating secure tunnels to localhost. Essential for webhook testing and exposing local services.
- **[bandwhich](https://github.com/imsnif/bandwhich)** — Terminal bandwidth utilization tool. Shows current network usage by process, connection, and remote IP.
- **[graftcp](https://github.com/hmgle/graftcp)** — Transparent TCP proxy for any application. Redirect TCP connections without modifying application code or configuration.
- **[easy-postman](https://github.com/lakernote/easy-postman)** — Load testing and integration testing tool for APIs. Simplified alternative to Postman with automated testing capabilities.
- **[share](https://github.com/schollz/share)** — End-to-end encrypted file transfer via web or CLI. Secure peer-to-peer file sharing without intermediary servers.
- **[FileZilla](https://filezilla-project.org/)** — Lightweight FTP client for file transfers. Upload files to servers and edit code directly on remote servers.
- **[RustDesk](https://github.com/rustdesk/rustdesk)** — Open-source remote desktop software. Self-hosted alternative to AnyDesk for remote access and support.
- **[LocalSend](https://github.com/localsend/localsend)** — Secure file sharing over local network. Encrypted file transfer between devices without cloud or internet.
- **[Bruno](https://github.com/usebruno/bruno)** — API client for testing REST, GraphQL, and SOAP APIs. Lightweight alternative to Postman and Insomnia with offline-first architecture.
- **[NETworkManager](https://github.com/BornToBeRoot/NETworkManager)** — Network toolkit with WiFi analyzer, port scanner, and RDP/SSH management. Professional network administration tool for Windows.
- **[Mirotalk](https://github.com/mirotalk/mirotalk)** — P2P video conferencing via WebRTC. Simple and fast alternative to Zoom and Google Meet with peer-to-peer connections.
- **[Chatwoot](https://github.com/chatwoot/chatwoot)** — Open-source customer engagement platform. Unified inbox for all customer conversations across multiple channels.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 🛠️ Development Tools

### Git Tools

Version control utilities that enhance your Git workflow.

- **[lazygit](https://github.com/jesseduffield/lazygit)** — Simple terminal UI for git commands. Stage hunks, manage branches, and resolve conflicts with keyboard-driven interface.
- **[tig](https://github.com/jonas/tig)** — Text-mode interface for Git. Browse repository history, blame view, and tree navigation in the terminal.
- **[git-extras](https://github.com/tj/git-extras)** — Collection of useful git utilities including summary, effort, changelog, and more.
- **[gh](https://github.com/cli/cli)** — GitHub's official command-line tool. Create issues, pull requests, and manage repositories without leaving the terminal.
- **[glab](https://github.com/profclems/glab)** — GitLab CLI tool for managing issues, merge requests, and pipelines directly from the command line.
- **[delta](https://github.com/dandavison/delta)** — Syntax-highlighting pager for git, diff, and grep output. Makes code review more pleasant with side-by-side diffs.

### Code Editors

Modern text editors optimized for productivity and extensibility.

- **[Neovim](https://github.com/neovim/neovim)** — Hyperextensible Vim-based text editor. Built-in LSP support, Lua configuration, and modern plugin ecosystem.
- **[Helix](https://github.com/helix-editor/helix)** — Post-modern text editor with built-in LSP, tree-sitter, and multiple selections. No configuration needed out of the box.
- **[micro](https://github.com/zyedidia/micro)** — Modern and intuitive terminal-based text editor. Supports mouse input and common keybindings (Ctrl+C, Ctrl+V).
- **[amp](https://github.com/jmacdonald/amp)** — Vi-inspired text editor written in Rust. Minimal design with extensible plugin system.
- **[ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium)** — Chromium browser without Google integration. Enhanced privacy and security with removed Google services and telemetry.
- **[librewolf](https://librewolf.net/)** - A privacy-focused fork of Firefox, pre-configured to disable telemetry, tracking, and fingerprinting while improving security and user control.
- **[Notepad++](https://notepad-plus-plus.org/)** — Feature-rich code and text editor for Windows. Supports all programming languages with syntax highlighting and plugins.
- **[GIMP](https://www.gimp.org/)** — Free and open-source image editor. Professional alternative to Photoshop for photo editing, logo creation, and graphic design.
- **[Inkscape](https://inkscape.org/)** — Professional vector graphics editor. Create scalable logos, illustrations, and print materials with precision.
- **[Scribus](https://www.scribus.net/)** — Desktop publishing software for layout and print preparation. Create magazines, brochures, and product packaging.

### Debugging

Tools for diagnosing and fixing issues in your applications.

- **[gdb](https://www.sourceware.org/gdb/)** — GNU Debugger for C, C++, and other languages. Industry-standard debugger with powerful scripting capabilities.
- **[lldb](https://lldb.llvm.org/)** — Next-generation debugger from LLVM project. Excellent for debugging C, C++, Objective-C, and Swift.
- **[delve](https://github.com/go-delve/delve)** — Debugger for the Go programming language. Supports goroutines, channels, and Go-specific debugging features.
- **[pdb++](https://github.com/pdbpp/pdbpp)** — Enhanced Python debugger with syntax highlighting, tab completion, and better introspection.
- **[fastcrud](https://github.com/benavlabs/fastcrud)** — Async CRUD operations for FastAPI with automatic JOINs. Simplified database operations with automatic relationship handling.
- **[bkhtmltopdf](https://github.com/bkhtmltopdf/bkhtmltopdf)** — Fast HTML to PDF converter. High-performance tool for generating PDF documents from HTML content.
- **[dnote](https://github.com/dnote/dnote)** — Terminal-based notebook on SQLite. Simple note-taking system with command-line interface and local storage.
- **[Cronboard](https://github.com/cronboard-io/cronboard)** — Text-based cron job management dashboard. Monitor and manage scheduled tasks from a simple interface.
- **[Parm](https://github.com/parm-pm/parm)** — Cross-platform package manager pulling releases directly from GitHub. Simple dependency management for open-source projects.
- **[dotbins](https://github.com/basnijholt/dotbins)** — CLI binary manager through dotfiles. Manage and version control command-line tools in your dotfiles repository.
- **[ito](https://github.com/heyito/ito)** — Voice dictation for any application. Universal voice input tool that works across different programs and platforms.
- **[Graphite](https://github.com/GraphiteEditor/Graphite)** — Professional-grade raster and vector graphics editor. Modern design tool with infinite canvas and powerful editing capabilities.
- **[drawdb](https://github.com/drawdb-io/drawdb)** — Database schema diagrams with automatic SQL generation. Visual database design tool with forward and reverse engineering.
- **[jsoncrack](https://github.com/AykutSarac/jsoncrack.com)** — Interactive JSON structure visualizer. Beautiful and intuitive tool for exploring complex JSON data structures.
- **[drawio-desktop](https://github.com/jgraph/drawio-desktop)** — Powerful diagram editor with offline support. Create flowcharts, UML diagrams, network topologies, and more.
- **[Netron](https://github.com/lutzroeder/netron)** — Visualizer for neural networks and ML models. View model architectures, layer details, and weights interactively.
- **[Lazarus IDE](https://www.lazarus-ide.org/)** — Cross-platform IDE for Pascal and Object Pascal. Free alternative to Delphi with visual component library.
- **[LibreOffice](https://www.libreoffice.org/)** — Free and open-source office suite. Complete alternative to Microsoft Office with Writer, Calc, Impress, and more.
- **[Qt](https://www.qt.io/)** — Cross-platform application framework for GUI development. Write once, deploy everywhere alternative to Electron with native performance.
- **[KeenWrite](https://github.com/DaveJarvis/keenwrite)** — Markdown editor with variable support and graph visualization. Advanced text editor for technical writing and documentation.
- **[Symiosis](https://github.com/Archit1208/Symiosis)** — Advanced note editor with search and vim mode. Powerful markdown-based note-taking with syntax highlighting.
- **[Lokus](https://github.com/ParentalControlHub/lokus)** — Local note-taking app with visual connections. Create linked notes with graph view of relationships between entries.

### Performance

Benchmarking and profiling tools for optimization.

- **[hyperfine](https://github.com/sharkdp/hyperfine)** — Command-line benchmarking tool with statistical analysis. Warm-up runs, parameterized benchmarks, and export to various formats.
- **[flamegraph](https://github.com/brendangregg/FlameGraph)** — Stack trace visualizer for performance profiling. Identify hotspots in CPU-intensive applications.
- **[valgrind](https://valgrind.org/)** — Instrumentation framework for building dynamic analysis tools. Detect memory leaks, race conditions, and cache misses.
- **[perf](https://perf.wiki.kernel.org/)** — Linux profiling tool with performance counters. Analyze CPU cycles, cache misses, and hardware events.
- **[KDiskMark](https://github.com/JonMagon/KDiskMark)** — Disk benchmark tool with GUI for Linux. Measure read/write speeds and I/O performance of storage devices.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 🐳 Docker & Cloud

Container management and cloud storage solutions.

- **[docker-compose](https://github.com/docker/compose)** — Tool for defining and running multi-container Docker applications. YAML-based configuration for reproducible environments.
- **[lazydocker](https://github.com/jesseduffield/lazydocker)** — Terminal UI for Docker and Docker Compose. Manage containers, view logs, inspect images, and restart services with keyboard shortcuts.
- **[Portainer](https://github.com/portainer/portainer)** — Lightweight container management UI. Web-based interface for Docker, Kubernetes, and Swarm.
- **[Dozzle](https://github.com/amir20/dozzle)** — Real-time log viewer for Docker containers. Simple web UI with filtering and search capabilities.
- **[Traefik](https://github.com/traefik/traefik)** — Modern reverse proxy and load balancer. Automatic service discovery, Let's Encrypt support, and middleware system.
- **[kubectl-ctx/kubectl-ns](https://github.com/ahmetb/kubectx)** — Faster way to switch between Kubernetes contexts and namespaces.
- **[k9s](https://github.com/derailed/k9s)** — Terminal UI for Kubernetes clusters. Monitor resources, view logs, and execute commands without memorizing kubectl syntax.
- **[Rclone](https://github.com/rclone/rclone)** — Command-line program to sync files and directories to and from cloud storage. Supports 40+ cloud providers.
- **[MinIO](https://github.com/minio/minio)** — High-performance, S3-compatible object storage. Self-hosted alternative to AWS S3 with enterprise features.
- **[Syncthing](https://github.com/syncthing/syncthing)** — Continuous file synchronization program. P2P sync without cloud intermediaries.
- **[docker-jdownloader-2](https://github.com/jlesage/docker-jdownloader-2)** — JDownloader 2 in a Docker container with web GUI. Automated file downloader with support for many file hosting services.
- **[dock-droid](https://github.com/sickcodes/dock-droid)** — Run Android x86/ARM in a Docker container. Full Android system emulation with hardware acceleration support.
- **[Nextcloud](https://github.com/nextcloud/server)** — Self-hosted file sync and collaboration platform. Complete alternative to Google Workspace with calendar, contacts, and more.
- **[ArchiveBox](https://github.com/ArchiveBox/ArchiveBox)** — Self-hosted web archive. Download and save websites for offline viewing with full-text search.
- **[kopia](https://github.com/kopia/kopia)** — Fast and secure backup tool. Cross-platform backup solution with deduplication and encryption.
- **[IronBucket](https://github.com/iron-bucket/iron-bucket)** — S3-compatible object storage written in Rust. Fast and efficient self-hosted storage solution.

### Databases

High-performance database systems and administration tools for various use cases.

- **[ClickHouse](https://github.com/ClickHouse/ClickHouse)** — Column-oriented database for real-time analytics. Extremely fast queries on large datasets with SQL interface.
- **[OceanBase](https://github.com/oceanbase/oceanbase)** — Distributed SQL database compatible with MySQL. Enterprise-grade database with high availability and scalability.
- **[stagDB](https://github.com/stagdb/stagdb)** — Advanced PostgreSQL admin panel with instant branch management. Visualize, manage, and branch your database schemas effortlessly.
- **[DBeaver](https://github.com/dbeaver/dbeaver)** — Universal database tool supporting 100+ database types. SQL editor, ER diagrams, data visualization, and query execution for MySQL, PostgreSQL, MongoDB, and more.

### Web Development

Modern frameworks and tools for building web applications.

- **[Svelte](https://github.com/sveltejs/svelte)** — Cybernetically enhanced web framework. Write less code, build smaller bundles with reactive component architecture.
- **[Babylon.js](https://github.com/BabylonJS/Babylon.js)** — Powerful 3D engine for the web. Create stunning 3D experiences in browsers with WebGL and WebGPU support.
- **[Cesium](https://github.com/CesiumGS/cesium)** — 3D globes and maps for the web. High-performance geospatial visualization with photorealistic rendering.
- **[Tauri](https://github.com/tauri-apps/tauri)** — Framework for building desktop applications with web technologies. Smaller binaries than Electron, better security, and native performance.
- **[Bun](https://github.com/oven-sh/bun)** — Fast all-in-one JavaScript runtime, bundler, and package manager. Drop-in replacement for Node.js with native TypeScript support and blazing speed.
- **[Deno](https://github.com/denoland/deno)** — Secure runtime for JavaScript and TypeScript. Built-in security, modern web APIs, and first-class TypeScript support without configuration.
- **[pnpm](https://github.com/pnpm/pnpm)** — Fast, disk space efficient package manager. Uses hard links and symlinks to save disk space while maintaining compatibility with npm.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 💻 IDE & Automation

Development environments and task automation tools.

- **[Cursor](https://github.com/getcursor/cursor)** — AI-powered code editor built on VS Code. Integrated AI assistant for code generation and refactoring.
- **[VS Code](https://github.com/microsoft/vscode)** — Extensible code editor with rich ecosystem. Built-in Git, debugging, and thousands of extensions.
- **[code-server](https://github.com/coder/code-server)** — VS Code in the browser. Access your development environment from anywhere with a web browser.
- **[Gitpod](https://github.com/gitpod-io/gitpod)** — Cloud development environments. Spin up ready-to-code dev environments for any GitHub, GitLab, or Bitbucket project.
- **[DevPod](https://github.com/loft-sh/devpod)** — Client-only tool to create reproducible dev environments. Works with Docker, Kubernetes, and cloud providers.
- **[Taskfile](https://github.com/go-task/task)** — Task runner and build tool. Simpler alternative to Make with cross-platform support and YAML configuration.
- **[Just](https://github.com/casey/just)** — Command runner inspired by Make. Save and run project-specific commands with simple syntax.
- **[act](https://github.com/nektos/act)** — Run GitHub Actions locally. Test workflows before pushing to avoid trial-and-error in CI.
- **[Ansible](https://github.com/ansible/ansible)** — Automation platform for configuration management, application deployment, and orchestration.
- **[n8n](https://github.com/n8n-io/n8n)** — Workflow automation tool with visual editor. Self-hosted alternative to Zapier with 200+ integrations.
- **[feeddeck](https://github.com/feeddeck/feeddeck)** — RSS and social media aggregator inspired by TweetDeck. Self-hosted feed reader with a familiar interface.
- **[Documize community](https://github.com/documize/community)** — Self-hosted knowledge base with wiki functionality. Organize documentation, runbooks, and team knowledge in one place.
- **[amphi-etl](https://github.com/AmphiAI/amphi-etl)** — Visual Python ETL pipeline builder. Drag-and-drop interface for creating data transformation workflows without coding.
- **[ETL Pipeline Builder](https://github.com/ETL-Pipeline-Builder/etl-pipeline-builder)** — Low-code visual ETL pipeline constructor. Build data transformation workflows with drag-and-drop interface.
- **[Automatisch](https://github.com/automatisch/automatisch)** — Self-hosted Zapier alternative for workflow automation. Connect apps and services without code, fully open-source and privacy-focused.
- **[cal.com](https://github.com/calcom/cal.com)** — Open-source scheduling infrastructure. Beautiful scheduling system for managing meetings, events, and appointments.
- **[Omnivore](https://github.com/omnivore-app/omnivore)** — Read-it-later service with synchronization. Save articles, newsletters, and documents for later reading across all devices.
- **[Espanso](https://github.com/espanso/espanso)** — Cross-platform text expander. Accelerate your typing with custom snippets and abbreviations.
- **[super-productivity](https://github.com/johannesjo/super-productivity)** — Task manager and project tracker. Time tracking, Jira integration, and Pomodoro timer for maximum productivity.
- **[Budibase](https://github.com/Budibase/budibase)** — Low-code platform for building business applications. Create internal tools, admin panels, and workflows without coding.
- **[Nyno](https://github.com/nyno-org/nyno)** — YAML-based workflow automation alternative to n8n. Lightweight workflow engine without cloud dependencies.
- **[Flowcraft](https://github.com/flowcraft-io/flowcraft)** — Dependency-free automation platform. Simple and lightweight workflow automation without external dependencies.
- **[Leantime](https://github.com/Leantime/leantime)** — Simple and powerful project management and strategic planning system. Agile methodology support with kanban boards and time tracking.
- **[Memos](https://github.com/usememos/memos)** — Lightweight note-taking service with Markdown support. Self-hosted alternative to Twitter/X for quick notes and thoughts.

### Business & Enterprise

ERP systems, helpdesk solutions, and business management tools.

- **[ERPNext](https://github.com/frappe/erpnext)** — Comprehensive open-source ERP system for automating companies. Financial accounting, inventory, CRM, and human resources in one platform.
- **[aureuserp](https://github.com/aurorum/aureuserp)** — Powerful free ERP for business, finance, and logistics management. Complete business automation solution built on Laravel.
- **[osTicket](https://github.com/osTicket/osTicket)** — Popular ticket management system for customer support. PHP-based helpdesk solution trusted by thousands of organizations.
- **[Helpy](https://github.com/helpyio/helpy)** — Open-source helpdesk with modern web interface. Customer support platform with knowledge base and ticketing system.
- **[Peppermint](https://github.com/peppermint-tools/peppermint)** — Help desk and issue management system. Alternative to Zendesk and Jira built with Node.js.
- **[Kimai](https://github.com/kimai/kimai)** — Time tracking and minimal accounting system for teams and freelancers. Track working hours and generate invoices.
- **[Unifiedtransform](https://github.com/kevwe7/unifiedtransform)** — Modern open-source software for school and educational management. Automation system for educational institutions.
- **[Bagisto](https://github.com/bagisto/bagisto)** — Free e-commerce platform built on Laravel. Complete online store solution with active community and extensive features.
- **[TastyIgniter](https://github.com/tastyigniter/TastyIgniter)** — Restaurant platform and online ordering system. Laravel-based solution for managing restaurants and food delivery.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 🤖 AI & Machine Learning

LLM frameworks, AI agents, and machine learning tools.

- **[Ollama](https://github.com/ollama/ollama)** — Get up and running with large language models locally. Supports Llama 2, Code Llama, Mistral, and other open models.
- **[LangChain](https://github.com/hwchase17/langchain)** — Framework for developing applications powered by language models. Build chatbots, agents, and RAG systems.
- **[FlowiseAI](https://github.com/FlowiseAI/Flowise)** — Visual LLM workflow builder with drag-and-drop interface. Create AI agents, chatbots, and multi-agent systems without coding.
- **[LocalAI](https://github.com/mudler/LocalAI)** — Drop-in replacement for OpenAI API running locally. Use consumer-grade hardware to run LLMs, generate images, and synthesize audio.
- **[PrivateGPT](https://github.com/imartinez/privateGPT)** — Interact with your documents using LLMs without internet. 100% private, no data leaves your execution environment.
- **[Jan](https://github.com/janhq/jan)** — Open-source ChatGPT alternative that runs 100% offline. Desktop application for running LLMs locally.
- **[Open WebUI](https://github.com/open-webui/open-webui)** — User-friendly web interface for LLMs. Works with Ollama and OpenAI-compatible APIs.
- **[Apple On Device OpenAI](https://github.com/gety-io/apple-on-device-openai)** — OpenAI-compatible API for local Apple models. Simplifies on-device inference for Apple Silicon with OpenAI API compatibility.
- **[open-codex](https://github.com/ymichael/open-codex)** — AI-powered terminal agent. Works with multiple LLM backends to assist with coding tasks directly in the terminal.
- **[vtcode](https://github.com/vinhnx/vtcode)** — Terminal AI coding agent. Intelligent code generation and assistance without leaving your terminal.
- **[spacy-llm](https://github.com/explosion/spacy-llm)** — Integrate LLMs into spaCy NLP pipelines. Combine traditional NLP with modern language models for enhanced text processing.
- **[spidercreator](https://github.com/carlosplanchon/spidercreator)** — LLM-powered web scraper generator. Automatically generate web scraping scripts using natural language descriptions.
- **[fastdup](https://github.com/visual-layer/fastdup)** — Find duplicates and anomalies in image datasets. Fast and efficient tool for dataset quality control and curation.
- **[Fabric](https://github.com/danielmiessler/fabric)** — Framework for integrating AI into personal workflows. Customizable AI patterns and prompts for everyday tasks.
- **[gpt-researcher](https://github.com/assafelovic/gpt-researcher)** — Autonomous research assistant powered by LLMs. Conducts deep research on any topic and generates comprehensive reports.
- **[Kimi-Dev-72B](https://github.com/moonshotai/Kimi-Dev-72B)** — Open-source LLM for engineering tasks. Code generation, bug detection, autonomous testing, and patching of large industrial codebases.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 🔄 CI/CD

Continuous Integration and Continuous Deployment platforms and tools.

- **[GitHub Actions](https://github.com/features/actions)** — Workflow automation for building, testing, and deploying code. Native integration with GitHub repositories.
- **[GitLab](https://gitlab.com/gitlab-org/gitlab)** — Complete DevOps platform with Git repository, CI/CD pipelines, issue tracking, and container registry.
- **[GoCD](https://github.com/gocd/gocd)** — Open-source continuous delivery server. Complex pipeline modeling with value stream visualization.
- **[Jenkins](https://github.com/jenkinsci/jenkins)** — Extensible automation server. Thousands of plugins for building, deploying, and automating projects.
- **[Drone](https://github.com/harness/drone)** — Container-native CI/CD platform. Pipeline as code with Docker-based builds.
- **[Woodpecker](https://github.com/woodpecker-ci/woodpecker)** — Community fork of Drone with focus on simplicity. Self-hosted CI/CD with YAML configuration.
- **[k6](https://github.com/grafana/k6)** — Modern load testing tool for performance testing. JavaScript-based with powerful scripting capabilities for load, stress, and spike testing.
- **[Locust](https://github.com/locustio/locust)** — Distributed load testing framework. Define test scenarios in Python and simulate millions of concurrent users.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 🎬 Video Processing

Tools for video generation, manipulation, and analysis.

- **[FFmpeg](https://github.com/FFmpeg/FFmpeg)** — Complete cross-platform solution for recording, converting, and streaming audio and video. Industry standard for multimedia processing.
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** — Feature-rich command-line video downloader. Fork of youtube-dl with additional features and fixes.
- **[Sora Extend](https://github.com/mshumer/sora-extend)** — Tool to chain and extend OpenAI Sora 2 video generations beyond 12-second limit. Automated prompt deconstruction and segment concatenation.
- **[HandBrake](https://github.com/HandBrake/HandBrake)** — Video transcoder with comprehensive format support. GUI and CLI versions for batch processing.
- **[wunjo](https://github.com/wladradchenko/wunjo)** — Head motion-driven animation generator from video. Deep learning-based tool for creating realistic facial animations.
- **[auto-subs](https://github.com/tmoroney/auto-subs)** — Automatic subtitle generator for videos. Offline-capable tool using speech recognition to create subtitle files.
- **[shutter-encoder](https://github.com/paulpacifico/shutter-encoder)** — Advanced video encoder and optimizer. Professional-grade video conversion with batch processing and format optimization.
- **[Jellyfin](https://github.com/jellyfin/jellyfin)** — Self-hosted media server. Free and open-source alternative to Plex and Emby for streaming your media collection.
- **[LibrePhotos](https://github.com/LibrePhotos/librephotos)** — Self-hosted photo management service. Open-source alternative to Google Photos with facial recognition and automatic tagging.
- **[Upscayl](https://github.com/upscayl/upscayl)** — AI-powered image upscaling tool. Enhance image quality using machine learning models locally.
- **[Shotcut](https://www.shotcut.org/)** — Powerful and simple video editor with regular updates. Perfect for educational content and basic video/audio editing.
- **[OBS Studio](https://obsproject.com/)** — Open-source streaming and recording software. Record desktop, stream to Twitch/YouTube, and capture calls for archives.
- **[Blender](https://www.blender.org/)** — Professional 3D creation suite. Modeling, animation, rendering, and compositing for films, games, and visual effects.
- **[Audacity](https://www.audacityteam.org/)** — Free, open-source audio editor. Record, edit, and mix audio tracks with professional-quality tools.
- **[VLC Media Player](https://www.videolan.org/vlc/)** — Universal media player. Plays virtually all video and audio formats without codec installation.
- **[MPV](https://mpv.io/)** — Lightweight, powerful media player. Command-line based with minimal GUI, highly customizable and scriptable.
- **[Immich](https://github.com/immich-app/immich)** — Self-hosted photo and video backup solution. Alternative to Google Photos with automatic backups and facial recognition.
- **[Pars Local Player (PLP)](https://github.com/pars-local-player/pars-local-player)** — Lightweight video player without telemetry or tracking. Privacy-focused media player with clean interface.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 🎯 3D Vision & Scanning

Open-source tools and libraries for 3D computer vision, scanning, reconstruction, and point cloud processing.

- **[OpenScan](https://openscan.eu)** — Modular open-source 3D scanner with photogrammetry. Includes schematics, documentation, and software for DIY assembly. Process scans locally or in the cloud for 3D printing, reverse engineering, and digital preservation.
- **[Meshroom](https://github.com/alicevision/meshroom)** — Powerful open-source photogrammetry pipeline for 3D reconstruction. Node-based visual programming interface, complete processing from photos to 3D models, Python API. Used in science, archaeology, and game development.
- **[PiLiDAR](https://github.com/iLiAR/PLiDAR)** — DIY LiDAR 3D scanner project using Raspberry Pi and camera. Open hardware and software with CC-NC-SA license. Low-cost laser scanner for point cloud experiments.
- **[Open3D](https://github.com/isl-org/Open3D)** — Comprehensive library for 3D data processing. Point cloud manipulation, mesh generation, visualization, scan registration. Python and C++ support with extensive documentation.
- **[CloudCompare](https://github.com/CloudCompare/CloudCompare)** — Open-source point cloud processing and analysis tool. Import/export standard formats, mesh generation, filtering, and scripting. Essential for comparing, merging, and analyzing point clouds.
- **[COLMAP](https://github.com/colmap/colmap)** — Industry-standard Structure-from-Motion and photogrammetry tool. Reconstruct 3D scenes from multiple images with automatic camera calibration and dense reconstruction pipelines.
- **[OpenCV](https://github.com/opencv/opencv)** — Fundamental computer vision library. Includes algorithms for stereo vision, depth processing, point cloud generation, stereo cameras, and post-processing.
- **[Salingo Virtual 3D Scanner](https://github.com/Salingo/virtual-3d-scanner)** — Synthetic RGB-D image and point cloud generator. Scans virtual 3D models to generate datasets for computer vision training and development.
- **[TripoSR](https://github.com/VAST-AI-Research/TripoSR)** — Deep learning toolkit for single-image 3D reconstruction. AI-powered surface reconstruction with fast inference and high accuracy for modern AI algorithms. [Website](https://triposrai.com/)
- **[Potree](https://github.com/potree/potree)** — WebGL-based point cloud renderer for large datasets. Interactive browser-based viewer supporting millions of points with level-of-detail rendering and measurement tools.
- **[PointLLM](https://github.com/OpenRobotLab/PointLLM)** — Extends Large Language Models to understand point clouds. Enables zero-shot 3D reasoning, question answering, and scene understanding from point cloud data. [ECCV 2024 Best Paper Candidate]
- **[PCL (Point Cloud Library)](https://github.com/PointCloudLibrary/pcl)** — Comprehensive library for 2D/3D image and point cloud processing. Industry-standard toolkit for filtering, segmentation, registration, surface reconstruction, and feature estimation.
- **[ReBound](https://github.com/ramdrop/ReBound)** — Open-source tool for visualizing and annotating LiDAR data. Designed for active learning systems in autonomous vehicles with intuitive 3D annotation interface.
- **[pyRANSAC-3D](https://github.com/leomariga/pyRANSAC-3D)** — Python tool for fitting primitive 3D shapes in point clouds using RANSAC algorithm. Fast and robust geometric primitive detection (planes, spheres, cylinders, etc.).

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 🏭 Industrial Automation & SCADA

Open-source tools for industrial automation, SCADA systems, PLC programming, and process control.

- **[OpenSCADA / Eclipse SCADA](https://openscada.org)** | [Eclipse SCADA](https://eclipse.org/scada) — Powerful platform for data acquisition, visualization, management, and automation (HMI, Modbus, OPC, SNMP, IEC protocols, archiving, scripting). Suitable for manufacturing, energy, transportation, PLC integration, and custom solutions.
- **[ScadaBR](https://github.com/ScadaBR/ScadaBR)** — Web-based SCADA system built on Java. Easy deployment with Modbus RTU/TCP, OPC, SNMP support. Visualization, alarms, trends — ideal for small and medium-sized manufacturing facilities.
- **[Rapid SCADA](https://github.com/RapidScada/Scada)** — Russian-language SCADA project with support for Siemens S7, Allen-Bradley, Arduino, Raspberry Pi. Flexible visualization, reporting, integration with industrial networks.
- **[OpenAPC](http://www.openapc.com)** — Open-source platform for industrial control and visualization. Extensible with custom plugins for specialized applications.
- **[OpenPLC](https://www.openplcproject.com)** | [GitHub](https://github.com/thiagoralves/OpenPLC_v3) — Comprehensive open-source platform for PLC programming (IEC 61131-3: Ladder, FBD, ST, IL, SFC). Simulation, deployment to Arduino/Raspberry Pi and industrial hardware, web-based monitoring, Modbus TCP/RTU, SCADA integration.
- **[Beremiz IDE](https://github.com/beremiz/beremiz)** — PLC platform with Python integration. Excellent for complex distributed projects with custom driver development capabilities.
- **[PLC Fiddle](https://www.plcfiddle.com)** — Web-based PLC simulator (IEC 61131). Learn and debug PLC programs without installing software.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 🏗️ CAD & BIM Design

Building Information Modeling (BIM) and Computer-Aided Design (CAD) tools for architecture, engineering, and construction.

- **[FreeCAD](https://github.com/FreeCAD/FreeCAD)** — Professional parametric 3D/2D CAD/BIM software with architectural workbench. FEM integration, Path (CAM/CNC), Python scripting. Suitable for architects, mechanical engineering, automation, and manufacturing.
- **[BlenderBIM](https://blenderbim.org)** — Extends Blender for BIM projects. IFC support, clash detection, documentation generation.
- **[BIMvision](https://bimvision.com)** — Free software for viewing and analyzing BIM models from any platform. Cost estimation, collision detection, quantity takeoff.
- **[IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell)** — Library for working with IFC/BIM formats. Generation, parsing, and integration into automation and construction projects.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 🔐 Security & OSINT

Security testing tools, OSINT frameworks, and vulnerability scanners.

- **[awesome-security](https://github.com/sbilly/awesome-security)** — Curated list of security resources including tools, frameworks, and learning materials.
- **[OSINT Framework](https://github.com/lockfale/osint-framework)** — Collection of OSINT tools organized by category. Web-based directory of open-source intelligence sources.
- **[Trivy](https://github.com/aquasecurity/trivy)** — Comprehensive security scanner for containers, filesystems, and IaC. Detects vulnerabilities, misconfigurations, and secrets.
- **[gitleaks](https://github.com/gitleaks/gitleaks)** — SAST tool for detecting hardcoded secrets in git repositories. Scan commits, branches, and entire histories.
- **[sherlock](https://github.com/sherlock-project/sherlock)** — Hunt social media accounts by username across 300+ websites. Python-based OSINT tool.
- **[theHarvester](https://github.com/laramies/theHarvester)** — Gather emails, subdomains, hosts, and employee names from public sources. Essential for reconnaissance.
- **[OWASP Amass](https://github.com/owasp-amass/amass)** — In-depth attack surface mapping and asset discovery. Network mapping of organizations through scraping and APIs.
- **[SpiderFoot](https://github.com/smicallef/spiderfoot)** — Automated OSINT collection tool with web interface. Gather intelligence about targets from 100+ sources.
- **[OWASP Juice Shop](https://github.com/juice-shop/juice-shop)** — Intentionally insecure web application for security training. Practice finding and exploiting vulnerabilities.
- **[HashiCorp Vault](https://github.com/hashicorp/vault)** — Secrets management and data protection. Identity-based access control for cloud applications.
- **[Nginx-Lua-Anti-DDoS](https://github.com/C0nw0nk/Nginx-Lua-Anti-DDoS)** — Lua-based anti-DDoS script for Nginx. JavaScript puzzle challenge system to protect against automated attacks.
- **[Certipy](https://github.com/ly4k/Certipy)** — Active Directory Certificate Services (AD CS) auditing and exploitation tool. Discover and abuse misconfigurations in AD CS.
- **[Vaultwarden](https://github.com/dani-garcia/vaultwarden)** — Self-hosted Bitwarden-compatible password manager. Lightweight server implementation with all Bitwarden client features.
- **[ente](https://github.com/ente-io/ente)** — End-to-end encrypted cloud storage for photos and videos. Privacy-first alternative to Google Photos with client-side encryption.
- **[wg-easy](https://github.com/wg-easy/wg-easy)** — Easy-to-use WireGuard VPN with web interface. Set up and manage VPN servers through a user-friendly dashboard.
- **[trufflehog](https://github.com/trufflesecurity/trufflehog)** — Detect leaked secrets in git repositories. Scans commits, branches, and PRs for exposed credentials and API keys.
- **[fail2ban](https://github.com/fail2ban/fail2ban)** — Intrusion prevention framework. Automatically ban IPs showing malicious behavior like brute-force attacks.
- **[GrapheneOS](https://grapheneos.org/)** — Privacy and security-focused Android distribution. Enhanced security features and hardened system for maximum privacy.
- **[Authelia](https://github.com/authelia/authelia)** — Single Sign-On and 2FA portal. Authentication server with multi-factor authentication and authorization policies.
- **[Authentik](https://github.com/goauthentik/authentik)** — Flexible identity provider with SSO and user management. Supports OAuth, SAML, LDAP, and more authentication protocols.
- **[Keycloak](https://github.com/keycloak/keycloak)** — Open-source identity and access management solution. Add authentication to applications with minimal code changes.
- **[Hanko](https://github.com/hankoio/hanko)** — Passwordless authentication server. Modern authentication solution with passkeys and WebAuthn support.
- **[PrivyDrop](https://github.com/privydrop/privydrop)** — Peer-to-peer file drop with Docker deployment. Share files without cloud storage, fully self-hosted.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 📚 Education

Learning resources, courses, and comprehensive guides for developers.

- **[freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp)** — Learn to code for free with interactive lessons. Full-stack web development curriculum with certifications.
- **[OSSU Computer Science](https://github.com/ossu/computer-science)** — Path to free self-taught education in Computer Science. Complete degree program using online courses.
- **[System Design Primer](https://github.com/donnemartin/system-design-primer)** — Learn how to design large-scale systems. Comprehensive guide with diagrams and examples.
- **[The Missing Semester](https://github.com/missing-semester/missing-semester)** — MIT course about computing tools every developer should know. Shell, vim, git, debugging, and more.
- **[The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)** — Master the command line in one page. Practical examples for everyday use.
- **[coding-interview-university](https://github.com/jwasham/coding-interview-university)** — Complete study plan to become a software engineer. Covers algorithms, data structures, and system design.
- **[build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)** — Learn by building your own version of technologies. Tutorials for databases, web servers, Git, Docker, and more.
- **[LearnGitBranching](https://github.com/pcottle/learnGitBranching)** — Interactive visual Git tutorial. Master branching, merging, rebasing, and advanced Git workflows through hands-on exercises.
- **[Joplin](https://github.com/laurent22/joplin)** — Cross-platform note-taking application. Markdown editor with synchronization, encryption, and plugin support.
- **[Wallabag](https://github.com/wallabag/wallabag)** — Self-hosted read-it-later service. Save articles for later reading with full-text search and tagging.
- **[Overleaf](https://github.com/overleaf/overleaf)** — Collaborative LaTeX editor. Real-time collaborative editing for scientific papers and documents.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 🌟 Other Awesome Collections

Curated lists covering specialized topics and tools.

- **[awesome](https://github.com/sindresorhus/awesome)** — The original awesome list. Curated list of awesome lists across all topics.
- **[awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted)** — Self-hosted alternatives to popular services. Privacy-focused applications you can run on your own servers.
- **[awesome-cli-apps](https://github.com/agarrharr/awesome-cli-apps)** — Curated list of command-line applications organized by category.
- **[awesome-shell](https://github.com/alebcay/awesome-shell)** — Command-line frameworks, toolkits, guides, and gizmos.
- **[terminals-are-sexy](https://github.com/k4m4/terminals-are-sexy)** — Curated list of terminal frameworks, plugins, and resources.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 📝 Research & Theses

👉 **[Browse Theses Collection](./theses/)**

The `theses/` directory contains in-depth research, technical analyses, and comprehensive notes on key topics:

- **[LLM for Business](./theses/llm_for_business.md)** — Analysis of Large Language Model adoption in Russian enterprises. Covers use cases, challenges, and implementation strategies.
- **[The Great Software Quality Crash](./theses/thesis_habr_great_software_crash_en.md)** — Deep dive into the software quality crisis. Examines memory leaks, system failures, and why $364 billion in infrastructure spending won't solve fundamental engineering problems.

### Project Ideas Collection

👉 **[Browse Project Ideas](./projects-ideas/)**

The `projects-ideas/` directory contains curated links to repositories with ideas, templates, and inspiration for work projects and personal side projects:

- **[Industrial Automation & SCADA](./projects-ideas/industrial-automation-scada.md)** — Comprehensive collection of tools for SCADA systems, PLC programming, BIM/CAD design, point cloud processing, and engineering AI applications.

### Contributing Theses

Use the provided [template](./theses/thesis_template_en.md) to contribute your own research and analysis.

[⬆ Back to Top](#-awesome-repositories-collection-)

---

## 🤝 Contributing

Contributions are welcome! Please read the [Contributing Guide](CONTRIBUTING.md) for details on how to submit pull requests.

### Quality Criteria

Before submitting, ensure your addition meets these standards:

- ✅ **Actively maintained** — Regular updates and community support
- ✅ **Clear documentation** — Comprehensive README with setup instructions
- ✅ **Production-ready** — Stable and widely adopted
- ✅ **Open-source** — Permissive licensing (MIT, Apache 2.0, GPL, etc.)
- ✅ **Solves real problems** — Clear use case and value proposition

### Submission Format

```markdown
- **[Repository Name](https://github.com/user/repo)** — Brief description highlighting key features, tech stack, and use cases. Explain what makes this tool unique and why developers should use it.
```

### Example

```markdown
- **[ripgrep](https://github.com/BurntSushi/ripgrep)** — Ultra-fast recursive search tool written in Rust. Respects .gitignore by default and outperforms grep, ag, and ack on large codebases with regex support and parallel execution.
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## 🌍 Language Versions

- [🇬🇧 English](README.md) — You are here
- [🇷🇺 Русский](README.ru.md) — Russian version
- [🇨🇳 简体中文](README.zh-CN.md) — Simplified Chinese version

---

<p align="center">
  <sub>Curated with ❤️ for the developer community</sub>
</p>
