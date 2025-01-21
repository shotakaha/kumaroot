# 互換性を確認したい（`plautopatch`）

:::{note}

(u)pLaTeXの設定です。
LuaLaTeXでは必要ありません。

:::

```latex
%\RequirePackage{plautopatch}
\documentclass{jsarticle}
```

(u)pLaTeXを使う場合は、ファイルの一番先頭で読み込んでおくとよいパッケージです。
(u)pLaTeXと互換性がないパッケージを読み込んでしまった場合に、
その衝突を解消できるパッケージを自動で読み込んでくれます。

パッケージの衝突があった場合は、
自動追加されたパッケージの一覧を実行結果で確認できます。
