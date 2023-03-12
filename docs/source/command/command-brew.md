# パッケージ管理したい（`brew`）

```bash
brew install フォーミュラ名
brew update
brew outdated
brew upgrade
```

## Homebrew をインストールしたい

[Homebrew 公式ページ（日本語）](https://brew.sh/index_ja)にあるスクリプトをコピペして、ターミナルに貼り付けます。

## zsh のパスを設定したい

```bash
# ... 他に設定してある場合はそのままでOK
eval "$(/opt/homebrew/bin/brew shellenv)"
```

`~/.zprofile`を編集して追記します。
Homebrew をインストールした末尾に表示されるスクリプトを実行しても OK です。

## fish のパスを設定したい

```bash
if status is-interactive
    # Commands to run in interactive sessions can go here
    # ... 他に設定してある場合はそのままでOK
    eval (/opt/homebrew/bin/brew shellenv) # <= ここを追記
end
```

`~/.config/fish/config.fish`を編集して追記します。
zsh 用の設定と微妙に異なる（`$`や`"`がいらない）ので注意が必要です。

## エラー

```
$ brew upgrade
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```

```bash
$ xcode-select --install
```

## フォントを追加したい

```bash
$ brew tap homebrew/cask-fonts
```

Google FontsにあるフォントはHomebrewを使ってインストールできます。
そのために、フォント用のtap（``homebrew/cask-fonts``）を使えるようにしておきます。
