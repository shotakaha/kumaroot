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
