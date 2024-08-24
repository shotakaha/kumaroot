# Git LFSしたい（``git-lfs``）

```console
$ brew install git-lfs

$ git lfs --version
git-lfs/3.5.1 (GitHub; darwin arm64; go 1.22.1)

$ git lfs install
Git LFS initialized.
```

```console
$ cd プロジェクトルート
$ git lfs track "*.csv"
$ git lfs track "*.csv.gz"
$ git lfs track "*.ipynb"
```

Git LFSはサイズの大きなファイルをGit管理するための仕組みです。
バイナリ系のファイルなど、大きなファイルの差分管理は、Gitは得意ではありません。
そこで、LFSオブジェクトとして実体は別の場所に保存し、
Git自身はそのハッシュ値を差分管理するという方法です。

GitHubやGitLabもLFSに対応しており、LFS専用のストレージがあります
無料アカウントの場合、同じ名前空間全体でストレージ容量は10GBです。

```console
// プロジェクト/.gitattributesを確認
$ cat .gitattributes
*.csv.gz filter=lfs diff=lfs merge=lfs -text
*.csv filter=lfs diff=lfs merge=lfs -text
*.ipynb filter=lfs diff=lfs merge=lfs -text
```
