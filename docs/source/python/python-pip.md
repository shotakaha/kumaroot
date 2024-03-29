# パッケージ管理したい（``pip``）

```console
$ pip3 install パッケージ名
$ pip3 install -U パッケージ名
$ pip3 uninstall パッケージ名
```

パッケージを追加するには``pip3``コマンドを使います。

```{note}
``pip``と``pip3``は同じコマンドです。
Python2系から3系の移行期には、``pip``（＝2系）と``pip3``（＝3系）で使い分けられるようになっていました。
いまは3系がメインなので``pip`` = ``pip3``となっていますが、僕は習慣で``pip3``を使っています。
```

## 複数パッケージを一括で追加したい

```bash
$ pip3 install --requirements ファイル名
$ pip3 install -r requirements.txt
```

パッケージ名を記載したファイルを使うと一括インストールできます。
ファイルには``requirements.txt``という名前がよく使われます。

## パッケージを更新したい

```bash
$ pip3 install -U パッケージ名
```

## パッケージを一括で更新したい

```bash
$ pip3 list --outdated | awk 'NR>2{print $1}' | xargs pip3 install -U pip
```

``pip3`には、新しいバージョンがリリースされたパッケージを一括で更新するコマンドがありません。

そのため``awk``と``xargs``と組み合わせて、以下の流れで処理しています。

1. ``pip3 list --outdated``で更新が必要なパッケージをリストします
2. その出力結果に対して``awk``を使ってパッケージ名（＝2行目以降の1列目）を抽出します
3. その出力結果を``xargs``に渡して``pip3 install -U 更新が必要なパッケージ名たち``を実行します
