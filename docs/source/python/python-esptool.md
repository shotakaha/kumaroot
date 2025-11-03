# ESP32したい（`esptool`）

```console
$ esptool flash-id
esptool v5.1.0
Connected to ESP32 on /dev/cu.usbserial-110:
Chip type:          ESP32-D0WD-V3 (revision v3.1)
Features:           Wi-Fi, BT, Dual Core + LP Core, 240MHz, Vref calibration in eFuse, Coding Scheme None
Crystal frequency:  40MHz
MAC:                04:83:08:61:ac:70

Stub flasher running.

Flash Memory Information:
=========================
Manufacturer: a1
Device: 4018
Detected flash size: 16MB
Flash voltage set by a strapping pin: 1.8V

Hard resetting via RTS pin...
```

`esptool`はEspressif公式のチップ確認ツールです。
上記はESP32-WROOM-32Eのチップに接続し`flash-id`を確認した様子です。

## インストールしたい

```console
$ uv tool install esptool
$ uvx esptool version
esptool v5.1.0
5.1.0
```
