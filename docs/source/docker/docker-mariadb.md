# MariaDBしたい（`mariadb`）

```console
$ docker container run -d
  -v db-data:/var/lib/mysql
  -e MARIADB_ROOT_PASSWORD=root_pass
  -e MARIADB_DATABASE=test_db
  -e MARIADB_USER=test_user
  -e MARIADB_PASSWORD=test_pass mariadb:11.6
```

MariaDBを起動するとき、`-e`オプションで環境変数を設定する必要があります。
環境変数名はDockerHubで確認できます。

この数のオプションを毎回入力するのはミスの元なので、`compose.yaml`で管理するのがよいと思います。

## Composeしたい（`mariadb`）

```yaml
services:
  db:
    image: mariadb:11.6
    environment:
      MARIADB_ROOT_PASSWORD: rootpass
      MARIADB_DATABASE: testdb
      MARIADB_USER: testuser
      MADIADB_PASSWORD: testpass
    volumes:
      - db-data:/var/lib/mysql

# named volumes
volumes:
  db-data:
```

## リファレンス

- [mariadb - DockerHub](https://hub.docker.com/_/mariadb)
