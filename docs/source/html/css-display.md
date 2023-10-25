# 要素を変更したい（``display``）

```css
display: 内側 外側;
```

[display](https://developer.mozilla.org/ja/docs/Web/CSS/display)プロパティを使って、HTMLタグの表示方法を設定できます。
内側は``block``と``inline``の2つのキーワード、
外側は``flow``、``flow-root``、``flex``、``grid``の4つのキーワードを指定できます。

これまでの1つのキーワードで書く方法も残してあります。

```css
display: block flow;  /* 現在の書き方 */
display: block;       /* これまでの書き方 */

display: inline flow-root;
display: inline-block;
```

## ブロック要素したい（``display: block flow``）

```bash
セレクタ {
    display: block flex;
    width: 100vw;
    height: 100vw;
}
```

ブロック要素は``width``と``height``を設定でき、要素の前後で改行します。

## インライン要素したい（``display: inline flow``）

```bash
セレクタ {
    display: inline flow;
}
```

インライン表示にできます。
