# アンインストールしたい

```console
$ cd ~/geant4/v11.X.Y/
$ rm -rf install
$ rm -rf build
```

`install`ディレクトリと`build`ディレクトリを削除することで、Geant4をアンインストールできます。

:::{note}

ここまでで紹介した手順は個人利用を想定しているため、システム全体にインストールしていません。
そのため`install`と`build`を削除するだけでアンインストールできます。

:::

## 完全にアンインストールしたい

```console
$ cd ~/geant4/
$ rm -rf v11.X.Y
$ rm -rf archives/geant4-v11.4.3.zip
```

ソースコードやアーカイブも含めて削除すれば、完全にアンインストールできます。
