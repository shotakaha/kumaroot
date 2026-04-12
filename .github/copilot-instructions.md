# Copilot Instructions for KumaROOT

## Build, lint, and validation commands

This repository is a documentation project. The main automated validation is Sphinx builds plus pre-commit checks.

| Purpose | Command |
| --- | --- |
| Install dependencies | `uv sync --all-extras` |
| Live preview | `task docs:serve` |
| Full lint/format validation | `uv run pre-commit run --all-files` |
| CI-equivalent docs build | `cd docs && uv run make dirhtml` |
| Static HTML build | `cd docs && uv run make html` |
| PDF build | `cd docs && uv run make latexpdf` |
| Build one page while editing | `cd docs && uv run sphinx-build -b dirhtml source build/dirhtml-single source/<section>/<page>.md` |

`task docs:build` currently invokes the live-preview target, so use `make dirhtml` or `make html` for non-interactive builds.

There is no separate unit-test suite in the repository; the narrowest scoped validation is building the affected page with `sphinx-build`.

## High-level architecture

- The repository’s source of truth is `docs/source/`. `docs/source/index.md` is the top-level site map and groups content into major categories with MyST `toctree` blocks.
- Each content area is centered on a hub page named `<topic>/<topic>-usage.md`. That hub page owns the section structure and links to the leaf pages for that topic. When adding a new page, register it in the corresponding `*-usage.md` file.
- Leaf pages are purpose-driven references such as `root/root-th1-fill.md` or `docker/docker-compose-up.md`, not API dumps. The site is organized as a “逆引き” reference: readers start from what they want to do.
- Sphinx is configured in `docs/source/conf.py`. It enables MyST, `sphinx_tags`, Japanese-language output, numbered figures/code blocks, OGP metadata, and PDF output settings. Tag pages under `docs/source/_tags/` are produced from front matter tags via `sphinx_tags`.
- Publishing and CI both build the docs from the same tree under `docs/`: PR validation runs `make dirhtml`, and GitHub Pages deploys `docs/build/dirhtml/`.

## Key conventions

- Write documentation in Japanese unless the technical content is naturally English. Follow JTF-style punctuation: use `。` and `、`, and do not insert spaces between Japanese and English terms.
- Keep the information architecture consistent:
  - Hub/index page: `<topic>/<topic>-usage.md`
  - Regular content page: `<topic>/<topic>-<feature>.md`
  - Docker example pages: `docker/docker-example-<name>.md`
- Organize pages around user intent. Titles and major sections commonly use the “〇〇したい” pattern rather than taxonomy-first headings.
- ROOT technical reference pages follow a repeatable structure: start with a practical C++ example with explicit `#include` lines, then provide the Python equivalent when applicable, then add a concise signature/parameter explanation, then use-case-specific sections.
- Prefer short, practical examples before long explanation. For ROOT docs, include explicit headers in every C++ snippet.
- Use MyST Markdown features that are already enabled in the project (`toctree`, colon-fence admonitions, definition lists, math, task lists) instead of switching formats unnecessarily.
- Versioning uses a calendar-based semver hybrid managed by Commitizen. `pyproject.toml` and `docs/source/conf.py` both carry the version and are updated together by the `task bump:*` commands.
- Conventional commits are enforced. For most documentation changes, use `fix(<scope>): <subject>` rather than `feat`.
