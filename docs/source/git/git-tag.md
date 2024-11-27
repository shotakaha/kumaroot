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

## タグ名を確認したい（``--list`` / ``--contains``）

```console
// すべてのタグを確認
$ git tag -l

// 指定したコミットIDを含むタグを確認
$ git tag --contains コミットID
```

`-l, --list`オプションでタグ一覧を表示できます。
`--contains`オプションで指定したコミットIDを含むタグ名を確認できます。

```console
// バージョン番号でソートする
$ git tag -l | sort -V

// 一番新しいタグを取得する
$ git tag -l | sort -V | tail -n 1
```

セマンティック・バージョニングを採用している場合、
`sort -V`コマンドにパイプすることで、バージョン番号の順番に並び替えて確認できます。
また、さらに`tail`コマンドにパイプすることで
一番新しいタグを確認できます。

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
