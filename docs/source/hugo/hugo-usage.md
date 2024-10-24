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
hugo-new
hugo-themes
hugo-demo
hugo-data
hugo-static
hugo-page-variables
hugo-frontmatter
hugo-shortcodes-figure
hugo-scratch
hugo-printf
hugo-tableofcontents
```

## 全体設定したい

```{toctree}
---
maxdepth: 1
---
hugo-config
hugo-config-menu
hugo-config-permalinks
hugo-config-copyright
hugo-config-format
hugo-config-paginate
hugo-config-markup
hugo-config-services
```

% hugo-templates-homepage
## テンプレートしたい

```{toctree}
---
maxdepth: 1
---
hugo-title
hugo-taxonomy
hugo-layouts-baseof
hugo-layouts-single
hugo-layouts-list
hugo-layouts-home
hugo-layouts-404
hugo-partials-head
hugo-partials-meta
hugo-ogp
hugo-partials-header
hugo-partials-aside
hugo-partials-breadcrumbs
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
