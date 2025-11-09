```{tags} raspi, time
```

# 時刻設定したい（`date`）

```bash
sudo date -s "YYYY-mm-dd HH:MM:SS"
```

```bash
# 現在の時刻を確認
date

# 新しい時刻を設定（スマホなどと合わせる）
sudo date -s "2025-11-09 15:30:45"
```

`date`コマンドで、システムに設定されている時刻を操作できます。

Raspberry Pi 4まではRTC（Real Time Clock）が非搭載なため、
電源をOFFにすると時計がそこで停止します。
再起動したあとは、時刻の再設定が必要です。

:::{note}

Raspberry Pi OSは`systemd-timesyncd`により、
デフォルトでNTP（Network Time Protocol）による時刻同期が有効です。
ネットワーク接続がある環境では、自動的に時刻が修正されます。

屋外などオフライン環境で使用する場合でも、
一時的にスマホにテザリング接続することで、時刻を修正できます。

:::

## リファレンス

- [date Manual](https://man7.org/linux/man-pages/man1/date.1.html)
- [Raspberry Pi Official Documentation](https://www.raspberrypi.com/documentation/)
