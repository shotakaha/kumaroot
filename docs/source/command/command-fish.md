# fish

```bash
$ brew install fish
```

Bash や Zsh のようなシェルの仲間です。
デフォルトでいい感じに表示してくれるので、パソコンを買い替えた場合に便利です。

## デフォルトシェルを fish にしたい

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
`fish`のパスは OS で異なることがあるので `which fish` で確認するとよいです。
`/etc/shells`の編集には管理者権限が必要です。
`chsh -s`を実行すると変更前に管理者パスワードを確認されます。

## fishを設定したい

```bash
$ fish_config
```

``fish_config``を実行すると、ブラウザが起動します。
色やプロンプトなど設定できます。

## プロンプトを微修正したい

```bash
$ code ~/.config/fish/functions/fish_prompt.fish
```

上記の``fish_config``で選んだプロンプトを少しだけ修正したい場合は、``fish_prompt.fish``を直接編集してしまいましょう。
僕は``Astronaut``の2段組のプロンプトを選んだのですが、作業中のディレクトリ名は省略形に変更したいです。
