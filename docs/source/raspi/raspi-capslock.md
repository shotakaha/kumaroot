# CapsLockを置換したい

```diff
## /etc/default/keyboard

# KEYBOARD CONFIGURATION FILE

# Consult the keyboard(5) manual page.

XKBMODEL="pc105"
XKBLAYOUT="us"
XKBVARIANT=""
-XKBOPTIONS=""
+XKBOPTIONS=ctrl:nocaps

BACKSPACE="guess"
```

{guilabel}`CapsLock`キーを{guilabel}`Control`キーに置き換えます。
{file}`/etc/default/keyboard`を編集し、
``XKBOPTIONS=ctrl:nocaps``に変更して、リブートします。
{file}`/etc/default/keyboard`の編集には管理者権限が必要です。

```console
$ sudo vi /etc/default/keyboard
```

## CapsLockを入れ替えたい

```diff
## /etc/default/keyboard

# ..省略
-XKBOPTIONS=""
+XKBOPTIONS=ctrl:swapcaps
```

{guilabel}`CapsLock`キーと{guilabel}`Control`キーを入れ替えます。
{file}`/etc/default/keyboard`を編集し、
``XKBOPTIONS=ctrl:swapcaps``に変更して、リブートします。

## XKBの設定項目

設定項目は``man keyboard``で確認できます。
以下はその内容の抜粋です。

XKBMODEL
: キーボードのモデル名を設定します。デフォルトは``pc105``です。

XKBLAYOUT
: キーボードのレイアウト名です。デフォルトは``us``です。

XKBVARIANT
: キーボードのバリアントです。デフォルトは``""（not set）``です。

XKBOPTIONS
: キーボードのオプション設定です。修飾キー（``Shift`` / ``Control`` など）が変更できます。デフォルトは``""（not set）``です。

BACKSPACE
: {guilabel}`BackSpace`と{guilabel}`Delete`キーの動作の設定です。
  ``bs`` / ``del`` / ``guess`` が設定できます。
  ``guess``の場合、現在のターミナルやカーネル設定が適用されます。
  ``bs``の場合、``VT100-conformant``な動作になります（``BackSpace`` = ``^H（ASCII BS）``、``Delete`` = ``^?（ASCII DEL）``
  ``del``の場合、``VT220-conformant``な動作になります（``BackSpace`` = ``^?（ASCII DEL）``、``Delete`` = special function sequence）

KMAP
: デフォルトでは設定不要です。
  XKBレイアウトを利用したくない場合に、代替キーマップを設定できます。
  （詳細は省略）
