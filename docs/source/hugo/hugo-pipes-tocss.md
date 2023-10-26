# Sassしたい

```html
{{ with resources.Get "sass/main.scss" | toCSS | minify | fingerprint }}
<link rel="stylesheet" href="{{ .RelPermalink }}" integrity="{{ .Data.Integrity }}" crossorigin="anonymous">
{{ end }}
```

[ToCSS関数](https://gohugo.io/hugo-pipes/transpile-sass-to-css/)を使って、SassからCSSに変換（トランスパイル）できます。
Hugo（のExtended版）には[LibSass](https://sass-lang.com/libsass/)が同梱されており、デフォルトで使えるようになっています。

:::{hint}

SassにはSASS記法（インデント）とSCSS記法（CSS-like）があります。
いろいろ調べてみたら、SCSS記法を使えばよさそうです。

:::

:::{note}

LibSassは2020年に開発が終了しました。
Sassの最新機能を利用する場合は[Dart Sass](https://sass-lang.com/dart-sass/)を使う必要があります。
``ToCss``のオプションで変更できます。

:::
