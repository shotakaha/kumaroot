# インストールしたい（`geant4`）

Geant4本体はソースコードを自分でビルドしてインストールする必要があります。
ここでは、Geant4の公式ドキュメントを参考にして、複数のバージョンを管理する（マイ）ベストプラクティスを紹介します。

```{toctree}
---
maxdepth: 1
---
geant4-install-brew
geant4-install-mkdir
geant4-install-download
geant4-install-configure
geant4-install-ccmake
geant4-install-build
geant4-install-clean
geant4-install-shell
```

前提として
`~/geant4`にGeant4専用のディレクトリを作成し、その中でバージョンごとにディレクトリを作成して管理することにします。
また、ダウンロードしたソースコードは`~/geant4/archives/`に保存することとします。

```text
~/geant4
  |-- archives/    # ソース（圧縮ファイル）の保存用
  |    |-- geant4.v11.3.2.tar.gz
  |    |-- geant4.v11.4.0.tar.gz
  |    |-- geant4.v11.4.3.tar.gz
  |-- v11.3.2/    # バージョンごとの作業ディレクトリ
  |-- v11.4.0/
  |-- v11.4.3/
      |-- source/    # ソース一式
      |-- build/     # ビルド用のディレクトリ
      |-- install/   # インストール先のディレクトリ
```

::: {seealso}

ここで紹介した手順を`Taskfile`を使って整理したリポジトリも作成しました。

- [qumasan/g4setup](https://gitlab.com/qumasan/g4setup)

:::
