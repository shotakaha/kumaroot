# データ管理したい（`dvc`）

```console
$ git init
$ dvc init
$ dvc add data/dataset.csv
$ dvc remote add -d storage s3://my-bucket/dvc-storage
$ git add .dvc data/.gitignore .dvcignore
$ git commit -m "Initialize DVC"
$ dvc stage add -n prepare -d data/raw.csv -o data/processed.csv python scripts/prepare.py
$ dvc repro
$ dvc push
$ git add dvc.yaml dvc.lock
$ git commit -m "Add data processing pipeline"
```

`dvc`（Data Version Control）は、
大規模なデータセットをバージョン管理するためのツールです。

Gitと組み合わせることで、データパイプラインの再現性を確保し、大規模なデータファイルを効率的に管理できます。

## インストールしたい（`dvc`）

- Homebrew

```console
$ brew install dvc
```

- uv

```console
$ uv tool install dvc
```

- pipx

```console
$ pipx install dvc
```

- uvx（一時的）

```console
$ uvx dvc --help
```

## 初期化したい（`dvc init`）

```console
$ dvc init
```

`dvc init`コマンドで`.dvc/`ディレクトリを作成し、DVCの設定ファイルを初期化します。
Gitリポジトリの中で実行します。

## トラッキングしたい（`dvc add`）

```console
$ dvc add data/dataset.csv
```

`dvc add`コマンドでデータファイルをトラッキングできます。
DVCはデータファイルの代わりに`.dvc`ファイル（メタデータ）を作成し、`.dvc`ファイルをGitで管理します。
実ファイルは`.gitignore`に追加します。

## URLから取得したい（`dvc get-url`）

```console
$ dvc get-url https://example.com/dataset.zip data/dataset.zip
```

`dvc get-url`コマンドで、リモートのURLから直接データをダウンロードできます。

## リモートストレージしたい（`dvc remote`）

```console
$ dvc remote add -d gdrive gdrive:://folder-id
```

`dvc remote add`コマンドでリモートストレージを追加できます。
`-d`オプションでデフォルトのリモート先を設定します。
複数のリモートを設定することも可能です。

### リモートストレージの種類

DVCは以下のストレージに対応しています。

- **Google Drive**: `gdrive://folder-id`
- **S3**: `s3://bucket-name/path`
- **Azure**: `azure://container-name`
- **Google Cloud Storage**: `gs://bucket-name`
- **ローカルパス**: `/local/path` または `./relative/path`

### リモートストレージにプッシュしたい（`dvc push`）

```console
$ dvc push
```

`dvc push`コマンドでローカルでトラッキングしているすべてのデータをリモートストレージにアップロードできます。

### リモートストレージから取得したい（`dvc pull`）

```console
$ dvc pull
```

`dvc pull`コマンドでリモートストレージに保存されているデータをローカルにダウンロードできます。

## Google Driveしたい

```console
$ git init
$ dvc init
$ dvc remote add -d gdrive 'gdrive://1mFgxxxxxx1234567890'
$ dvc add data/dataset.csv
$ dvc push
$ git add data/dataset.csv.dvc .gitignore .dvc/config
$ git commit -m "Add dataset to DVC with Google Drive"
```

Google Driveをリモートストレージとして使用する場合の、手順のサンプルです。

### フォルダーIDを取得したい

1. [Google Drive](https://drive.google.com) にアクセスします
2. リモートストレージとして使うフォルダーを作成します
3. そのフォルダーを開きます
4. URLからIDを取得します。例：`https://drive.google.com/drive/folders/1mFgxxxx...` の場合、フォルダーIDは `1mFgxxxx...`

### Google Driveで認証したい

初回使用時、ブラウザで認証画面が表示されます。
DVCがGoogle Driveにアクセスすることを許可します。

## リファレンス

- [DVC 公式ドキュメント](https://dvc.org/doc)
- [DVC GitHub リポジトリ](https://github.com/iterative/dvc)
