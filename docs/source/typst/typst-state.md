# 状態管理したい（`state`）

```typst
// stateを作成
#let s = state("key", initial_value)

// 値を取得（必ずcontext内でget）
#context s.get()

// 値を更新
#s.update(new_value)
#s.update(old_value => new_value)

// タイムトラベル機能
#context s.at(<label>)    // 特定のラベル位置での値
#context s.final()      // 最終値
```

`state`はドキュメントの状態を管理するための機能です。
Typstでは、関数の外部にある変数は読み取り専用となり、上書きできません。
また、Typstの内部処理において評価順序（evaluation order）と
レイアウト順序（layout order）があり、それぞれ更新のタイミングが異なります。
`state`で管理されたオブジェクトは常にレイアウト順序で更新されるため、
ドキュメントの最終的な見た目に基づいた正しい（＝より直感的な）順序で状態を取得できます。

さらに「タイムトラベル機能」があり、ドキュメント内の任意の位置から、
ラベルした他の位置での状態値を取得できます。

## 見出しカウンターしたい

```typst
#let chapter = state("chapter", 0)    // 章番号を初期化
#let section = state("section", 0)    // 節番号を初期化

// 見出し1が呼ばれるときに・・・
#show: heading.where(level: 1): it => {
    chapter.update(n => n+1)    // 章番号をインクリメント
    section.update(0)           // 節番号をリセット
    block[
        // 第 n 章 : 見出し1のテキスト
        第 #context chapter.get() 章 : #it.body
    ]
}

// 見出し2が呼ばれるときに・・・
#show: heading.where(level: 2): it => {
    section.update(n => n+1)    // 節番号をインクリメント
    block[
        // 第 n.m 節 : 見出し2のテキスト
        第 #context chapter.get().#context section.get() 節 : #it.body
    ]
}
```

「第n章」「第n.m節」のように見出しをカスタマイズするサンプルです。
章番号と節番号でそれぞれの`state`を定義し、見出しが呼ばれたときに更新しています。
`#context`を使って値を取得することで、レイアウト順序にしたがって適切に番号を振ることができます。

## 多言語対応

```typst
#let language = state("lang", "en")
#let translations = (
    en: (title: "Document", page: "Page"),
    ja: (title: "ドキュメント", page: "ページ"),
    fr: (title: "Document", page: "Page"),
)

#let t(key) = context {
    let lang = language.get()
    translations.at(lang).at(key)
}

#language.update("ja")
#t("title"): My Document
#t("page") 1 of 10
```

## リファレンス

- [state](https://typst.app/docs/reference/introspection/state/)
