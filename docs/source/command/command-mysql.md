# データベースしたい（``mysql``）

```console
$ mysql -u ユーザー名 -p
$ mysql -u ユーザー名 -p データベース名
```

``mysql``コマンドでMySQLのデータベースに接続できます。
データベースの本体は`/var/lib/mysql`などにあります。

:::{caution}

`-p / --password`オプションは、
``-pPASSWORD``のようにパスワードを引数に指定できます。しかし、パスワードをつけてしまうと、
シェルの履歴に文字列が残ってしまうため、
基本は直接指定せずに使います。

:::

## データベース名を確認／選択したい（``SHOW DATABASES`` / ``USE``）

```mysql
SHOW DATABASES;
USE データベース名;
```

``SHOW DATABASES;``でデータベースに含まれるデータベース名を確認できます。
表示されたデータベース名を``USE``で選択します。

データベースを``mysqldump``でダンプするときも、
このデータベース名の中から指定します。

## テーブル名を確認したい（``SHOW TABLES``）

```mysql
SHOW TABLES;
```

選択したデータベースに含まれるテーブル名を確認できます。
WordPressなどでは``wp_``から始まるテーブル名になっていることが多いです。

## テーブルの内容を確認したい（``SELECT * FROM``）

```mysql
SELECT * FROM テーブル名 LIMIT 行数;

// 投稿を10件表示する
SELECT * FROM wp_posts LIMIT 10;
```

``SELECT * FROM``で、指定したテーブル名の内容を取得できます。

## テーブルの構造を確認したい（``DESCRIBE``）

```mysql
DESCRIBE テーブル名
```

``DESCRIBE``でテーブルのカラム名、データ型、キー情報などの構造を取得できます。

## データベースを終了したい（``EXIT``）

```mysql
EXIT;
```

``EXIT``でMySQLのセッションを終了します。

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
``-u / --username``オプションや``-p / --password``オプションは``mysql``と同様です。

``--result-file``オプションもしくはリダイレクトで、ダンプ先のファイル名を指定します。

``--all-databases``オプションで、すべてのデータベースをダンプします。
