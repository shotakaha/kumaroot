# LSPしたい（`tinymist`）

`tinymist`はTypstのLSP（Language Server Protocol）です。
同じ開発者が作成した`Tinymist Typst`（VS Code拡張）でVS Codeでも利用できます。

:::{note}

Typstの公開直後には`typst-lsp`がありましたが、開発が止まっています。
現在は`tinymist`がデファクトで使われているようです。

:::

## インストール（`tinymist`）

```console
$ brew install tinymist
$ tinymist --version
tinymist 0.13.26
```

`tinymist`はHombrewでインストールできました。

```console
$ cargo install tinymist
```

Rustで書かれているので`cargo`でインストールできます。
