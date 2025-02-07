# 欧文フォントしたい（`fontsetup`）

```latex
% プリアンブル
\usepackage[default]{fontsetup}
% mainfont: NewComputerModern
% mathfont: NewComputerModern Math
```

`fontsetup`は欧文の本文フォントと数式フォントを揃えて設定できるパッケージです。
内部で
[fontspecパッケージ](./latex-fontspec.md)と
[unicode-mathパッケージ](./latex-unicode-math.md)を
使っています。
