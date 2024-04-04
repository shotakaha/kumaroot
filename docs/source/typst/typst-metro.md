# SI単位系したい（``metro``）

```typ
#import "@preview/metro:0.1.0": *

#qty(数量, "単位")
#unit("単位")
```

[metro](https://github.com/typst/packages/tree/main/packages/preview/metro/0.1.1)パッケージを使って、物理量を表現できます。

LaTeXの[siunitx](https://ctan.org/pkg/siunitx)パッケージのポート（を目指した）パッケージで、``#qty``や``#unit``関数などが使えます。

:::{seealso}

- [](../latex/latex-siunitx.md)

:::

## 物理量したい

```typ
SuperKEKBは周長が約#qty(3, "km")の加速器です。
Belle II 測定器は重さが約#qty(1400, "tonne")
縦横高さがそれぞれ約#qtyproduct(8 x 8 x 8, "meter")の巨大な装置です。
#qty(7, "GeV")の電子ビームと
#qty(4, "GeV")の陽電子ビームを衝突させ、大量のB中間子を生成します。
```

``#qty(数値, "単位"``コマンドで物理量をお手軽に表現できます。
単位は国際単位系（SI単位系）とその組立単位、また非SI単位系ですが慣習的に使っている単位などが利用できます。

:::{caution}

LaTeXの``siunitx``パッケージで便利な``qtyproduct``や``qtyrange``系のコマンドは実装されていないようです。

:::

## 電子ボルトした

```typ
// 単位名
#unit("electronvolt")
#unit("mega electronvolt")
#unit("giga electronvolt")
#unit("tera electronvolt")

// 省略した単位名
#unit("eV")
#unit("MeV")
#unit("GeV")
#unit("TeV")
```

「電子ボルト（``eV``）」は非SI単位系ですが、慣例的に利用してもよい単位のひとつです。
素粒子物理学で使うエネルギーの単位で、メガ（``M``）、ギガ（``G``）、テラ（``T``）の接頭辞と合わせることが多いです。
これらの接頭辞も含めて、話し言葉で使うような流れで表現できるようになっています。

:::{caution}

LaTeXの``siunitx``パッケージと違い、接頭辞と単位名の間に``_（半角スペース）``が必要です。

:::

## 指数したい

```typ
#num(6.02, e:23)
#num(1.6, e:-19)
```

## リファレンス

- [metro - Typst Universe](https://typst.app/universe/package/metro)
- [fenjalien/metro - GitHub](https://github.com/fenjalien/metro)
