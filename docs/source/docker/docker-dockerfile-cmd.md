# デフォルトコマンドしたい（``CMD``）

```docker
CMD ["/bin/bash"]
```

[CMD](https://docs.docker.com/reference/dockerfile/#cmd)コマンドで、
コンテナを起動したときのデフォルトコマンドを設定できます。
上記のように``CMD ["/bin/bash"]``としておくと、
コンテナ起動時のコマンド引数がなくても``bash``が起動します。

```console
// CMD設定前
$ docker container run -it -rm イメージ名 bash

// CMD設定後
$ docker container run -it -rm イメージ名    # <-- "bash" が不要
```

:::{note}

このコマンドはDockerfileにひとつだけ書くことができます。
2つ以上書いた場合は、最後に書いた設定が有効になります。

:::

## リファレンス

- [CMD - docs.docker.com](https://docs.docker.com/reference/dockerfile/#cmd)
