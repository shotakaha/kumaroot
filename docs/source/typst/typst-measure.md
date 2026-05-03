# コンテンツサイズしたい（`measure`）

```typst
#let content = "Hello, world!"

#context {
  let size = measure(content)
}
```

`measure`関数で、指定したコンテンツのサイズ（`width`と`height`）を取得できます。
この関数は`context`関数の中で使用する必要があります。
