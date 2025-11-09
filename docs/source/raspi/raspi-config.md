# raspi-configしたい

```bash
sudo raspi-config
```

`raspi-config`は、Raspberry Pi OSの設定を管理するコマンドラインツールです。

ホスト名、タイムゾーン、インターフェイス設定など、さまざまな設定をGUIから簡単に変更できます。


## カメラを有効にしたい

```bash
sudo raspi-config
# Interface Options → Camera を選択
# Yes を選択して有効化
```

カメラを有効にすることで、接続したカメラモジュールを使用できます。

## SPI通信を有効にしたい

```bash
sudo raspi-config
# Interface Options → SPI を選択
# Yes を選択して有効化
```

SPI（Serial Peripheral Interface）を有効にすることで、SPIデバイスと通信できます。

## I2C通信を有効にしたい

```bash
sudo raspi-config
# Interface Options → I2C を選択
# Yes を選択して有効化
```

I2C（Inter-Integrated Circuit）を有効にすることで、I2Cデバイスと通信できます。

## 1-Wire通信を有効にしたい

```bash
sudo raspi-config
# Interface Options → 1-Wire を選択
# Yes を選択して有効化
```

1-Wire（ワンワイヤ）を有効にすることで、温度センサーなどの1-Wireデバイスと通信できます。

## シリアルポート通信を有効にしたい

```bash
sudo raspi-config
# Interface Options → Serial Port を選択
```

シリアルポート通信を有効にすることで、UART経由でシリアル通信できます。

## メモリ分割を変更したい

```bash
sudo raspi-config
# Performance Options → GPU Memory を選択
# GPU用メモリ容量を入力（MByte単位）
```

GPUに割り当てるメモリ容量を変更できます。
グラフィック処理が多い場合は容量を増やし、CPUヘビーな処理が多い場合は容量を減らします。

## オーバークロックしたい

```bash
sudo raspi-config
# Performance Options → Overclock を選択
```

オーバークロックすることで処理速度を上げることができます。

:::{warning}

オーバークロックは動作の不安定化や寿命低下のリスクがあります。
十分な冷却と正しい設定が必要です。

:::

## ブートアニメーションを無効にしたい

```bash
sudo raspi-config
# Display Options → Splash Screen を選択
# 無効化する
```

ブート時に表示されるスプラッシュスクリーンを非表示にできます。

## ディスプレイ解像度を変更したい

```bash
sudo raspi-config
# Display Options → Resolution を選択
# 希望する解像度を選択
```

ディスプレイの解像度を変更できます。



## 自動ログインを有効にしたい

```bash
sudo raspi-config
# System Options → Boot / Auto Login を選択
# ログインオプションを選択
```

起動時に自動的にユーザーがログインされるように設定できます。

## ブートモードを変更したい

```bash
sudo raspi-config
# System Options → Boot / Auto Login を選択
# Desktop または Console を選択
```

起動時にデスクトップ環境を起動するか、コンソールを起動するか選択できます。

## 設定を確認したい

現在の設定状況を確認することはできませんが、各設定項目で現在の状態（有効/無効）が表示されます。

コマンドラインで確認する場合は、以下のコマンドを使用できます：

```bash
# ホスト名確認
hostnamectl

# タイムゾーン確認
timedatectl

# インターフェース設定確認
ls /sys/class/gpio  # GPIO有効化確認
```

## リファレンス

- [raspi-config - Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/computers/configuration.html)
- [Raspberry Pi Official Configuration Tool](https://github.com/RPi-Distro/raspi-config)
