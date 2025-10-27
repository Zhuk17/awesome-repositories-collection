# 实用工具集合 ⚡

> 精心挑选的命令行实用工具和开发工具列表

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## 语言 / Languages / Языки

- [English](README.md)
- [Русский](README.ru.md)
- [简体中文](README.zh-CN.md)

## 目录

- [命令行工具](#命令行工具)
  - [文件导航](#文件导航)
  - [搜索和替换](#搜索和替换)
  - [系统监控](#系统监控)
  - [网络](#网络)
- [开发工具](#开发工具)
  - [Git](#git)
  - [代码编辑器](#代码编辑器)
  - [调试](#调试)
- [性能](#性能)
- [安全](#安全)
- [如何贡献](#如何贡献)

## 命令行工具

### 文件导航

- **[fzf](https://github.com/junegunn/fzf)** - 命令行模糊搜索器。用于搜索文件、命令历史等的通用工具。
  ```bash
  # 通过 Homebrew 安装
  brew install fzf
  
  # 使用示例
  vim $(fzf)
  ```

- **[fd](https://github.com/sharkdp/fd)** - `find` 命令的简单、快速和用户友好的替代品。
  ```bash
  # 查找所有 Python 文件
  fd -e py
  
  # 区分大小写搜索文件
  fd -s readme
  ```

- **[exa](https://github.com/ogham/exa)** - 具有增强功能和美观输出的现代 `ls` 替代品。
  ```bash
  # 树状列出文件
  exa --tree --level=2
  
  # 详细列表
  exa -la
  ```

### 搜索和替换

- **[ripgrep](https://github.com/BurntSushi/ripgrep)** - 极快的搜索工具，递归搜索目录中的正则表达式模式。
  ```bash
  # 在当前目录中搜索
  rg "函数"
  
  # 搜索时显示上下文
  rg -C 3 "错误"
  ```

- **[sd](https://github.com/chmln/sd)** - 直观的 `sed` 查找和替换替代品。
  ```bash
  # 在文件中替换文本
  sd '旧文本' '新文本' 文件.txt
  ```

### 系统监控

- **[htop](https://htop.dev/)** - 交互式进程查看器，改进的 `top` 版本。
  ```bash
  htop
  ```

- **[btop](https://github.com/aristocratos/btop)** - 漂亮的资源监控器，显示 CPU、内存、磁盘、网络和进程的使用情况。
  ```bash
  btop
  ```

- **[dust](https://github.com/bootandy/dust)** - 用 Rust 编写的更直观的 `du` 版本。
  ```bash
  # 显示磁盘使用情况
  dust
  
  # 限制深度
  dust -d 2
  ```

### 网络

- **[httpie](https://httpie.io/)** - 具有直观语法的用户友好的命令行 HTTP 客户端。
  ```bash
  # GET 请求
  http GET api.example.com/users
  
  # POST 带 JSON 数据
  http POST api.example.com/users name="张三" email="zhangsan@example.com"
  ```

- **[curlie](https://github.com/rs/curlie)** - curl 语法与 httpie 输出的结合。
  ```bash
  curlie GET https://api.github.com/users/zhuk17
  ```

## 开发工具

### Git

- **[lazygit](https://github.com/jesseduffield/lazygit)** - git 命令的简单终端用户界面。
  ```bash
  lazygit
  ```

- **[delta](https://github.com/dandavison/delta)** - git、diff 和 grep 输出的语法高亮器。
  ```bash
  # 添加到 git 配置
  git config --global core.pager delta
  ```

- **[gh](https://cli.github.com/)** - GitHub 官方命令行界面。
  ```bash
  # 创建新仓库
  gh repo create 我的项目 --public
  
  # 查看 pull requests
  gh pr list
  ```

### 代码编辑器

- **[micro](https://micro-editor.github.io/)** - 现代直观的终端文本编辑器。
  ```bash
  micro 文件.txt
  ```

- **[helix](https://helix-editor.com/)** - 后现代模态文本编辑器。
  ```bash
  hx 文件.rs
  ```

### 调试

- **[gdb](https://www.gnu.org/software/gdb/)** - GNU 项目调试器。
  ```bash
  gdb ./我的程序
  ```

- **[strace](https://strace.io/)** - Linux 诊断、调试和指导用户空间跟踪器，用于监控系统调用。
  ```bash
  strace ls
  ```

## 性能

- **[hyperfine](https://github.com/sharkdp/hyperfine)** - 命令行基准测试工具。
  ```bash
  # 比较两个命令
  hyperfine '命令1' '命令2'
  ```

- **[tokei](https://github.com/XAMPPRocky/tokei)** - 快速准确地统计代码行数。
  ```bash
  # 统计项目中的代码行数
  tokei
  ```

## 安全

- **[age](https://github.com/FiloSottile/age)** - 简单、现代、安全的文件加密工具。
  ```bash
  # 加密文件
  age -r 接收者 文件.txt > 文件.txt.age
  
  # 解密文件
  age -d -i 密钥.txt 文件.txt.age > 文件.txt
  ```

- **[pass](https://www.passwordstore.org/)** - 标准的 Unix 密码管理器。
  ```bash
  # 初始化密码存储
  pass init 你的-gpg-id
  
  # 添加新密码
  pass insert 邮箱/google
  ```

## 如何贡献

欢迎贡献！请先阅读[贡献指南](CONTRIBUTING.md)开始。

1. Fork 仓库
2. 创建功能分支 (`git checkout -b feature/惊艳功能`)
3. 提交更改 (`git commit -m '添加惊艳功能'`)
4. 推送到分支 (`git push origin feature/惊艳功能`)
5. 打开 Pull Request

## 许可证

本项目根据 MIT 许可证分发 - 详情请参阅 [LICENSE](LICENSE) 文件。

## 致谢

- 所有上述开源项目的贡献者
- 社区为建议和测试这些优秀工具所做的贡献

---

⭐ 如果你喜欢这个项目，请在 GitHub 上给个星标！
