# プロジェクトをはじめたい（``myst init``）

```console
$ myst init
```

``myst init``で設定ファイル（``myst.yml``）を作成します。
``myst.yml``は実行したディレクトリに作成されます。

そのまま``myst start``が実行され、プレビュー用のサーバーがローカルホスト（デフォルトは ``http://localhost:3000``）に起動します。

:::{note}

``myst init``を実行したディレクトリが空の場合、``myst start``は失敗します。
その場合は、なんでもいいので``.md``ファイルを作成すればOKです。

トップページとしてよく使われるファイル名は、
``index.md / index.ipynb``、
``README.md / README.ipynb``、
``main.md / main.ipynb``
があります。参考までに。

:::

## 他ツールから移行したい

```console
$ mkdir mystmd  # myst用のディレクトリを作成する
$ cd mystmd
$ myst init
```

Sphinxなどの他ツールから移行する場合、プロジェクト直下に``mystmd``のようなmyst用のディレクトリを作成するとよいです。
