# rsync

```bash
rsync [OPTION]... SRC [SRC]... DEST
rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST
```

## ファイルをアップロードしたい

```bash
rsync -auvz ファイル名1 [ファイル名2]... [ユーザー名@]ホスト名:ディレクトリ名/
```

{option}`-a`, {option}`--archive`
: アーカイブモード；{option}`-rlptgoD`に相当

{option}`-u`, {option}`--update`
: 差分同期（相手先のファイルの方が新しければスキップする）

{option}`-v`, {option}`--verbose`
: メッセージ出力を増やす

{option}`-z`, {option}`--compress`
: 転送時にデータを圧縮する

## ディレクトリごとをアップロードしたい

```bash
rsync -auvz ディレクトリ名/ [ユーザー名@]ホスト名:ディレクトリ名/
```

```{note}
ディレクトリ名の末尾に``/``をつける／つけないで動作が変わるので、自分の作業内容に合わせて使い分けてください。
```

## アップロード前に確認したい（``--dry-run``）

```bash
rsync -auvzn ディレクトリ名/ [ユーザー名@]ホスト名:ディレクトリ名/
```

{option}`-n`, {option}`--dry-run`
: 転送される内容を確認する


## 完全に同期したい（``--delete``）

差分同期（{option}`--update`）でサーバーにアップロードした場合、
手元のコンテンツを削除しても、サーバーにデータが残ったままになってしまいます。
手元のコンテンツとサーバーのコンテンツを完全に同期させたい場合は{option}`--delete`オプションを使います。

```bash
rsync -auvz --delete ディレクトリ名/ [ユーザー名@]ホスト名:ディレクトリ名/
```

{option}`--delete`
: delete extraneous files from destination dirs

デフォルトだと、データは転送前に削除（{option}`--delete-before`）されます。
必要であれば転送中に削除（{option}`--delete-during`）、転送後に削除（{option}`--delete-after`）のオプションを使ってください。


## 特定のファイルを除外したい（``--exclude``）

``.DS_Store``など、サーバーにアップロードする必要がない／したくないファイルがある場合は{option}`--exclude`もしくは{option}`--exclude-from`オプションを使います。

```bash
rsync -auvz --exclude ".DS_Store" ディレクトリ名/ [ユーザー名@]ホスト名:ディレクトリ名/
rsync -auvz --exclude=".DS_Store" ディレクトリ名/ [ユーザー名@]ホスト名:ディレクトリ名/
rsync -auvz --exclude-from="除外するファイル一覧" ディレクトリ名/ [ユーザー名@]ホスト名:ディレクトリ名/
```


{option}`--exclude=PATTERN`
: exclude files matching PATTERN

{option}`--exclude-from=FILE`
: read exclude patterns from FILE

除外したいファイルの数が少ない場合は{option}`--exclude`オプションで十分ですが、多い場合は除外するファイル名を一覧にしたファイルを用意するとよいです。
