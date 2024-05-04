# リポジトリをクローンしたい（``git clone``）

```console
$ git clone リポジトリのURL

$ git clone https://github.com/shotakaha/kumaroot.git
$ ls
kumaroot
```

``git clone``コマンドでリポジトリをクローンできます。
クローンすると、デフォルトでリポジトリ名のディレクトリが作成されます。

## タグ／ブランチをしていしたい（``-b / --branch``）

```console
$ git clone --branch タグ名（orブランチ名） リポジトリのURL
$ git clone -b ブランチ名 --single-branch リポジトリのURL
```

``--branch``オプションでタグ／ブランチを指定してクローンできます。
ブランチ名やタグ名は、それぞれリポジトリのウェブサイトで事前に確認してください。

``--single-branch``オプションを追加すると、特定のブランチだけクローンできます。

## シャロークローンしたい（``--depth``）

```console
$ git clone --depth 1 リポジトリのURL
$ git clone -b ブランチ名 --single-branch --depth 1 リポジトリのURL
```

``--depth``オプションで、取得するコミット履歴を制限できます。
前述した``--branch ブランチ名`` / ``--single-branch``と一緒に使うのがよいみたいです。

## パーシャルクローンしたい（``--filter``）

```console
# blob-less クローン
$ git clone --filter=blob:none リポジトリのURL

# tree-less クローン
$ git clone --filter=tree:0 リポジトリのURL
```

``--filter=blob:none``オプションで、blob-lessクローンできます。
このクローンは、到達可能なすべてのコミット履歴とツリーを取得し、blob（＝ファイル）は必要に応じて取得する形式です。

``--filter=tree:0``オプションで、tree-lessクローンできます。
このクローンでは、到達可能なすべてのコミット履歴を取得し、ツリーとblob（＝ファイル）は必要に応じて取得する形式です。

## リファレンス

- [パーシャルクローンとシャロークローンを活用しよう](https://github.blog/jp/2021-01-13-get-up-to-speed-with-partial-clone-and-shallow-clone/)
