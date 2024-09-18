# GitHub Actionsしたい

## Changelogを定期更新したい

```{code-block} yaml
---
caption: .github/workflows/update_changelog.yml
---
name: Update Changelog


on:
  schedule:
    # 毎週月曜日の午前0時5分（UTC）に実行
    # cronの書式: 分 時 日 月 曜日
    - cron: "5 0 * * 1"
  workflow_dispatch: # 手動トリガーを有効にする

jobs:
  update_changelog:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        # リポジトリをチェックアウトする
        # czでタグ情報も必要になるため
        # すべての履歴とタグを取得する
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # すべての履歴とタグを取得
      - name: Setup Python
        # Pythonをセットアップする
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install Commitizen
        # pipxでcommitizenをインストール
        run: pipx install commitizen
      - name: Update Changelog
        # 変更履歴の差分を生成する
        run: cz changelog --incremental
      - name: Commit Changes
        # git status --porcelain で変更の有無を確認
        # 変更がある場合はコミットする
        #  - ユーザー名: GitHub Actions
        #  - メールアドレス: github-actions[bot]
        #  - メッセージ: [skip ci]をつける
        # 変更がない場合はメッセージを残す
        run: |
          if [ -n "$(git status --porcelain)" ]; then
            git config --global user.email "github-actions[bot]@users.noreply.github.com"
            git config --global user.name "GitHub Actions"
            git add CHANGELOG.md
            git commit -m "chore: update changelog [skip ci]"
            git push origin main
          else
            echo "No changes in CHANGELOG.md Skipping commit."
          fi
```


## Dependabotしたい

[Dependabot](https://docs.github.com/ja/code-security/dependabot/working-with-dependabot)は、プロジェクトで使っているツールが依存している
パッケージに更新があったことを、
プルリクエストにできるツールです。

```{code-block} yaml
---
caption: .github/dependabot.yml
---
version: 2

# 依存関係のアップデートに関する設定
updates:
# - package-ecosystem: "poetry" # パッケージマネージャー
#   directory: "/"  # 依存関係を管理するファイルがあるパス
#   schedule:
#     interval: "daily", "weekly", "monthly" のいずれか
  - package-ecosystem: "poetry"
    directory: "/"
    schedule:
      interval: "weekly"
#  パッケージマネージャーを追加する場合
#  - package-ecosystem: "npm"
#    directory: "/"
#    schedule:
#      interval: "montly"

# 依存関係のアップデートがあった場合
# pull-requestを作成してお知らせ
```
