# VNCしたい

Raspberry Pi OS Bookworm（Debian 12）以降、Raspberry Pi 4/5シリーズではWaylandベースの**WayVNC**がデフォルトのVNCサーバーになりました。

## WayVNCを起動したい

```bash
# WayVNCサービスを起動
sudo systemctl start wayvnc

# 自動起動を有効化
sudo systemctl enable wayvnc

# サービスの状態を確認
sudo systemctl status wayvnc
```

### WayVNCを停止したい

```bash
# WayVNCサービスを停止
sudo systemctl stop wayvnc

# 自動起動を無効化
sudo systemctl disable wayvnc
```

## GUIしたい

デスクトップの設定からVNCを有効にします。

1. {guilabel}`Preferences` → {guilabel}`Raspberry Pi Configuration`を選択する
2. {guilabel}`Interface`タブを選択する
3. {guilabel}`VNC`のトグルボタンを有効にする

## WayVNCについて

**WayVNC**はWaylandベースのVNCサーバーです。

### 特徴

- デフォルトで暗号化通信（TLS）が有効
- ローカルユーザー認証がデフォルト
- TigerVNC ViewerやRealVNC Viewer（0.7.0以降）で接続可能

### 設定ファイル

WayVNCの詳細設定は以下のファイルで行えます：

```bash
~/.config/wayvnc/config
```

## VNCクライアントしたい

```bash
# Homebrewでインストール
brew install tigervnc-viewer

# vncviewerコマンドで接続
vncviewer <raspi-ip>:5900
```

Raspberry PiにアクセスするためのVNCクライアントには
[TigerVNC Viewer](https://tigervnc.org/)が推奨されています。
TigerVNCはHomebrewでインストールできます。

:::{warning}

macOS標準のScreen Sharingアプリ（Finder.appから接続）は、**WayVNCと互換性がありません**。

Screen SharingはRFB（RFBプロトコル）のレガシー形式のみの対応で、
WayVNCのTLS暗号化やRSA-AES認証に対応していません。
そのため、バージョンの不一致エラーが発生します。

どうしてもFinder.appから接続したい場合は、
Raspberry Pi側でX11モードに切り替える必要があります。

```bash
sudo raspi-config
# Advanced options → Wayland → X11 を選択
# 再起動
```

ただし、セキュリティ上の理由からX11からWaylandへの移行が進められており、わざわざこの方法を使うことは推奨されていません。

:::

## SSH経由でセキュアに接続したい

ネットワーク経由でVNC接続する場合、セキュリティを強化するためSSHトンネリングの使用を推奨します。

```bash
# SSH トンネルの確立（クライアントマシンで実行）
ssh -L 5900:localhost:5900 <raspi-user>@<raspi-ip>

# その後、VNCクライアントで localhost:5900 に接続
```

これにより、VNCトラフィックがSSHで暗号化されます。
