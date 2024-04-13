# イメージを指定したい（``FROM``）

```docker
FROM イメージ:タグ
```

``Dockerfile``の先頭に、ベースとして使うイメージ名を指定します。
タグを指定しない場合は``latest``になります。
利用できるイメージ名は[Docker Hub](https://hub.docker.com/)などから探します。

## Pythonしたい

```docker
FROM python:3.12-slim
```

## BusyBoxしたい

```dockerfile
FROM busybox
```

