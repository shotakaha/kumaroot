# 下書きしたい（`draft`）

```toml
draft = true
```

`draft`キーで下書き状態に設定できます。
下書き状態のページはレンダリングされません。

## テンプレートしたい（`.Draft`）

```html
{{ if .Draft }}
    <h1>[DRAFT]{{ .Title }}</h1>
{{ else }}
    <h1>{{ .Title }}</h1>
{{ end }}
```

`.Draft`で下書き状態かどうかを判定できます。
このサンプルでは、下書き状態のページタイトルに`[DRAFT]`を自動挿入しています。

## 設定したい

```toml
# hugo.toml
buildDraft = true
```

## オプションしたい

```console
$ hugo server --buildDraft
```

`--buildDraft`オプションで、下書き状態のページをビルドできます。
