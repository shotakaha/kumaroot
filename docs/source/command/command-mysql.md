# データベースしたい（``mysql``）

## バックアップしたい（``mysqldump``）

```console
// データベース名を指定してバックアップ
$ mysqldump --user ユーザー名 --password データベース名 > パス/ファイル名.sql
$ mysqldump --user ユーザー名 --password データベース名 --result-file=パス/ファイル名.sql

// すべてのデータベース
$ mysqldump --user ユーザー名 --password --all-databases > パス/ファイル名.sql

// リモートにあるデータベース
$ mysqldump --host=IPアドレス/ホスト名 --user ユーザー名 --password --all-databases > パス/ファイル名.sql
```

``mysqldump``でMySQLデータベースをバックアップを取得できます。
``-u / --username``オプションでデータベースのユーザー名を指定します。
``-p / --password``オプションでパスワード入力します。
``--result-file``オプションもしくはリダイレクトで、ダンプ先のファイル名を指定します。

``--all-databases``オプションで、すべてのデータベースをダンプします。
