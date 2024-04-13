# Python3したい

DockerHubにあるPython3のイメージを検索してイメージ取得し、
コンテナを起動してVS Codeから接続するまでの一連の操作方法を確認しました。

## イメージを検索する（``docker search``）

```console
$ docker search python
NAME                              DESCRIPTION                                     STARS     OFFICIAL
python                            Python is an interpreted, interactive, objec…   9555      [OK]
hylang                            Hy is a Lisp dialect that translates express…   59        [OK]
pypy                              PyPy is a fast, compliant alternative implem…   387       [OK]
circleci/python                   Python is an interpreted, interactive, objec…   88
bitnami/python                    Bitnami container image for Python              27
...
```

``docker search``で公開されているイメージ名を検索しました。
1つ目の公式イメージを使うことにしました。

## イメージを取得する（``docker image pull``）

```console
$ docker image pull python:3.12
3.12: Pulling from library/python
609c73876867: Pull complete
7247ea8d81e6: Pull complete
be374d06f382: Pull complete
b4580645a8e5: Pull complete
aa7e0aca67dd: Pull complete
84816cb735e2: Pull complete
85e25f7ceb91: Pull complete
849540060de4: Pull complete
Digest: sha256:e0e2713ebf0f7b114b8bf9fbcaba9a69ef80e996b9bb3fa5837e42c779dcdc0f
Status: Downloaded newer image for python:3.12
docker.io/library/python:3.12
```

``docker image pull``でイメージを取得しました。
タグは``python:3.12``としました。

## イメージを確認する（``docker image ls``）

```console
$ docker image ls
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
python       3.12      099bf23b94d9   2 days ago      1.02GB
```

``docker image ls``でイメージの一覧を確認しました。
他にもダウンロードしてあるイメージがあれば、ここに表示されます。

## イメージを削除する（``docker image rm``）

```console
$ docker image rm python
Error response from daemon: No such image: python:latest

$ docker image rm python:3.12
Untagged: python:3.12
Untagged: python@sha256:e0e2713ebf0f7b114b8bf9fbcaba9a69ef80e996b9bb3fa5837e42c779dcdc0f
Deleted: sha256:099bf23b94d964410e2782137f32fa313512da95a5eaff6d2d2460f31ff94aba
Deleted: sha256:1662c2f3c4bb8933bd0a4d08ae8f93c2864a1a584472582c3fc8a06b9889f88d
Deleted: sha256:c27ad9c246b3c2b3fa2a02a6c5b0df94f08cb535db3ee17d94ae36611115d266
Deleted: sha256:460857397f38f400e120413d0a3e6916ec9cd70ff24a3887b4a20ece5b8eaa51
Deleted: sha256:1d6b115dfde7fdd5b8d02411d280a707c0583754bf37e20392e7bec7dd29e02c
Deleted: sha256:4681e3614185920b157ef90420741ddcaab7b1bf011590529bbaf0be27a64f30
Deleted: sha256:9d4edd551247e9e251259300c8892e15a0a9333d80c50c6d95328fabcfe8a0fa
Deleted: sha256:8f7e9d0b5106f868f52eea87d5d757c642b9ed403444770629f80ed98bd9f739
Deleted: sha256:c5bb35826823702969891b025087135cceefb084dec1452af5a6fb2938bd9a13

$ docker image ls
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
```

削除するときの操作確認のために``docker image rm``でイメージを削除しました。
イメージ名はタグを含めて指定する必要がありました。

## コンテナを起動する（``docker container run``）

```console
$ docker container run python:3.12

$ docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

``docker container run``でコンテナを起動したのですが、何も起動していませんでした。
これは、起動してすぐに終了してしまったためでした。

```console
$ docker container run -it python:3.12
Python 3.12.3 (main, Apr 10 2024, 14:35:18) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

正しくは``-it``オプションをつける必要がありました。
Python3.12にインタープリターを起動できました。

```console
$ docker container ls
CONTAINER ID   IMAGE         COMMAND     CREATED         STATUS         PORTS     NAMES
97a81bf0ef4a   python:3.12   "python3"   7 seconds ago   Up 7 seconds             pensive_maxwell
```

もうひとつ別にシェルを起動し、``docker container ls``で確認しました。
``97a81bf0ef4a``というID、``pensive_maxwell``という名前でコンテナが起動していることが確認できました。

## シェルを起動する（``docker container run``）

```console
$ docker container run -it python:3.12 bash
root@92019f951c8b:/# pwd
/
root@92019f951c8b:/# ls
bin  boot  dev	etc  home  lib	lib64  media  mnt  opt	proc  root  run  sbin  srv  sys  tmp  usr  var

root@92019f951c8b:~# echo $HOME
/root
```

インタープリターではなく、シェル（``bash``）を起動させてみました。
ログイン直後のパスは``/``になっていました。
ホームディレクトリは``/root``でした。

```console
$ docker container ls
CONTAINER ID   IMAGE         COMMAND   CREATED          STATUS          PORTS     NAMES
92019f951c8b   python:3.12   "bash"    11 seconds ago   Up 11 seconds             flamboyant_bell
```

もうひとつのシェルで``docker container ls``確認し、IDと名前が変わっていることを確認しました。

```console
$ docker container run -it --user einstein python:3.12 bash
docker: Error response from daemon: unable to find user einstein: no matching entries in passwd file.
ERRO[0000] error waiting for container: context canceled
```

ユーザー名を変更してログインを試みましたがダメでした。
これは調べる必要があります。

### OSを確認する

```console
root@92019f951c8b:/# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
```

OSのバージョンを確認しました。
Debian 12 (bookworm) ベースでした。

### 利用可能なシェルを確認する

```console
root@92019f951c8b:/# cat /etc/shells
# /etc/shells: valid login shells
/bin/sh
/usr/bin/sh
/bin/bash
/usr/bin/bash
/bin/rbash
/usr/bin/rbash
/bin/dash
/usr/bin/dash
```

デフォルトで利用できるシェルを確認しました。
``sh``、``bash``、``dash``が利用できます。

## VS Codeから操作する

```console
$ docker container run -it python:3.12
```

コンテナが起動した状態（``docker container run``）であれば、VS Codeからコンテナを操作できました。
MS公式の[Dockerプラグイン](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)を使いました。

## 開発環境を整える

```console
root@b2a3ddb82a42:/# pip3 list
Package    Version
---------- -------
pip        24.0
setuptools 69.2.0
wheel      0.43.0
```

公式イメージから起動したコンテナには、最低限のパッケージしかインストールされていません。
いくつかのパッケージを追加して開発環境を整えていきます。

```console
root@b2a3ddb82a42:/# pip3 list -o
Package    Version Latest Type
---------- ------- ------ -----
setuptools 69.2.0  69.4.0 wheel

root@b2a3ddb82a42:/# pip3 install -U setuptools
Requirement already satisfied: setuptools in /usr/local/lib/python3.12/site-packages (69.2.0)
Downloading setuptools-69.4.0-py3-none-any.whl (823 kB)
Successfully installed setuptools-69.4.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
```

まず、``setuptools``を更新しました。
``root``で実行したため、仮想環境を使うといいよという警告が表示されました。

### 仮想環境を追加する

```console
root@b2a3ddb82a42:/# pip3 install virtualenv

root@b2a3ddb82a42:/# virtualenv venv
created virtual environment CPython3.12.3.final.0-64 in 326ms

root@b2a3ddb82a42:/# source venv/bin/activate
(venv) root@b2a3ddb82a42:/#
```

``virtualenv``で仮想環境を構築しました。

### パッケージ管理ツールを追加する

```console
(venv) root@b2a3ddb82a42:/# pip3 install -U poetry
(venv) root@b2a3ddb82a42:/# which poetry
/venv/bin/poetry
(venv) root@b2a3ddb82a42:/# poetry --version
Poetry (version 1.8.2)
```

パッケージ管理ツールとして``poetry``を追加しました。
Poetryの公式ドキュメントでは、``pip``を使ったインストールは推奨されていないようですが、一時的なコンテナ環境なのでよしとしました。

## Dockerfileを作成する

ここまで作成した環境は、一度シェルから抜けるとリセットされてしまいます。
毎回、手動で設定するのは手間です。
設定手順が決まっているなら``Dockerfile``に保存しておくことができます。

```docker
# Dockerfile
FROM python:3.12
RUN mkdir work
WORKDIR /work
RUN pip3 install -U virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip3 install -U poetry
CMD ["/bin/bash"]
```

上記の内容の``Dockerfile``をホストPCに作成して、イメージをビルドしました。
イメージサイズを節約するためには、``RUN``コマンドをひとまとめにするほうがよいそうです。
今回は、動作確認のためとりあえず、それぞれ書くことにしました。

```console
$ mkdir -p sandbox/docker-python3/
$ cd sandbox/docker-python3/
$ touch Dockerfile
// 上記の内容を編集する

$ docker build .
[+] Building 12.1s (11/11) FINISHED docker:desktop-linux
 => [internal] load build definition from Dockerfile 0.0s
 => => transferring dockerfile: 207B 0.0s
 => [internal] load metadata for docker.io/library/python:3.12 0.0s
 => [internal] load .dockerignore 0.0s
 => => transferring context: 2B 0.0s
 => [1/7] FROM docker.io/library/python:3.12 0.0s
 => CACHED [2/7] RUN mkdir work 0.0s
 => CACHED [3/7] WORKDIR /work 0.0s
 => CACHED [4/7] RUN pip3 install -U virtualenv 0.0s
 => CACHED [5/7] RUN virtualenv venv 0.0s
 => CACHED [6/7] RUN . venv/bin/activate 0.0s
 => [7/7] RUN pip3 install -U poetry 11.5s
 => exporting to image 0.5s
 => => exporting layers 0.5s
 => => writing image sha256:98a8e65e9ad79fcb37cfd4917e151a099854ad2ebba07887ab1b89bf4d117f1b 0.0s

What's Next?
  View a summary of image vulnerabilities and recommendations → docker scout quickview
```

```console
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
<none>       <none>    98a8e65e9ad7   8 seconds ago        1.12GB
<none>       <none>    bd54a11ae615   About a minute ago   1.06GB
<none>       <none>    1c7489ad3729   4 minutes ago        1.06GB
python       3.12      099bf23b94d9   3 days ago           1.02GB
```

``1.12GB``のイメージができていました。
``1.06GB``のイメージは、下記のエラーで失敗した残骸です。

```console
--------------------
   5 |     RUN pip3 install -U virtualenv
   6 |     RUN virtualenv venv
   7 | >>> RUN source venv/bin/activate
   8 |     RUN pip3 install -U poetry
   9 |
--------------------
ERROR: failed to solve: process "/bin/sh -c source venv/bin/activate" did not complete successfully: exit code: 127
```

今回使ったイメージでは、ビルドの際に``sh``（=``dash``）が使われていました。
``source``コマンドが見つからないためのエラーだったので、``.``に置き換えたらOKでした。

```console
$ docker container run -it 98a8e65e9ad7

root@2efac1aa7f10:/work#
root@2efac1aa7f10:/work# pwd
/work

root@2efac1aa7f10:/work# poetry --version
Poetry (version 1.8.2)
```

作成したイメージのID（今回は98a8e65e9ad7）を指定して、コンテナを起動しました。
``CMD ["/bin/bash"]``を指定したので、コンテナ名の後にコマンドがなくても``bash``が起動することが確認できました。
コンテナにログインした直後のディレクトリも``WORKDIR /work``になっていました。
開発環境で``poetry``が使えることも確認できました。

```console
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
<none>       <none>    98a8e65e9ad7   14 minutes ago   1.12GB
<none>       <none>    bd54a11ae615   15 minutes ago   1.06GB
<none>       <none>    1c7489ad3729   18 minutes ago   1.06GB
python       3.12      099bf23b94d9   3 days ago       1.02GB

$ docker image rm 1c7489ad3729
Error response from daemon: conflict: unable to delete 1c7489ad3729 (must be forced) - image is being used by stopped container 2caf4b98cb6f

$ docker container stop 1c7489ad3729
Error response from daemon: No such container: 1c7489ad3729

$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

$ docker image rm -f 1c7489ad3729
Deleted: sha256:1c7489ad3729ac06dedbf685cd92121888af5934cf869e68186b2ad343d93523

// bd54a11ae615 も同様に削除した

$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
<none>       <none>    98a8e65e9ad7   17 minutes ago   1.12GB
python       3.12      099bf23b94d9   3 days ago       1.02GB
```

作成に失敗したイメージを削除しました。
通常の``docker image rm``ではエラーがでました。
コンテナを停止させてみたり、プロセスを確認してみたりしましたが、
起動している様子がなかったので、強制削除（``docker image rm -f``）しました。
指定したイメージが削除できたことを確認しました。

## サイズを節約したい

```console
$ docker image pull python:3.12-slim
3.12-slim: Pulling from library/python
13808c22b207: Pull complete
6c9a484475c1: Pull complete
78bef5c7424f: Pull complete
42f0d54f5caa: Pull complete
1723cff2f16b: Pull complete
Digest: sha256:541d45d3d675fb8197f534525a671e2f8d66c882b89491f9dda271f4f94dcd06

$ docker image ls
REPOSITORY   TAG         IMAGE ID       CREATED         SIZE
python       3.12        099bf23b94d9   3 days ago      1.02GB
python       3.12-slim   0e42464fe231   3 days ago      130MB
```

``python:3.12-slim``のイメージはサイズが10分の1くらいのようです。
これまで確認したことを、``slim``イメージでも実行できることを確認しました。

```console
// Dockerfileを修正してから再ビルド
$ docker build .

$ docker image ls
REPOSITORY   TAG         IMAGE ID       CREATED          SIZE
<none>       <none>      140edf9fc946   10 seconds ago   231MB
python       3.12        099bf23b94d9   3 days ago       1.02GB
python       3.12-slim   0e42464fe231   3 days ago       130MB
```

``FROM python:3.12-slim``に修正して、再ビルドしたDockerイメージのサイズは231MBでした。

:::{note}

``python:3.12``と``python:3.12-slim``では、デフォルトのコマンド数などが異なります。

```console
$ docker container run -it python:3.12 bash
root@e6c5e9cc0332:/# ls /usr/bin/ | wc
    671     671    6635
```

```console
$ docker container run -it python:3.12-slim bash
root@c1e899682772:/# ls /usr/bin/ | wc
    277     277    1986
```

``python:3.12-slim``には``git``などのコマンドが含まれていないため、自分で追加する必要があります。

:::

## Gitを追加したい

```docker
FROM python:3.12-slim

RUN apt-get update
RUN apt-get install -y --no-install-recommends git
RUN apt-get -y clean
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir work
WORKDIR /work
RUN pip3 install -U virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip3 install -U poetry
CMD ["/bin/bash"]
```

```console
docker build .
[+] Building 0.1s (15/15)FINISHED docker:desktop-linux
 => [internal] load build definition from Dockerfile 0.0s
 => => transferring dockerfile: 357B 0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim 0.0s
 => [internal] load .dockerignore 0.0s
 => => transferring context: 2B 0.0s
 => [ 1/11] FROM docker.io/library/python:3.12-slim 0.0s
 => CACHED [ 2/11] RUN apt-get update 0.0s
 => CACHED [ 3/11] RUN apt-get install -y --no-install-recommends git 0.0s
 => CACHED [ 4/11] RUN apt-get -y clean 0.0s
 => CACHED [ 5/11] RUN rm -rf /var/lib/apt/lists/* 0.0s
 => CACHED [ 6/11] RUN mkdir work 0.0s
 => CACHED [ 7/11] WORKDIR /work 0.0s
 => CACHED [ 8/11] RUN pip3 install -U virtualenv 0.0s
 => CACHED [ 9/11] RUN virtualenv venv 0.0s
 => CACHED [10/11] RUN . venv/bin/activate 0.0s
 => CACHED [11/11] RUN pip3 install -U poetry 0.0s
 => exporting to image 0.0s
 => => exporting layers 0.0s
 => => writing image sha256:a7a2226589fee35e6b723730b2eaac6e7b4ab1b085a05a7c9d14e35ff4154333 0.0s

$ docker image ls
REPOSITORY   TAG         IMAGE ID       CREATED         SIZE
<none>       <none>      a7a2226589fe   2 minutes ago   333MB
python       3.12-slim   0e42464fe231   3 days ago      130MB
```

``git``を追加すると``333 MB``に増加しました。

## リファレンス

- [python - DockerHub](https://hub.docker.com/_/python/)
