```{eval-rst}
.. index::
    pair: Hugo; usage
```

# Hugoの使い方

``Hugo``はGo製の静的サイトジェネレーター（SSG）です。
[Benefits of static site generator](https://gohugo.io/about/benefits/)や
[Hugo Features](https://gohugo.io/about/features/)にHugoを使う利点が書かれています。
[各種エディター用のプラグイン](https://gohugo.io/tools/editors/)もあります。

より具体的な使い方は[Blowfishテーマのドキュメント](https://blowfish.page/docs/)がとても参考になりました。

:::{hint}

[Site Generators - Jamstack](https://jamstack.org/generators/)で流行のSSGを確認できます。
[Next.js](https://nextjs.org/)や[Gatsby](https://www.gatsbyjs.com/)といったJSベースのSSGが人気の上位を占めていますが、JavaScript/TypeScript（やJSX/MDX）といった知識も必要で、僕にはちょっとキャパオーバーでした。
HugoはJSの知識がなくても（そしてGoの知識がなくても）、HTML/CSS/Markdownの知識だけでなんとかできるのがよいと思っています。

:::

```{toctree}
---
maxdepth: 1
---
hugo-install
hugo-page-bundles
hugo-config
hugo-content
hugo-layouts
hugo-data
hugo-assets
hugo-static
hugo-themes
```

## 再編中

```{toctree}
---
maxdepth: 1
---
hugo-new
hugo-demo
hugo-page-variables
hugo-frontmatter
hugo-shortcodes-figure
hugo-scratch
hugo-printf
hugo-tableofcontents
```

## テンプレートしたい

```{toctree}
---
maxdepth: 1
---
hugo-title
hugo-ogp
hugo-pipes-tocss
```

## 多言語したい

```{toctree}
---
maxdepth: 1
---
hugo-config-languages
hugo-i18n
```

## デプロイしたい

```{toctree}
---
maxdepth: 1
---
hugo-gitlab
```

## リファレンス

- [Hugo](https://gohugo.io/)
