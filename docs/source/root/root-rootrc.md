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

```unixconfig
Canvas.Style Modern
Canvas.SaveAsDefaultType pdf

# Default histogram binnings for TTree::Draw()
Hist.Binning.1D.x: 100
Hist.Binning.2D.x: 40
Hist.Binning.2D.y: 40
Hist.Binning.2D.Prof: 100
Hist.Binning.3D.x: 20
Hist.Binning.3D.y: 20
Hist.Binning.3D.z: 20
Hist.Binning.3D.Profx: 100
Hist.Binning.3D.Profy: 100

# Default histogram precision for TTree::Draw()
Hist.Precision.1D: float
Hist.Precision.2D: float
Hist.Precision.3D: float

# Rint Settings
Rint.History $(HOME)/.root_hist
Rint.WelcomeLite no
```

## プロジェクト設定したい（ `rootlogon.C` ）

プロジェクトごとの設定は、ディレクトリ直下の``rootlogon.C``で設定できます。
