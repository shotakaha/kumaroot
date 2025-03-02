# TeX Liveしたい

```console
$ docker container run --rm -v "$(pwd)":/workdir -w /workdir texlive/texlive:latest-full latexmk main.tex
```

[texlive/texlive](https://hub.docker.com/r/texlive/texlive)に、
（おそらく）公式のTeX Liveイメージがあります。
イメージのタグは、TeX Liveの`scheme`に合わせて用意されています。
`latest`タグは毎週更新されます。

上記の`docker`コマンドを毎回入力するのは大変なので、
下記の`docker-compose.yaml`を作成するのがオススメです。

## Docker Composeしたい

```yaml
version: "3"
services:
  texlive:
    image: texlive/texlive:latest-full
    volumes:
      - .:/workdir
    working_dir: /workdir
    command: ["latexmk", "main.tex"]
```

冒頭の`docker`コマンドの内容を`docker-compose.yaml`にしました。

```console
$ docker compose up
```

`docker compose up`で`$ latexmk main.tex`が実行されます。
実行後、コンテナは自動的に停止します。

## ファイルを変更したい

```console
$ docker compose run texlive latexmk another.tex
```

`docker compose run コンテナ名 コマンド`で`command`を上書きできます。

```console
$ docker compose run texlive latexmk -pvc main.tex
$ docker compose down
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

TeX Liveはschemeと、含まれているパッケージ数を確認しました。
また、日本語LaTeXに必要なパッケージの有無も確認しました。

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

## 必要なパッケージを追加したい

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

`basic`などイメージを選択した場合、必要なパッケージは自分で追加する必要があります。
`Dockerfile`を作成し、カスタムイメージを作成します。

```console
$ docker image build --tag イメージ名:タグ名 .
```

イメージ名:タグ名を指定して、カスタムイメージを作成します。

```console
$ docker container run --rm -v "$(pwd)":/workdir -w /workdir タグ名 latexmk main.tex
```

カスタムイメージを指定して`docker`コマンドを実行し、LaTeX文書がタイプセットできるか確認します。
