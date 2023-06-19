# 二段組したい（``twocolumn``）

```latex
\documentclass[twocolumn]{jlreq}
```

```latex
\documentclass[twocolumn]{ltjsarticle}
\documentclass[uplatex, dvipdfmx, twocolumn]{jsarticle}
```

``jlreq``も``jsclasses``系も``twocolumn``オプションを使います。

## 段間を変更したい（``column_gap``）

```latex
\documentclass[twocolumn, column_gap=2zw]{jlreq}
```

``jlreq``では、段間（``column_gap``）をクラスオプションで設定します。

## 段間を変更したい（``\columnsep``）

```latex
\documentclass[uplatex, dvipdfmx, twocolumn]{jsarticle}
\setlength{\columnsep}{2zw}
```

``jsclasses``系は``\setlength``を使って``\columnsep``の値を設定します。
