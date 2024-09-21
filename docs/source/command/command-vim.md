# Vimしたい（``vi``）

```console
$ brew install vim
```

## キーバインド設定

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

`[nivsctx]noremap`コマンドで、キーバインドを設定できます。

:::{note}

キーバインド設定には
再帰的な`remap`系と
非再帰的な`noremap`系のコマンドがあります。
精通するまでは`noremap`系から使い始めればOKです。

:::

