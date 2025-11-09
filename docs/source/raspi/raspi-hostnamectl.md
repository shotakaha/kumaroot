# ホスト名したい（`hostnamectl`）

```bash
sudo hostnamectl set-hostname <新しいホスト名>
```

ホスト名を変更することで、ネットワーク上で識別しやすくなります。
変更後は再起動が必要な場合があります。

## GUIしたい

```bash
sudo raspi-config
# System Options → Hostname を選択
```
