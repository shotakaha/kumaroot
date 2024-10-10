# セマンティック・バージョニングしたい（``commitizen``）

```console
$ cz commit
$ cz changelog --increment
$ cz bump
```

``commitizen``はGitを使ったバージョン管理をサポートしてくれるパッケージです。
コマンド名は``cz``です。
``cz サブコマンド``するだけで、セマンティック・バージョニングを簡単化できます。

## インストールしたい

- `pip`でインストール

```console
$ pip3 install commitizen
$ which cz
```

:::{note}

同じ名前の``npm``パッケージがあります。
自分がどちらを使っているのか、混乱しないようにしましょう。

:::

- `pipx`でインストール

```console
$ pipx install commitizen
$ which cz
~/.local/bin/cz
```

- `poetry`でインストール

```console
$ poetry add commitizen --group dev
```

Poetryを使ってチームで開発している場合は、開発環境にインストールしておくとよいかもしれません。
``commitizen``はパッケージでは直接使わないため、
``dev``グループに追加するとよいと思います。

## 初期化したい（``cz init``）

```bash
$ cd プロジェクト名
$ cz init
```

`cz init`で`commitizen`が使えるようにプロジェクトを初期化できます。
ターミナルに表示されるダイアログにしたがって矢印キーで選択すると、設定ファイルが作成されます。

Pythonパッケージを開発している場合は{file}`pyproject.toml`に設定を追加してまとめることができます。
その他の場合は、自分の好みの形式を選択すればよいと思います。
僕は{file}`.cz.toml`を選択する場合が多いです。

生成された設定ファイルは次のようになっていました。
最近のPythonパッケージは（暗黙の）ルールとして
``[tool.パッケージ名]``の下に設定を書くようになっています。
（ただの慣習なのか、それを定義したPEPが存在するかは未確認です）

```toml
[tool]
[tool.commitizen]
name = "cz_conventional_commits"
version = "0.0.1"
tag_format = "$version"
```

## コミットしたい（``cz c``）

```console
$ git add ステージしたいファイル名
$ cz commit
$ cz c
```

``cz``にステージするためのコマンドはないため``git add``でステージします。

ステージしたファイルがある状態で、``git commit``の代わりに``cz commit``（もしくは`cz c`）でコミットを作成します。

プロンプトが表示されるので、聞かれた内容に沿って情報を選択／入力するとコミットメッセージができあがります。

コミットメッセージのテンプレートは``cz info``もしくは``cz schema``、サンプルは``cz example``で確認できます。

## 変更ログしたい（``cz changelog``）

```console
// 変更ログを作成（すべてのログ）
$ cz changelog
$ cz ch

// 前回からの差分ログ
$ cz changelog --incremental

// 標準出力で確認
$ cz changelog --dry-run
```

`cz changelog`（もしくは`cz ch`）で、これまでのコミットログを使って変更ログ（changelog）を生成できます。
デフォルトのファイル名は``CHANGELOG.md``です。
ファイルがすでに存在する場合は上書きされます。
`--file-name`オプションで変更できます。

`--increment`オプションで、前回からの差分を追記できます。
このオプションの使用はデフォルトにするとよいと思います。

`--dry-run`オプションで事前確認できます。
ファイルに保存せず、標準出力に表示されます。

## バージョンアップしたい（``cz bump``）

```bash
$ cz bump --changelog --check-consistency
$ cz bump -ch -cc
```

``cz bump``で、これまでのコミットの内容／種類をベースに
``semver``に沿ったバージョン番号のタグを作成し、
設定ファイル内のバージョン番号を更新できます。
プログラムの開発にひと区切りついたら、タグをつけましょう。

``-ch``オプションを使うと、{file}`CHANGELOG.md`を更新できます。
バージョンアップしたり、変更履歴をまとたりする作業はなかなか大変ですが、一発でやってくれるのでとても助かります。

```{note}
使い始めてみるとすぐに気が付くと思いますが、
バージョンアップが先か、CHANGELOGの整理が先か問題があります。
僕はバージョンアップをしてから、CHANGELOGを整理することにしています。
```

## バージョン番号を一元管理したい

```toml
[tool]
[tool.commitizen]
...
version = "バージョン"
tag_format = "v$version"
version_files = [
    # "ファイルのパス:変数名" の形式
    "pyproject.toml:version",
    "src/__init__.py:__version__",
    "docs/conf.py:version",
    "docs/conf.py:release",

]
```

``[tool.commitizen.version_files]``に
`"ファイルのパス:変数名"`の形式で設定することで、
ソースコードの中にあるバージョン番号も
`cz bump`でまとめて更新できるようになります。

Pythonの場合、バージョン番号を書くファイルに決まりがありませんが、なんとなく、次のような慣習があります。

- ``src/__init__.py:__version__``
- ``src/__version__.py``

また、Sphinxでドキュメントを作成している場合は、
次のパスを設定すればOKです。

- `docs/conf.py:version`
- `docs/source/conf.py:version`（`--sep`した場合）

せっかく`commitizen`を使って`semver`管理しても、
ソースコードの中にバージョン番号が散らばっていたら、
意味がありません。
初期設定のときに追加しておくとよいと思います。

## フックしたい（`commitizen`）

```yaml
repos:
- repo: https://github.com/commitizen-tools/commitizen
  rev: v3.29.0
  hooks:
  - id: commitizen
    stages:
    - commit-msg
```

`commitizen (cz)`は[pre-commit](./python-pre-commit.md)に組み込むことができます。
`stages: [commit-msg]`でコミットメッセージを保存したあとにフックがかかるようにしておきます。
