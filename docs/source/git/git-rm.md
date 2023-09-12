# ファイルを削除したい（``git rm``）

```console
$ git rm ファイル名
$ git rm -r ディレクトリ名
```

Git管理しているファイルを削除する場合は``git rm``します。
ファイル／ディレクトリは削除されると同時にステージされます。

## ファイルを完全に削除したい（``git filter-repo``）

```console
$ brew install git-filter-repo
```

``git filter-branch``は公式でも非推奨なようなので、``git-filter-repo``を追加でインストールします。
手順は[Gitから機微なデータの削除 - GitHub](https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)を参照してください。
