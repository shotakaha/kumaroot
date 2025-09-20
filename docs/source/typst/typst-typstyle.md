# フォーマッターしたい（`typstyle`）

```console
$ typstyle --check src/*.typ
$ typstyle --diff src/*.typ
$ typstyle --inplace src/*.typ
```

`typstyle`コマンドでTypstファイルをフォーマットできます。
zero-configで利用できるので、とりあえず導入するとよいです。

## インストール（`typstyle`）

```console
$ brew install typstyle
$ typstyle -V
typstyle 0.13.17

```

`typstyle`はHomebrewでインストールできます。

```console
$ cargo install typstyle
```

Rustで書かれているため`cargo`でもインストールできます。
