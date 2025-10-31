# Translation Automation Guide

## 📖 Overview

This repository includes an **automated translation synchronization system** for README files across multiple languages (English, Russian, Chinese). The system works via **GitHub Actions** and uses **free open-source translators** (argostranslate with local models and LibreTranslate API) for machine translation.

### How It Works

1. ✍️ You edit `README.md` (English version)
2. 🚀 Push to `main` branch
3. 🤖 GitHub Actions automatically translates to Russian and Chinese
4. ✅ Translated files are committed back to the repository

---

## 🏗️ Architecture

### Components

#### 1. GitHub Actions Workflow

**Location:** `.github/workflows/auto-translate-readmes.yml`

**Triggers:**
- Automatically on push to `main` when `README.md` changes
- Manually via `workflow_dispatch` for custom translations

**Features:**
- Python translation script in `scripts/translate_readmes.py`
- Support for free translation methods (argostranslate, LibreTranslate)
- Automatic commit and push of translations
- **No API keys required** - completely free and open-source

#### 2. Python Translation Script

**Location:** `scripts/translate_readmes.py`

**Capabilities:**
- Uses **argostranslate** (local models) as primary method - fastest and most reliable
- Falls back to **LibreTranslate API** (public servers) if needed
- Preserves markdown formatting automatically
- Doesn't translate technical terms, URLs, code blocks
- Smart handling of repository names and file paths

---

## ⚙️ Setup

### 1. No API Keys Required! 🎉

The system uses **completely free** translation services:
- **argostranslate**: Downloads language models automatically (no API keys)
- **LibreTranslate**: Uses public servers (no authentication needed)

Just push your changes and it works!

### 2. Configure GitHub Actions Permissions

Ensure GitHub Actions can commit changes:

```
Settings → Actions → General → Workflow permissions
→ Select "Read and write permissions"
→ Check "Allow GitHub Actions to create and approve pull requests"
→ Save
```

### 3. Verify Workflow File

Check that `.github/workflows/auto-translate-readmes.yml` exists and is properly configured.

---

## 🚀 Usage

### Automatic Translation (Recommended)

**Simple workflow:**

1. Edit `README.md` (English version only)
2. Commit and push to `main` branch:
   ```bash
   git add README.md
   git commit -m "Update README with new tools"
   git push origin main
   ```
3. GitHub Actions automatically:
   - Detects the change
   - Translates to Russian (`README.ru.md`)
   - Translates to Chinese (`README.zh-CN.md`)
   - Commits translations back to `main`

**Check progress:**
- Go to **Actions** tab in your repository
- Click on the latest "Auto-Translate READMEs" workflow run
- Monitor the progress and check for any errors

### Manual Translation

For special cases (translating from Russian source, selective languages, etc.):

1. Go to **Actions** → **Auto-Translate READMEs**
2. Click **Run workflow** button
3. Configure options:
   - **Source language:** `en`, `ru`, or `zh-CN`
   - **Target languages:** Comma-separated list (e.g., `ru,zh-CN`)
4. Click **Run workflow**

**Example use cases:**
- Translate Russian version to English and Chinese: `source: ru`, `target: en,zh-CN`
- Update only Chinese version: `source: en`, `target: zh-CN`

---

## 🖥️ Local Development

### Prerequisites

```bash
# Install required Python packages
pip install -r requirements.txt
# or manually:
pip install argostranslate requests python-dotenv pyyaml
```

### Setup

No environment variables needed! The script will automatically:
1. Download language models for argostranslate on first run
2. Use public LibreTranslate servers if needed

### Extract Translation Script

The script is embedded in the workflow file. Extract it:

```bash
mkdir -p scripts
```

Then copy the Python code from `.github/workflows/auto-translate-readmes.yml` (between `EOF` markers, lines 64-187) to `scripts/translate_readmes.py`.

Or run the workflow once — it will auto-create the script.

### Run Locally

```bash
# Translate from English to Russian and Chinese
export SOURCE_LANG=en
export TARGET_LANGS=ru,zh-CN
python scripts/translate_readmes.py
```

```bash
# Translate from Russian to English only
export SOURCE_LANG=ru
export TARGET_LANGS=en
python scripts/translate_readmes.py
```

### Test Before Pushing

```bash
# Make changes to README.md
vim README.md

# Run translation locally
export SOURCE_LANG=en
export TARGET_LANGS=ru,zh-CN
python scripts/translate_readmes.py

# Review translations
git diff README.ru.md README.zh-CN.md

# If satisfied, commit and push
git add README*.md
git commit -m "Update README and translations"
git push origin main
```

---

## 🔧 Configuration

### Supported Languages

Currently configured languages:

| Code | Language | File |
|------|----------|------|
| `en` | English | `README.md` |
| `ru` | Russian | `README.ru.md` |
| `zh-CN` | Simplified Chinese | `README.zh-CN.md` |

### Adding New Languages

To add support for a new language (e.g., Spanish):

1. **Update translation script** in `.github/workflows/auto-translate-readmes.yml`:

```python
LANGUAGE_CODES = {
    'en': 'English',
    'ru': 'Russian (Русский)',
    'zh-CN': 'Simplified Chinese (简体中文)',
    'es': 'Spanish (Español)'  # Add this
}

README_FILES = {
    'en': 'README.md',
    'ru': 'README.ru.md',
    'zh-CN': 'README.zh-CN.md',
    'es': 'README.es.md'  # Add this
}
```

2. **Update workflow inputs** (lines 24-27):

```yaml
options:
  - en
  - ru
  - zh-CN
  - es  # Add this
```

3. **Update default targets** (line 31):

```yaml
default: 'ru,zh-CN,es'
```

### Translation Methods

The system uses two methods in order of preference:

1. **argostranslate** (primary)
   - Local translation models (downloaded automatically)
   - Fast and reliable
   - No API calls, completely offline after initial download
   - Models are installed automatically on first use

2. **LibreTranslate API** (fallback)
   - Public servers: `translate.argosopentech.com`, `libretranslate.de`
   - Used if argostranslate models are unavailable
   - No authentication required

### Improving Translation Quality

Since we use free translation services, quality depends on:
1. **Clear source text** - Write descriptive, grammatically correct English
2. **Technical terms** - System automatically preserves links, code, URLs
3. **Retry if needed** - Sometimes LibreTranslate servers are busy, retry the workflow

**Tips:**
- Use complete sentences rather than fragments
- Be consistent with terminology
- Include context in descriptions

---

## 📋 Translation Rules

### What Gets Translated

✅ **Translated:**
- Headers and titles
- Paragraph text
- Tool descriptions
- Explanations and instructions

### What Stays in English

🚫 **Not translated:**
- URLs and hyperlinks
- GitHub repository names (e.g., `neovim/neovim`)
- Code blocks and command examples
- File paths (e.g., `scripts/translate.py`)
- Tags (e.g., `*Tags: Python, Docker, AI*`)
- Technical terms (often kept in English even in other languages)

### Example

**Input (English):**
```markdown
- **[ripgrep](https://github.com/BurntSushi/ripgrep)** — Ultra-fast search tool written in Rust.
  - *Tags: Rust, CLI, Search*
```

**Output (Russian):**
```markdown
- **[ripgrep](https://github.com/BurntSushi/ripgrep)** — Сверхбыстрый инструмент поиска, написанный на Rust.
  - *Tags: Rust, CLI, Search*
```

**Notice:** Repository name, URL, and tags remain unchanged.

---

## 🐛 Troubleshooting

### Workflow Doesn't Trigger

**Symptoms:** Push to `main` but no workflow runs

**Solutions:**
1. ✅ Verify Actions are enabled: `Settings → Actions → General → Actions permissions`
2. ✅ Check file changed: Workflow only triggers on `README.md` changes
3. ✅ Verify branch: Must push to `main` branch
4. ✅ Check workflow file: Ensure `.github/workflows/auto-translate-readmes.yml` exists

### Translation Method Errors

**Symptoms:** Workflow fails with "translation failed" or "model not found"

**Solutions:**
1. ✅ **Check argostranslate models:** First run downloads models automatically, this may take a few minutes
2. ✅ **LibreTranslate servers down:** Wait and retry, or the workflow will automatically retry
3. ✅ **Network issues:** Ensure GitHub Actions runner has internet access
4. ✅ **Language pair unavailable:** Some language pairs might not be available, check argostranslate documentation

### Poor Translation Quality

**Symptoms:** Translations are inaccurate or awkward

**Solutions:**
1. ✅ **Improve source description:** Better English = better translation
2. ✅ **Lower temperature:** Change from `0.3` to `0.1` for more consistency
3. ✅ **Check translation servers:** LibreTranslate servers might be temporarily unavailable
4. ✅ **Retry workflow:** Sometimes network issues resolve on retry

### Merge Conflicts

**Symptoms:** Workflow creates conflicts with manual edits

**Solutions:**
1. ✅ **Only edit `README.md`:** Never manually edit `README.ru.md` or `README.zh-CN.md`
2. ✅ **Pull before push:** Always `git pull` before pushing new changes
3. ✅ **Resolve conflicts:** If conflict occurs, keep `README.md` changes and regenerate translations

### Script Creation Fails

**Symptoms:** Error about missing `scripts/translate_readmes.py`

**Solutions:**
1. ✅ **Let workflow create it:** First run auto-creates the script
2. ✅ **Check permissions:** Ensure workflow has write permissions
3. ✅ **Create manually:** Extract script from workflow file if needed

---

## 💡 Best Practices

### 1. Edit Only English Version

✅ **DO:** Edit `README.md` only
❌ **DON'T:** Manually edit `README.ru.md` or `README.zh-CN.md`

**Why:** Translations are auto-generated. Manual edits will be overwritten.

### 2. Write Clear Descriptions

Good source text = good translations

**Good:**
> Ultra-fast recursive search tool written in Rust. Respects .gitignore by default.

**Bad:**
> Fast search thing.

### 3. Use Consistent Terminology

**Be consistent with technical terms:**
- Container (not Docker box)
- Repository (not repo in formal descriptions)
- Command-line (not CLI in full descriptions)

### 4. Review Translations

After automatic translation:
1. ✅ Check `README.ru.md` and `README.zh-CN.md`
2. ✅ Verify technical terms weren't mistranslated
3. ✅ Ensure formatting is preserved
4. 🐛 Open issue if systematic problems occur

### 5. Monitor Translation Performance

**Track translation quality:**
- Review translations after each update
- Check Actions logs for any errors
- Models are cached after first download for faster subsequent runs

**Performance:**
- First run: ~2-5 minutes (downloads models)
- Subsequent runs: ~30-60 seconds
- Completely free - no API costs!

### 6. Test Locally First

For major changes:

```bash
# Test translation before pushing
python scripts/translate_readmes.py

# Review diff
git diff README.ru.md

# If good, commit and push
git add README*.md
git commit -m "Major update to README"
git push origin main
```

---

## 📊 Workflow Examples

### Example 1: Adding New Tools

```bash
# 1. Edit English README
vim README.md
# Add tools to appropriate sections

# 2. Commit and push
git add README.md
git commit -m "add: ffmpeg and handbrake to video section"
git push origin main

# 3. Wait ~2-3 minutes for automatic translation
# 4. Pull translated versions
git pull origin main
```

### Example 2: Fixing Translation Error

```bash
# If you notice a translation error:
# 1. Check if it's a source problem
vim README.md
# Fix the English description if needed

# 2. Push the fix
git add README.md
git commit -m "fix: clarify description for tool X"
git push origin main

# 3. Translations regenerate automatically
```

### Example 3: Manual Translation Run

```bash
# Translate only to Russian (useful for testing)
# 1. Go to Actions tab
# 2. Click "Auto-Translate READMEs"
# 3. Click "Run workflow"
# 4. Set:
#    - Source: en
#    - Target: ru
# 5. Click "Run workflow"
```

---

## 🔍 Advanced: Workflow Customization

### Custom Trigger Paths

Edit `.github/workflows/auto-translate-readmes.yml`:

```yaml
on:
  push:
    branches:
      - main
    paths:
      - 'README.md'              # Main file
      # Add other files if needed:
      # - 'docs/README.md'
      # - 'CONTRIBUTING.md'
```

### Commit Message Customization

Change line 201:

```yaml
git commit -m "chore: auto-sync README translations"
```

To:

```yaml
git commit -m "🌍 Auto-update translations [skip ci]"
```

**Note:** `[skip ci]` prevents infinite loops.

### Email Notifications

Add to workflow:

```yaml
- name: Notify on failure
  if: failure()
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: smtp.gmail.com
    server_port: 465
    username: ${{ secrets.MAIL_USERNAME }}
    password: ${{ secrets.MAIL_PASSWORD }}
    subject: Translation workflow failed
    to: your-email@example.com
    from: GitHub Actions
    body: Check the workflow run at ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}
```

---

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [argostranslate Documentation](https://github.com/argosopentech/argos-translate)
- [LibreTranslate API](https://libretranslate.com/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Python `argostranslate` Library](https://pypi.org/project/argostranslate/)

---

## 🆘 Support

**Need help?**

- 💬 [Open a Discussion](https://github.com/cheesewhe/awesome-repositories-collection/discussions)
- 🐛 [Report a Bug](https://github.com/cheesewhe/awesome-repositories-collection/issues)
- 📖 Review workflow logs in Actions tab
- 🔍 Check existing issues for similar problems

---

## 🎯 Summary

**Workflow:**
1. ✍️ Edit `README.md` only
2. 🚀 Push to `main`
3. 🤖 Automatic translation happens
4. ✅ Pull and verify translations

**Remember:**
- Only edit English version
- Translations are automatic
- Review but don't manually edit translated files
- Monitor API costs
- Test major changes locally

Happy contributing! 🌍✨
