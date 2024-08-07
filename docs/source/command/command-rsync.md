# rsync

```console
$ rsync [OPTION]... SRC [SRC]... DEST
$ rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST
```

ローカルとリモートのファイルをアップロード／ダウンロードしたいときに使うコマンドです。
ファイルの差分を調べて実行してくれるので便利です。

## ファイルをアップロードしたい

```console
$ rsync -auvz ファイル名1 [ファイル名2]... [ユーザー名@]ホスト名:ディレクトリ名/
$ rsync -auvz --no-p ファイル名1 [ファイル名2]... [ユーザー名@]ホスト名:ディレクトリ名/
```

ファイルをアップロードする場合は、とりあえず``-auvz``をつけて同期すれば問題ないです。
オプションはそれぞれ``-a``（アーカイブモード）、``-u``（更新があったファイルを同期）、``-v``（メッセージ出力）、``-z``（転送時にデータを圧縮）です。

### アーカイブモード

アーカイブモードは``-rlptgoD``に相当します。
``--recursive``（再帰的に同期）、
``--link``（シンボリックリンクをリンボリックリンクとして同期）、
``--perms``（パーミションを保ったまま同期）、
``--times``（時刻を保ったまま同期）、
``--group``（グループを保ったまま同期）、
``--owner``（オーナーを保ったまま同期）、
``--devices``（デバイルを保ったまま同期）
``--special``（特殊ファイルを同期）

アーカイブモードから除外したいオプションがある場合は、
それぞれ``--no-r`` / ``--no-l`` / ``--no-p`` / ``--no-t`` / ``--no-g`` / ``--no-o`` / ``--no-D`` で選択できます。

## ディレクトリごとアップロードしたい

```console
$ rsync -auvz ディレクトリ名/ [ユーザー名@]ホスト名:ディレクトリ名/
```

ローカルのディレクトリの内容を丸ごとリモートサーバーにアップロードできます。
ディレクトリ名の末尾に``/（スラッシュ）``をつける／つけないで、アップロードされる内容が変わるので注意が必要です。
``--dry-run``オプションを使って事前に確認をし、作業したい内容に合わせて使い分けてください。

## 実行内容を事前に確認したい（``--dry-run``）

```console
$ rsync -auvzn ディレクトリ名/ [ユーザー名@]ホスト名:ディレクトリ名/
```

``-n``（``--dry-run``）オプションを使うと、転送される内容を事前に確認できます。

## 完全に同期したい（``--delete``）

```console
$ rsync -auvz --delete ディレクトリ名/ [ユーザー名@]ホスト名:ディレクトリ名/
```

差分同期（``--update``）でリモートサーバーにアップロードした場合、
手元のコンテンツを削除して再び同期しても、サーバー側にデータが残ったままになってしまいます。
手元とサーバーのコンテンツを完全に同期させたい場合は``--delete``オプションを使います。

デフォルトだと、データは転送前に削除（``--delete-before``）されます。
他にも転送中に削除（``--delete-during``）、転送後に削除（``--delete-after``）のオプションがあります。

## 特定のファイルを除外したい（``--exclude``）

```console
$ rsync -auvz --exclude ".DS_Store" ディレクトリ名/ [ユーザー名@]ホスト名:ディレクトリ名/
$ rsync -auvz --exclude=".DS_Store" ディレクトリ名/ [ユーザー名@]ホスト名:ディレクトリ名/
$ rsync -auvz --exclude-from="除外パターンをまとめたファイル名" ディレクトリ名/ [ユーザー名@]ホスト名:ディレクトリ名/
```

``.DS_Store``など、サーバーにアップロードする必要がないファイルを除外したい場合は``--exclude``もしくは``--exclude-from``オプションを使います。

除外したいファイルの数が少ない場合は``--exclude``オプションで十分ですが、多い場合は除外パターンをまとめたファイルを用意して``--exclude-from``で読み込ませるのがよいです。

## 強制同期したい（``--rsync-path``）

```console
$ rsync -auvz --rsync-path="リモートサーバーのパス" ホスト名:ディレクトリ名 ローカルのディレクトリ名
$ rsync -auvz --rsync-path="~/.local/bin/rsync" ホスト名:ディレクトリ名 ローカルのディレクトリ名
```

``rsyncd``が起動していないリモートサーバーでも、
``--rsync-path``でパスを指定して同期できます。

:::{note}

``rsyncd``が起動していないリモートサーバーには、
``rsync``コマンドが入っていない可能性があります。
そのような場合は、自分でインストールする必要があります。
僕は``$HOME/.local/``にインストールすることにしています。

:::
