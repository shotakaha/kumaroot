# 絞り込み検索したい（`peco`）

```console
$ peco ファイル名
$ コマンド | peco
$ history | peco
$ ps aux | peco
$ git log --oneline | peco
```

`peco`は、絞り込み検索（incremental search）できるコマンドです。
ほとんどすべての入力に対して「絞り込み検索」で候補を絞り込むことができます。
大量のデータに対しても高速で動作します。

## インストールしたい（`peco`）

```console
$ brew install peco
$ peco --version
peco version 0.6.0 (built with go1.26.0)
```

`peco`はHomebrewでインストールできます。

## 検索条件を指定したい（`--query` / `--initial-filter`）

```console
$ history | peco --query "git"
$ history | peco --initial-filter Fuzzy
```

`--query`で、起動時点の検索文字列をあらかじめ指定できます。
`--initial-filter`で、絞り込みの方式を指定できます。
`IgnoreCase`（デフォルト、大文字小文字を区別しない）や`Fuzzy`（あいまい検索）などが選べます。

## 複数選択したい（`Ctrl-Space`）

`peco`には`fzf`の`--multi`のようなオプションはなく、デフォルトで複数選択に対応しています。

- {kbd}`Ctrl-Space`: 選択・選択解除して次の候補へ移動
- {kbd}`Enter`: 選択済みの候補すべてを確定

## コマンドを実行したい（`--exec`）

```console
$ ps aux | peco --exec "kill {}"
```

`--exec`で、選択した候補を渡して別のコマンドを実行できます。
候補は標準入力として渡され、`peco`自体はコマンドの実行後に終了します。
