# fish

```bash
$ brew install fish
```

Bash や Zsh のようなシェルの仲間です。
デフォルトでいい感じに表示してくれるので、パソコンを買い替えた場合に便利です。

## ログインシェルを fish にしたい

1. `/etc/shells` に`fish`を追記する
2. `chsh -s`コマンドでデフォルトシェルを変更する

```bash
$ which fish
# /usr/local/bin/fish
# /opt/homebrew/bin/fish
$ sudo vi /etc/shells
$ chsh -s /opt/homebrew/bin/fish
```

`fish`のパスを`/etc/shells`に追記すると `chsh -s` できるようになります。

`fish`のパスは OS で異なることがあるので `which fish` で確認しておきます。
`/etc/shells`の編集には管理者権限が必要です。
`chsh -s`を実行すると変更前に管理者パスワードを確認されます。

## fishを設定したい

```bash
$ fish_config
```

``fish_config``を実行すると、ブラウザが起動します。
色やプロンプトなど設定できます。

## 変更点を確認したい

```bash
$ fish_delta
```

fishのデフォルトから変更を加えた箇所を確認できます。

## プロンプトを微修正したい

```bash
$ code ~/.config/fish/functions/fish_prompt.fish
```

上記の``fish_config``で選んだプロンプトを少しだけ修正したい場合は、``fish_prompt.fish``を直接編集してしまいましょう。
僕は``Astronaut``の2段組のプロンプトを選んだのですが、作業中のディレクトリ名は省略形に変更したいです。

## パスを設定したい（``fish_add_path``）

```fish
# Homebrew
fish_add_path /usr/local/bin

# pipx
fish_add_path $HOME/.local/bin

# Rust
fish_add_path $HOME/.cargo/bin
```

``fish_add_path``を使ってパスを追加できます。

:::{note}
これまでは以下の方法``set -x``を使った方法でよかったのですが、v3.2から非推奨になりました。

```console
$ set -x PATH $PATH $HOME/.cargo/bin
```

:::

### パスを確認したい（``fish_user_paths``）

```console
$ echo $fish_user_paths
echo $fish_user_paths
~/.cargo/bin ~/.local/bin /usr/local/bin

$ printf '%s\n' $fish_user_paths
~/.cargo/bin
~/.local/bin
/usr/local/bin
```

パスは``fish_user_paths``で確認できます。

## 変数を設定したい（``set``）

```bash
set 変数名 値
set -l 変数名 値1 値2
set -gx 変数名 値    # bash/zshのexportに相当
set 変数名    # ""に初期化
set -q 変数名    # 変数名が定義されているかを確認
```

``bash`` / ``zsh``では``export``コマンドを使って変数を定義しますが、``fish``では``set``コマンドを使います。

``set``には変数のスコープを指定できるオプション（``-l / --local``、``-g / --global``、``-u / --universal``）が3種類あります。
また、変数を外部変数にするかを指定できるオプション（``-x / --export``、``-u / --unexport``）があります。
外部変数にすると、別のプログラムから変数が参照できるようになります。

``set -q``で変数が定義されているか確認できます。
``if``文と組み合わせて条件分岐に使えます。

## リダイレクトしたい

```
$ pbcopy < ~/.gitconfig
$ echo "hello" > stdout.md
$ echo "hello" 2> stderr.md
$ echo "hello" 2>&1 stdout_and_stderr.md
```

## コマンド補完を整理したい

```console
$ fish_update_completions
Parsing man pages and writing completions to ~/.local/share/fish/generated_completions/
  7148 / 7148 : zic.8
```

``fish_update_completions``でコマンド補完の候補を更新できます。
有効になったコマンド補完は``~/.local/share/fish/generated_completions/``で確認できます。

## コマンド履歴を整理したい

```console
// 履歴の数を確認
$ wc -l ~/.local/share/fish/fish_history
   41529

// 履歴ファイルの内容を確認
$ tail -n 30 ~/.local/share/fish/fish_history
- cmd: fish_key_reader
  when: 1718746545
- cmd: bind
  when: 1718746557
- cmd: fish_update_completions
  when: 1718746615
- cmd: cd ~/.local/share/fish/
  when: 1718746873
  paths:
    - ~/.local/share/fish/
- cmd: wc -l ~/.local/share/fish/fish_history
  when: 1718747030
  paths:
    - ~/.local/share/fish/fish_history
- cmd: tail -n 30 ~/.local/share/fish/fish_history
  when: 1718747220
  paths:
    - ~/.local/share/fish/fish_history
```

Fishはコマンド履歴からも補完してくれます。
しかし、打ち間違えてしまったコマンドを覚えてしまっていることもあります。
そのときは履歴ファイル（``~/.local/share/fish/fish_history``）を直接開き、
該当するコマンド履歴を削除します。

コマンド履歴の構造は、以下のようになっていました。
不要な項目は、この構造ごと削除します。

```yaml
- cmd: コマンド名
  when: 時刻（unixtime）
  paths:
    - 実行したパス
```

めんどくさい場合は、履歴ファイルをまるっと削除してもいいかもしれません。

