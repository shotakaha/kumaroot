# JSONしたい（`jq`）

```console
$ brew install jq
```

`jq`コマンドでJSON形式のファイルを確認できます。

```console
$ jq [オプション] <フィルタ> [ファイル名...]
```

`jq <フィルタ> ファイル名`が基本的な書式です。
複数のファイルを指定できます。

```console
$ cat ファイル名.json | jq <フィルタ>
```

`cat`で表示した内容をパイプして使うこともできます。

## すべて表示したい

```console
$ jq . ファイル名.json
```

`.`フィルタで、JSONファイルの内容をすべて表示できます。

## 最上位のオブジェクトを表示したい（`keys`）

```console
$ jq 'keys' ファイル名.json
[
    "key 1",
    "key 2",
    "key3 "
]
```

`keys`フィルタで最上位のオブジェクトを抽出できます。
大きなJSONファイルの概要を把握するのに使います。

```console
$ jq '.[0] | keys' ファイル名.json
```

最上位のセクションが配列の場合、最初の要素（`.[0]`）に対してキーを取り出すようにします。

## 任意の階層のオブジェクトを表示したい

```console
$ jq -r 'paths(scalars) | select(length == N) | [.-1]' ファイル名.json
```

`paths(型)`フィルタで、**型** にマッチしたオブジェクトのすべてのパスの配列形式のリストを取得できます。
`scalars`はスカラー型のフィルタで数値、文字列、`true` / `false` / `null`にマッチします。
型を指定しない場合は「すべて（`scalars` / `objects` / `arrays` / `numbers` / `strings` / `booleans` / `nulls`）」にマッチします。
`select(条件式)`フィルタで、条件式にマッチした値を取得できます。
`.[-1]`フィルタで、リストの最後の要素を取得できます。

## 親の階層も表示したい

```console
$ jq -r 'paths(scalars) | select(length == 3) | "\\(.[1]) > \\(.[2])"' ファイル名.json
Level2_Key1 > Level3_Key1
Level2_Key2 > Level3_Key2
Level2_Key3 > Level3_Key3
```

`\(...)`の文字列テンプレート機能で、表示する文字列を制御できます。
`.[1]`でパスのインデックスが1（=2番目）の要素、
`.[2]`でパスのインデックスが2（=3番目）の要素が取得できるので
`レベル2 > レベル3`のようにキーが表示されます。

```console
$ jq -r 'paths(scalars) | select(length == 3) | "\\(.[1]) > \\(.[2])"' ファイル名.json | sort | uniq
```

大きなJSONファイルだと、同じ構造が繰り返されていることが多いです。
`sort`コマンドと`uniq`コマンドと組み合わせると、重複を削除できます。
キーの順番は失われますが、ファイルの概要を把握するのに役立ちます。

## 構造をしりたい

```console
$ jq 'paths | length' ファイル名.json | sort -n | tail -1
```

ファイルの階層の深さを確認できます。
`paths`フィルタで、すべてのオブジェクトをリストに変換します。
`length`フィルタで、リストのサイズを取得します。
`sort -n`で番号順にソートし、`tail -1`で末尾の値を表示します。

```console
$ jq 'walk(if type == "object" or type == "array" then . else type end)' ファイル名
```

ファイルの階層構造を保ちながら、値の型を表示します。

## YAMLしたい

```console
jq -r 'paths(scalars) as $p | "\($p | join(".")) = \(getpath($p))"' ファイル名.json
```

擬似的なYAML形式で表示します。
