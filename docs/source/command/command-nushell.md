# nushellしたい（`nushell`）

```console
$ nu
     __  ,
 .--()°'.' Welcome to Nushell,
'|, . ,'   based on the nu language,
 !_-(_\    where all data is structured!

Version: 0.115.0 (aarch64-apple-darwin)
```

`nushell`は、Rust製のモダンなシェルです。
Unix系のシェルのように、テキストを扱うのではなく、構造化されたデータを扱うことができるのが特徴です。

## インストールしたい（`nushell`）

```console
$ brew info nushell
$ brew install nushell
$ brew upgrade nushell

$ nu --version
0.115.0
```

`nushell`はHomebrewでインストールできます。
フォーミュラ名は`nushell`です。
コマンド名は`nu`です。

## コマンドを実行したい（`-c` / `--commands`）

```console
$ nu -c "ls | select name | first 2"
```

`-c`オプションで、`nu`を対話シェルとして起動せず、指定したコマンドを実行して終了できます。
シェルスクリプトやCIから`nushell`のワンライナーを呼び出したいときに使います。

## 標準入力を渡したい（`--stdin`）

```console
$ echo "hello" | nu --stdin -c 'print $in'
```

`--stdin`オプションで、パイプで渡した標準入力を`$in`として扱えます。
他のコマンドの出力を`nushell`のワンライナーに渡して処理したいときに使います。

## 設定ファイルを無視して起動したい（`-n` / `--no-config-file`）

```console
$ nu -n
```

`-n`オプションで、`config.nu`や`env.nu`を読み込まずに起動できます。
設定ファイルのトラブルシューティングや、素の状態での動作確認に使います。

## テーブルの見た目を変えたい（`--table-mode`）

```console
$ nu --table-mode compact -c "[[a b]; [1 2] [3 4]]"
```

`--table-mode`オプションで、テーブル表示の罫線スタイルを変更できます。
デフォルトは`rounded`です。

:::{caution}

`--table-mode`などの起動オプションは、`-c`より前に指定する必要があります。
`-c`より後ろに置くと、`nu`の起動オプションとしてではなく別の引数として扱われ、反映されません。

:::

## 改行なしで出力したい（`--no-newline`）

```console
$ nu --no-newline -c "1 + 1"
2
```

`--no-newline`オプションで、`-c`で実行した式の戻り値を末尾の改行なしで出力できます。
他のコマンドの引数としてそのまま渡したいときに便利です。
