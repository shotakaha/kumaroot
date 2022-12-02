# 例文を差し込みたい（``bxjalipsum``）

```latex
\usepackage{bxjalipsum}
```

英文のサンプルでは``Lorem ipsum ...``がよく使われていて、``lipsum``パッケージもあります。
その日本語が``bxjalipsum``です。

## いろは唄したい

```latex
\jalipsum{iroha}
```

## 寿限無したい

```latex
\jalipsum{jugemu}
\jalipsum{jugemuP}  % 句読点（Punctuation）あり
```

## 憲法したい

```latex
\jalipsum{preamble}  % 日本国憲法・序文；4段落
```

## 夏目漱石したい

```latex
\jalipsum{wagahai}  % 吾輩は猫である；33段落
\jalipsum[2]{wagahai}
\jalipsum[1-3]{wagahai}
\jalipsum{kusamakura}  % 草枕；13段落
```

## 島崎藤村したい

```latex
\jalipsum{hatsukoi}  % 初恋；4段落
```
