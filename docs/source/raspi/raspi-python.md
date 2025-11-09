```{tags} raspi, python
```

# Pythonしたい

```bash
sudo apt install python3-pip python3-venv python3-dev
```

まず基本的なPythonツールをインストールします。

- `python3-pip` - Pythonパッケージマネージャー
- `python3-venv` - 仮想環境作成ツール
- `python3-dev` - Python開発用ヘッダーファイル

## pipxをインストールしたい

```bash
sudo apt install pipx
pipx ensurepath
```

`pipx`はPythonツールをシステム全体に影響を与えずに、独立した環境にインストールできるツールです。
インストール後は`pipx ensurepath`でパスを設定してください。

## uvをインストールしたい

```bash
pipx install uv
uv --version
```

Raspberry PiでPython開発ツールを使用するために、`uv tool install`でCLIツールをインストールします。
`uv`は`apt`パッケージが存在しないため、`pipx`を使ってインストールします。

## ruffをインストールしたい

```bash
uv tool install ruff

# コードをチェック
ruff check .

# 自動フォーマット
ruff format .
```

`ruff`はPythonコードのリンティングとフォーマッティングを高速に行うツールです。

## pre-commitをインストールしたい

```bash
uv tool install pre-commit

# .pre-commit-config.yaml を作成して設定
pre-commit install

# 手動でテスト実行
pre-commit run --all-files
```

`pre-commit`はGitコミット前に自動的に検査を実行するツールです。

## インストール済みツールを確認したい

```bash
uv tool list
```

## ツールをアップグレードしたい

```bash
uv tool upgrade <ツール名>
uv tool upgrade --all
```

## リファレンス

- [uv Documentation](https://docs.astral.sh/uv/)
- [ruff Documentation](https://docs.astral.sh/ruff/)
- [pre-commit Documentation](https://pre-commit.com/)
- [Python Official Documentation](https://docs.python.org/3/)
