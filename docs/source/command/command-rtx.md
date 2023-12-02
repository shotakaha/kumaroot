# 開発環境を切り替えたい（``rtx``）

```console
$ brew install rtx
$ rtx --version
2023.12.1 macos-x64 (2023-12-01)   # Intelの場合
2023.12.1 macos-arm64 (2023-12-01) # Apple Siliconの場合
```

環境開発を切り替えるツールです。
同様のツールに[anyenv](https://anyenv.github.io/)や[asdf](https://asdf-vm.com/)などがありますが、
最近は[rtx](https://github.com/jdx/rtx)を使うのがよさそうです。

## 有効／無効にしたい

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

## プラグイン名を確認したい（``plugins ls-remote``）

```console
$ rtx plugins ls-remote
```

``plugins ls-remote``コマンドで、利用できるプラグイン名を一覧できます。

## プラグイン名のバージョンを一覧したい（``ls-remote``）

```console
$ rtx ls-remote プラグイン名
$ rtx ls-remote python
$ rtx ls-remote poetry
$ rtx ls-remote pipx
$ rtx ls-remote node
$ rtx ls-remote go
$ rtx ls-remote hugo
```

``ls-remote プラグイン名``コマンドで、インストールできるバージョンを一覧できます。
プラグインによっては、下記のようなメッセージが表示されるので``y(es)`を入力します。

```console
$ rtx ls-remote pipx
⚠️  pipx is a community-developed plugin: https://github.com/yozachar/asdf-pipx
Would you like to install pipx? (y/n)
```

## Pythonを使いたい

```console
$ rtx install python@3.11
```

``install``コマンドで、使いたいプラグイン（とバージョン）を指定します。
バージョンを省略すると``latest``になります。

```console
$ rtx use python@3.11
$ rtx use python@3.12

$ rtx ls
python 3.11.6
python 3.12.0 ~/repos/sandbox/rtx-usage/.rtx.toml 3.12

$ which python
~/.local/share/rtx/installs/python/3.12.0/bin/python
```

``use``コマンドで、利用するプラグイン（とバージョン）の切り替えができます。
設定ファイル``.rtx.toml``がカレントディレクトリに作成されます。
プラグインが見当たらない場合は、インストール（``rtx install``）してくれます。

```console
$ rtx use python@3.11
$ rtx use poetry@1.7.1
$ rtx use pipx@1.2.1

$ rtx ls
pipx   1.2.1  ~/repos/sandbox/rtx-usage/.rtx.toml 1.2.1
poetry 1.7.1  ~/repos/sandbox/rtx-usage/.rtx.toml 1.7
python 3.11.6 ~/repos/sandbox/rtx-usage/.rtx.toml 3.11
python 3.12.0

$ which python3
~/.local/share/rtx/installs/python/3.11.6/bin/python3

$ which poetry
~/.local/share/rtx/installs/poetry/1.7.1/bin/poetry

$ which pipx
~/.local/share/rtx/installs/pipx/1.2.1/bin/pipx
```

## Nodeを使いたい

```console
$  myst --version  # ~/.local/bin/myst
MyST requires node 16, 18, or 20; you are running node 21.

$ rtx use node@20  # ~/.local/share/rtx/installs/node/20.10.0/bin/node

$ myst --version
v1.1.32
```

``rtx``によるバージョン管理の具体例を紹介します。
Homebrewを使ってインストールした``node``を``noode@21``に更新してしまい、``mystmd``が動かなくなってしまいました。
カレントディレクトリだけ``node@20``に設定し、無事``mystmd``を動かすことができました。
