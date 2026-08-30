# RSSしたい（`Atom`）

```html
<!-- HTML の head で、フィードの場所を知らせる -->
<link rel="alternate" type="application/atom+xml"
      href="/feed.xml" title="サイト名の更新情報">
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="ja">
    <title>サイト名</title>
    <link href="https://example.com/" rel="alternate"/>
    <link href="https://example.com/feed.xml" rel="self"/>
    <id>https://example.com/</id>
    <updated>2026-08-30T12:00:00+09:00</updated>

    <entry>
        <title>記事のタイトル</title>
        <link href="https://example.com/blog/1" rel="alternate"/>
        <id>https://example.com/blog/1</id>
        <updated>2026-08-30T09:00:00+09:00</updated>
        <summary>記事の概要</summary>
    </entry>
</feed>
```

RSS／Atomは、サイトの更新情報を配信するためのXMLファイルです。
フィードリーダーがこのファイルを定期的に読みにきて、新着記事を利用者に知らせます。

古い`RSS 2.0`と新しい`Atom`の2つの形式がありますが、
仕様が明確な`Atom`が書きやすいので、ここでは`Atom`で説明します。

## フィードの場所を知らせたい（`<link rel="alternate">`）

```html
<head>
    <link rel="alternate" type="application/atom+xml"
          href="/feed.xml" title="サイト名の更新情報">
</head>
```

各ページの`head`に`<link rel="alternate">`を書くと、
ブラウザやフィードリーダーに「このサイトのフィードはここ」と伝えられます。

- `type="application/atom+xml"` … Atomフィードであること（RSS 2.0なら`application/rss+xml`）
- `href` … フィードファイルのパス
- `title` … フィードの名前

## フィード全体の情報を書きたい

```xml
<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="ja">
    <title>サイト名</title>
    <link href="https://example.com/" rel="alternate"/>
    <link href="https://example.com/feed.xml" rel="self"/>
    <id>https://example.com/</id>
    <updated>2026-08-30T12:00:00+09:00</updated>
    <author>
        <name>著者名</name>
    </author>
    <subtitle>サイトの説明</subtitle>
</feed>
```

`<feed>`タグの直下に、サイト全体の情報を書きます。

- `<title>` … サイト名
- `<link rel="alternate">` … サイトのトップページのURL
- `<link rel="self">` … このフィードファイル自身のURL
- `<id>` … フィードを一意に識別する文字列。ふつうはサイトのURLを使う
- `<updated>` … フィードを最後に更新した日時（ISO 8601形式）
- `<author>` … 著者。`<name>`を入れ子にする

## 記事を追加したい（`<entry>`）

```xml
<entry>
    <title>記事のタイトル</title>
    <link href="https://example.com/blog/1" rel="alternate"/>
    <id>https://example.com/blog/1</id>
    <published>2026-08-30T09:00:00+09:00</published>
    <updated>2026-08-31T10:00:00+09:00</updated>
    <summary>記事の概要（1〜2文）</summary>
    <author>
        <name>記事の著者</name>
    </author>
</entry>
```

記事1本ごとに`<entry>`タグを作り、`<feed>`の中に新しい順で並べます。

- `<published>` … 公開日時
- `<updated>` … 最終更新日時。公開時は`<published>`と同じでよい
- `<id>` … 記事を一意に識別する文字列。記事のURLを使う。**あとから変えない**
- `<summary>` … 記事の要約。本文全体を入れるなら`<content type="html">`を使う

並べる件数は10〜20件くらいが目安です。
古い記事はフィードから外します。

## 確認したい

書いたフィードが正しいXMLになっているかは、検証ツールで確認できます。

- [W3C Feed Validation Service](https://validator.w3.org/feed/)

`<id>`や`<updated>`の日時形式（ISO 8601）を間違えやすいので、公開前に一度通しておくとよいです。

## リファレンス

- [RFC 4287: The Atom Syndication Format](https://www.rfc-editor.org/rfc/rfc4287)
- [W3C Feed Validation Service](https://validator.w3.org/feed/)
- [RSS 2.0 Specification](https://www.rssboard.org/rss-specification)
