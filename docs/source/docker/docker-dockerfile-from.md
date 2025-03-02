# イメージを指定したい（``FROM``）

```docker
FROM イメージ:タグ
```

`FROM`を`Dockerfile`の先頭に記述し、ベースとして使うイメージ名を指定します。
タグを指定しない場合は`latest`になります。
利用できるイメージ名は[Docker Hub](https://hub.docker.com/)などの
コンテナレジストリから探します。

## Pythonしたい

```docker
FROM python:3.12-slim
```

Docker Hubにある
[Pythonの公式レジストリ](https://hub.docker.com/_/python)
から必要なタグを指定します。

`bookworm`や`bullesye`がついたタグでDebianのバージョンを指定できます。
`slim`がついたタグは、不要なライブラリが省かれた軽量版です。
`alpine`がついたタグはAlpine Linuxベースの超軽量版です。

## BusyBoxしたい

```dockerfile
FROM busybox
```
