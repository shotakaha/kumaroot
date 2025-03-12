# TeX Liveしたい

```console
$ docker container run --rm -v "$(pwd)":/workdir -w /workdir texlive/texlive:latest-full latexmk main.tex
```

[texlive/texlive](https://hub.docker.com/r/texlive/texlive)に、
（おそらく）公式のTeX Liveイメージがあります。
`latest`タグは毎週更新されます。
イメージのタグは、TeX Liveの`scheme`に合わせて用意されています（後述）。

`docker`コマンドを毎回入力するのは大変なので、
下記の`compose.yaml`を作成するのがオススメです。

## Docker Composeしたい

```yaml
# compose.yaml
services:
  tex:
    image: texlive/texlive:latest-full
    volumes:
      - .:/workdir
    working_dir: /workdir
    command: ["latexmk", "main.tex"]
```

サービス名を`tex`としました。
`image`は原則、最新版（`latest`）を指定します。
`volumes`でホストディレクトリを`/workdir`にバインドマウントすることで、
手元のファイルをコンテナ内で処理できるようにしています。
`command`にコンテナを起動したときに実行する内容をリスト形式で記述しています。

```console
$ docker compose up
```

`docker compose up`すると`command`に設定した内容の
`$ latexmk main.tex`が実行されます。
実行後、コンテナは自動的に停止します。

## 過去のTeX Liveを使いたい

```yaml
services:
  tex:
    image: texlive/texlive:TL2024-historic
    volumes:
      - .:/workdir
    working_dir: /workdir
    command: ["latexmk", "main.tex"]
```

`TL{年}-historic`で、過去のTeX Liveを指定できます。
この`historic`タグは、年ごとにひとつだけ存在します。
このタグは毎月リビルドされ、関連するパッケージなどは最新版に保たれるようになっています。

:::{note}

通常のタグは「その時点の状態」を指しますが、
TeX Liveの場合、通常とは異なる意味を持つので少し注意が必要です。

:::

## ファイルを変更したい

```console
$ docker compose run --rm tex latexmk another.tex
```

`docker compose run コンテナ名 コマンド`で`command`の内容を上書きできます。
コンパイル対象のファイル名を変更したり、
`latexmk`にオプションを追加したり、のような修正ができます。

```console
$ docker compose run tex latexmk -pvc main.tex
$ docker compose down
```

`-pvc`オプションでライブビューを有効にした場合、
`docker compose down`して明示的にコンテナを終了する必要があります。

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
