# 画像したい（`{{< figure >}}`）

- 本文

```markdown
![](画像ファイルのパス)
```

- 出力

```html
<img src="画像ファイルのパス">
```

## キャプションしたい

- ショートコード

```go
{{< figure src="画像ファイルのパス" title="画像のタイトル" >}}
```

- 出力

```html
<figure>
    <img src="画像ファイルのパス">
    <figcaption><h4>画像のタイトル</h4></figcaption>
</figure>
```

画像の表示を制御したい場合は、ビルトインの`{{< figure >}}`ショートコードを使います。

## オプションしたい

`figure`ショートコードは、さまざまなオプションに対応しています。

- `src`: 画像のパスもしくはURL
- `alt`: alt属性
- `title`: 画像のタイトル
- `caption`: 画像のキャプション
- `class`: class属性
- `height`: height属性
- `width`: width属性
- `loading`: loading属性
- `attr`:
- `attrlink`:
- `link`: 画像からリンクさせるURL
  - `target`: `target`属性
  - `rel`: `rel`属性
