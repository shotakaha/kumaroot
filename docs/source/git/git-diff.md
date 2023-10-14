# 差分を確認したい（``git diff``）

```console
$ git diff ブランチ名
$ git diff --stat ブランチ名
$ git diff origin/main
```

``git diff``を使って変更箇所を確認できます。
デフォルトはステージ前の変更箇所を確認できます。

引数にブランチ名を指定すると、ローカルブランチとの差分を確認できます。
リモートブランチ名を指定すると、リモートリポジトリとの差分を確認できます。

## ``git add``する前に確認したい

```console
$ git diff
```

デフォルトの挙動です。

## ``git add``した後に確認したい

```console
$ git diff --cached
```

``--cached``オプションで、ステージした内容を確認できます。

## ``git commit``直後に確認したい

```console
$ git diff HEAD^
$ git  show
```

``HEAD^``を指定するとコミットした内容を確認できます。
``git show``の方が簡単です。

## ``git pull``する前に確認したい

```console
$ git diff HEAD..リモート名/ブランチ名
$ git diff HEAD..origin/main
```

## ``git push``する前に確認したい

```console
$ git diff リモート名/ブランチ名..HEAD
$ git diff origin/main..HEAD
```
