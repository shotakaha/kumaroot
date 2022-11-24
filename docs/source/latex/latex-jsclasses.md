# ``jsclasses``クラスを使いたい

```latex
\documentclass{ltjsarticle}                     % LuaLaTeX
\documentclass[uplatex, dvipdfmx]{jsarticle}    % upLaTeX
\documentclass[dvipdfmx]{jsarticle}             % pLaTeX
```

使用するLaTeXエンジンによって、利用するドキュメントクラスが少し変わります。



## トンボを表示したい

```latex
\documentclass[tombow]{ltjsarticle}
\documentclass[uplatex, dvipdfmx, tombo]{jsarticle}
```

## リファレンス

- {command}`texdoc jsclasses`
- {command}`texdoc ltjsclasses`
