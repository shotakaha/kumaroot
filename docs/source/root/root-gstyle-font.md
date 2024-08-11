# フォントしたい（``gStyle->SetTextFont``）

```cpp
// フォント
gStyle->SetTextFont(62);

// 図タイトル
gStyle->SetTitleFont(62, "xyz");

// 軸ラベル
gStyle->SetLabelFont(62, "xyz");

// 凡例
gStyle->SetLegendFont(62);

// 統計情報
gStyle->SetStatFont(62);
```

``SetXXXFont``でフォントを変更できます。
フォントは以下の計算式で得られるコード番号で指定します。
フォントIDは14種類が設定されています。
任意の和文フォントを設定することはできなさそうです。

- ``font_code = 10 * font_id + precision``
  - ``font_id``: 1 - 14 (default: 6)
  - ``precision`` : 0 - 2  (default: 2)

## フォントID一覧

| Font ID | X11 | TrueType name | Is italic | boldness |
|---|---|---|---|---|
| 1 | times-medium-i-normal | Times New Roman | Yes | 4 |
| 2 | times-bold-r-normal | Times New Roman | No | 7 |
| 3 | times-bold-i-normal | Times New Roman | Yes | 7 |
| 4 | helvetica-medium-r-normal | Arial | No | 4 |
| 5 | helvetica-medium-o-normal | Arial | Yes | 4 |
| 6 | helvetica-bold-r-normal | Arial | No | 7 |
| 7 | helvetica-bold-o-normal | Arial | Yes | 7 |
| 8 | courier-medium-r-normal | Courier New | No | 4 |
| 9 | courier-medium-o-normal | Courier New | Yes | 4 |
| 10 | courier-bold-r-normal | Courier New | No | 7 |
| 11 | courier-bold-o-normal | Courier New | Yes | 7 |
| 12 | symbol-medium-r-normal | Symbol | No | 6 |
| 13 | times-medium-r-normal | Times New Roman | No | 4 |
| 14 | | Wingdings | No | 4 |

## リファレンス

- [9. Graphics and the Graphical User Interface - ROOT Users Guide](https://root.cern.ch/root/htmldoc/guides/users-guide/ROOTUsersGuide.html#graphics-and-the-graphical-user-interface)
