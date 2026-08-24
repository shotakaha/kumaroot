# ランタイム管理したい（`mise`）

```console
$ mise use python@3.11
```

`mise`（ミーズ）は、開発環境で使うランタイム（実行環境）を切り替えるコマンドです。

`mise`で追加したランタイムは、`~/.local/share/mise/installs/`に配置されます。
`mise activate`で有効にしたシェルセッションでは、このパスが`PATH`の先頭に追加され、優先的に見つかるようになります。
また、`mise plugins`で、ランタイムごとの対応をプラグイン形式で追加できます。

:::{note}

Homebrewでインストールしたパッケージを上書きしたり、削除したりするわけではありません。
`mise`が有効化されていないセッションでは、いつも通りHomebrewのパッケージが使用できます。

:::

## インストールしたい（`mise`）

```console
$ brew install mise

$ mise --version
2026.8.11 macos-x64 (2026-08-23)    # Intelの場合
2026.8.11 macos-arm64 (2026-08-23)  # Apple Siliconの場合
```

`mise`はHomebrewでインストールできます。
フォーミュラ名は`mise`です。

:::{note}

2024年1月に[コマンド名がrtxからmise](https://github.com/jdx/mise/releases/tag/v2024.1.0)されました。

:::

## 設定したい（`mise.toml`）

```console
$ mise config ls
PATH                         Tools
~/.config/mise/config.toml   node
./mise.toml                  python
```

`mise.toml`で、`mise`の設定を管理できます。
プロジェクト単位の設定は`./mise.toml`、
ユーザー設定は`~/.config/mise/config.toml`
を使います。

同じランタイムが両方の設定ファイルに書かれている場合は、プロジェクト単位の設定が優先されます。

```console
$ mise config ls
```

`mise config ls`（`config list`）で、現在有効な設定ファイルと、ランタイムがどちらの設定に由来するかを確認できます。

## ランタイムを再現したい（`mise install`）

```console
$ cat mise.toml
[tools]
python = "3.10"
node = "18"

$ mise install
mise node@18.20.8       [1/3] download node-v18.20.8-darwin-arm64.tar.gz
mise node@18.20.8       [2/3] checksum node-v18.20.8-darwin-arm64.tar.gz
mise node@18.20.8       [3/3] extract node-v18.20.8-darwin-arm64.tar.gz
mise python@3.10.21     [1/3] extract cpython-3.10.21+...-install_only_stripped.tar.gz
mise python@3.10.21   ✓ installed
mise node@18.20.8     ✓ installed
```

`mise install`で、`mise.toml`の設定にあるランタイムを一括でインストールできます。
`mise.toml`を共有すれば、他のマシンやCI環境でも同じランタイム構成を再現できます。

```console
$ mise install python@3.12
mise python@3.12.14 ✓ installed
mise WARN  python installed but not activated — it is not in any config file.
To install and activate, run:
  mise use python
```

`mise install python@3.12`のように、引数を指定すると、そのランタイムだけを`~/.local/share/mise/installs/`にインストールします。
この場合は`mise.toml`に追記されません。

ランタイムの切り替えは`mise use`で行います。

## ランタイムを有効／無効にしたい（`mise activate` / `mise deactivate`）

:::{note}
2023年11月に[fishで自動的に有効](https://github.com/jdx/mise/releases/tag/v2023.11.9)にする機能が追加されました。
なので、このコマンドはもう必要ありません。
:::

```console
$ eval "$(mise activate bash)"
$ eval "$(mise activate zsh)"
$ mise activate fish | source
$ execx($(mise activate xonsh))
```

`mise activate`で、現在のセッションで`mise`を有効にできます。
利用するシェルによって、コマンドが異なります。
`mise`をお試しで使ってみたい場合によいでしょう。
常用する場合は、シェルの設定ファイルに追記します。

```console
$ mise deactivate
```

`mise deactivate`で、セッションを無効にできます。

## ランタイムを確認したい（`mise ls`）

```console
$ mise ls
Tool      Version   Config Source                 Requested
node      23.0.0    ~/.config/mise/config.toml    latest
python    3.11.10
```

`ls`（`list`）コマンドで設定されているランタイムと`mise`設定のパスを確認できます。

## ランタイムを切り替えたい（`mise use`）

```console
// プロジェクト（＝現在のディレクトリ）に追加
$ mise use python@3.11
python@3.11.16
mise /tmp/test-mise/mise.toml tools: python@3.11.16

$ cat ./mise.toml
[tools]
python = "3.11"
```

`use`（`u`）コマンドでランタイムのバージョンを切り替えることができます。
設定は`./mise.toml`に保存されます。

指定したバージョンのランタイムが見つからない場合は、`mise install`コマンドが自動実行され、
`~/.local/share/mise/installs/`の中にインストールされます。
実行ファイルはバージョンごとに分けてインストールされます。

```console
// システムに追加
$ mise use --global python@3.12
$ cat ~/.config/mise/config.toml
[tools]
python = "3.12"

[env]
```

`--global`オプションでユーザー設定に追加できます。
設定は`~/.config/mise/config.toml`に保存されます。

## ランタイムを更新したい（`mise upgrade`）

```console
$ mise ls
Tool    Version            Config Source              Requested
python  3.12.2 (outdated)  ~/.config/mise/config.toml 3.12

$ mise upgrade
mise python@3.12.3 ✓ installed
mise python@3.12.2 ✓ removing ~/.local/share/mise/installs/python/3.12.2

$ mise ls
Tool    Version  Config Source             Requested
python  3.12.3  ~/.config/mise/config.toml 3.12
```

`mise upgrade`（`up`）コマンドで、指定したランタイムを最新バージョンに更新できます。
`mise ls --outdated`で、更新可能なランタイムを確認できます。

## ランタイムを削除したい（`mise uninstall`）

```console
$ mise uninstall python@3.12
mise python@3.12 ✓ removing ~/.local/share/mise/installs/python/3.12
```

`mise uninstall`コマンドで、指定したランタイムを削除できます。

## ランタイムの提供元を調べたい（`mise registry`）

```console
$ mise registry uv
aqua:astral-sh/uv asdf:asdf-community/asdf-uv pipx:uv

$ mise registry node
core:node

$ mise registry poetry
vfox:mise-plugins/vfox-poetry pipx:poetry
```

`registry`コマンドで、ツール名がどのバックエンド経由でインストールされるかを確認できます。
複数のバックエンドが表示される場合、先頭が優先的に使われます。

- `core:` — mise本体に組み込み（プラグイン不要）
- `aqua:` / `npm:` / `cargo:` / `pipx:`など — 各パッケージレジストリ経由（プラグイン不要）
- `asdf:` / `vfox:` — プラグイン（Gitリポジトリ）経由

`asdf:`や`vfox:`だけが表示されるツールは、`mise use`や`mise install`の際にプラグインが自動でインストールされます。

```console
$ mise registry --backend aqua
```

`--backend`オプションで、特定のバックエンドが使われているツールだけに絞り込めます。

## プラグインのバージョンを一覧したい（`mise ls-remote`）

```console
$ mise ls-remote プラグイン名
$ mise ls-remote python
$ mise ls-remote uv
$ mise ls-remote node
$ mise ls-remote go
```

`ls-remote`（`list-remote` / `list-all`）コマンドで、インストールできるバージョンを一覧できます。

```console
$ mise ls-remote uv | fzf
```

たくさんのバージョンが表示されるため、
`peco`や`fzf`にパイプして絞り込むとよいです。

## プラグイン名を確認したい（`mise plugins ls-remote`）

```console
$ mise plugins ls-remote
```

`plugins ls-remote`（`plugins list-remote` / `plugins list-all`）コマンドで、利用できるプラグイン名を一覧できます。

```console
$ mise plugins ls-remote | rg uv
uv
```

たくさんのプラグインが表示されるため、`rg`や`grep`で絞り込むとよいです。

## プラグインを追加したい（`mise plugins install`）

```console
$ mise plugins install プラグイン名
$ mise plugins install poetry
mise plugin:poetry      clone https://github.com/mise-plugins/vfox-poetry.git
mise plugin:poetry    ✓ https://github.com/mise-plugins/vfox-poetry.git#3dec0d6
```

`plugins install`（`i` / `a` / `add`）コマンドで、プラグインをインストールできます。
実体はGitHubリポジトリで、`~/.local/share/mise/plugins/`にcloneされます。

:::{note}

`uv`や`node`のように`aqua`バックエンドで提供されているツールは、プラグインなしで直接インストールできます。
`mise use`や`mise install`でツールを指定すると、プラグインが必要な場合のみ自動でインストールされるため、`plugins install`を明示的に使う機会は多くありません。

:::

## プラグインを確認したい（`mise plugins ls`）

```console
$ mise plugins ls
poetry

$ mise plugins ls --urls
poetry  https://github.com/mise-plugins/vfox-poetry.git  HEAD 3dec0d6
```

`plugins ls`（`plugins list`）コマンドで、インストール済みのプラグインを確認できます。
`--urls`オプションで、プラグインのリポジトリURLと現在のコミットも確認できます。

## プラグインを更新／削除したい（`mise plugins update` / `mise plugins uninstall`）

```console
$ mise plugins update poetry
mise plugin:poetry      update git repo
mise plugin:poetry    ✓ https://github.com/mise-plugins/vfox-poetry.git#3dec0d6
```

`plugins update`（`up` / `upgrade`）コマンドで、プラグイン自体を最新化できます。
ランタイムのバージョンではなく、プラグインのコード（Gitリポジトリ）が更新される点に注意してください。

```console
$ mise plugins uninstall poetry
mise plugin:poetry      uninstall
mise plugin:poetry      remove ~/.local/share/mise/plugins/poetry
mise plugin:poetry    ✓ uninstalled
```

`plugins uninstall`（`remove` / `rm`）コマンドで、プラグインを削除できます。

## Pythonを使いたい（`mise use python`）

```console
$ mise use python
$ mise use python@バージョン

// $HOMEで実行した場合
$ mise use -g python  # システム全体（--global）はlatest を利用する
mise ~/.config/mise/config.toml tools: python@3.12.2

$ mise ls python
python  3.12.2   ~/.config/mise/config.toml latest

$ which python
~/.local/share/mise/installs/python/latest/bin/python

// $KumaROOTで実行した場合
$ mise use python@3.11  # このリポジトリは3.11を指定する
mise ~/repos/github.com/shotakaha/kumaroot/mise.toml tools: python@3.11.8

$ mise ls python
Tool    Version  Config Source                                   Requested
python  3.11.6
python  3.11.8   ~/repos/github.com/shotakaha/kumaroot/mise.toml 3.11
python  3.12.2

$ which python
~/.local/share/mise/installs/python/3.11/bin/python
```

`uv`もmiseで一緒に管理できます。

```console
$ mise use python@3.11 uv@latest
$ cat ./mise.toml
[tools]
python = "3.11"
uv = "latest"

$ which uv
~/.local/share/mise/installs/uv/0.12.5/bin/uv
```

## Nodeを使いたい（`mise use node`）

```console
$ mise use node@20
$ mise ls node
Tool  Version  Config Source                Requested
node  20.20.2  ~/repos/example/mise.toml    20

$ which node
~/.local/share/mise/installs/node/20.20.2/bin/node
```

`mise use node@バージョン`で、プロジェクトごとにNodeのバージョンを切り替えられます。
Homebrewなどでインストールしたシステム全体の`node`とは別に管理されるため、プロジェクトごとに異なるバージョンを使い分けたい場合に便利です。

## Hugoを使いたい（`mise use hugo`）

```console
$ mise plugins install hugo
$ mise use hugo@latest
$ cat ./mise.toml
[tools]
hugo = "latest"

$ which hugo
~/.local/share/mise/installs/hugo/0.165.0/bin/hugo
```

`hugo`は`asdf`プラグイン経由でインストールされるツールです。
まず`mise plugins install hugo`でプラグインを追加してから、
`mise use hugo@latest`します。
