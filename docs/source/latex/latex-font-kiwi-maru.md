# キウイ丸したい（`KiwiMaru`）

```console
$ brew install --cask font-kiwi-maru
```

Googleフォントにある[Kiwi Maru](https://fonts.google.com/specimen/Kiwi+Maru)を使います。
Homebrewでインストールできます。

```latex
% プリアンブル
\usepackage{luatexja-fontspec}

% 欧文フォント
\setmainfont{KiwiMaru-Light}
\setsansfont{KiwiMaru-Medium}
\setmonofont{KiwiMaru-Regular}

% 和文フォントの設定
\setmainjfont{KiwiMaru-Light}
\setsansjfont{KiwiMaru-Medium}
\setmonojfont{KiwiMaru-Regular}
```

3スタイルあるので、
見出しを`Medium`にし、本文を`Light`にしています。

:::{note}

フォント名を設定するとき、ハイフンはあってもなくてもOKです。

```latex
\setmainjfont{KiwiMaru-Light}  % OK
\setmainjfont{KiwiMaruLight}   % これもOK
```

:::
