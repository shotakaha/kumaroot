# 環境のバージョン管理したい（``asdf``）

```bash
$ brew install asdf
```

開発環境のバージョンを切り替えできるコマンドです。
Read the Docsのビルド手順で、Pythonのバージョン指定に使われていたので、使い方を調べてみます。

## プラグインを確認したい

```bash
$ asdf plugin list all
initializing plugin repository...Cloning into '~/.asdf/repository'...
...（省略）...
1password-cli                 https://github.com/NeoHsu/asdf-1password-cli.git
R                             https://github.com/asdf-community/asdf-r.git
...
bat                           https://gitlab.com/wt0f/asdf-bat.git
...
git                           https://gitlab.com/jcaigitlab/asdf-git.git
...
gohugo                        https://github.com/nklmilojevic/asdf-hugo.git
hugo                          https://github.com/NeoHsu/asdf-hugo.git
...
poetry                        https://github.com/asdf-community/asdf-poetry.git
python                        https://github.com/danhper/asdf-python.git
...
rust                          https://github.com/code-lever/asdf-rust.git
rust-analyzer                 https://github.com/Xyven1/asdf-rust-analyzer
...
```

``asdf``で管理できるツールのプラグインが思ってた以上にたくさんあることが分かりました。
とりあえず興味のあるものを抜粋してみました。

## プラグインをインストールしたい

```bash
asdf plugin add プラグイン名
```

## ツールのバージョンを指定したい

```bash
$ asdf global プラグイン名 バージョン  # global version
$ asdf local プラグイン名 バージョン  # local version
```

## リファレンス

- [asdf](https://asdf-vm.com/)
- [asdf-python](https://github.com/asdf-community/asdf-python)
