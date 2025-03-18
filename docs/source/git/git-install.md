```{eval-rst}
.. index::
    pair: Git; install
```

# インストール

```console
$ brew install git

$ which git
/opt/homebrew/bin/git

$ git --version
git version 2.49.0
```

Homebrewを使って最新版をインストールしておきます。

```console
$ brew install git-lfs

$ which git-lfs
/opt/homebrew/bin/git-lfs

$ git lfs --version
git-lfs/3.6.1 (GitHub; darwin arm64; go 1.23.4)
```

また、大きなサイズのファイルのバージョン管理することがあるかもしれないので、Git LFSも使えるようにしておきます。

:::{note}

```console
$ /usr/bin/git --version
git version 2.39.5 (Apple Git-154)
```

macOSにはデフォルトで `/usr/bin/git` がインストールされています。
まずはじめは、そちらを使ってみてもよいかもしれません。

:::
