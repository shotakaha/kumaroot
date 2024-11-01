# フッターしたい（`footer`）

```html
<body>
    <main>...</main>
    <footer>
        <p>&copy; 2024 - KumaROOT</p>
    </footer>
</body>
```

`footer`タグでウェブサイトのフッター情報を囲みます。
ページ末尾に表示するため`main`タグの後に配置します。

フッターにはウェブサイトのコピーライト情報や、
サイト全体のナビゲーションを掲載することが多いです。

ウェブサイト全体で共通するパーツなので、
SSGやCMSを利用している場合は
部分テンプレートとして作成しておくとよいです。

## コンテンツ情報したい

```html
<body>
    <main>
        <article>
            コンテンツ本体
            <footer>
                コンテンツのメタ情報（作成日、著者名、など）
            </footer>
        </article>
    </main>
    <footer>...</footer>
</body>
```

`footer`要素はほとんどのフローコンテンツ要素の子要素として配置できます。
作成したページのメタ情報を表示したい場合は、
`article`の子要素として配置するとよいです。

## リファレンス

- [footer](https://developer.mozilla.org/ja/docs/Web/HTML/Element/footer)
