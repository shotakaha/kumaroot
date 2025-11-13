# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**KumaROOT** is a documentation project for high-energy physics tools (mainly ROOT). The documentation uses Sphinx with MyST Parser (supporting both Markdown and reStructuredText).

**Key characteristics:**

- Target audience: Physics students/researchers with basic ROOT knowledge
- Purpose: "逆引き形式" (inverted reference/purpose-based organization) - "〇〇したい" (I want to do X)
- Language: Japanese (with some English technical content)
- Built with Sphinx + MyST Parser, published on Read the Docs

## Development Commands

### Setup

```bash
poetry install --no-root
source .venv/bin/activate
```

### Documentation Preview

```bash
task docs
# Opens http://localhost:8000 with live reload
# Runs: cd docs && poetry run make livehtml

# Or manually:
cd docs && make livehtml
```

### Dependency Management

```bash
task update      # Update all dependencies + export requirements.txt
task outdated    # Show outdated packages
task export      # Export requirements.txt
```

### Version Management (Commitizen)

```bash
task bump             # Bump PATCH version with commitizen
task bump:minor       # Bump MINOR version with commitizen
task changelog        # Generate incremental changelog
```

**Custom Versioning Scheme:**

This project uses a **calendar-based semantic versioning** scheme:

- **MAJOR version**: Incremented when the calendar year changes（e.g., 2024.x.x → 2025.x.x）
- **MINOR version**: Incremented when the calendar month changes（e.g., 2025.11.x → 2025.12.x）
- **PATCH version**: Incremented for each `fix` or `feat` commit

**Important notes:**

- `task bump` always uses `--increment PATCH`（configured in Taskfile.yml）
- Automatic increment detection is disabled; all bumping is explicit
- When a new year/month begins, manually bump MAJOR or MINOR as needed
- Example version progression: `2025.11.6` → `2025.11.7`（patch）→ `2025.12.0`（new month）→ `2026.1.0`（new year）

### Code Quality

```bash
task pre-commit      # Run all pre-commit hooks on all files
```

### Building Distribution

```bash
make latexpdf        # Generate PDF in docs/
make html            # Generate HTML in docs/_build/
```

## Documentation Structure

### Directory Organization

```text
docs/source/
├── docker/           # Docker containerization examples
├── command/          # Command-line tools (git, npm, etc.)
├── python-*/         # Python library guides
├── geant4/           # GEANT4 simulation framework
├── root/             # ROOT data analysis framework
├── git/              # Git version control
├── html/             # HTML/CSS topics
├── typst/            # Typst document preparation
├── gas/              # Google Apps Script
├── emacs/            # Emacs editor
├── hugo/             # Hugo static site generator
└── conf.py           # Sphinx configuration
```

### File Naming Convention

- **Usage/getting started**: `<category>/<category>-usage.md`
- **Features/examples**: `<category>/<category>-<feature>.md`
- **Docker examples**: `docker/docker-example-<osname>.md`

Example:

- `docker/docker-examples.md` - Main index with toctree
- `docker/docker-example-ubuntu.md` - Ubuntu Docker guide
- `docker/docker-example-almalinux.md` - AlmaLinux Docker guide

## Documentation Style Guidelines

### Japanese Text Formatting

- Follow **JTF (Japan Typesetting Foundation) style guide** for spacing and punctuation
- Use full-width Japanese punctuation: `。` (period) and `、` (comma)
- Remove spaces between Japanese and English: `DockerコンテナーでRaspberry Pi環境` not `Docker コンテナーで Raspberry Pi 環境`
- Use katakana for foreign words: `オススメ` not `お勧め`
- Use hiragana for common verbs: `もっとも` not `最も`

### Content Organization - "逆引き形式"

Each guide follows purpose-driven organization:

1. **Title**: `<Purpose>したい（`identifier`）` (e.g., "Ubuntuしたい（`ubuntu`）")
2. **Overview**: Brief explanation of what this tool/service is
3. **Basic Setup**: docker-compose.yaml or installation example first
4. **Use Cases**: 3-5 practical scenarios with code examples
   - パッケージをインストールしたい (I want to install packages)
   - 開発環境として使いたい (I want to use as dev environment)
   - テスト環境として使いたい (I want to use as test environment)
5. **Version/Characteristics Info**: Comparison tables
   - バージョンについて (Version information)
   - 特徴 (Characteristics) - Merits, Demerits, Best use cases
6. **References**: Links to official documentation

### Code Examples

- Lead with practical code (YAML, config) before explanations
- Include console output with `$ prompt` format
- Use Japanese comments with English code
- Show expected output/results

## Pre-commit Hooks Configuration

The repository uses pre-commit hooks for code quality:

```yaml
# .pre-commit-config.yaml
- Commitizen: Validates commit messages (conventional commits)
- Poetry: Validates pyproject.toml and poetry.lock
- Standard hooks: Trailing whitespace, merge conflicts, case conflicts
- JSON/TOML/YAML/XML validation
- Ruff: Python code formatting
```

**Important notes:**

- All commits must follow conventional commit format (enforced by commitizen)
- The repository uses `poetry check --lock` (strict mode)
- Pre-commit hook may auto-format markdown/Python code
- If formatting changes occur after commit, the commit will be retried with amended changes

## Sphinx Configuration

**Key extensions:**

- `myst_parser`: Markdown support with extended syntax
- `sphinx_tags`: Tag-based navigation
- `sphinx_rtd_theme`: Read the Docs theme
- `sphinx_design`: Card/grid layouts
- `sphinx_copybutton`: Copy code button
- `sphinxcontrib.mermaid`: Diagram support

**MyST Parser enabled extensions:**

- Math: amsmath, dollarmath
- Content: colon_fence, deflist, fieldlist, html_admonition, html_image
- Text: replacements, smartquotes, strikethrough, substitution, tasklist

**Markdown features:**

- Code fences with syntax highlighting
- Math: `$inline$` and `$$display$$`
- Definition lists, task lists
- Admonitions: `:::{note}`, `:::{warning}`, etc.
- Strikethrough: `~~text~~`

## Common Workflows

### Adding a New Docker Example

1. Create `docker/docker-example-<osname>.md`
2. Follow the structure: Title → Overview → Setup (YAML) → Use cases → Version table → Characteristics
3. Add entry to `docker/docker-examples.md` toctree
4. Include characteristics section with: メリット (Merits), デメリット (Demerits), 最適な用途 (Best use cases)
5. Run `task pre-commit` to validate
6. Commit with conventional format: `fix(docker-<osname>): add <description>`

### Adding a New Guide

1. Create `<category>/<category>-<feature>.md`
2. Register in toctree of main index file
3. Follow purpose-based ("したい") organization
4. Include code examples before explanations
5. Ensure JTF style compliance

### Updating Version Information

- Check official release schedules
- Update version tables with: バージョン (Version) | リリース日 (Release date) | サポート終了 (End of support) | 特徴 (Features)
- Use Japanese date format: YYYY年M月D日 (e.g., 2025年11月13日)

### Building and Deploying

- **Read the Docs (automatic)**: Push to main → RTD builds automatically
- **Local preview**: `task docs` or `cd docs && make livehtml`
- **PDF generation**: `make latexpdf` (output: `docs/_build/latex/`)

## Git Workflow

**Conventional Commit Format** (enforced by commitizen):

```text
<type>(<scope>): <subject>

<body (optional)>

<footer (optional)>
```

**Commit types used in this project:**

- `fix()`: Documentation updates, bug fixes, and corrections (primary type for this documentation project)
- `refactor()`: Reorganization without functionality change
- `bump()`: Version bumping (handled by `task bump`)
- `feat()`: New features (rarely used)

**Examples:**

- `fix(docker-example-ubuntu): add characteristics section`
- `fix(docker-example-almalinux): add AlmaLinux container documentation`
- `fix(docker-example-raspi): add comprehensive version information tables`
- `fix(CLAUDE): add CLAUDE.md developer guidance file`
- `bump: version 2025.11.6 → 2025.11.7`

**Note:** Since this is primarily a documentation project, use `fix()` for all documentation changes (content additions, updates, improvements, new guides, etc.). Reserve `refactor()` for reorganizing existing content structure.

**Branch strategy:**

1. Create feature branch from `main`
2. Make changes and commit with conventional format
3. Push to GitHub and create Pull Request
4. Automatic tests validate PR
5. Merge after tests pass

## Important Notes for Future Development

### Japanese Text Processing

- Always validate JTF style compliance with pre-commit hooks
- Common errors: spacing between Japanese/English, wrong punctuation marks
- Tools: Repository has linting for Japanese text via pre-commit

### Documentation Priority

- This is a **documentation project**, not a software project
- Content accuracy and clarity are paramount
- Always verify version numbers, dates, and support timelines
- Include practical examples users can copy-paste

### Sphinx/MyST Specific

- Use `# Heading` syntax (not over/underline)
- MyST admonitions: `:::{note}`, `:::{warning}`, `:::{tip}`
- Links to files: `[filename.ts](src/filename.ts)` markdown format
- Code blocks specify language: ` ```python`

### Poetry & Dependencies

- Project requires Python ≥ 3.12
- Optional dev dependencies include: pandas, jupyterlab, scipy, scikit-learn, matplotlib
- Use `task update` to keep dependencies current
- Maintain both `pyproject.toml` and `requirements.txt`

### Version Management Strategy

This project uses **calendar-based semantic versioning** (YYYY.MM.PATCH):

**When to bump versions:**

- **PATCH**: After each content addition, improvement, or bug fix (`fix` or `feat` commits)
  - Use: `task bump`
  - Example: `2025.11.6` → `2025.11.7`

- **MINOR**: When the calendar month changes
  - Use: `task bump:minor`
  - Example: `2025.11.x` → `2025.12.0`
  - Usually done manually on the first commit of a new month

- **MAJOR**: When the calendar year changes
  - Use: `cz bump --increment MAJOR`
  - Example: `2025.x.x` → `2026.1.0`
  - Reset MINOR to 1 and PATCH to 0 when entering a new year

**Important constraints:**
- Do NOT use automatic increment detection (`cz bump` without `--increment`)
- All bumping is explicit via configured task commands
- MAJOR/MINOR bumps must be coordinated with the actual calendar date
- Each PATCH bump automatically creates a git tag and updates CHANGELOG

## Tag System

The repository uses `sphinx_tags` for categorizing content:

- Tags are assigned in front matter (YAML)
- Automatic tag index generation in `docs/source/_tags/`
- Useful for grouping related documentation across categories
