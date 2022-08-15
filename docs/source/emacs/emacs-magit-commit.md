# コミット（`C-x g c c`）

``Staged changes`` にあるファイルはコミットできます。
{kbd}`c`を押すとコミット用バッファ（``magit-commit-popup``）がポップアップします
（{numref}`fig-magit-commit-popup`）。

ポップアップ内にある``Switches``、``Options``、``Actions``から操作を選択し、頭に付いている記号を入力します。
通常のコミットの場合は{kbd}`c`を押します。

```{figure} ./emacs-magit/magit-commit-popup.png
---
name: fig-magit-commit-popup
---
コミット用バッファ
```

すると、画面が上下2分割されて
``magit-diff``バッファ（画面上）と
``.git/COMMIT_EDITMSG``バッファ（画面下）が表示されます
（{numref}`fig-magit-commit-edit`）。

``magit-diff``バッファには変更した箇所が表示されているので、それを確認しながら、
``.git/COMMIT_EDITMSG``バッファにコミットメッセージを書きます。
コミットメッセージの編集が終わったら{kbd}`C-c C-c`で保存します。
コミットをキャンセルする場合は{kbd}`C-c C-k`で破棄できます。

```{figure} ./emacs-magit/magit-commit-edit.png
---
name: fig-magit-commit-edit
---
コミットメッセージの編集
```

コミットが終わると ``Unpushed commits`` に
コミットメッセージが表示されます
（{numref}`fig-magit-commit-done`）。

```{figure} ./emacs-magit/magit-commit-done.png
---
name: fig-magit-commit-done
---
magit-commit-done
```

コミットを取り消したい場合は{kbd}`C-x g U HEAD^` とすればよいはずです（やったことない）。
もしくはシェルを起動して{command}`git reset HEAD^` しましょう（やったことある）。
