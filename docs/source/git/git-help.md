# ヘルプの使い方

```console
$ git help
$ git --help
```

Gitにはたくさんのサブコマンドがあります。
それらをすべて暗記する必要はなく、すべてヘルプで確認できます。

## さくっと確認したい（``-h``）

```console
$ git サブコマンド名 -h
$ git init -h
$ git status -h
$ git branch -h
$ git remote -h
```

## しっかり確認したい（``--help``）

```console
$ git サブコマンド名 --help
$ git init --help    ## = $ man git-init
$ git status --help  ## = $ man git-status
$ git branch --help  ## = $ man git-branch
$ git remote --help  ## = $ man git-remote
```

ロングヘルプ（``--help``）は``man``コマンドと同じ内容です。
