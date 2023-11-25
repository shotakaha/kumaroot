# ネストしたい

```css

:root {
    --color-text-main: black;
    --color-text-active: blue;
}

a {
    display: inline flow-root;
    color: var(--color-text-main);
    text-decoration: none;

    &:hover {
        color: var(--color-text-active);
    }
}
```

スタイルを入れ子構造で記述できます。
入れ子にすることで、スタイルの適用範囲が分かりやすくなります。

上記サンプルのように、リンクにホバーしたときに文字色を変えたい場合は、書くのがとても楽になりました。

:::{note}

これまでの書き方だと、以下のようになります。

```css
a {
    display: inline flow-root;
    text-decoration: none;
    color: var(--color-text-main);
}

a:hover {
    color: var(--color-text-active);
}
```

:::

:::{note}

[Can I use](https://caniuse.com/mdn-css_selectors_nesting)を確認すると、まだブラウザでフルサポートされていません。

:::
