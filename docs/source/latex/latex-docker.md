# Dockerしたい

```console
$ docker container texlive/texlive:latest latexmk
```

## コンテナーを選びたい

```console
$ docker pull texlive/texlive:latest
$ docker pull texlive/texlive:latest-full
$ docker pull texlive/texlive:latest-medium
$ docker pull texlive/texlive:latest-small
$ docker pull texlive/texlive:latest-basic
$ docker pull texlive/texlive:latest-minimal
```

TeXLiveの`scheme`に合わせて、イメージのタグが用意されています。
これらのイメージは毎週更新されます。

まずは、すべてのパッケージが利用できる`full`を選択すればOKです。
必要最低限なパッケージでよい場合は`medium`、
ゴリゴリにカスタマイズしたい場合は`basic`からはじめるのがよいと思います。

| タグ | サイズ |
|---|---|
| `latest` | 2.3 GB |
| `latest-full` | 2.3 GB |
| `latest-medium` | 689 MB |
| `latest-small` | 378 MB |
| `latest-basic` | 334 MB |
| `latest-minimal` | 305 MB |

## リファレンス

- [texlive/texlive - DockerHub](https://hub.docker.com/r/texlive/texlive)
