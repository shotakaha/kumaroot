# ベーステンプレートを作りたい（``/layouts/_default/baseof.html``）


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

ベーステンプレートは、
ウェブサイト内の全種類のページに共通する外骨格を定義するためのテンプレートで、
{file}`/layouts/_default/baseof.html`で定義します。

**記事ページ**などのシングルテンプレートや
**記事一覧**などのリストテンプレートを、
このベーステンプレートから派生させて設計することで、
これまで繰り返していた記述を共通化し、開発にかかる手間を削減できます。

具体的なコンテンツの内容は必要とせず「こういう構造だよ」ということを、
基本的なHTMLタグを使って設計します。
派生先のテンプレートで変更したい箇所は、
ブロックテンプレート機能を使って上書きできるようにしておきます。


## リファレンス

- [Base Templates and Blocks](https://gohugo.io/templates/base/)
