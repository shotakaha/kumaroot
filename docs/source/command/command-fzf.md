# あいまい検索したい（`fzf`）

```console
$ fzf
$ コマンド | fzf
$ history | fzf
$ ps aux | fzf
$ git log --oneline | fzf
```

`fzf`は、あいまい検索（fuzzy search）できるコマンドです。
ほとんどすべての入力に対して「あいまい検索」で候補を絞り込むことができます。

コマンドの実行結果をパイプで渡すことで、あいまい検索の対象にできます。

## インストールしたい（`fzf`）

```console
$ brew install fzf
$ fzf --version
0.74.3 (Homebrew)
```

`fzf`はHomebrewでインストールできます。
