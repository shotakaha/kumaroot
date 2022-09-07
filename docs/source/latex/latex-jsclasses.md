# ``jsclasses``パッケージ

```latex
\documentclass{ltjsarticle}                     % LuaLaTeX
\documentclass[uplatex, dvipdfmx]{jsarticle}    % upLaTeX
\documentclass[dvipdfmx]{jsarticle}             % pLaTeX
```

使用するLaTeXエンジンによって、利用するドキュメントクラスが少し変わります。

 ``(u)pLaTeX``の場合、従来どおり``jsarticle``系のドキュメントクラスを利用します。
ドキュメントクラスのオプションには用紙サイズ（``[a4paper, papersize]``）、欧文フォントサイズ（``[12pt]``）、ドライバー（``[dvipdfmx]``）などを指定します。

``LuaLaTeX``の場合は、``jsarticle``と互換性の高い``ltjsarticle``クラスが利用できます。
``ltjsarticle``系ではドライバーの指定が不要です。

## 用紙サイズを変更したい

```latex
\documentclass[a4paper]{ltjsarticle}  % A4サイズ
\documentclass[a5paper]{ltjsarticle}  % A5サイズ
\documentclass[uplatex, b4paper, papersize]{jsarticle}  % B4サイズ
\documentclass[uplatex, b5paper, papersize]{jsarticle}  % B5サイズ
```

和文デフォルトは``a4paper``です。
``jsarticle``系は、``papersize``オプションも一緒に指定して、ドライバー（``dvipdfmx``）にPDFのページサイズを教えてあげる必要があります。

## フォントサイズを変更したい

```latex
\documentclass[10pt]{ltjsarticle}  % 10pt（デフォルト）
\documentclass[uplatex, 12pt]{jsarticle}  % 12pt
```

## 段組みしたい

```latex
\documentclass[twocolumn]{ltjsarticle}
\documentclass[uplatex, twocolumn]{jsarticle}
```

## トンボを表示したい

```latex
\documentclass[tombow]{ltjsarticle}
\documentclass[tombo]{ltjsarticle}
```

## リファレンス

- {command}`texdoc jsclasses`
- {command}`texdoc ltjsclasses`
