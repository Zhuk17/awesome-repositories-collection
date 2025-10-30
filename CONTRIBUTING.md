# Contributing Guide

Thank you for your interest in contributing to the Awesome Repositories Collection! 🎉

## How to Contribute

### Adding a New Tool

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b add-tool-name`)
3. **Add the tool** to the appropriate section in `README.md`
4. **Follow the format** (see below)
5. **Commit your changes** (`git commit -m 'Add tool-name'`)
6. **Push to your branch** (`git push origin add-tool-name`)
7. **Open a Pull Request**

### Submission Format

Each tool entry should follow this exact format:

```markdown
- **[Tool Name](https://github.com/user/repo)** — Brief description explaining what the tool does, its key features, and why developers should use it. Mention the tech stack if relevant.
```

**Example:**

```markdown
- **[ripgrep](https://github.com/BurntSushi/ripgrep)** — Ultra-fast recursive search tool written in Rust. Respects .gitignore by default and outperforms grep, ag, and ack on large codebases with regex support and parallel execution.
```

### Quality Criteria

Before submitting, ensure your addition meets these standards:

- ✅ **Actively maintained** — Project has recent commits and responds to issues
- ✅ **Clear documentation** — Comprehensive README with installation and usage instructions
- ✅ **Production-ready** — Stable release available and widely adopted
- ✅ **Open-source** — Permissive license (MIT, Apache 2.0, GPL, BSD, etc.)
- ✅ **Solves real problems** — Clear use case with practical value
- ✅ **Not a duplicate** — Tool offers unique value or significantly differs from existing entries

### Category Guidelines

- Choose the most appropriate category for your tool
- If creating a new category, ensure it has at least 3-4 quality tools
- Maintain alphabetical order within categories when possible
- Keep descriptions concise but informative (1-2 sentences)

### Writing Good Descriptions

A great description should answer:
1. **What** — What does the tool do?
2. **Why** — What problem does it solve?
3. **How** — What makes it special or different?

**Good Description:**
> Ultra-fast recursive search tool written in Rust. Respects .gitignore by default and outperforms grep, ag, and ack on large codebases.

**Bad Description:**
> Search tool (too vague)

---

## Updating Existing Entries

If you notice outdated information or broken links:

1. Verify the information is incorrect
2. Find the correct/updated information
3. Submit a PR with the fix
4. Explain the change in your PR description

---

## Contributing Theses

We welcome in-depth technical research and analysis! See the [Theses README](./theses/README.md) for guidelines.

### Thesis Requirements

1. Use the provided [template](./theses/thesis_template_en.md)
2. Original analysis or comprehensive synthesis of existing research
3. Clear structure with TL;DR, key observations, discussion, and takeaways
4. Properly cited sources
5. English language (translations welcome after original is merged)

### Thesis Submission Process

1. Create your thesis file in `theses/` directory
2. Follow naming convention: `thesis_topic_name_en.md`
3. Add entry to `theses/README.md` table
4. Submit PR with your thesis and table update

---

## Language Versions

### Translation System

This repository uses **automated translation** via GitHub Actions:

- ✍️ **Only edit `README.md`** (English version)
- 🤖 Translations to Russian and Chinese are **generated automatically**
- ⚡ Workflow triggers on push to `main` branch

### When Translations Need Manual Fixes

If you notice translation errors:

1. **Check if the issue is in the source** (`README.md`) first
2. If source is correct but translation is wrong, open an issue
3. Automated translations will be regenerated on next `README.md` update

### Testing Translations Locally

```bash
# Set up Python environment
pip install openai anthropic requests python-dotenv pyyaml

# Set your API key
export OPENAI_API_KEY="your_key_here"

# Run translation script
export SOURCE_LANG=en
export TARGET_LANGS=ru,zh-CN
python scripts/translate_readmes.py
```

---

## Pull Request Guidelines

### Before Submitting

- [ ] Tool meets all quality criteria
- [ ] Description follows the format
- [ ] Links are working and point to correct repositories
- [ ] No spelling or grammar mistakes
- [ ] Changes made only to `README.md` (English version)

### PR Title Format

Use one of these prefixes:

- `add:` — Adding new tool(s)
- `update:` — Updating existing entry
- `fix:` — Fixing broken links or errors
- `docs:` — Documentation improvements

**Examples:**
- `add: ripgrep to Search & Replace section`
- `update: description for htop`
- `fix: broken link to fzf repository`

### PR Description

Include:
1. What you're adding/changing
2. Why this tool/change is valuable
3. Any additional context

---

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other contributors

### Unacceptable Behavior

- Harassment or discriminatory comments
- Trolling or insulting/derogatory comments
- Publishing others' private information
- Any conduct inappropriate in a professional setting

---

## Questions?

- 💬 Open a [GitHub Discussion](https://github.com/zhukovgreen/awesome-repositories-collection/discussions)
- 🐛 Found a bug? Open an [Issue](https://github.com/zhukovgreen/awesome-repositories-collection/issues)
- 📧 Need help? Check existing issues or start a discussion

---

## Recognition

Contributors will be recognized in:
- GitHub's built-in contributors list
- Release notes (for significant contributions)
- Our gratitude! 🙏

Thank you for making this collection better! ⭐
