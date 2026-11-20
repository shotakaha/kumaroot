# 互換性を確認したい（`plautopatch`）

:::{note}

(u)pLaTeXの設定です。
LuaLaTeXでは必要ありません。

:::

```latex
\RequirePackage{plautopatch}
\documentclass{jsarticle}
```

(u)pLaTeXを使う場合は、`\documentclass`より前で読み込んでおくとよいパッケージです。
クラスファイルなどが互換性のないパッケージを読み込む可能性があるため、先に読み込んでおきます。
(u)pLaTeXと互換性がないパッケージを読み込んでしまった場合に、
その衝突を解消できるパッケージを自動で読み込んでくれます。

自動で追加されたパッケージがある場合は、`\end{document}`の時点で、
「List of packages loaded by 'plautopatch'」として一覧が表示されます。
