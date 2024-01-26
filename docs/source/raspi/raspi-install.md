# インストールしたい

Raspberry Piのインストール手順は[公式サイト](https://www.raspberrypi.com/documentation/computers/getting-started.html#install-using-imager)に詳しく載っているので、まず、そちらを参照するとよいです。

## 事前準備

- Raspberry Pi 本体 + 周辺機器
- マイクロSDカード（32GB / FAT）
- Raspberry Pi Imager のインストール

OSイメージの書き込み公式の[Raspberry Pi Imager](https://www.raspberrypi.com/software/)を使います。
Homebrewを使ってインストールできます。

```console
$ brew install --cask raspberry-pi-imager
```

## マイクロSDカードを用意する

Raspberry Pi OSを書き込むマイクロSDカードを用意します。
マイクロSDカードは``FAT32``形式でフォーマットされている必要があります。

## OSを準備する

Raspberry Piで使用するOSイメージをマイクロSDカードに書き込みます。
