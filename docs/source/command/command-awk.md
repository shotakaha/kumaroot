# awk


## スペース区切りのファイルからカラムを抽出したい

```bash
$ awk '{print $5}' ファイル名  # 5番目のカラム
```

## 文字列を指定したカラムを抽出したい

```bash
$ awk '/foo/ {print $2}' ファイル名
```

##  最後のカラムを抽出したい

```bash
$ awk -F ',' '{print $NF}' filename
```
