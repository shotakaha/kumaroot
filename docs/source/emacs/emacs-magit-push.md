# プッシュ（`C-x g P P`）

ある程度編集が進んだ場合や、1日の終わりには「プッシュ」を行い、
リモートへ変更を反映させましょう。

プッシュをするには``magit-buffer``で{kbd}`P`を押して
``magit-push``バッファを呼び出します
（{numref}`fig-magit-push`）。
そこで{kbd}`P`を押すとプッシュできます。

ただし、プッシュするブランチがローカルで作ったもので、
リモート先のブランチとの紐付けができていない場合、プッシュは失敗します。
そんな時は{kbd}`-u P`（``--set-upstream``）すれば大丈夫です。

```{figure} ./emacs-magit/magit-push.png
---
name: fig-magit-push
---
magit-push
```

ちゃんとプッシュできているか確認したい場合は{kbd}`$`を押します。
すると ``magit-process`` バッファが起動します
（{numref}`fig-magit-process`）。

プロセスが成功していれば最後のコマンドの行頭のステータスが ``0``、
失敗していればエラーコードが赤色で表示されます。
プロセスの詳細は ``TAB`` もしくは ``C-i`` で展開できます。

```{figure} ./emacs-magit/magit-process.png
---
name: fig-magit-process
---
Gitプロセスの表示
```
