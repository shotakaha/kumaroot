# 開発環境を切り替えたい（``mise``）

```console
$ mise use python@3.11
```

`mise`（ミーズ）は開発環境のバージョンを切り替えるためのツールです。
同様のツールに[anyenv](https://anyenv.github.io/)や[asdf](https://asdf-vm.com/)などがありますが、
最近は[mise](https://github.com/jdx/mise)を使うのがよさそうです。

## インストールしたい（`mise`）

```console
$ brew install mise

$ mise --version
2024.3.11 macos-x64 (2024-03-30)    # Intelの場合
2024.3.11 macos-arm64 (2024-03-30)  # Apple Siliconの場合
```

`mise`はHomebrewでインストールできます。

:::{note}

2024年1月に[コマンド名がrtxからmise](https://github.com/jdx/mise/releases/tag/v2024.1.0)されました。

:::

## 環境を切り替えたい（`mise use`）

```console
// プロジェクト（＝現在のディレクトリ）に追加
$ mise use python@3.11
$ cat ./.mise.toml
[tools]
python = "3.11"
```

`use`コマンドでツールの環境を切り替えることができます。
設定は`./.mise.toml`に保存されます。

指定したバージョンのツールが見つからない場合は、``mise install``コマンドが自動実行され、
``~/.local/share/mise/installs/``の中にインストールされます。
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

## 環境を確認したい（``ls``）

```console
$ mise ls
Tool      Version   Config Source                 Requested
node      23.0.0    ~/.config/mise/config.toml    latest
python    3.11.10
```

`ls`コマンドで設定されている環境と`mise`設定のパスを確認できます。

## 更新したい（``up`` / ``upgrade``）

```console
$ mise ls
Plugin  Version            Config Source              Requested
python  3.12.2 (outdated)  ~/.config/mise/config.toml 3.12

$ mise up
mise python@3.12.3 ✓ installed
mise python@3.12.2 ✓ removing ~/.local/share/mise/installs/python/3.12.2

$ mise ls
Plugin  Version  Config Source             Requested
python  3.12.3  ~/.config/mise/config.toml 3.12
```

``list``コマンドでプラグインの更新の有無を確認できます。
``upgrade``コマンドでプラグイン本体を一括で更新できます。

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
mise ~/repos/github.com/shotakaha/kumaroot/.mise.toml tools: python@3.11.8

$ mise ls python
Plugin  Version  Config Source                                    Requested
python  3.11.6
python  3.11.8   ~/repos/github.com/shotakaha/kumaroot/.mise.toml 3.11
python  3.12.2

$ which python
~/.local/share/mise/installs/python/3.11/bin/python
```

## Nodeを使いたい（`mise use node`）

```console
$ which myst
~/.local/bin/myst    # pipx でインストールした
$ myst --version  # ~/.local/bin/myst
MyST requires node 16, 18, or 20; you are running node 21.

// Node20に変更
$ mise use node@20  # ~/.local/share/mise/installs/node/20.10.0/bin/node
$ mise ls node
Plugin  Version  Config Source                                  Requested
node    20.9.0   ~/repos/gitlab.com/qumasan/haniwers/.mise.toml 20
$ myst --version
v1.1.32
```

``mise``を使って、Nodeのバージョンを変更した具体例です。

Homebrewを使ってインストールした``node``を``noode@21``に更新してしまったため、``mystmd``（v1.1.31）が動かなくなってしまいました。
このプロジェクトだけ``node@20``に切り替えて、``mystmd``を動かすことができました。

:::{note}

``mystmd``（v1.1.42）は、Node@21でも動作するようになっていました。

:::

## プラグイン名を確認したい（``mise plugins ls-remote``）

```console
$ mise plugins ls-remote
```

``plugins ls-remote``コマンドで、利用できるプラグイン名を一覧できます。

## プラグインのバージョンを一覧したい（``mise ls-remote``）

```console
$ mise ls-remote プラグイン名
$ mise ls-remote python
$ mise ls-remote poetry
$ mise ls-remote pipx
$ mise ls-remote node
$ mise ls-remote go
$ mise ls-remote hugo
```

``ls-remote プラグイン名``コマンドで、インストールできるバージョンを一覧できます。
プラグインによっては、下記のようなメッセージが表示されるので``y(es)`を入力します。

```console
$ mise ls-remote pipx
⚠️  pipx is a community-developed plugin: https://github.com/yozachar/asdf-pipx
Would you like to install pipx? (y/n)
```

## 有効／無効にしたい

:::{note}
2023年11月に[fishで自動的に有効](https://github.com/jdx/mise/releases/tag/v2023.11.9)にする機能が追加されました。
なので、このコマンドはもう必要ありません。
:::

```console
$ eval "$(rtx activate bash)"
$ eval "$(rtx activate zsh)"
$ rtx activate fish | source
$ execx($(rtx activate xonsh))
```

``activate``コマンドを使って、現在のセッションで``rtx``を有効にできます。
利用するシェルによって、コマンドが異なる点に注意してください。
``rtx``をお試しで使ってみたい場合によいでしょう。
常用する場合は、シェルの設定ファイルに追記します。

```console
$ rtx deactivate
```

``deactivate``コマンドで無効にできます。
