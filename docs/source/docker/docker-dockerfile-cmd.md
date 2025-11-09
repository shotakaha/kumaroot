# デフォルトコマンドを指定したい（`CMD`）

```dockerfile
CMD ["python", "app.py"]
```

`CMD`でコンテナー起動時のデフォルトコマンドを指定します。
コンテナー実行時にコマンドを省略できます。

## デフォルトコマンドを指定したい（exec形式）

```dockerfile
CMD ["python", "app.py"]
```

exec形式を使うことで、シェルを経由せずにコマンドを直接実行します。

**特徴：**

- 配列形式で指定
- シェルを経由しないため高速
- シェル変数展開が行われない
- 推奨形式

## デフォルトコマンドを指定したい（シェル形式）

```dockerfile
CMD python app.py
```

シェル形式を使うことで、シェル機能（パイプ、リダイレクトなど）が利用できます。

**特徴：**

- 文字列形式で指定
- シェルを経由して実行
- シェル変数展開が可能
- パイプやリダイレクトが使える

## Pythonアプリケーションを実行したい

```dockerfile
FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Pythonスクリプトをコンテナー起動時に実行します。

**実行方法：**

```bash
# デフォルトコマンドで起動（CMDで指定したコマンドが実行）
docker run myimage

# CMDを上書きして別のコマンドを実行
docker run myimage python other_script.py
```

## Node.jsアプリケーションを実行したい

```dockerfile
FROM node:18-alpine
WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci --omit=dev

COPY . .

CMD ["node", "index.js"]
```

Node.jsアプリケーションをコンテナー起動時に実行します。

## ENTRYPOINTとCMDの違い

```dockerfile
# CMD のみ
CMD ["echo", "hello"]

# ENTRYPOINT + CMD
ENTRYPOINT ["echo"]
CMD ["hello"]
```

**CMD のみの場合：**

```bash
docker run myimage          # hello と出力
docker run myimage world    # world と出力（CMDが上書きされる）
```

**ENTRYPOINT + CMD の場合：**

```bash
docker run myimage          # echo hello と出力
docker run myimage world    # echo world と出力（CMDのみが上書きされる）
```

**CMD：**

- コンテナー起動時のデフォルトコマンド
- 実行時に完全に上書きできる
- 単独でも、ENTRYPOINTと共に使用できる

**ENTRYPOINT：**

- コンテナーの「実行ファイル」として機能
- 実行時に上書きできない（通常）
- CMDはENTRYPOINTの引数として機能

## 注意事項

:::{note}

Dockerfile内で複数の`CMD`を指定した場合、最後のものだけが有効になります。
他のすべての`CMD`は無視されます。

:::

:::{warning}

シェル形式でCMDを指定する場合、PID 1（メインプロセス）がシェルになります。
Dockerコンテナー内ではシグナル転送が正常に機能しないため、
exec形式を使用することを推奨します。

:::

## リファレンス

- [CMD - Docker docs](https://docs.docker.com/reference/dockerfile/#cmd)
- [ENTRYPOINT - Docker docs](https://docs.docker.com/reference/dockerfile/#entrypoint)
- [Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
