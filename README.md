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

- **130+** curated tools and resources
- **13** main categories
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
- [IDE & Automation](#-ide--automation)
- [AI & Machine Learning](#-ai--machine-learning)
- [CI/CD](#-cicd)
- [Video Processing](#-video-processing)
- [Security & OSINT](#-security--osint)
- [Education](#-education)
- [Other Collections](#-other-awesome-collections)
- [Research & Theses](#-research--theses)
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

### Debugging

Tools for diagnosing and fixing issues in your applications.

- **[gdb](https://www.sourceware.org/gdb/)** — GNU Debugger for C, C++, and other languages. Industry-standard debugger with powerful scripting capabilities.
- **[lldb](https://lldb.llvm.org/)** — Next-generation debugger from LLVM project. Excellent for debugging C, C++, Objective-C, and Swift.
- **[delve](https://github.com/go-delve/delve)** — Debugger for the Go programming language. Supports goroutines, channels, and Go-specific debugging features.
- **[pdb++](https://github.com/pdbpp/pdbpp)** — Enhanced Python debugger with syntax highlighting, tab completion, and better introspection.
- **[fastcrud](https://github.com/benavlabs/fastcrud)** — Async CRUD operations for FastAPI with automatic JOINs. Simplified database operations with automatic relationship handling.
- **[bkhtmltopdf](https://github.com/bkhtmltopdf/bkhtmltopdf)** — Fast HTML to PDF converter. High-performance tool for generating PDF documents from HTML content.
- **[dnote](https://github.com/dnote/dnote)** — Terminal-based notebook on SQLite. Simple note-taking system with command-line interface and local storage.
- **[dotbins](https://github.com/basnijholt/dotbins)** — CLI binary manager through dotfiles. Manage and version control command-line tools in your dotfiles repository.
- **[ito](https://github.com/heyito/ito)** — Voice dictation for any application. Universal voice input tool that works across different programs and platforms.

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
