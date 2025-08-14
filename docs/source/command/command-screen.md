# 仮想ターミナルしたい（`screen`）

```console
# 起動している screen を確認
$ screen -ls

# 新しいセッション
$ screen -S <セッション名>

# 再アタッチ
$ screen -r <セッション名 or セッションID>
$ screen -R
```

## インストールしたい

```console
$ sudo apt install screen
$ screen
```

`screen`はサーバー側にインストールすることが多いです。
Raspberry Piにも`apt`でインストールできました。

## キーバインドしたい

```bash
# プリフィックスを C-o に変更（デフォルトは C-a）
escape ^o^o

startup_message off
autodetach on

defscrollback 10000

hardstatus on
hardstatus alwayslastline
hardstatus string "%{.bW}%-w%{.rW}%n %t%{-}%+w %=%{..G} %H %{..Y} %m/%d %C%a "
```

`~/.screenrc`で設定を変更できます。
デフォルトのプリフィックスは`C-a`です。

`C-a`はターミナル操作でもよく使うので、
`C-o`に割り当て直すとよいです。

## セッション内操作したい

| キーバインド | 内容 |
|---|---|
| `C-o d` | デタッチ |
| `C-o c` | 新しいウィンドウを作成 |
| `C-o n` | 次のウィンドウ |
| `C-o p` | 前のウィンドウ |
| `C-o "` | ウィンドウ一覧 |
| `C-o [` | コピー&スクロール |
| `C-o ]` | ペースト |

## ステータス表示したい（`hardstatus`）

```bash
hardstatus on

## 画面最下部にウィンドウ一覧を"常に"表示
hardstatus alwayslastline
hardstatus string "%{= wk}%-Lw%{= bw}%n%f* %t%{= wk}%+Lw %{= wk}%=%{= gk} %Y/%m/%d %c

# %{= wk}  ## 文字:白（w）、背景：黒（k）に変更（=）
# %-Lw     ## 新しくウィンドウを作ったときに、画面下部のリストに追加する
# %{= bw}  ## 文字:青（b）、背景：白（w）に変更（=）
# %n       ## ウィンドウ番号
# %f       ## （不明）
# *        ## カレントウィンドウに * マーク
# %t       ## ウィンドウのタイトル; C-o A で変更できる
# %{= wk}  ## 文字:白（w）、背景：黒（k）に変更（=）
# %+Lw     ## ウィンドウ番号と名前のリスト（w）を追加（+）
# %{= wk}  ## 文字:白（w）、背景：黒（k）に変更（=）
# %=       ## 変更（=）
# %{= gk}  ## 文字:緑（g）、背景：黒（k）に変更（=）
# %Y/%m%d  %c ## 現在日時（yyyy/mm/dd 時刻（24h表示）
```
