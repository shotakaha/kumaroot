# Raspberry Piしたい

```console
$ docker image ls
REPOSITORY                         TAG                       IMAGE ID       CREATED        SIZE
balenalib/raspberrypi4-64-python   bookworm-build-20240429   5eeca56e63bb   3 months ago   1.09GB
balenalib/raspberrypi4-64-python   bullseye-build-20240429   4b9714fe0218   3 months ago   939MB
```

BalenaがDockerHubに公開しているRaspberry Pi OSのイメージを使いました。
Raspi3 / Raspi4があったり、中のDebianのバージョン（buster / bulleseye / bookworm）など
さまざまなvariantsがあります。

## コンテナー起動

```console
$ docker container run --rm -it 5eeca56e63bb bash
```

Dockerfileなどは作成せず、イメージIDを指定して、コンテナーを直接起動しました。

## ユースケース

宇宙線測定のためのツールがRaspberry Piの実機にインストールできないケースがありました。
今回は、インストール手順を確認するため、macOS上でDockerコンテナーを使いました。

```console
root:/# apt update
root:/# apt upgrade
root:/# apt autoremove
root:/# apt install pipx
root:/# pipx ensurepath   # 実行後、.bashrcの再読み込みが必要
root:/# pipx haniwers
```

RPi3/RPi4、bulleseye/bookwormの組み合わせで4種をテストしました。
結果は以下のとおりで、RPi4/bookwormを使うしかないことが分かりました。

| OS | Python | pipx | 結果 | エラー |
|---|---|---|---|---|
| RPi3 / bulleseye | 3.9 | 0.12.3.1 | 失敗 | Cargo is not installed |
| RPi3 / bookworm | - | 1.1.0 | 失敗 | pip seemed to fail to build pendulum |
| RPi4 / bulleseye | 3.11.2 | ない |  | |
| RPi4 / bookworm | 3.11.2 | 1.1.0 | 成功 | |

## リファレンス

- [balenalib/raspberrypi4-64-python](https://hub.docker.com/r/balenalib/raspberrypi4-64-python)
- [balenalib/raspberrypi4-64-debian](https://hub.docker.com/r/balenalib/raspberrypi4-64-debian)
