# TeX Liveしたい

```dockerfile
FROM texlive/texlive:latest-basic
RUN tlmgr update --all \
  tlmgr install \
  luatexja \
  fontspec \
  siunitx \
  caption \
  minted \
  biblatex \
  markdown \
WORKDIR /workdir
VOLUME ["/workdir"]
CMD ["latexmk", "main.tex"]
```

```yaml
version: "3"
services:
  texlive:
    build: .
    volumes:
      - ./tex:/workdir
      - ./output:/output
    working_dir: /workdir
    command: ["latexmk", "main.tex"]
```

```console
$ docker compose up
```

## イメージを選びたい

```console
$ docker pull texlive/texlive:latest
$ docker pull texlive/texlive:latest-full
$ docker pull texlive/texlive:latest-medium
$ docker pull texlive/texlive:latest-small
$ docker pull texlive/texlive:latest-basic
$ docker pull texlive/texlive:latest-minimal

$ docker container run --rm -it イメージ名 bash
[コンテナ内]$ tlmgr info --list --only-installed | wc -l
[コンテナ内]$ exit
```

Docker Hubの[texlive/texlive](https://hub.docker.com/r/texlive/texlive)に（おそらく）公式イメージがあります。
TeX Liveの`scheme`に合わせて、イメージのタグが用意されています。
`latest`タグは毎週更新されます。

| タグ名 | サイズ | パッケージ数 | `luatex` | `lualatex` | `luatexja` |
|---|---|---|---|---|---|
| `full` | 5.2 GB| 4832 | Yes | Yes | Yes |
| `medium` | 1.8 GB | 1474 | Yes | Yes | No |
| `small` | 1.2 GB | 355 | Yes | Yes | No |
| `basic` | 1.0 GB | 139 | Yes | Yes | No |
| `minimal` | 985 MB | 63 | Yes | No | No |

個人の環境に構築する場合は`full`を選択すればOKです。
レジストリのサイズは2.3GBと表示されていますが、
ダウンロードして展開すると5.2GBになりました。

プロジェクト用の環境を構築する場合は`basic`を選択し、
必要なパッケージを追加するのがよいと思います。
