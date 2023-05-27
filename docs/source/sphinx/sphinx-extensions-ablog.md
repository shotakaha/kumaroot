# 記事したい（``ablog``）

```conosole
$ pip3 install ablog
```

```python
extensions = [
    "ablog",
    "sphinx.ext.intersphinx",
]

post_date_format = "%Y-%m-%d"
post_date_format_short = "%Y-%m-%d"
```

ブログのように時系列で記事を作成する場合、[ABlog for Sphinx](https://ablog.readthedocs.io/en/stable/index.html)を使うと便利です。
記事にはカテゴリやタグ、著者などのメタ情報も追加できます。
設定の詳細は[ABlog Configuration Options](https://ablog.readthedocs.io/en/stable/manual/ablog-configuration-options.html)を参照してください。

:::{hint}

``post_date_format_short``のようにドキュメントに記載がないオプションもありました。
[sunpy/ablog - GitHub](https://github.com/sunpy/ablog)にあるソースコードも確認するとよさそうです。

:::

## 1ページに1記事したい（``blogpost``）

```md
---
blogpost: true
date: 公開日
category: カテゴリ名
tags: タグ1, タグ2, タグ3
---

# 記事のタイトル

記事の本文。記事の本文。記事の本文。記事の本文。記事の本文。
記事の本文。記事の本文。記事の本文。記事の本文。記事の本文。

```

ページ全体を記事にする場合、フロントマターに``blogpost: true``を設定し、必要なメタデータを設定します。

## 1ページに複数記事したい（``post``）

```md
# 1ページに複数記事したい

:::{post} 公開日1
---
category: カテゴリ名
tags: タグ1, タグ2, タグ3
---

## 記事1のタイトル

記事1の本文。記事1の本文。記事1の本文。記事1の本文。記事1の本文。
記事1の本文。記事1の本文。記事1の本文。記事1の本文。記事1の本文。

:::

:::{post} 公開日2

---
category: カテゴリ名
tags: タグ1, タグ2, タグ3
---

## 記事2のタイトル

記事2の本文。記事2の本文。記事2の本文。記事2の本文。記事2の本文。
記事2の本文。記事2の本文。記事2の本文。記事2の本文。記事2の本文。

:::

```

``post``ディレクティブを使って、1ページに複数の記事を書くことができます。

## 記事一覧したい（``postlist``）

```md
:::{postlist}
---
format: "{date} : {title}"
sort: reversed
---
:::

```

``postlist``ディレクティブを使って、記事の一覧を作成できます。
リストを作成するときの表示形式は``format``で設定できます。

:::{hint}

サイドバーに表示する[recentsposts.html - GitHub](https://github.com/sunpy/ablog/blob/main/src/ablog/templates/ablog/recentposts.html)の``{date}``の表示形式は{file}``conf.py``の``post_date_format_short``が適用されます。
これは、ドキュメントに書かれてなくてハマったのでメモしておきます。

:::
