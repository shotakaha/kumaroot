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

## プレビュー表示したい（`--preview`）

```console
$ fzf --preview 'cat {}'
$ fzf --preview 'bat --color=always {}'
```

`--preview`で、選択中の候補をプレビュー表示できます。
`{}`は、選択中の候補（ファイル名）に置き換わるプレースホルダーです。

## 複数選択したい（`-m` / `--multi`）

```console
$ fzf -m
$ fzf --multi
```

`--multi`（`-m`）で、複数の候補を選択できるようになります。
{kbd}`Tab`で選択・選択解除、
{kbd}`Enter`で選択済みの候補すべてを確定します。
