# あいまい検索したい（`fzf`）

```console
$ fzf
$ コマンド | fzf
$ history | fzf
$ ps aux | fzf
$ git log --oneline | fzf
```

`fzf`は、あいまい検索（fuzzy find）できるコマンドです。
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

## シェル設定したい

```bash
$ fzf --fish | source
```

`fish`では、上記をコマンドラインで実行するか`config.fish`に追記することで、
{kbd}`Ctrl-R`（コマンド履歴のあいまい検索）や
{kbd}`Ctrl-T`（ファイルパスの挿入）などのキーバインドが使えるようになります。

```bash
# ~/.bashrc に追記
eval "$(fzf --bash)"

# ~/.zshrc に追記
eval "$(fzf --zsh)"
```

`bash`/`zsh`の場合は、それぞれの設定ファイルに`eval`を追記します。
Homebrewでインストールした場合は、`$(brew --prefix)/opt/fzf/install`を実行して
シェル統合スクリプトを自動生成することもできます。
