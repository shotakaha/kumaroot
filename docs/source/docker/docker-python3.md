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
root@92019f951c8b:/# ls
bin  boot  dev	etc  home  lib	lib64  media  mnt  opt	proc  root  run  sbin  srv  sys  tmp  usr  var
root@92019f951c8b:/# pwd
/
root@92019f951c8b:/# cd
root@92019f951c8b:~# pwd
/root
```

インタープリターではなく、シェル（``bash``）を起動させてみました。
ログイン直後のパスは``/``になっていました。
ホームディレクトリは``/root``です。

```console
$ docker container ls
CONTAINER ID   IMAGE         COMMAND   CREATED          STATUS          PORTS     NAMES
6848a3150200   python:3.12   "bash"    11 seconds ago   Up 11 seconds             flamboyant_bell
```

もうひとつのシェルで``docker container ls``確認し、IDと名前が変わっていることを確認しました。

```console
$ docker container run -it --user einstein python:3.12 bash
docker: Error response from daemon: unable to find user einstein: no matching entries in passwd file.
ERRO[0000] error waiting for container: context canceled
```

ユーザー名を変更してログインを試みましたがダメでした。
これは調べる必要があります。

## VS Codeから操作する

```console
$ docker container run -it python:3.12
```

コンテナが起動した状態（``docker container run``）であれば、VS Codeからコンテナを操作できました。
MS公式の[Dockerプラグイン](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)を使いました。

## リファレンス

- [python - DockerHub](https://hub.docker.com/_/python/)
