# セマンティック・バージョニングしたい（``commitizen``）

```console
$ cz commit
$ cz changelog --increment
$ cz bump
```

``commitizen``（``cz``）はGitのコミットメッセージをテンプレート化し、セマンティック・バージョニング（semantic versioning）に基づいたバージョン管理を簡単にするツールです。

コミットメッセージを入力するだけで、ルールに沿った変更履歴（CHANGELOG）の生成やバージョンタグの自動作成ができます。

## インストールしたい（`commitizen`）

- pipxでインストール

```console
$ pipx install commitizen
$ which cz
~/.local/bin/cz
```

`commitizen`はグローバルに使うCLIなので、
`pipx`で隔離してインストールするとよいです。

- pipでインストール

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install commitizen
$ which cz
```

プロジェクトで使う場合は、[venv](./python-venv.md)で作った仮想環境にインストールする方法でもよいです。

- uvでインストール

```console
$ uv add commitizen --dev
```

- Poetryでインストール

```console
$ poetry add commitizen --group dev
```

チームで開発する場合、プロジェクトに開発環境として含めておくと便利です。`commitizen`はツールとして使うだけなので、`dev`グループに追加します。

:::{note}

同じ名前の`npm`パッケージがありますが、まったく別のプロジェクトです。
自分がどちらを使っているのか混乱しないようにしましょう。

:::

## 初期化したい（``cz init``）

```console
$ cd プロジェクト名
$ cz init
```

`cz init`コマンドでプロジェクトを初期化し、`commitizen`の設定ファイルを作成します。
ターミナルに表示されるダイアログに従い、矢印キーで選択します。

### 設定ファイルの配置

Pythonパッケージを開発している場合は、{file}`pyproject.toml`に設定を追加する方法を推奨します。
その他の場合は、{file}`.cz.toml`など好みの形式を選択できます。

### 初期設定ファイルの例

生成された設定ファイルは以下のようになっています。

```toml
[tool.commitizen]
name = "cz_conventional_commits"
version = "0.0.1"
tag_format = "$version"
```

## コミットしたい（``cz commit``）

```console
$ git add ファイル名
$ cz commit
```

`cz commit`（短縮形：`cz c`）でコミットを作成します。
通常の`git commit`の代わりです。
ファイルのステージングはいつもどおり`git add`してください。

プロンプトが表示されるので、聞かれた内容に沿って情報を選択・入力すると、セマンティック・バージョニングに対応したコミットメッセージが自動生成されます。

### テンプレートの確認

- `cz info` - コミットメッセージのテンプレートを表示
- `cz schema` - 詳細なスキーマを表示
- `cz example` - テンプレートの使用例を表示

## 変更ログしたい（``cz changelog``）

```console
$ cz changelog
```

`cz changelog`（短縮形：`cz ch`）で、コミットログから自動的に変更ログ（CHANGELOG）を生成できます。

デフォルトでは`CHANGELOG.md`というファイル名で作成されます。
すでに存在する場合は上書きされます。

### 変更ログのオプション

```console
# 前回からの差分のみを追記
$ cz changelog --increment

# ファイルに保存せず、標準出力で確認
$ cz changelog --dry-run

# ファイル名を変更
$ cz changelog --file-name HISTORY.md
```

### 推奨される使い方

新しいバージョンをリリースするときは、`--increment`オプションを使って前回からの変更分だけを追記するのが便利です。

## バージョンアップしたい（``cz bump``）

```console
$ cz bump --changelog --check-consistency
```

プログラムの開発にひと区切りついたら、`cz bump`でバージョンアップします。

このコマンドは以下の処理を自動で行います：

- コミット履歴をもとに、セマンティック・バージョニング（semver）に従ったバージョン番号を決定
- 設定ファイル内のバージョン番号を更新
- Gitタグを作成
- `CHANGELOG.md`を更新（`--changelog`オプション使用時）
- 複数ファイルのバージョン番号を一括更新（設定済みの場合）

### よく使うオプション

```console
# CHANGELOG.md を更新して、バージョン番号の一貫性をチェック
$ cz bump --changelog --check-consistency

# 短縮形
$ cz bump -ch -cc
```

### バージョンタイプを指定したい

通常、commitizenはコミット履歴から自動的にバージョンを決定しますが、明示的に指定することもできます：

```console
# パッチ版をリリース（例：1.0.0 -> 1.0.1）
$ cz bump --increment PATCH

# マイナー版をリリース（例：1.0.0 -> 1.1.0）
$ cz bump --increment MINOR

# メジャー版をリリース（例：1.0.0 -> 2.0.0）
$ cz bump --increment MAJOR

# CHANGELOG も同時に更新
$ cz bump --increment PATCH --changelog
```

### 詳細なオプション一覧

| オプション | 短縮形 | 説明 |
|-----------|-------|------|
| `--changelog` | `-ch` | `CHANGELOG.md`を更新する |
| `--check-consistency` | `-cc` | バージョン番号の一貫性をチェック |
| `--increment MAJOR\|MINOR\|PATCH` | | バージョンタイプを指定 |
| `--dry-run` | | 実際には変更せず、どのような操作を行うか表示 |
| `--no-verify` | | pre-commitフックをスキップ |

```{note}
バージョンアップとCHANGELOGの管理は、バージョンアップを先に行い、その後CHANGELOGを整理するのが推奨されます。
```

## バージョン番号を一元管理したい

プロジェクトの複数の場所にバージョン番号が散らばっていると、`cz bump`で更新するたびに手動で修正する手間が増えます。
`version_files`を設定することで、`cz bump`時にすべてのバージョン番号を一括更新できます。

### 設定方法

```toml
[tool.commitizen]
version = "0.1.0"
tag_format = "v$version"
version_files = [
    "pyproject.toml:version",
    "src/__init__.py:__version__",
    "docs/conf.py:version",
]
```

`version_files`に`ファイルパス:変数名`の形式で設定します。

### Pythonプロジェクトでの慣例

バージョン番号を管理するファイル：

- `pyproject.toml` - プロジェクト設定ファイル（推奨）
- `src/__init__.py` - パッケージの`__version__`変数
- `src/__version__.py` - バージョン専用ファイル

### ドキュメント設定

Sphinxでドキュメントを作成している場合：

- `docs/conf.py:version` - 通常のSphinx設定
- `docs/source/conf.py:version` - `--sep`オプション使用時

複数のファイルにバージョン番号を定義している場合は、初期設定のときにまとめて追加しておくことをオススメします。

## フックしたい（`commitizen`）

[pre-commit](./python-pre-commit.md)フレームワークを使用することで、`commitizen`をGitフックとして自動実行できます。

```yaml
repos:
- repo: https://github.com/commitizen-tools/commitizen
  rev: v3.29.0
  hooks:
  - id: commitizen
    stages:
    - commit-msg
```

`stages: [commit-msg]`を指定することで、コミットメッセージが保存されたあとに検証が実行されます。
これにより、セマンティック・バージョニングに従わないコミットメッセージは自動的に拒否されます。
