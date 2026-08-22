# パッケージ管理したい（`brew`）

```console
$ brew install フォーミュラ名
$ brew update
$ brew outdated
$ brew upgrade
```

Homebrewは、macOSやLinuxで使えるパッケージ管理ツールです。

## インストールしたい（`brew`）

```console
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

$ brew --version
Homebrew 6.0.18-113-gecbeb2e
Homebrew/homebrew-cask (git revision c856cc02d26; last commit 2026-08-21)
```

https://brew.sh/ に書かれているコマンドをコピペして実行すると、Homebrewをインストールできます。
コマンド名は`brew`です。

## パッケージを探したい（`brew search`）

```console
$ brew search 検索パターン

// 例：ブラウザを検索
$ brew search browser
```

`brew search`で、Homebrewで管理されているパッケージを検索できます。
検索パターンは曖昧マッチに（おそらく）対応しているので、思いついたパターンをそのまま入力すればOKです。

ヒットした検索名が多すぎる場合は、検索コマンド（[grep](./command-grep.md)）などで絞り込むか、検索パターンを考え直すか、してください。

## パッケージの詳細を調べたい（`brew info`）

```console
$ brew info フォーミュラ名

// 例：Brave Browser
$ brew info brave-browser
$ brew home brave-browser
```

`brew info`で、指定したパッケージの詳細情報を表示できます。
パッケージの配布先や依存パッケージ、競合パッケージなどを調べることができます。

`brew home`で、指定したパッケージの提供元ウェブサイトやGitHubリポジトリなどを確認できます。
ブラウザが自動で立ち上がり、パッケージの公式情報を確認できます。

`brew search`でヒットしたパッケージ名だけでは求めているパッケージかどうか判断できないこともあります。
もしかしたら、同じような名前の別のパッケージかもしれません。
はじめてインストールするパッケージの場合は、`brew info`および`brew home`で必ず調べるクセをつけておくとよいと思います。

## パッケージを更新したい（`brew upgrade`）

```console
// パッケージリストを更新する
$ brew update

// 更新が必要なパッケージを表示する
$ brew outdated

// パッケージを更新する
$ brew upgrade
```

`brew update`で、Homebrewのパッケージリストを更新できます。
このコマンドは、HomebrewのリポジトリをGitで更新するだけです。
パッケージ自体は更新されません。

`brew outdated`で、更新が必要なパッケージを一覧できます。

`brew upgrade`で、更新があるパッケージをすべて更新できます。
`brew upgrade フォーミュラ名`で、指定したパッケージだけを更新することもできます。

## インストール済みパッケージを確認したい（`brew list`）

```console
$ brew list
```

`brew list`で、インストール済みのパッケージ名を一覧できます。

## パッケージを削除したい（`brew uninstall`）

```console
$ brew uninstall フォーミュラ名
```

`brew uninstall`で、インストール済みのパッケージを削除できます。

## 不要なファイルを削除したい（`brew cleanup`）

```console
// 削除対象を確認（実際には削除しない）
$ brew cleanup --dry-run

// 実際に削除する
$ brew cleanup
```

`brew cleanup`で、不要になったキャッシュなどを削除できます。
`--dry-run`オプションで、削除対象を事前に確認できます。

パッケージを更新したあと、古いバージョンのパッケージやダウンロードキャッシュが残っていることがあります。
知らないうちに数百MB〜数GB溜まっていることも多いので、定期的に実行しておくとよいです。

## 自分で依存したパッケージを確認したい（`brew leaves`）

```console
$ brew leaves
```

`brew leaves`コマンドで、自分で明示的にインストールしたパッケージだけを一覧できます。
`brew list`は依存関係で自動インストールされたパッケージも含まれるため、区別したいときに使います。

## 依存関係を確認したい（`brew deps`）

```console
$ brew deps python3
ca-certificates
lz4
mpdecimal
openssl@3
readline
sqlite
xz
zstd
```

`brew deps`コマンドで、指定したフォーミュラが依存しているパッケージを確認できます。

## 環境を診断したい（`brew doctor`）

```console
$ brew doctor
Your system is ready to brew.
```

`doctor`コマンドで、Homebrewの設定に問題がないか診断できます。
問題がない場合は
`Your system is ready to brew.`
と表示されます。
インストールがうまくいかないときなど、トラブルシューティングの入口として使います。

## パスを知りたい（`brew --prefix`）

```console
$ brew --prefix
/opt/homebrew
```

`brew --prefix`で、Homebrewがインストールされているパスを確認できます。
デフォルトで
macOS ARM（Apple Silicon）の場合は`/opt/homebrew/`、
macOS Intelの場合は`/usr/local/`、
Linuxの場合は`/home/linuxbrew/.linuxbrew/`になっています。

```console
$ brew --prefix python3
/opt/homebrew/opt/python@3.14

$ brew --prefix fish
/opt/homebrew/opt/fish
```

`brew --prefix フォーミュラ名`で、指定したフォーミュラがインストールされているパスを確認できます。
単体で使うことはあまりなく、シェルスクリプトを組み合わせて使うと便利です。

```bash
cmake -DCMAKE_PREFIX_PATH=$(brew --prefix qt@5)
# ARMの場合: cmake -DCMAKE_PREFIX_PATH=/opt/homebrew/qt@5
# Intelの場合: cmake -DCMAKE_PREFIX_PATH=/usr/local/qt@5
```

上のサンプルでは、`cmake`でビルドするときにリンクする`qt@5`のパスを追加しています。
OSの違いを気にせずに同じコマンドを使いまわすことができます。

## フォントを追加したい（`homebrew/cask-fonts`）

```console
$ brew tap homebrew/cask-fonts

```

`homebrew/cask-fonts`は、フォント用のタップです。
フォントを追加したい場合は、
`brew tap homebrew/cask-fonts`
でタップしておく必要があります。

:::{seealso}

```console
Warning: Formula homebrew/cask-fonts/font-fira-code was renamed to homebrew/cask/font-fira-code.
```

2024年（のどこか）から、フォントがCaskに取り込まれたようで、
``brew tap homebrew/cask-fonts``する必要はなくなりました。

```console
$ brew doctor
Warning: You have the following deprecated, official taps tapped:
  Homebrew/homebrew-cask-fonts
Untap them with `brew untap`.

$ brew untap Homebrew/homebrew-cask-fonts
Untapping homebrew/cask-fonts...
Untapped (263 files, 24.9MB).
```

:::

[Google Fonts](https://fonts.google.com/)にあるフォントもインストールできます。

- ``brew install font-cherry-bomb-one`` [Cherry Bomb One](https://fonts.google.com/specimen/Cherry+Bomb+One)
- ``brew install font-chokokutai`` [Chokokutai](https://fonts.google.com/specimen/Chokokutai))
- ``brew install font-darumadrop-one``
- ``brew install font-dotgothic16``
- ``brew install font-hachi-maru-pop``
- ``brew install font-hackgen-nerd``
- ``brew install font-hackgen`` [HackGen](https://github.com/yuru7/HackGen)
- ``brew install font-klee-one``
- ``brew install font-merienda-one``
- ``brew install font-merienda``
- ``brew install font-monaspace`` [Monaspace](https://monaspace.githubnext.com/)
- ``brew install font-monomaniac-one`` [Monomaniac One](https://fonts.google.com/specimen/Monomaniac+One)
- ``brew install font-noto-sans-cjk-jp``
- ``brew install font-noto-serif-cjk-jp``
- ``brew install font-plemol-jp`` [PlemolJP](https://github.com/yuru7/PlemolJP)
- ``brew install font-rampart-one``
- ``brew install font-reggae-one`` [Reggae One](https://fonts.google.com/specimen/Reggae+One)
- ``brew install font-rocknroll-one``
- ``brew install font-source-han-code-jp``
- ``brew install font-source-han-sans``
- ``brew install font-source-han-serif``
- ``brew install font-stick``
- ``brew install font-yomogi``
- ``brew install font-yusei-magic`` [Yusei Magic](https://fonts.google.com/specimen/Yusei+Magic)

## zsh のパスを設定したい

```zsh
# ~/.zprofile を編集する
# ... 他に設定してある場合はそのままでOK
eval "$(/opt/homebrew/bin/brew shellenv)"
```

``brew shellenv``を実行すると、シェルごとのHomebrew設定が出力されます。
その中身をシェル起動時のスクリプトで``eval``しています。
ZSHの場合は{file}`~/.zprofile`に追記します。
Homebrewをインストールした末尾に表示されるスクリプトを実行してもOKです。

## fish のパスを設定したい

```fish
# ~/.config/fish/config.fish
if status is-interactive
    # Commands to run in interactive sessions can go here
    # ... 他に設定してある場合はそのままでOK
    eval (/opt/homebrew/bin/brew shellenv) # <= ここを追記
end
```

Fishの場合は{file}`~/.config/fish/config.fish`に追記します。
Zsh用の設定と微妙に異なる（`$`や`"`がいらない）ので注意が必要です。

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
