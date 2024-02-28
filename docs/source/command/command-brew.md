# パッケージ管理したい（``brew``）

```console
$ brew install フォーミュラ名
$ brew update
$ brew outdated
$ brew upgrade
```

## パスを知りたい（``brew --prefix``）

```console
$ brew --prefix フォーミュラ名
$ brew --prefix fish
$ brew --prefix qt@5
```

``--prefix``オプションで、フォーミュラがインストールされたパスを確認できます。

macOS ARM（Apple Silicon）の場合は``/opt/homebrew/``の下、
macOS Intelの場合は``/usr/local/``の下、
Linuxの場合は``/home/linuxbrew/.linuxbrew/``に
フォーミュラがインストールされています。

```bash
cmake -DCMAKE_PREFIX_PATH=$(brew --prefix qt@5)
# ARMの場合: cmake -DCMAKE_PREFIX_PATH=/opt/homebrew/qt@5
# Intelの場合: cmake -DCMAKE_PREFIX_PATH=/usr/local/qt@5
```

単体で使うことはほぼないかもしれませんが、シェルスクリプトを組み合わせて使うと便利なときがあります。
上のサンプルでは、``cmake``でビルドするときにリンクする``qt@5``のパスを追加しています。
環境の違いを気にせずに同じコマンドを使いまわすことができます。

## パッケージを探したい（``brew search``）

```console
$ brew search 検索パターン

// 例：ブラウザを検索
$ brew search browser
```

``search``コマンドを使って、パッケージ名（＝フォーミュラ）を検索できます。
検索パターンは曖昧マッチに（おそらく）対応しているので、思いついたパターンをそのまま入力すればOKです。

ヒットした検索名が多すぎる場合は、検索コマンド（[grep](./command-grep.md)）などで絞り込むか、検索パターンを考え直すか、してください。

## パッケージの詳細を調べたい（``brew info``）

```console
$ brew info フォーミュラ名

// 例：Brave Browser
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
// パッケージリストを更新する
$ brew update

// 更新が必要なパッケージを表示する
$ brew outdated

// パッケージを更新する
$ brew upgrade
```

``update``コマンドでパッケージ一覧を更新します。
``outdated``コマンドで更新があるパッケージ一覧を表示できます。
``upgrade``コマンドで更新があるパッケージをダウンロードできます。

## フォントを追加したい

```console
$ brew tap homebrew/cask-fonts
```

フォント用のタップ（``homebrew/cask-fonts``）を使えるようにしておきます。
[Google Fonts](https://fonts.google.com/)にあるフォントもインストールできます。

- ``brew install font-monomaniac-one`` [Monomaniac One](https://fonts.google.com/specimen/Monomaniac+One)
- ``brew install font-cherry-bomb-one`` [Cherry Bomb One](https://fonts.google.com/specimen/Cherry+Bomb+One)
- ``brew install font-darumadrop-one``
- ``brew install font-dotgothic16``
- ``brew install font-hachi-maru-pop``
- ``brew install font-hackgen``
- ``brew install font-hackgen-nerd``
- ``brew install font-klee-one``
- ``brew install font-merienda``
- ``brew install font-merienda-one``
- ``brew install font-noto-sans-cjk-jp``
- ``brew install font-noto-serif-cjk-jp``
- ``brew install font-rampart-one``
- ``brew install font-rocknroll-one``
- ``brew install font-source-han-code-jp``
- ``brew install font-source-han-sans``
- ``brew install font-source-han-serif``
- ``brew install font-stick``
- ``brew install font-yomogi``
- ``brew install font-yusei-magic`` [Yusei Magic](https://fonts.google.com/specimen/Yusei+Magic)
- ``brew install font-reggae-one`` [Reggae One](https://fonts.google.com/specimen/Reggae+One)
- ``brew install font-chokokutai`` [Chokokutai](https://fonts.google.com/specimen/Chokokutai))

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
