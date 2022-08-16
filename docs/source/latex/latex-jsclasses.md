# ``jsclasses``パッケージ

```latex
\documentclass[dvipdfmx]{jsarticle}             % pLaTeX
\documentclass[uplatex, dvipdfmx]{jsarticle}    % upLaTeX
\documentclass{ltjsarticle}                     % LuaLaTeX
```

使用するLaTeXの種類によって、書き方を少し変える必要があります。

``pLaTeX/upLaTeX``の場合は、これまでどおり``jsarticle``系（``jsclasses``）の
ドキュメントクラスを利用すればよいです。
LuaLaTeXの場合は、``jsarticle``と互換性の高い``ltjsarticle``という
ドキュメントクラスが利用できます。

```latex
\documentclass[uplatex, a4paper, 12pt, papersize, dvipdfmx]{jsarticle}
\documentclass[uplatex, a4paper, 12pt, papersize, dvipdfmx]{jsreport}
\documentclass[uplatex, a4paper, 12pt, papersize, dvipdfmx]{jsbook}
```

ドキュメントクラスのオプションには用紙サイズ（``[a4paper, papersize]``）、欧文フォントサイズ（``[12pt]``）、ドライバ（``[dvipdfmx]``）などを指定します。


## バリエーション

```latex
\documentclass{ltjsarticle}   % 論文・レポート用
\documentclass{ltjsreport}    % レポート用
\documentclass{ltjsbook}      % 書籍用
\documentclass{ltjspf}        % 某学会誌用
\documentclass{ltjskiyou}     % 某紀要用
```

## リファレンス

- {command}`texdoc jsclasses`
- {command}`texdoc ltjsclasses`
