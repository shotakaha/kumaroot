# Arduinoしたい（`arduino-cli`）

```console
$ arduino-cli board list
$ arduino-cli sketch new スケッチ名
$ arduino-cli compile スケッチ名
$ arduino-cli upload スケッチ名
```

`arduino-cli`で、ターミナルでArduino IDEのような操作ができます。

:::{note}

VS CodeのArduino IDEプラグインがdeprecatedになってしまったので、こちらのコマンドも覚えることにしました。

:::

## インストールしたい（`arduino-cli`）

```console
$ brew install arduino-cli

$ arduino-cli version
arduino-cli  Version: 1.0.4 Commit: Homebrew Date: 2024-08-12T13:32:50Z
```

## ボードを確認したい（`board`）

```console
// 接続されたボードを確認
$ arduino-cli board list
Port                            Protocol Type        Board Name FQBN Core
/dev/cu.Bluetooth-Incoming-Port serial   Serial Port Unknown

// すべてのボード名とFQBNを確認
$ arduino-cli board listall
```

`board`コマンドとそのサブコマンドで、ボード情報を確認できます。
`list`コマンドで、いまのパソコンに接続されているボード名を確認できます。
デバイスを接続したはずなのに通信できない場合は、まずこのコマンドを使って、認識されているか確認できます。

FQBN（Full Qualified Board Name）は、Arduinoボードに一意に割り当てられる識別子です。
`<パッケージ名>:<アーキテクチャ名>:<ボード名>`という形式で書かれています。

| モジュール名 | FQBN |
|---|---|
| ESP32 Dev Module | `esp32:esp32:esp32` |
| ESP32C3 Dev Module | `esp32:esp32:esp32c3` |
| ESP32S2 Dev Module | `esp32:esp32:esp32s2` |
| ESP32-WROOM-DA Module | `esp32:esp32:esp32da` |

ESP32系のモジュールもいろいろな種類があり、それぞれに異なるFQBNが割り当てられています。

## パッケージ／ライブラリ更新したい（`update` / `outdated` / `upgrade`）

```console
// インデックスを更新
$ arduino-cli update
Downloading index: library_index.tar.bz2 downloaded
Downloading index: package_index.tar.bz2 downloaded

$ arduino-cli outdated
ID          Name  Installed  Latest Location Description
esp32:esp32 esp32 2.0.11     3.0.5

$ arduino-cli upgrade
```

`update`コマンドで、コアパッケージとライブラリのインデックスを更新できます。
`core update-index`と`lib update-index`をそれぞれ実行しているのだと思います。

## コアパッケージしたい（`core`）

```console
// インストール済みのコアパッケージを確認
$ arduino-cli core list
ID          Installed Latest Name
arduino:avr 1.8.6     1.8.6  Arduino AVR Boards
esp32:esp32 2.0.11    3.0.5  esp32

// インデックスを更新
$ arduino-cli core update-index
Downloading index: package_index.tar.bz2 downloaded

// コアパッケージを更新
$ arduino-cli core upgrade
Tool arduino:dfu-util@0.11.0-arduino5 already installed
Tool esp32:mklittlefs@3.0.0-gnu12-dc7f933 already installed
Tool esp32:mkspiffs@0.2.3 already installed
Downloading packages...
esp32:esp-rv32@2302 downloaded
esp32:esp-x32@2302 downloaded
esp32:esp-xs2@2302 downloaded
esp32:esp-xs3@2302 downloaded
esp32:esp32-arduino-libs@idf-release_v5.1-33fbade6 downloaded
esp32:esptool_py@4.6 downloaded
esp32:openocd-esp32@v0.12.0-esp32-20240821 downloaded
esp32:riscv32-esp-elf-gdb@12.1_20231023 downloaded
esp32:xtensa-esp-elf-gdb@12.1_20231023 downloaded
esp32:esp32@3.0.5 downloaded
Installing esp32:esp-rv32@2302...
Configuring tool....
esp32:esp-rv32@2302 installed
Installing esp32:esp-x32@2302...
Configuring tool....
esp32:esp-x32@2302 installed
Installing esp32:esp-xs2@2302...
Configuring tool....
esp32:esp-xs2@2302 installed
Installing esp32:esp-xs3@2302...
Configuring tool....
esp32:esp-xs3@2302 installed
Installing esp32:esp32-arduino-libs@idf-release_v5.1-33fbade6...
Configuring tool....
esp32:esp32-arduino-libs@idf-release_v5.1-33fbade6 installed
Installing esp32:esptool_py@4.6...
Configuring tool....
esp32:esptool_py@4.6 installed
Installing esp32:openocd-esp32@v0.12.0-esp32-20240821...
Configuring tool....
esp32:openocd-esp32@v0.12.0-esp32-20240821 installed
Installing esp32:riscv32-esp-elf-gdb@12.1_20231023...
Configuring tool....
esp32:riscv32-esp-elf-gdb@12.1_20231023 installed
Installing esp32:xtensa-esp-elf-gdb@12.1_20231023...
Configuring tool....
esp32:xtensa-esp-elf-gdb@12.1_20231023 installed
Replacing platform esp32:esp32@2.0.11 with esp32:esp32@3.0.5...
Uninstalling esp32:esp32@2.0.11...
Running pre_uninstall script....
Platform esp32:esp32@2.0.11 uninstalled
Uninstalling esp32:xtensa-esp32-elf-gcc@esp-2021r2-patch5-8.4.0, tool is no more required...
Running pre_uninstall script....
Tool esp32:xtensa-esp32-elf-gcc@esp-2021r2-patch5-8.4.0 uninstalled
Uninstalling esp32:xtensa-esp32s2-elf-gcc@esp-2021r2-patch5-8.4.0, tool is no more required...
Running pre_uninstall script....
Tool esp32:xtensa-esp32s2-elf-gcc@esp-2021r2-patch5-8.4.0 uninstalled
Uninstalling esp32:xtensa-esp32s3-elf-gcc@esp-2021r2-patch5-8.4.0, tool is no more required...
Running pre_uninstall script....
Tool esp32:xtensa-esp32s3-elf-gcc@esp-2021r2-patch5-8.4.0 uninstalled
Uninstalling esp32:xtensa-esp-elf-gdb@11.2_20220823, tool is no more required...
Running pre_uninstall script....
Tool esp32:xtensa-esp-elf-gdb@11.2_20220823 uninstalled
Uninstalling esp32:riscv32-esp-elf-gcc@esp-2021r2-patch5-8.4.0, tool is no more required...
Running pre_uninstall script....
Tool esp32:riscv32-esp-elf-gcc@esp-2021r2-patch5-8.4.0 uninstalled
Uninstalling esp32:riscv32-esp-elf-gdb@11.2_20220823, tool is no more required...
Running pre_uninstall script....
Tool esp32:riscv32-esp-elf-gdb@11.2_20220823 uninstalled
Uninstalling esp32:openocd-esp32@v0.11.0-esp32-20221026, tool is no more required...
Running pre_uninstall script....
Tool esp32:openocd-esp32@v0.11.0-esp32-20221026 uninstalled
Uninstalling esp32:esptool_py@4.5.1, tool is no more required...
Running pre_uninstall script....
Tool esp32:esptool_py@4.5.1 uninstalled
Uninstalling esp32:mkspiffs@0.2.3, tool is no more required...
Uninstalling esp32:mklittlefs@3.0.0-gnu12-dc7f933, tool is no more required...
Uninstalling arduino:dfu-util@0.11.0-arduino5, tool is no more required...
Configuring platform....
Platform esp32:esp32@3.0.5 installed

// パッケージ名の検索とインストール／アンインストール
$ arduino-cli core search パッケージ名
$ arduino-cli core install パッケージID
$ arduino-cli core uninstall パッケージID
```

`core`コマンドとそのサブコマンドでコアパッケージ操作ができます。

## ライブラリしたい（`lib`）

```console
// インストール済みのライブラリを確認
$ arduino-cli lib list
Name                    Installed Available     Location Description
Adafruit BME280 Library 2.2.4     -             user     -
Adafruit BusIO          1.16.0    1.16.1        user     This is a library for abstracting awa...
Adafruit Unified Sensor 1.1.14    -             user     -

// ライブラリのインデックスを更新
$ arduino-cli lib update-index
Downloading index: library_index.tar.bz2 downloaded

// インストール済みのライブラリを一括で更新
$ arduino-cli lib upgrade
Downloading Adafruit BusIO@1.16.1...
Adafruit BusIO@1.16.1 downloaded
Installing Adafruit BusIO@1.16.1...
Replacing Adafruit BusIO@1.16.0 with Adafruit BusIO@1.16.1...
Installed Adafruit BusIO@1.16.1

// ライブラリの検索とインストール／アンインストール
$ arduino-cli lib search ライブラリ名
$ arduino-cli lib install ライブラリ名
$ arduino-cli lib uninstall ライブラリ名
```

`lib`コマンドとそのサブコマンドを使ってライブラリ操作ができます。
ライブラリを吟味する場合は、IDEの詳細画面を使ったほうがやりやすいかもしれません。
インストールしたライブラリの確認と更新には、このコマンドが便利です。

## コンパイルしたい（`compile`）

```console
$ arduino-cli compile スケッチ名 --fqbn ボードのFQBN
```

`compile`コマンドで、スケッチをコンパイルできます。
`--fqbn`オプションで、ボードのFQBNを指定できます。

## 書き込みたい（`upload`）

```console
// ポート名とFQBNを確認
$ arduino-cli board list

$ arduino-cli upload スケッチ名 --port ポート名 --fqbn ボードのFQBN
```

`upload`コマンドで、Arduinoデバイスにスケッチを書き込めます。

## コマンド補完したい（`completion`）

```console
$ arduino-cli completion fish > ~/.config/fish/completions/arduino-cli.fish
```

## 設定したい（`config`）

```console
// 現在の設定を確認する
$ arduino-cli config dump
{}

// 設定を初期化する
$ arduino-cli config init
Config file written to: ~/Library/Arduino15/arduino-cli.yaml

// 設定を確認する
$ arduino-cli config dump
board_manager:
    additional_urls: []
```

`config`コマンドで、Arduino周りの設定ができます。
設定ファイルは`~/Library/Arduino15/arduino-cli.yaml`に作成されました。
