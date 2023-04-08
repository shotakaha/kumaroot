# リンクを確認したい（``make linkcheck``）

```bash
$ cd $MyPROJECT/docs/
$ make linkcheck > checked.txt
$ less checked.txt | grep broken
$ less checked.txt | grep redirect
```

ドキュメントに記載した外部リンクが有効かどうかを確認できます。
リンクにアクセスできない場合は、``broken``と表示され、エラーコード（``404``や``500``）が表示されます。
またリダイレクトされている場合はリダイレクト先のURLが表示されます。

結果は標準出力（＝ターミナル）に表示されますが、外部リンクが多い場合はスクロールして戻る必要があります。
いったんテキストファイルにリダイレクトして保存し、あとでファイル内検索するとよいと思います。
