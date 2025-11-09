# Dockerfileしたい

`Dockerfile`は、Dockerイメージを作成するための手順を記述したテキストファイルです。
既存のベースイメージをカスタマイズして、アプリケーション用のイメージを構築できます。

```dockerfile
FROM python:3.12-slim
WORKDIR /app
SHELL ["/bin/bash", "-c"]
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

以下は、`Dockerfile`で使用される主なコマンドです。
実装時は下記の順番で指定することをオススメします。

```{toctree}
---
maxdepth: 2
---
docker-dockerfile-from
docker-dockerfile-workdir
docker-dockerfile-shell
docker-dockerfile-copy
docker-dockerfile-run
docker-dockerfile-cmd
```
