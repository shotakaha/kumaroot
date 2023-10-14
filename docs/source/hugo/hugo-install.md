```{eval-rst}
.. index::
    pair: Hugo; install
```

# インストールしたい

```console
$ brew install hugo
```

[Hugo](https://gohugo.io/)はHomebrewでインストールできます。

```console
$ brew install go
```

[hugo mod](https://gohugo.io/commands/hugo_mod/)を使う場合はGoのインストールが必要です。

## npm版Hugo

```bash
$ brew install node
```

ウェブサイトのテーマなどは``npm``で提供されているものが多いです。
それらを利用する場合は``Node.js``のインストールが必要です。

また、Hugoのnpmパッケージもあります。
npmベースで作成する場合は設定ファイルを``package.json``だけにまとめることができて、CIするのに便利です。

（公式ではないと思いますが）以下の3種類のパッケージがあります。

- https://www.npmjs.com/package/hugo-bin
- https://www.npmjs.com/package/hugo
- https://www.npmjs.com/package/hugo-extended

どれを使ってもよいですが、Extendedバージョンを使うようにするとよいです。
その観点からすると``hugo-extended``がパッケージ名が明らかでよいと思います。
