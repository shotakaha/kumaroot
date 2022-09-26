# pendulum

```bash
$ pip3 install pendulum
```

## 現在時刻を取得したい

```python
import pendulum
now = pendulum.now()
```

## 一般的な形式の時刻を取得したい

```python
dt = pendulum.parse("2022-09-26T17:00:00)
dt = pendulum.parse("2022-09-26T17:00:00, tz="Asia/Tokyo")
```

## ISO8601形式で出力したい

```python
dt.to_iso8601_string()
```

## リファレンス

- [Pendulum](https://pendulum.eustace.io/)
