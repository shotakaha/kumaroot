# パッケージ管理したい（`brew`）

```console
$ brew install フォーミュラ名
$ brew update
$ brew outdated
$ brew upgrade
```

## パッケージを探したい（``brew search``）

```console
$ brew search 検索パターン

# 例：ブラウザを検索
$ brew search browser
```

``search``コマンドを使って、パッケージ名（＝フォーミュラ）を検索できます。
検索パターンは曖昧マッチに（おそらく）対応しているので、思いついたパターンをそのまま入力すればOKです。

## パッケージの詳細を調べたい（``brew info``）

```console
$ brew info フォーミュラ名

# 例：Brave
$ brew info brave-browser
$ brew home brave-browser
```

``search``コマンドでパッケージ名を探したら``info``コマンドを使って詳細を表示します。
パッケージの配布先や依存パッケージ、競合パッケージなどを調べることができます。
さらに``home``コマンドで提供元のウェブサイトを確認できます。

パッケージによっては名前だけで判別しにくいものもあります。
もしかしたら求めていたものと違うパッケージの場合もあるので、はじめてインストールするパッケージの場合は、必ず調べるクセをつけておくとよいと思います。

## パッケージを更新したい（``brew upgrade``）

```console
# パッケージリストを更新する
$ brew update

# 更新が必要なパッケージを表示する
$ brew outdated

# パッケージを更新する
$ brew upgrade
```

``update``コマンドでパッケージ一覧を更新します。
``outdated``コマンドで更新があるパッケージ一覧を表示できます。
``upgrade``コマンドで更新があるパッケージをダウンロードできます。

## フォントを追加したい

```console
$ brew tap homebrew/cask-fonts
```

Homebrewを使って、Google Fontsにあるフォントをインストールできます。
フォント用のタップ（``homebrew/cask-fonts``）を使えるようにしておきます。

## zsh のパスを設定したい

```zsh
# ~/.zprofile
# ... 他に設定してある場合はそのままでOK
eval "$(/opt/homebrew/bin/brew shellenv)"
```

{file}`~/.zprofile`を編集して追記します。
Homebrew をインストールした末尾に表示されるスクリプトを実行しても OK です。

## fish のパスを設定したい

```fish
# ~/.config/fish/config.fish
if status is-interactive
    # Commands to run in interactive sessions can go here
    # ... 他に設定してある場合はそのままでOK
    eval (/opt/homebrew/bin/brew shellenv) # <= ここを追記
end
```

{file}`~/.config/fish/config.fish`を編集して追記します。
zsh 用の設定と微妙に異なる（`$`や`"`がいらない）ので注意が必要です。

## エラー：xcrun

```console
$ brew upgrade
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```

```console
$ xcode-select --install
```

新しく買ったパソコンだったり、Xcodeをアップグレードしたあとは、Homebrewが動かないときがあります。
``xcrun``が見つからないエラーの場合、``xcode-select --install``すると解決します。
