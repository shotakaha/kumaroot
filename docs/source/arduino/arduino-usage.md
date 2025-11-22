# Arduinoの使い方

## Arduinoしたい

```{toctree}
arduino-setup
arduino-loop
```

## 開発環境したい

- arduino-platformio

## タイミングしたい

- arduino-delay
- arduino-delayMicroseconds
- arduino-micros
- arduino-millis

## デジタル入出力したい

- arduino-pinmode
- arduino-digitalwrite

## アナログ入出力したい

- arduino-analogread

## UART通信したい

```{toctree}
---
maxdepth: 1
---
- arduino-serial-begin
- arduino-serial-available
- arduino-serial-read
arduino-serial-print
arduino-json-serialize
```

## SPI通信したい

- arduino-spi-begin
- arduino-spi-beginTransaction
- arduino-spi-transfer
- arduino-spi-endTransaction

## I2C通信したい

- arduino-wire-begin
- arduino-wire-beginTransmission
- arduino-wire-write
- arduino-wire-endTransmission
- arduino-wire-requestFrom
- arduino-wire-available
- arduino-wire-read

## Wi-Fi通信したい

```{toctree}
arduino-wifi-begin
- arduino-wifi-mode
- arduino-wifi-connect
- arduino-wifi-status
- arduino-wifi-localip
```

## Bluetooth通信したい

- arduino-bledevice-init
- arduino-bledevice-power
- arduino-bledevice-advertising
- arduino-bledevice-securityauth
- arduino-bledevice-securitypasskey
- arduino-bledevice-createserver

## BME280センサーしたい

- bme280-begin
- bme280-readTemperature
- bme280-readPressure
- bme280-readHumidity

## ファイル保存したい

```{toctree}
arduino-littlefs
arduino-littlefs-open
arduino-littlefs-read
arduino-littlefs-print

- arduino-littlefs-rename
- arduino-littlefs-remove
- arduino-littlefs-mkdir
- arduino-littlefs-rmdir
```
