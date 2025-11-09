# raspi-configしたい

```bash
sudo raspi-config
```

`raspi-config`は、Raspberry Pi OSの設定を管理するコマンドラインツールです。

ホスト名、タイムゾーン、インターフェイス設定など、さまざまな設定をGUIから簡単に変更できます。

## ホスト名を変更したい

```bash
sudo raspi-config
# System Options → Hostname を選択
```

ホスト名を変更することで、ネットワーク上で識別しやすくなります。
変更後は再起動が必要な場合があります。

**別の方法（コマンドラインのみ）：**

```bash
sudo hostnamectl set-hostname <新しいホスト名>
```

## タイムゾーンを設定したい

```bash
sudo raspi-config
# Localisation Options → Timezone を選択
# 地域と都市を選択
```

タイムゾーンを設定することで、ログのタイムスタンプや自動タスクの実行時刻が正確になります。

**別の方法（コマンドラインのみ）：**

```bash
sudo timedatectl set-timezone Asia/Tokyo
```

## ロケールを設定したい

```bash
sudo raspi-config
# Localisation Options → Locale を選択
# デフォルトロケールを選択
```

ロケールを設定することで、言語や文字エンコーディングが正確に設定されます。

**別の方法（コマンドラインのみ）：**

```bash
# 利用可能なロケール一覧を表示
locale -a

# ロケールを設定
sudo update-locale LANG=ja_JP.UTF-8
```

## WiFiを設定したい

```bash
sudo raspi-config
# System Options → Wireless LAN を選択
# SSID（ネットワーク名）とパスワードを入力
```

WiFiを設定することで、イーサネットケーブルなしにRaspberry Piをネットワークに接続できます。

## SSHを有効にしたい

```bash
sudo raspi-config
# Interface Options → SSH を選択
# Yes を選択して有効化
```

SSHを有効にすることで、リモートからコマンドラインでアクセスできます。

詳細は[SSH設定](raspi-ssh.md)を参照してください。

## VNCを有効にしたい

```bash
sudo raspi-config
# Interface Options → VNC を選択
# Yes を選択して有効化
```

VNCを有効にすることで、リモートからGUIデスクトップにアクセスできます。

詳細は[VNC設定](raspi-vnc.md)を参照してください。

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

## Waylandから X11に切り替えたい

```bash
sudo raspi-config
# Advanced Options → Wayland を選択
# X11 を選択
# 再起動
```

Raspberry Pi OS BookwormではデフォルトでWaylandが使用されていますが、
X11ベースのデスクトップ環境に切り替えることができます。

:::{note}

セキュリティ上の理由からWaylandへの移行が推奨されているため、
特別な理由がない限りX11への切り替えは推奨されません。

:::

## パスワードを変更したい

```bash
sudo raspi-config
# System Options → Password を選択
# 新しいパスワードを入力
```

Piユーザーのパスワードを変更できます。

**別の方法（コマンドラインのみ）：**

```bash
passwd
# 現在のパスワードと新しいパスワードを入力
```

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
