# タグしたい（`git tag`）

```console
$ git tag -l
$ git tag タグ名
$ git push origin タグ名
```

## タグを作成したい

```console
// 現在のコミットからタグを作成
$ git tag タグ名

// 特定のコミットからタグを作成
$ git tag タグ名 コッミトID

// タグの説明を追加
$ git tag タグ名 -m タグの説明
```

## タグをプッシュしたい

```console
$ git push origin タグ名
$ git push origin --tags
```

## タグを更新したい

```console
$ git fetch --tags
```

`fetch --tags`コマンドで、
リモートリポジトリにあるタグ情報を取得できます。

## タグを削除したい（`--delete`）

```console
// タグ名を確認する
$ git tag -l

// ローカルのタグを削除する
$ git tag -d タグ名

// リモートリポジトリのタグを削除する
$ git push origin --delete タグ名

// タグを再作成してプッシュする
$ git tag タグ名  # 同名のタグもOK
$ git push origin タグ名
```

`-d, --delete`オプションでタグを削除できます。
作業前にタグ名を確認しておきます。
リモートリポジトリにタグをプッシュしている場合は、
そちらも削除しておくとよいです。

