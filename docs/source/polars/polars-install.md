# インストールしたい（``polars``）

```console
$ pip3 install polars
```

## オプションしたい

```console
$ pip3 install "polars[all]"
$ poetry add polars -E all
$ rye add polars --features all
```

関連するパッケージを合わせてインストールできます。
オプションは個別に指定できますが、ひとまず``all``しておけばよいと思います。

## リファレンス

- [Installation - Polars User's Guide](https://docs.pola.rs/user-guide/installation/)
