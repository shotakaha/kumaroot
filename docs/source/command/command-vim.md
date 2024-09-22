# Vimしたい（``vi``）

```console
$ brew install vim
```

## コマンド操作したい

```vim
dd    " 1行を削除
d$    " 行末まで削除
d0    " 行頭まで削除
d10l  " 10文字削除
d10j  " 下10行を削除
d10k  " 上10行を削除
```

ノーマルモードで編集用のコマンド操作ができます。

## 設定ファイルしたい（`~/.vimrc`）

```config
~/
|-- .vimrc    # メインの設定ファイル
|-- .vim/
    |-- autoload/    # 自動読み込みするプラグインや関数
    |-- colors/    # テーマ
    |-- plugin/    # 自動的に読み込まれるプラグイン
    |-- ftplugin/  # ファイルタイプごとの設定
    |-- syntax/    # シンタックスハイライトの設定
    |-- bundle/    # プラグイン管理
    |-- undo/      # Undoファイルを保存
```

`vim`の設定は`~/.vimrc`に記述します。
また、プラグインなどの関連ファイルは`~/.vim/`ディレクトリの中に保存します。

:::{note}

プラグイン関連のサブディレクトリが複数に散らばっているようです。
利用するプラグインやプラグイン管理ツールの使い方を読んで、使い分けてください。

:::

```vim
" 設定ファイルのパスを確認
:echo $MYVIMRC
" ~/.vimrc

" 設定ファイルを編集
:edit $MYVIMRC

" 設定ファイルを再読み込み
:source $MYVIMRC
```

メインの設定ファイルのパスはエディター上で`:echo $MYVIMRC`コマンドで確認できます。
`$MYVIMRC`は`vim`が自動で設定する環境変数です。

## 基本設定したい

```vim
set nocompatible  " vi互換モードを無効化（推奨）
syntax enable
set title
set mouse=a  " マウス操作を有効化
set lazyredraw
set ttyfast

" エンコーディング
set encoding=utf-8
set fileencoding=utf-8

" 行番号表示
set number
set relativenumber

" カーソル表示
set cursorline
set cursorcolumns

" コマンド表示
set cmdheight=2
set showcmd

" コマンド補完
set wildmenu
set wildmode=longest:full,full

" 無名レジスタ＝クリップボード
set clipboard=unnamedplus

" 検索
set ignorecase
set smartcase
set hlsearch
set incsearch

" インデント
set tabstop=4
set shiftwidth=4
set expandtab
set smartindent
set autoindent

" 余白
set scroffoff=8
set sidescroll=8
set wrap
set linebreak
set showbreak=>>>
set splitbelow
set splitright
```

## ステータスラインしたい（`:set statusline`）

```vim
set statusline=[%{mode()}]\ %F%m\ \(%l,%c\)[%p%%\ %LL]%<%=%r%h%w%y[%{&fileencoding}][%{&fileformat}]%=[b=%n][t=%{&tabstop}][i=%{&shiftwidth}]
```

| コード | 表示内容 |
|---|---|
| `%f` / `%F` / `%t` | ファイル名 |
| `%m` / `%M` | 修正フラグ |
| `%r` / `%R` | ROフラグ |
| `%h` / `%H` | Helpフラグ |
| `%w` / `%W` | Previewフラグ |
| `%y` / `%Y` | ファイルタイプ |
| `%n` | バッファー番号 |
| `%l` / `%c` | 行番号 / 列番号 |
| `%L` | 行数 |
| `%p%%` | 位置 |
| `%<` | truncate |
| `%=` | 均等 |

## レジスターしたい

| 記号 | レジスターの種類 |
|---|---|
| `"` | 無名レジスタ（デフォルト） |
| `"0-9` | 番号付きレジスタ |
| `"a-z` | 名前付きレジスタ |
| `"+` | システムクリップボード |
| `"-` | カットレジスタ |
| `"/` | 検索レジスタ |
| `"_` | ブラックホールレジスタ |

レジスターは`vim`上の一時的な保存領域です。
削除やヤンク、検索したテキストは自動でレジスターに登録されます。

レジスター（の概念）を理解することで、`vim`でのテキスト操作やキーバインド設定がイメージしやすくなるのではないかと思います。

```vim
" 保存されているレジスターを確認
:registers
```

`:registers`コマンドで、保存されているレジスターを確認できます。

```vim
" ~/.vimrc

set clipboard=unnapedplus
```

デフォルトのレジスタを`"`（無名レジスタ）から`"+`（システムクリップボード）に変更できます。

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

モードごとにキーバインド設定を追加できます。
再帰的な`remap`系と
非再帰的な`noremap`系のコマンドがあります。
精通するまでは`noremap`系から使い始めればOKです。

ぼくは、すでにEmacs-likeなキーバインドに慣れ親しんでしまっているので、ここではそれにできるだけ操作感が近づくように設定を整理しました。

## リーダーキーしたい（`mapleader`）

```vim
let mapleader = " "

nnoremap <leader>ev :edit $MYVIMRC<CR>
nnoremap <leader>sv :source $MYVIMRC<CR>
```

`mapleader`でリーダーキーを変更できます。
リーダーキーを`"␣"`（空白スペース）に設定すると、ノーマルモードでのコマンド呼び出しを簡略化できます。

:::{seealso}

SpacemacsやVSpaceCode的な操作感です。

:::

上記のサンプルでは、ノーマルモードのときに
`␣ev`で設定ファイルを編集、
`␣sv`で設定ファイルを再読み込みできるようにしています。

```vim
" ~/.vimrc

nnoremap <leader>w :w<CR>
nnoremap <leader>q :q<CR>
nnoremap <leader>x :wq<CR>
```

## keyboard-quitしたい

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

Emacsでは困ったときに`C-g`（`keyboard-quit`）（を連打して）コマンドを中断できます。
`<Esc>`（の3連打）に割り当てることで、ノーマルモードに戻ってこれるようにしました。

:::{note}

実際に`vim`を使っているときにも、クセで`C-g`してしまうことが多いので、このバインドは必須でした。

:::

## 移動したい

```vim
nnoremap <C-b> h
inoremap <C-b> <Left>
xnoremap <C-b> <Left>

nnoremap <C-f> l
inoremap <C-f> <Right>
xnoremap <C-f> <Right>

nnoremap <C-p> k
inoremap <C-p> <Up>
xnoremap <C-p> <Up>

nnoremap <C-n> j
inoremap <C-n> <Down>
nnoremap <C-n> <Down>

nnoremap <C-a> 0
inoremap <C-a> <Home>
xnoremap <C-a> <Home>

nnoremap <C-e> $
inoremap <C-e> <End>
xnoremap <C-e> <End>
```

Emacsの移動系のバインド（でよく使うもの）を`vim`バインドに割り当てました。

## ページ操作したい

```vim
nnoremap <C-v> <PageDown>
inoremap <C-v> <PageDown>
xnoremap <C-v> <PageDown>

nnoremap <M-v> <PageUp>
inoremap <M-v> <PageUp>
xnoremap <M-v> <PageUp>

nnoremap <C-l> zz
```

Emacsのページ操作系のコマンドを`vim`に割り当てました。

`C-v`はvimのビジュアルモード（visual-block）に割り当てられていますが、`v`もしくは`V`で代替することにして、上書きしています。

## ファイル操作したい

```vim
" 作成
nnoremap <C-x><C-f> :e
inoremap <C-x><C-f> <Esc>:e

" 保存
nnoremap <C-x><C-s> :w<CR>
inoremap <C-x><C-s> <Esc>:w<CR>

" 終了
nnoremap <C-x><C-c> :q<CR>
inoremap <C-x><C-c> <Esc>:q<CR>
```

Emacsのファイル操作系のコマンドに合わせてvimバインドを割り当てています。

:::{note}

vimデフォルトでは
編集モードでの補完コマンドが
`C-x`系バインドに割り当てられています。

```vim
inoremap <C-x><C-l> <Nop> " whole line completion
inoremap <C-x><C-f> <Nop> " filename completion
inoremap <C-x><C-n> <Nop> " next completion match
inoremap <C-x><C-p> <Nop> " previous completion match
inoremap <C-x><C-k> <Nop> " dictionary completion
inoremap <C-x><C-t> <Nop> " tag completion
inoremap <C-x><C-i> <Nop> " included files completion
inoremap <C-x><C-u> <Nop> " complete uncapitalized
inoremap <C-x><C-o> <Nop> " omni completion
```

あらかじめ無効にする設定を追加しておいてもよいかもしれません。

:::

## 検索したい

```vim
nnoremap <C-s> /
inoremap <C-s> <Esc>/

nnoremap <C-r> ?
inoremap <C-r> <Esc>?
```

Emacsの検索系コマンドをvimバインドに割り当てました。

## Undoしたい

```vim
" デフォルト
" <u> :undo
" <C-r> :redo

nnoremap u :undo<CR>
nnoremap U :redo<CR>
```

デフォルトのvimバインドでは、
`:undo`と`:redo`のバインドが対称的でないため、設定を追加しました。

```vim
inoremap <C-/> <Esc>:undo<CR>
inoremap <C-_> <Esc>:undo<CR>
inoremap <C-?> <Esc>:redo<CR>

xnoremap u <Esc>:undo<CR>
xnoremap U <Esc>:redo<CR>
```

また、Emacsのようなバインドも追加しました。

:::{note}

Emacsには`redo`コマンドはありませんが、`undo-tree`や`redo+`などの外部パッケージで推奨されているバインドを参考にしました。

:::

## view-modeしたい

```vim
nnoremap <C-x><C-r> <Esc><Esc><Esc>
inoremap <C-x><C-r> <Esc><Esc><Esc>
xnoremap <C-x><C-r> <Esc><Esc><Esc>

nnoremap <C-x><C-q> <Esc><Esc><Esc>
inoremap <C-x><C-q> <Esc><Esc><Esc>
xnoremap <C-x><C-q> <Esc><Esc><Esc>
```

`C-x C-r`もしくは`C-x C-q`でノーマルモードにできるよう追加しました。

## 編集したい

```vim
" デフォルト
" cc: 行全体を編集（カットして編集モード）
" C : 行末までを編集
" dd: 行全体をカット
" D : 行末までをカット
" yy: 行全体をヤンク
" Y : 行全体をヤンク -> 行末までヤンクに変更

nnoremap Y y$

inoremap <C-h> <BS>
inoremap <C-d> <Del>

nnoremap <C-k> D
inoremap <C-k> <Esc>Da

nnoremap <C-y> p
inoremap <C-y> <Esc>pa
```

`Y`は、もともと**行全体をヤンク**するコマンドですが、他の編集系のコマンドと操作感を揃えるため、**行末までヤンク**に変更しています。

また、Emacsの編集系の操作に合わせてvimバインドを割り当てています。

編集モード（`inoremap`）でキル／ヤンクしたあとは、`a`コマンドで編集モードに戻ってこれるようにしています。

## 削除したい

```vim
" デフォルト
" x : 1文字削除

nnoremap x "_d
nnoremap X "_D
xnoremap x "_x
onoremap x d
```

vimmerのキーバインド記事でオススメされていた`x`と`d`コマンドを使い分け設定を採用しました。

`x`は、もともと1文字削除（して無名レジスタに追加）するコマンドですが、`d`と機能的に似ています。
そのため、レジスタに追加しない（＝`"_`（ブラックホールレジスタ）に追加）ようにするとよいそうです。

`X`は、もともと前の文字を削除するコマンドですが、`D`と組み合わせて行末までを対象とすることで、大文字コマンドの操作感に統一感を持たせることができます。
