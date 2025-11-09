# ロケールしたい（`locale` / `update-locale`）

```bash
# 利用可能なロケール一覧を表示
locale -a

# ロケールを設定
sudo update-locale LANG=ja_JP.UTF-8
```

ロケールを設定することで、言語や文字エンコーディングが正確に設定されます。

## GUIしたい

```bash
sudo raspi-config
# Localisation Options → Locale を選択
# デフォルトロケールを選択
```
