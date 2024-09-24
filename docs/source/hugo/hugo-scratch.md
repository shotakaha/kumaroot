# スクラッチ変数したい（``.Scratch / .newScratch``）

```go
{{ .Scratch.Set "キー" "値" }}
{{ .Scratch.Add "キー" "値" }}  // +演算子と同等
{{ .Scratch.Get "キー"}}
{{ .Scratch.Delete "キー" }}
```

[.Scratch](https://neohugo.github.io/functions/scratch/)関数は、Go templateのスコープ制限に対応するために導入されました。

テンプレートの中でよく使われているため、役割を理解しておくと、他の人が作成したテーマを読む時に役立つと思います。

## 辞書型したい

```go
{{ .Scratch.SetInMap "キー" "キー1" "値1"}}
{{ .Scratch.SetInMap "キー" "キー2" "値2"}}
{{ .Scratch.Get "キー" }}
```

## ローカル変数したい（``.newScratch``）

```go
{{ $変数名 := newScratch }}
{{ $変数名.Set "キー" "値" }}
```

スコープがローカルに限定された[.newScrach](https://neohugo.github.io/functions/scratch/#the-local-newscratch)関数もあります。

``.Scratch``に比べると、より変数っぽく使えます。
