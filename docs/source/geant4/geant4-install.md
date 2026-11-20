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
geant4-install-configure-options
geant4-install-ccmake
geant4-install-build
geant4-install-clean
geant4-install-shell
geant4-install-switch
```

前提として、次の4点を満たすようにします。

- Geant4本体をソースコードからインストールする
- 複数のバージョンを共存させる
- システム全体にはインストールしない（`/usr/local`などを使わない）
- アプリごとに、使うバージョンを切り替えられる

`~/geant4`にGeant4専用のディレクトリを作成し、その中でバージョンごとにディレクトリを作成して管理することにします。
また、ダウンロードしたソースコードは`~/geant4/archives/`に保存することとします。

```text
~/geant4
  |-- archives/    # ソース（圧縮ファイル）の保存用
  |    |-- geant4-v11.4.0.zip
  |    |-- geant4-v11.4.3.zip
  |-- v11.4.0/    # バージョンごとの作業ディレクトリ
  |-- v11.4.3/
      |-- source/    # ソース一式
      |-- build/     # ビルド用のディレクトリ
      |-- install/   # インストール先のディレクトリ
```

::: {seealso}

ここで紹介した手順を`Taskfile`を使って整理したリポジトリも作成しました。

- [qumasan/g4setup](https://gitlab.com/qumasan/g4setup)

:::
