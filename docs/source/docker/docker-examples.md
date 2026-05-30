# Dockerコンテナーを試したい

Docker Composeを使ってすぐにコンテナーを起動・操作できるように、各ツールやサービスの基本的な使い方を整理しました。
各ページの冒頭にある`compose.yaml`をコピーして、
`docker compose up -d` で起動し、
`docker compose exec`でコンテナー内にログインして操作できます。

```{toctree}
---
maxdepth: 1
---
docker-example-ubuntu
docker-example-almalinux
docker-example-rockylinux
docker-example-nginx
docker-example-httpd
docker-example-mariadb
docker-example-postgresql
docker-example-busybox
docker-example-wordpress
docker-example-wordpress-bitnami
docker-example-python3
docker-example-raspi
docker-example-texlive
```
