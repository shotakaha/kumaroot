# Vimしたい（``vi``）

```console
$ brew install vim
```

## 設定ファイル（`~/.vimrc`）

```vim
" 設定ファイルのパスを確認
:echo $MYVIMRC
" ~/.vimrc

" 設定ファイルを編集
:edit $MYVIMRC

" 設定ファイルを再読み込み
:source $MYVIMRC
```

`vim`の設定ファイルは`~/.vimrc`です。
エディターの中で`:echo $MYVIMRC`で確認できます。

:::{note}

`$MYVIMRC`は`vim`が自動で設定する環境変数です。

:::

## リーダーキーしたい（`mapleader`）

```vim
let mapleader = " "

nnoremap <leader>ev :edit $MYVIMRC<CR>
nnoremap <leader>sv :source $MYVIMRC<CR>
```

`mapleader`でリーダーキーを変更できます。
`"␣"`（空白スペース）に設定するとよいみたいです。

上記のサンプルでは、ノーマルモードのとき
`␣ev`で設定ファイルを編集、
`␣sv`で設定ファイルを再読み込みできるようにしています。

## キーバインド設定したい

```vim
nnoremap キー コマンド    " ノーマルモード
inoremap キー コマンド    " 編集モード
vnoremap キー コマンド    " ヴィジュアルモード
snoremap キー コマンド    " 選択モード
cnoremap キー コマンド    " コマンド待機モード
tnoremap キー コマンド    " ターミナルモード
xnoremap キー コマンド    " ヴィジュアル + 編集モード
```

`noremap`系のコマンドで、キーバインド設定を追加できます。
ぼくは、すでにEmacs-likeなキーバインドに慣れ親しんでしまっているので、以下ではそれにできるだけ操作感が近づくように設定しています。

:::{note}

キーバインド設定には
再帰的な`remap`系と
非再帰的な`noremap`系のコマンドがあります。
精通するまでは`noremap`系から使い始めればOKです。

:::

## ノーマルモードしたい

```vim
" いろいろキャンセル
nnoremap <C-g> <Esc><Esc><Esc>
inoremap <C-g> <Esc><Esc><Esc>
vnoremap <C-g> <Esc><Esc><Esc>
snoremap <C-g> <Esc><Esc><Esc>
cnoremap <C-g> <Esc><Esc><Esc>
tnoremap <C-g> <Esc><Esc><Esc>
" xnoremap <C-g> <Esc><Esc><Esc>
```
