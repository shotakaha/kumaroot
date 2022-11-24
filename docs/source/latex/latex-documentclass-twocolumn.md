# 二段組したい

```latex
\documentclass[twocolumn]{jlreq}
\documentclass[twocolumn]{ltjsarticle}
\documentclass[uplatex, dvipdfmx, twocolumn]{jsarticle}
```

``jlreq``も``jsclasses``系も``twocolumn``オプションを使います。

## 段間を変更したい

```latex
\documentclass[twocolumn, column_gap=2zw]{jlreq}
```

``jlreq``では、段間（``column_gap``）をクラスオプションで設定します。

```latex
\documentclass[uplatex, dvipdfmx, twocolumn]{jsarticle}
\setlength{\columnsep}{2zw}
```

``jsclasses``系は``\setlength``を使って``\columnsep``の値を設定します。
