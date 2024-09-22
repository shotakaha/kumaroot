# Vimしたい（``vi``）

```console
$ brew install vim
```

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
```

## Undoしたい

```vim
" デフォルト
" <u> :undo
" <C-r> :redo

nnoremap u :undo<CR>
nnoremap U :redo<CR>

inoremap <C-/> <Esc>:undo<CR>
inoremap <C-_> <Esc>:undo<CR>
inoremap <C-?> <Esc>:redo<CR>

xnoremap u <Esc>:undo<CR>
xnoremap U <Esc>:redo<CR>
```

ノーマルモードで`u`と`U`が対になるように変更します。
また、編集モードではEmacsのようなバインドを追加しています。

## Read-Onlyしたい

```vim
nnoremap <C-x><C-r> <Esc><Esc><Esc>
inoremap <C-x><C-r> <Esc><Esc><Esc>
xnoremap <C-x><C-r> <Esc><Esc><Esc>
```

`C-x C-r`でノーマルモードにできるよう追加しました。

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

`vim`では困ったときに`Esc`を連打すれば、
とりあえずノーマルモードに戻ってこれます。
この仕草は、`Emacs`だと`C-g`（`keyboard-quit`）を連打するのに似ていると思っています。
実際に`vim`を使っているときにも、クセで`C-g`することが多かいので`Esc`（の3連打）に設定してみました。

## ヤンクしたい

```vim
" デフォルト
" cc: 行全体を編集（カットして編集モード）
" C : 行末までを編集
" dd: 行全体をカット
" D : 行末までをカット
" yy: 行全体をヤンク
" Y : 行全体をヤンク

nnoremap Y y$  " 行末までヤンクに変更
```

## 削除したい

```vim
" デフォルト
" x : 1文字削除

nnoremap x "_d
nnoremap X "_D
xnoremap x "_x
onoremap x d
```
