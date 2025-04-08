# パッケージ管理したい（``pip``）

```console
$ pip3 install パッケージ名
$ pip3 install -U パッケージ名
$ pip3 uninstall パッケージ名
```

`pip`（`pip3`）はPython標準のパッケージ管理ツールです。

:::{note}
`pip`と`pip3`は同じコマンドです。
Python2系から3系の移行期には、`pip`（＝2系）と`pip3`（＝3系）で使い分けられるようになっていました。
いまは3系がメインなので`pip` = `pip3`となっていますが、僕は習慣で`pip3`を使っています。
:::

:::{hint}

`pip`は、複数のパッケージ間の依存関係の管理があまり得意ではありません。
そのため、システム全体ではなく、プロジェクトごとの仮想環境にインストールするのが最近の定番です。

簡単に仮想環境で管理できるパッケージ管理ツールも多数あります。
[poetry](./python-poetry.md)や[uv](./python-uv.md)、[pipx](./python-pipx.md)などを使ってみるのがよいと思います。

:::

## パッケージを更新したい（`--upgrade`）

```console
$ pip3 install -U パッケージ名
```

`-U / --upgrade`オプションでパッケージを更新できます。
初回インストール時にこのオプションをつけても問題ありません。

## パッケージを一括で更新したい

```console
$ pip3 list --outdated | awk 'NR>2{print $1}' | xargs pip3 install -U pip
```

`pip3`には、新しいバージョンがリリースされたパッケージを一括で更新するコマンドがありません。
そのため[awkコマンド](../command/command-awk.md)と[xargsコマンド](../command/command-xargs.md)と組み合わせてパイプ処理します。

1. `pip3 list --outdated`で更新が必要なパッケージをリストします
2. その出力結果に対して`awk`を使ってパッケージ名（＝2行目以降の1列目）を抽出します
3. その出力結果を`xargs`に渡して`pip3 install -U 更新が必要なパッケージ名たち`を実行します

## 一括で追加したい（`--requirements`）

`bash
$ pip3 install --requirements ファイル名
$ pip3 install -r requirements.txt
`

`-r / --requirements`オプションでファイルに書かれているパッケージを一括インストールできます。
ファイル名は通常`requrirements.txt`を使います。
