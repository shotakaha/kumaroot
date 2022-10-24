# 正規表現を使いたい

```python
import re
re.match("正規表現パターン", "対象文字列")
re.search("正規表現パターン", "対象文字列")
```

``match``は文字列の先頭でのみマッチを確認し、
``search``は文字列のどこでもマッチを確認する基本的な感数です。
それぞれの動作の違いの詳細は[search vs. match](https://docs.python.org/ja/3/library/re.html#search-vs-match)を参照してください。

同じ正規表現パターンを繰り返して利用する場合は、``re.compile``して正規表現オブジェクトを作成するとよいみたいです。

```python
p = re.compile("正規表現パターン")
p.match("対象文字列")
p.search("対象文字列")
```

## IPアドレスを検索したい

```python
matched = re.search("(\d{1,3}\.){3}\d{1,3}", "対象文字列") # IPv4
matched.group()
```

```python
matched = re.search("([0-9A-Fa-f]{0,4}:){7}[0-9A-Fa-f]{0,4}", "対象文字列") # IPv6
matched.group()
```

``\d``は``[0-9]``を意味するメタ文字です。
IPv4アドレスに必要な3桁の整数値は``\d{1,3}``で表現できます。
これをピリオド（``.``）を使って4つ組み合わせています。

```{note}
``\d{1,3}``は0--999にマッチします。
IPv4アドレス値は0--255（8ビット）しか取らないのですが、
これをきちんと書こうとするとめんどくさいので手を抜いています。

きちんと書くと ``(\d{1,2}|1\d{2}|2[0-5]{2})``（= 0--99 + 100--199 + 200--255）でしょうか。
```

## 16進数を検索したい

```python
matched = re.search("[0-9A-Fa-f]", "対象文字列")
matched.group()
```

1桁の16進数は``[0-9A-Fa-f]``で表すことができます。
IPv6アドレスをマッチさせたい場合などに、この正規表現を繰り返して使います。

## リファラーを検索したい

```python
matched = re.search('\"[\S\s]+?\"', "対象文字列")
matched = re.search('(?P<referer>(\"[\S\s]+?\"))', "対象文字列")
matched.group("referer")
```

Apacheログに記録されているリファラー（``\"%{Referer}i\"``）やユーザーエージェント（``\"%{User-agent}i\"``）のように、``""``で囲まれたすべて文字列を検索できる正規表現です。

すべての文字を対象とするため``\S``（すべての非空白文字）と``\s``（すべての空白文字）のメタ文字を組み合わせています。
文字列の長さが分からないですが、あまりヒットさせすぎないように``+?``で最短マッチさせています。

## Apacheのアクセスログを検索したい

```python
regex_string = '(?P<remote_host>(\d{1,3}\.){3}\d{1,3}) (?P<ident>(\S+|-)) (?P<user>(\S+|-)) (?P<time>(\[[\S\s]+?\])) (?P<request_first_line>(\"[\S\s]+?\")) (?P<status>(\d+)) (?P<size>(\d+|-)) (?P<referer>([\S\s]*)) (?P<ua>(\"[\S\s]+?\"))'
p = re.compile(regex_string)
matched = p.match("ログ一行")

matched.group("remote_host")
matched.group("time")
matched.group("request_first_line")
matched.group("status")
matched.group("size")
matched.group("referer")
matched.group("ua")
```

正規表現を理解したかった大きな理由です。
まだ完全ではないですが、これで大体理解できた気がします。
名前をつけてマッチさせているので、``m.group("名前")``でデータを確認できます。

```text
%h : (\d{1,3}\.){3}\d{1,3} #IPv4のみ
%l : (\S+|-)
%u : (\S+|-)
%t : (\[[\S\s]+?\])
\"%r\" : (\"[\S\s]+?\")
%>s : (\d+)
%b : (\d+|-)
\"%{Referer}i\" : ([\S\s]*)
\"%{User-agent}i\" : (\"[\S\s]+?\")
```

## リファレンス

- [re - 正規表現操作](https://docs.python.org/ja/3/library/re.html)
- [re - search() vs. match()](https://docs.python.org/ja/3/library/re.html#search-vs-match)
