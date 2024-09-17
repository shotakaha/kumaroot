# コミット履歴を確認したい（``git log``）

```console
$ git log
```

## グラフしたい

```console
# 現在のブランチ
$ git log --oneline --graph

# すべてのブランチ
$ git log --oneline --graph --all
```

``--graph``オプションでグラフ（っぽく）表示できます。
``--oneline``オプションと一緒に使うのがオススメです。

## コミットごとの変更量をしりたい

```console
$ git log --stat
$ git log --stat --oneline
```

``--stat``オプションで、コミットごとの
変更したファイル名と変更した行数を確認できます。

## コミットごとの差分したい

```console
$ git log -p
```

``-p``オプションでコミットごとの差分が確認できます。

## 日付したい

```console
# 指定した日付より前のログ
$ git log --before "2024-09-17"

# 指定した日付より後のログ
$ git log --after "2024-09-15"

# 指定した期間のログ
$ git log --after "2024-09-15" --before "2024-09-17"
```
