# タイムゾーンしたい（`timedatectl`）

```bash
sudo timedatectl set-timezone Asia/Tokyo
```

タイムゾーンを設定することで、ログのタイムスタンプや自動タスクの実行時刻が正確になります。

## GUIしたい

```bash
sudo raspi-config
# Localisation Options → Timezone を選択
# 地域と都市を選択
```
