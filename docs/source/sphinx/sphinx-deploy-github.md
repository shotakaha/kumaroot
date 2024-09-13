# GitHub Actionsしたい（`.github/workflows/static.yml`）

GitHub Actionsを設定することで、Sphinxで生成したドキュメントを
GitHub Pagesに自動で公開できるようになります。
設定は``.github/workflows/``の中にYAML形式で記述します。

以下では、
デフォルトブランチ（`main`）にプッシュした場合と、
それ以外のブランチにプッシュした場合に分けたサンプルです。

## デフォルトブランチ

- `.github/workflows/static.yml`

```yaml
# ワークフローの説明
name: Deploy Sphinx Document to GitHub Pages

# 実行するタイミングを設定
on:
  # デフォルトブランチにプッシュした場合
  push:
    branches: ["main"]
  # GitHub Actionのページで手動で実行した場合
  workflow_dispatch:

# 権限の設定
permissions:
  contents: read
  pages: write
  id-token: write

#
concurrency:
  group: "pages"
  cancel-in-progress: false

# ジョブの設定
jobs:
  deploy:
    # 環境変数
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    # 実行OS
    runs-on: ubuntu-latest
    # ステップの設定
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Install Poetry
        run: pipx install poetry
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "poetry"
      - name: Check poetry
        run: |
          poetry --version
          poetry config --list
      - name: Show outdated packages
        run: poetry show --outdated
      - name: Install dependencies
        run: poetry install
      - name: Build sphinx document
        run: |
          cd docs
          poetry run make dirhtml
      - name: Setup Pages
        uses: actions/configure-pages@v5
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: "./docs/_build/dirhtml/"
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

## それ以外のブランチ

- `.github/workflows/branch.yml`

```yaml
name: Check Sphinx Build on Branches

on:
  push:
    branches-ignore: ["main"]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Install Poetry
        run: pipx install poetry
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "poetry"
      - name: Check poetry
        run: |
          poetry --version
          poetry config --list
      - name: Show outdated packages
        run: poetry show --outdated
      - name: Install dependencies
        run: poetry install
      - name: Build sphinx
        run: |
          cd docs
          poetry run make dirhtml
          ls -ltr _build/
          ls -lst _build/dirhtml/
```

## リファレンス

- [actions/checkout](https://github.com/actions/checkout)
- [actions/setup-python](https://github.com/actions/setup-python)
- [actions/configure-pages](https://github.com/actions/configure-pages)
- [actions/upload-pages-artifact](https://github.com/actions/upload-pages-artifact)
- [actions/deploy-pages](https://github.com/actions/deploy-pages)
