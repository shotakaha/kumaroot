# Helixしたい（``hx``）

```console
$ brew install helix
```

[vim](./command-vim.md)などにインスパイアされたモーダルエディターです。
vimより、コマンド操作のキーバインドに一貫性があったり、
ヘルプ／補完パネルを表示してくたりと親切です。

真のvimmerを目指さないのであれば、こちらのほうが使いやすいと思いました。
僕はGitエディターに``hx``を設定しています。

```cfg
# ~/.gitconfig
[core]
    editor = hx
```

## マイナーモードしたい

| キー | 操作内容 | コマンド |
|---|---|---|
| `v` | selectモード | `select_mode` |
| `:` | commandモード | `command_mode` |
| `g` | gotoモード | |
| `m` | matchモード | |
| `z` | viewモード | |
| `Z` | sticky-viewモード | |
| `Ctrl-w` | windowモード | |
| `Space` | spaceモード | |

## カーソル移動したい

| キー | 操作内容 | コマンド |
|---|---|---|
| `h` | 左に移動 | `move_char_left` |
| `j` | 下に移動 | `move_visual_line_down` |
| `k` | 上に移動 | `move_visual_line_up` |
| `l` | 右に移動 | `move_char_right` |
| `w` | 次の文字に移動 | `move_next_word_start` |
| `b` | 前の文字に移動 | `move_prev_word_start` |
| `G <n>` | `<n>`行目に移動 | `goto_line` |
| `Ctrl-f` | 1ページ進む | `page_down` |
| `Ctrl-b` | 1ページ戻る | `page_up` |
| `Ctrl-d` | 半ページ進む | `page_cursor_half_down` |
| `Ctrl-u` | 半ページ戻る | `page_cursor_half_up` |

### gotoモード

| キー | 操作内容 | コマンド |
|---|---|---|
| `g` `g` | ファイルの先頭に移動 | `goto_file_start` |
| `g` `e` | ファイルの末尾に移動 | `goto_last_line` |
| `g` `h` | 行の先頭に移動 | `goto_line_start` |
| `g` `l` | 行の末尾に移動 | `goto_line_end` |
| `g` `t` | ウィンドウの上部に移動 | `goto_window_top` |
| `g` `c` | ウィンドウの中央に移動 | `goto_window_center` |
| `g` `b` | ウィンドウの下部に移動 | `goto_window_bottom` |
| `g` `n` | 次のバッファーに移動 | `goto_next_buffer` |
| `g` `p` | 前のバッファーに移動 | `goto_previous_buffer` |
| `g` `a` | 直前のバッファーに移動 | `goto_last_accessed_file` |


## 検索したい

| キー | 操作内容 | コマンド |
|---|---|---|
| `/` | 検索（正規表現） | `search` |
| `?` | 検索（前のパターン） | `rsearch` |
| `n` | 次のマッチに移動 | `search_next` |
| `N` | 前のマッチに移動 | `search_prev` |
| `*` | 選択範囲の文字列を検索 | `search_selection` |

## 範囲選択したい

| キー | 操作内容 | コマンド |
|---|---|---|
| `%` | 全選択 | `select_all` |
| `x` | 現在の行を選択 | `extend_line_below` |
| `_` | 選択範囲から空白をトリム | `trim_selections` |
| `;` | 選択を解除 | `collapse_selection` |

## 編集したい

| キー | 操作内容 | コマンド |
|---|---|---|
| `d` | 選択範囲を削除 | `delete_selection` |
| `i` | カーソル位置に挿入 | `insert_mode` |
| `I` | 行頭に挿入 | `insert_at_line_start` |
| `a` | カーソル位置に追加 | `append_mode` |
| `A` | 行末に挿入 | `insert_at_line_end` |
| `o` | カーソル位置の下に空行を追加 | `open_below` |
| `O` | カーソル位置の上に空行を追加 | `open_above` |
| `.` | 最後の挿入をリピート | |
| `u` | Undo | `undo` |
| `U` | Redo | `redo` |
| `y` | 選択範囲をヤンク | `yank` |
| `p` | カーソル位置の後にペースト | `paste_after` |
| `P` | カーソル位置の前にペースト | `paste_before` |
| `>` | Indent | `indent` |
| `<` | Unindent | `unindent` |
| `Q` | マクロを記録（開始／停止） | `record_macro` |
| `q` | マクロを再生 | `replay_macro` |

## ウィンドウ分割したい

| キー | 操作内容 | コマンド |
|---|---|---|
| `Ctrl-w` | windowモード | |
| `Ctrl-w` `Ctrl-s` | 水平に分割 | `hsplit` |
| `Ctrl-w` `Ctrl-v` | 垂直に分割 | `vsplit` |
| `Ctrl-w` `Ctrl-w` | 次のウィンドウに移動 | `rotate_view` |
| `Ctrl-w` `Ctrl-h` | 左のウィンドウに移動 | `jump_view_left` |
| `Ctrl-w` `Ctrl-j` | 下のウィンドウに移動 | `jump_view_down` |
| `Ctrl-w` `Ctrl-k` | 上のウィンドウに移動 | `jump_view_up` |
| `Ctrl-w` `Ctrl-l` | 右のウィンドウに移動 | `jump_view_right` |
| `Ctrl-w` `Ctrl-q` | 現在のウィンドウを閉じる | `wclose` |
| `Ctrl-w` `Ctrl-o` | 他のウィンドウを閉じる | `wonly` |

{kbd}`control + w`でwindowモードを起動して、コマンドを入力します。
{kbd}`control`キーを押したまま、操作できるようになっています。
