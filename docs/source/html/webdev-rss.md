# RSSの作り方

```xml
<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="ja">
...ページの概要
...記事の概要
...記事の概要
...
</feed>
```

## ページ全体の概要

```xml
<title>ページのタイトル</title>
<link href="ページのURL" rel="alternate"/>
<link href="RSSのURL" rel="self" type="application/atom+xml"/>
<id>tag:タグ</id>
<updated>最終更新日</updated>
<author>
<name>ページの著者名</name>
</author>
<subtitle>
ページの概要
</subtitle>
<rights>ページのコピーライト</rights>
<generator>RSSジェネレーター名</generator>
```

## 記事の情報を追加したい

記事の情報は``<entry>...</entry>``の中にまとめます。

```xml
<entry>
<title>記事のタイトル</title>
<link href="記事のURL" rel="alternate"/>
<published>記事の公開日</published>
<updated>記事の更新日</updated>
<id>tag:タグ</id>
<summary>記事の概要</summary>
<author>
<name>記事の作成者</name>
</author>
</entry>
```

## タグを作りたい



## リファレンス

- [W3C Feed Validation Service3](https://validator.w3.org/feed/)
