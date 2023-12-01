# 開発環境を切り替えたい（``rtx``）

```console
$ brew install rtx
$ rtx version
2023.12.1 macos-x64 (2023-12-01)
```

Rust製の環境開発マネージャーです。

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
