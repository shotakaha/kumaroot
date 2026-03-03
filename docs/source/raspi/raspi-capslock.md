# キーボード設定したい（`/etc/default/keyboard`）

```console
// ファイルを編集する
$ sudo vi /etc/default/keyboard
// 再起動する
$ sudo reboot
```

`/etc/default/keyboard`を編集して
Raspberry Piのキーボードレイアウトやキーマッピングを変更できます。

ファイルの編集には管理者権限が必要です。
また、編集後は再起動が必要です。

## オプションキーしたい（`XKBOPTIONS`）

```bash
XKBOPTIONS=""
# XKBOPTIONS="ctrl:nocaps"    # CapsLock -> Ctrlに置き換える
# XKBOPTIONS="ctrl:swapcaps"  # CapsLock <-> Ctrlを入れ替える
# XKBOPTIONS="shift:both_capslock"  # 左右のShiftを押してCapsLockを有効化
# XKBOPTIONS="compose:ralt"  # 右AltキーをComposeキーに置き換える
```

`XKBOPTIONS`でShift、Control、CapsLockなどの修飾キーのマッピングを変更できます。
デフォルトは未設定です。

### Caps Lockを Ctrl に置き換えたい（`XKBOPTIONS="ctrl:nocaps"`）

```diff
## /etc/default/keyboard

# KEYBOARD CONFIGURATION FILE

# Consult the keyboard(5) manual page.

XKBMODEL="pc105"
XKBLAYOUT="us"
XKBVARIANT=""
-XKBOPTIONS=""
+XKBOPTIONS="ctrl:nocaps"

BACKSPACE="guess"
```

`XKBOPTIONS="ctrl:nocaps"`で、
Caps LockキーをControlキーに変更できます。

:::{note}

よく使う設定なので、ファイル全体をサンプルとして書いておきます。

:::

### CapsLockとCtrlを入れ替えたい（`XKBOPTIONS="ctrl:swapcaps"`）

```diff
-XKBOPTIONS=""
+XKBOPTIONS=ctrl:swapcaps
```

`XKBOPTIONS="ctrl:swapcaps"`で、
CapsLockキーとControlキーを入れ替えることができます。

## XKB設定したい

```console
$ man keyboard
```

`/etc/default/keyboard`ファイルはXKB（X Keyboard Extension）の設定を管理するファイルです。
詳細な設定項目は`man keyboard`で確認できます。

## キーボードのモデルしたい（`XKBMODEL`）

```bash
XKBMODEL="pc105"
# XKBMODEL="pc104"  # PC104キーボード
```

`XKBMODEL`でキーボードのモデル名を変更できます。
デフォルトは`pc105`（標準的なPC用キーボード）です。

## キーボードのレイアウトしたい（`XKBLAYOUT`）

```bash
XKBLAYOUT="us"
# XKBLAYOUT="jp"  # 日本語配列
# XKBLAYOUT="gb"  # UK配列
```

`XKBLAYOUT`でキーボードのレイアウト名です。
デフォルトは`us`（USキーボード）です。

## レイアウトのバリアントしたい（`XKBVARIANT`）

```bash
XKBVARIANT=
# XKBVARIANT="dvorak"   # Dvorakレイアウト
# XKBVARIANT="colemak"  # Colemakレイアウト
```

`XKBVARIANT`でキーボードレイアウトのバリアント（変種）を変更できます。
デフォルトは未設定です。

## 削除キーしたい（`BACKSPACE`）

```bash
BACKSPACE="guess"    # 自動判定
# BACKSPACE="bs"     # VT100準拠
# BACKSPACE="del"    # VT200準拠
```

`BACKSPACE`でBackspaceキーとDeleteキーの動作を変更できます。
デフォルトは`guess`です。

| 値 | 説明 |
|----|------|
| `guess` | 現在のターミナルやカーネル設定に基づいて自動判定（デフォルト） |
| `bs` | VT100準拠（Backspace = `^H` (ASCII BS)、Delete = `^?` (ASCII DEL)） |
| `del` | VT220準拠（Backspace = `^?` (ASCII DEL)、Delete = special sequence） |

## KMAP

XKBレイアウトの代わりに使用する従来型のキーマップファイルを指定します。
通常は設定不要です。

## リファレンス

- [man keyboard - Ubuntu Manpages](https://manpages.ubuntu.com/manpages/focal/man5/keyboard.5.html)
- [XKB - Wikipedia](https://en.wikipedia.org/wiki/X_keyboard_extension)
