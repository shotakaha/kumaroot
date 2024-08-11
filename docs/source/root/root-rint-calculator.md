# 電卓したい

![ROOTで電卓](./root-tutorial/root-calc.png)

ROOTのインタープリター（RINT）は電卓代わりに使えます。

四則演算の記号
{kbd}`+`
{kbd}`-`
{kbd}`*`
{kbd}`/`
{kbd}`%` はそのまま使えます。
べき乗や累乗根などはROOTの ``TMath``クラスを使います。
円周率 $\pi$（ ``TMath::Pi()`` ）や
自然定数 $e$（ ``TMath::E()`` ）のような
定数も入っています。
