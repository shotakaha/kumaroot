# ヘルプの使い方

Gitのコマンドはいろいろあるので、いちいち覚えてられません。
でも、ヘルプを表示できれば、すべてを覚える必要はありません。

```shell
$ git help
$ git --help
```

## さくっと確認したい（{command}`-h`）

```shell
$ git init -h
$ git status -h
$ git branch -h
$ git remote -h
```

## しっかり確認したい（{command}`--help`）

ロングヘルプ（{command}`--help`）は{command}`man`コマンドと同じ内容です。

```shell
$ git init --help    ## = $ man git-init
$ git status --help  ## = $ man git-status
$ git branch --help  ## = $ man git-branch
$ git remote --help  ## = $ man git-remote
```
