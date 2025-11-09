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

**特徴：**

- デフォルトで暗号化通信（TLS）が有効
- ローカルユーザー認証がデフォルト
- TigerVNC ViewerやRealVNC Viewer（0.7.0以降）で接続可能

**推奨VNCクライアント：**

- **TigerVNC Viewer**（もっとも推奨）
  - 公式サイト: [https://tigervnc.org/](https://tigervnc.org/)
  - Homebrewでインストール: `brew install tigervnc-viewer`

**設定ファイル：**

WayVNCの詳細設定は以下のファイルで行えます：

```bash
~/.config/wayvnc/config
```

## SSH経由でセキュアに接続したい

ネットワーク経由でVNC接続する場合、セキュリティを強化するためSSHトンネリングの使用を推奨します。

```bash
# SSH トンネルの確立（クライアントマシンで実行）
ssh -L 5900:localhost:5900 pi@<raspberry-pi-ip>

# その後、VNCクライアントで localhost:5900 に接続
```

これにより、VNCトラフィックがSSHで暗号化されます。
