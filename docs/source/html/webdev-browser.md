# ブラウザ対応を確認したい

```console
# 使いたい機能の対応状況を調べる
https://caniuse.com/?search=container-queries
```

新しいHTML・CSS・JavaScriptの機能は、ブラウザによって使えたり使えなかったりします。
コードを書く前に「その機能が今どこまで使えるか」を確認します。

やり方は大きく2つです。

1. 開発時に [Can I use](https://caniuse.com/) や [Baseline](https://web.dev/baseline/) で対応状況を調べる
2. コード側で「対応していれば使う」と分岐を書く（`@supports`、機能検出）

## 対応状況を調べたい（Can I use）

```console
https://caniuse.com/mdn-css_at-rules_container
```

[Can I use](https://caniuse.com/)で機能名を検索すると、
ブラウザごと・バージョンごとの対応状況が表で見られます。

- 緑 … 対応済み
- 赤 … 未対応
- 黄 … 部分対応・フラグ付き

ページ下部の「Global」の数字が、世界全体でその機能を使える利用者の割合です。

MDNの各ページ下部にも、同じデータの「ブラウザーの互換性」表があります。

## 広く使えるか知りたい（Baseline）

[Baseline](https://web.dev/baseline/)は、
「主要ブラウザすべてで安定して使えるか」をひとことで示す指標です。

- **Newly available** … 最近すべての主要ブラウザで使えるようになった
- **Widely available** … 使えるようになってから十分に時間が経ち、安心して使える

MDNのページ冒頭にも`Baseline`のバッジが表示されます。
「Widely available」なら、フォールバックなしで使ってよい目安になります。

## CSSで分岐したい（`@supports`）

```css
/* グリッドに対応していれば使う */
@supports (display: grid) {
    .layout {
        display: grid;
    }
}

/* 対応していない場合 */
@supports not (display: grid) {
    .layout {
        display: block flow-root;
    }
}
```

`@supports`で、「そのCSSプロパティと値の組み合わせに対応しているか」で分岐できます。

対応していないブラウザは`@supports`のブロックをまるごと無視するので、
新しいCSSを安全に足していけます。

## JavaScriptで分岐したい（機能検出）

```javascript
// その機能（プロパティやメソッド）が存在するか調べる
if ("IntersectionObserver" in window) {
    // 対応している場合の処理
} else {
    // 対応していない場合の代替処理
}
```

JavaScriptでは、「使いたい機能が存在するか」を直接調べます（機能検出、feature detection）。

## User-Agentでの判定は避ける

```javascript
// 避けたい書き方
if (navigator.userAgent.includes("Chrome")) { ... }
```

`navigator.userAgent`（や`User-Agent`ヘッダー）でブラウザ名を調べて分岐する方法は、昔よく使われました。

しかし、UA文字列は各ブラウザが他のブラウザのふりをするために複雑化しており、判定を間違えやすいです。
新しいブラウザが出るたびに条件の追加も必要になります。

「Chromeかどうか」ではなく「その機能が使えるか」で分岐するのが、いまの基本です。
どうしても環境情報が必要な場合は、UA文字列より[User-Agent Client Hints](https://developer.mozilla.org/ja/docs/Web/HTTP/Guides/Client_hints)を使います。

## リファレンス

- [Can I use](https://caniuse.com/)
- [Baseline](https://web.dev/baseline/)
- [@supports](https://developer.mozilla.org/ja/docs/Web/CSS/@supports)
- [User-Agent](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Headers/User-Agent)
- [ユーザーエージェント文字列を用いたブラウザーの判定](https://developer.mozilla.org/ja/docs/Web/HTTP/Guides/Browser_detection_using_the_user_agent)
