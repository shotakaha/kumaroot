# 変更履歴したい（`changes`）

```latex
% プリアンブル
\usepackage{changes}

% レビュワーを設定
\definechangesauthor[name=<名前>, color=<色>]{<ID>}

% 本文
\added[id=<ID>, comment=<コメント>]{追加したテキスト}
\deleted[id=<ID>, comment=<コメント>]{削除するテキスト}
\replaced[id=<ID>, comment=<コメント>]{追加したテキスト}{削除するテキスト}
\highlight[id=<ID>, comment=<コメント>]{ハイライトするテキスト}
\comment[id=<ID>]{コメント}

% 変更箇所を一覧表示
\listofchanges[
    style=<style>,
    title=<title>,
    show=<type>]
```

`changes`は変更箇所をわかりやすく表示できるパッケージです。
Wordなどの変更履歴ツールのように、追加した部分や修正した部分を色とコメント付きで出力できます。

`\definechangesauthor[]{}`でレビュワーの情報を設定します。
ここで設定したIDで
`\added{}`、`\deleted{}`、`\replaced{}{}`、
などのコマンドを使います。
