# CapsLockを消したい

{guilabel}`CapsLock`キーを{guilabel}`Control`キーに置き換える方法です。

{file}`/etc/default/keyboard`を編集し、
`XKBCONFIG=ctrl:nocaps`の設定を追加します。

```console
$ sudo vi /etc/default/keyboard
```

```unixconfig
...
XKBCONFIG=ctrl:nocaps
...
```
