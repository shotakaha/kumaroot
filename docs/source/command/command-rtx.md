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

## ツールを有効／無効にしたい

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

## Pythonを使いたい

```console
$ rtx install python@3.11
$ rtx install pipx@1.2.1
$ rtx install poetry@1.7.1

$ rtx use python@3.11
$ rtx use --global pipx@1.2.1
$ rtx use --global poetry@1.7.1

$ rtx ls
pipx   1.2.1  ~/.rtx.toml                    1.2.1
poetry 1.7.1  ~/.rtx.toml                    1.7.1
python 3.11.6 ~/repos/github.com/shotakaha/kumaroot/.rtx.toml 3.11
python 3.12.0
```
