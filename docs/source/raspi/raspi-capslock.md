# キーボード設定したい（`/etc/default/keyboard`）

Raspberry Piのキーボードレイアウトやキーマッピングは、`/etc/default/keyboard`ファイルで設定できます。

## Caps Lockを Ctrl に置き換えたい

```bash
sudo vi /etc/default/keyboard
```

`/etc/default/keyboard`ファイルを編集し、`XKBOPTIONS`行を以下のように変更します。

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

その後、再起動してください。

```bash
sudo reboot
```

Caps LockキーがControlキーとして機能するようになります。

## CapsLockとCtrlを入れ替えたい

```bash
sudo vi /etc/default/keyboard
```

`/etc/default/keyboard`ファイルの`XKBOPTIONS`行を以下のように変更します：

```diff
-XKBOPTIONS=""
+XKBOPTIONS=ctrl:swapcaps
```

再起動してください。

```bash
sudo reboot
```

CapsLockキーとControlキーの役割が入れ替わります。

## /etc/default/keyboard について

`/etc/default/keyboard`ファイルはXKB（X Keyboard Extension）の設定を管理します。
詳細な設定項目は`man keyboard`で確認できます。

### XKBMODEL

キーボードのモデル名を設定します。デフォルトは`pc105`（標準的なPC用キーボード）です。

例：

- `pc105` - 標準的なPC 105キーボード（推奨）
- `pc104` - PC 104キーボード

### XKBLAYOUT

キーボードのレイアウト名です。デフォルトは`us`（USキーボード）です。

例：

- `us` - US配列
- `jp` - 日本語配列
- `gb` - UK配列

### XKBVARIANT

キーボードレイアウトのバリアント（変種）です。デフォルトは未設定です。

例：
- 空文字列（未設定）
- `dvorak` - Dvorakレイアウト
- `colemak` - Colemakレイアウト

### XKBOPTIONS

キーボードのオプション設定です。修飾キー（Shift、Controlなど）のマッピングを変更できます。
デフォルトは未設定です。

よく使う設定値：

| オプション | 説明 |
|----------|------|
| `ctrl:nocaps` | Caps Lockを Ctrlに置き換え |
| `ctrl:swapcaps` | Caps Lockと Ctrlを入れ替え |
| `shift:both_capslock` | 両方の Shiftキーを押して Caps Lockを有効化 |
| `compose:ralt` | 右 Altキーを Composeキーに設定 |

### BACKSPACE

BackspaceキーとDeleteキーの動作を設定します。

| 値 | 説明 |
|----|------|
| `guess` | 現在のターミナルやカーネル設定に基づいて自動判定（デフォルト） |
| `bs` | VT100準拠（Backspace = `^H` (ASCII BS)、Delete = `^?` (ASCII DEL)） |
| `del` | VT220準拠（Backspace = `^?` (ASCII DEL)、Delete = special sequence） |

### KMAP

XKBレイアウトの代わりに使用する従来型のキーマップファイルを指定します。
通常は設定不要です。

## リファレンス

- [man keyboard - Ubuntu Manpages](https://manpages.ubuntu.com/manpages/focal/man5/keyboard.5.html)
- [XKB - Wikipedia](https://en.wikipedia.org/wiki/X_keyboard_extension)
