# ランタイム管理したい（`mise`）

```console
$ mise use python@3.11
```

`mise`（ミーズ）は、開発環境で使うランタイム（実行環境）を切り替えるコマンドです。

## インストールしたい（`mise`）

```console
$ brew install mise

$ mise --version
2026.8.11 macos-x64 (2026-08-23)    # Intelの場合
2026.8.11 macos-arm64 (2026-08-23)  # Apple Siliconの場合
```

`mise`はHomebrewでインストールできます。

:::{note}

2024年1月に[コマンド名がrtxからmise](https://github.com/jdx/mise/releases/tag/v2024.1.0)されました。

:::

## 設定したい（`mise.toml`）

```console
$ mise config ls
~/.config/mise/config.toml   node
./mise.toml                  python
```

`mise.toml`で、`mise`の設定を管理できます。

プロジェクト単位の設定は`./mise.toml`、
ユーザー設定は`~/.config/mise/config.toml`
を使います。

同じツールが両方の設定ファイルに書かれている場合は、プロジェクト単位の設定が優先されます。

```console
$ mise config ls
```

`mise config ls`（`config list`）で、現在有効な設定ファイルと、ツールがどちらの設定に由来するかを確認できます。

## 有効／無効にしたい（`mise activate` / `mise deactivate`）

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

## プラグイン名を確認したい（`mise plugins ls-remote`）

```console
$ mise plugins ls-remote
```

`plugins ls-remote`（`plugins list-remote` / `plugins list-all`）コマンドで、利用できるプラグイン名を一覧できます。

## プラグインのバージョンを一覧したい（`mise ls-remote`）

```console
$ mise ls-remote プラグイン名
$ mise ls-remote python
$ mise ls-remote uv
$ mise ls-remote node
$ mise ls-remote go
$ mise ls-remote hugo
```

`ls-remote`（`list-remote` / `list-all`）コマンドで、インストールできるバージョンを一覧できます。

## 環境を切り替えたい（`mise use`）

```console
// プロジェクト（＝現在のディレクトリ）に追加
$ mise use python@3.11
$ cat ./mise.toml
[tools]
python = "3.11"
```

`use`（`u`）コマンドでツールの環境を切り替えることができます。
設定は`./mise.toml`に保存されます。

指定したバージョンのツールが見つからない場合は、`mise install`コマンドが自動実行され、
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

`--global`オプションで個人環境全体に追加できます。
設定は`~/.config/mise/config.toml`に保存されます。

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

## 環境を確認したい（`mise ls`）

```console
$ mise ls
Tool      Version   Config Source                 Requested
node      23.0.0    ~/.config/mise/config.toml    latest
python    3.11.10
```

`ls`（`list`）コマンドで設定されている環境と`mise`設定のパスを確認できます。

## 更新したい（`mise upgrade`）

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

`ls`コマンドでツールの更新の有無を確認できます。
`upgrade`（`up`）コマンドでツールを一括で更新できます。
