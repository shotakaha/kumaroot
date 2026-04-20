```{eval-rst}
.. index::
    single: ビルドしたい; Sphinx
```

# ビルドしたい（`sphinx-build`）

```console
$ sphinx-build --builder html SOURCE_DIR BUILD_DIR
$ sphinx-build --builder dirhtml SOURCE_DIR BUILD_DIR
$ sphinx-build --builder latex SOURCE_DIR BUILD_DIR
```

`sphinx-build`コマンドで、Sphinxドキュメントをビルドできます。
`--builder`オプションで、ビルド形式を変更できます。

```console
// 利用可能なビルダーを確認する
$ make help
$ make html
$ make dirhtml
$ make latexpdf
```

`sphinx-quickstart`コマンドでプロジェクトを作成した場合は、
`Makefile`が自動生成されます。
`make help`コマンドで、利用可能なビルダーを確認できます。

:::{important}

ゆくゆくは{file}`Makefile`に依存しない``sphinx``コマンドを作る予定のようです。
（GitHubのみたので、Issue番号が分かればはる）

:::

## KumaROOTをビルドしたい

```console
// GitHubにあるリポジトリをクローンする
$ git clone https://github.com/shotakaha/kumaroot.git
$ cd kumaroot
$ uv sync

$ cd docs
$ uv run make html
$ uv run make latexpdf
```

`KumaROOT`のドキュメントをビルドする手順です。

```{note}
Python開発環境の構築に`uv`を使っています。
詳しくは[](../python/python-uv.md)を参照してください。
```

```console
$ git clone https://github.com/shotakaha/kumaroot.git
$ cd kumaroot
$ uv sync

$ task docs:build    // uv run make html
$ task docs:pdf      // uv run make latexpdf
$ task docs:serve    // uv run make livehtml
```

現在は[taskコマンド](../command/command-task.md)を使って、
より簡単にビルドできるようにしています。
