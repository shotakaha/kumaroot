# ベーステンプレートを作りたい

```text
/layouts/_default/baseof.html
```

ウェブサイトの外骨格を定義するためのテンプレートです。
内容は必要なく「こういう構造だよね」というのを書けばOKです。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        {{ block "main" . }}
        <!-- メインのテンプレートで定義する -->
        {{ end }}

        {{ block "footer" . }}
        <!-- フッターのテンプレートで定義する -->
        {{ end }}
    </body>
</html>
```

## リファレンス

- [Base Templates and Blocks](https://gohugo.io/templates/base/)
