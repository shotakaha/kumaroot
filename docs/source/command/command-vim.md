# Vimしたい（``vi``）

```console
$ brew install vim
```

## コマンド操作したい

| コマンド | 操作 |
|---|---|
| `Esc` | ノーマルモードに切り替える |
| `j` `k` | カーソルを上下に移動する |
| `h` `l` | カーソルを左右に移動する |
| `v` `V` | 矩形選択モードに切り替える |
| `0` `$` | 行頭・行末に移動する |
| `d$` | カーソル位置から行末までカットする |
| `y$` | カーソル位置から行末までコピーする |
| `p` `P` | カーソル位置の前後にペーストする |
| `x` | 1文字削除する |
| `dd` | 1行削除する |
| `yy` | 1行コピーする |
| `i` `a` `o` `O` | 挿入モードに切り替える |
| `:` | コマンドモードに切り替える |
| `C-o` | 挿入モードで一時的のノーマルモードに切り替える |
| `C-c` | コマンドモードでコマンドを中断しノーマルモードに切り替える |

よく使うコマンド操作を整理しました。
独特なキーバインドには慣れるほかないです。

操作はノーマルモード↔︎挿入モードの切り替えが基本です。
なので`Esc`と`i`をよく使います。
ノーマルモードでは`j`/`k`/`l`/`h`でカーソルを移動します。
挿入モードではまず矢印キーで移動すればよいです。

`C-o`も覚えておくとよいコマンドのひとつです。
このコマンドは、挿入モードで使えるコマンドで、一時的にノーマルモード（でコマンド）を実行し、
また挿入モードに戻ることができます。
なので、`<C-o>d$` → `p`で、挿入モードのままカット＆ペーストができます。

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
nnoremap キー コマンド    " normalモード
inoremap キー コマンド    " insertモード
xnoremap キー コマンド    " visual + select
cnoremap キー コマンド    " commandモード
vnoremap キー コマンド    " visualモード
snoremap キー コマンド    " selectモード
tnoremap キー コマンド    " terminalモード
```

モードごとにキーバインド設定を追加できます。
再帰的な`remap`系と
非再帰的な`noremap`系のコマンドがあります。
精通するまでは`noremap`系から使い始めればOKです。

## Emacs風キーバインドにしたい

Emacs風キーバインドの設定を[Gist](https://gist.github.com/shotakaha/39fa568a150084380a256b18b647612c)に整理しました。
ご自由にお使いください。

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
nnoremap <C-g> <Esc><Esc>
xnoremap <C-g> <Esc><Esc>
inoremap <C-g> <Esc><Esc>
cnoremap <C-g> <C-c><Esc><Esc>
```

`C-g`（`keyboard-quit`）は、コマンドを中断するキーです。
Emacsでは操作に困った時、とりあえずこのキーを連打すればOKです。
`<Esc>`（の連打）に割り当てることで、ノーマルモードに戻ってこれるようにしました。

:::{note}

実際に`vim`を使っているときにも、クセで`C-g`してしまうことが多いので、このバインドは必須でした。

:::

## 移動したい

```vim
" C-f: forward char
nnoremap <C-f> l
xnoremap <C-f> l
inoremap <Right>
cnoremap <Right>

" C-b: backward char
nnoremap <C-b> h
xnoremap <C-b> h
inoremap <C-b> <Left>
cnoremap <C-b> <Left>

" C-n: next line
nnoremap <C-n> j
xnoremap <C-n> j
inoremap <C-n> <Down>
cnoremap <C-n> <Down>

" C-p: previous line
nnoremap <C-p> k
xnoremap <C-p> k
inoremap <C-p> <Up>
cnoremap <C-p> <Up>

" C-a: beginning of the line
nnoremap <C-a> 0
xnoremap <C-a> 0
inoremap <C-a> <Home>
cnoremap <C-a> <Home>

" C-e: end of the line
nnoremap <C-e> $
xnoremap <C-e> $
inoremap <C-e> <End>
cnoremap <C-e> <End>
```

Emacsの移動系のバインド（でよく使うもの）を`vim`バインドに割り当てました。

## ページ操作したい

```vim
" C-v: next page
nnoremap <C-v> <PageDown>
xnoremap <C-v> <PageDown>
inoremap <C-v> <PageDown>
cnoremap <C-v> <PageDown>


" M-v: previous page
nnoremap <M-v> <PageUp>
xnoremap <M-v> <PageUp>
inoremap <M-v> <PageUp>
cnoremap <M-v> <PageUp>


" C-l: center page
nnoremap <C-l> zz
xnoremap <C-l> zz
inoremap <C-l> <C-o>zz
cnoremap <C-l> <C-c>zz
```

Emacsのページ操作系のコマンドを`vim`に割り当てました。

:::{note}

`C-v`はvimのビジュアルモード（visual-block）への切り替えに割り当てられています。
`V`（大文字）で切り替えることができるので、ここでは上書きしています。

:::

## ファイル操作したい

```vim
" C-x C-f: open file
nnoremap <C-x><C-f> :e<SPACE>
xnoremap <C-x><C-f> :e<SPACE>
inoremap <C-x><C-f> <C-o>:e<SPACE>
cnoremap <C-x><C-f> <C-c>:e<SPACE>

" C-x C-s: save file
nnoremap <C-x><C-s> :w<CR>
xnoremap <C-x><C-s> :w<CR>
inoremap <C-x><C-s> <C-o>:w<CR>
cnoremap <C-x><C-s> <C-c>:w<CR>

" C-x C-c: quit
nnoremap <C-x><C-c> :q<CR>
xnoremap <C-x><C-c> :q<CR>
inoremap <C-x><C-c> <C-o>:q<CR>
cnoremap <C-x><C-c> <C-c>:q<CR>
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
" C-s: forward search
nnoremap <C-s> /
xnoremap <C-s> /
inoremap <C-s> <Esc>/
cnoremap <C-s> <Esc>/

" C-r: backward search
nnoremap <C-r> ?
xnoremap <C-r> ?
inoremap <C-r> <Esc>?
cnoremap <C-r> <Esc>?
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
" C-x C-r: view-mode (read-only)
nnoremap <C-x><C-r> :set<SPACE>readonly!<CR>
xnoremap <C-x><C-r> :set<SPACE>readonly!<CR>
inoremap <C-x><C-r> <C-o>:set<SPACE>readonly!<CR>
cnoremap <C-x><C-r> <C-c>:set<SPACE>readonly!<CR>

" C-x C-q: view-mode (read-only)
nnoremap <C-x><C-q> :set<SPACE>readonly!<CR>
xnoremap <C-x><C-q> :set<SPACE>readonly!<CR>
inoremap <C-x><C-q> <C-o>:set<SPACE>readonly!<CR>
cnoremap <C-x><C-q> <C-c>:set<SPACE>readonly!<CR>
```

`:set readonly!`で読み取り専用モードをトグルできます。
`C-x C-r`もしくは`C-x C-q`に割り当ててトグルできるようにしました。

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

#
