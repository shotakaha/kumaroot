# ``jsclasses``クラスを使いたい

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





## 段組みしたい

```latex
\documentclass[twocolumn]{ltjsarticle}
\documentclass[uplatex, dvipdfmx, twocolumn]{jsarticle}
```

## トンボを表示したい

```latex
\documentclass[tombow]{ltjsarticle}
\documentclass[uplatex, dvipdfmx, tombo]{jsarticle}
```

## リファレンス

- {command}`texdoc jsclasses`
- {command}`texdoc ltjsclasses`
