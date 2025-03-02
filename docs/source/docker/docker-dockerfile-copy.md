# コピーしたい（`COPY`）

```dockerfile
WORKDIR /app

# COPY <src> <dest>
COPY . .
```

`COPY`でホストPCにあるファイルなどを、イメージ内にコピーできます。

## 所有者したい（`--chown`）

```dockerfile
COPY --chown=ユーザー名:グループ名 <src>... <dest>
```

`--chown`オプションで、コピーしたファイルの所有者を変更できます。
