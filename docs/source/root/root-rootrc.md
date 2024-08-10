# ユーザー設定したい（ `.rootrc` ）

ROOTのユーザー設定は {file}`~/.rootrc` で設定できます。

```console
// ROOTをインストールしたパスを確認する
$ root-config --prefix
/opt/homebrew/Cellar/root/6.32.02_1

// system.rootrcのパスを確認する
$ locate system.rootrc
/opt/homebrew/Cellar/root/6.32.02_1/etc/root/system.rootrc
/opt/homebrew/etc/root/system.rootrc

// system.rootrc を $HOME/.rootrc にコピーする
$ cp $(root-config --prefix)/etc/system.rootrc ~/.rootrc
```

{file}`{ROOTをインストールしたパス}/etc/system.rootrc` にデフォルトのファイルがあります。
これをホームディレクトリにコピーして編集するのがお手軽でよいと思います。

## プロジェクト設定したい（ `rootlogon.C` ）

プロジェクトごとの設定は、ディレクトリ直下の``rootlogon.C``で設定できます。
