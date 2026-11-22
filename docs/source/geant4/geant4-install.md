# インストールしたい（`geant4`）

Geant4本体はソースコードを自分でビルドしてインストールする必要があります。
ここでは、Geant4の公式ドキュメントを参考にして、複数のバージョンを管理する個人的なベストプラクティスを紹介します。

```{toctree}
---
maxdepth: 1
---
geant4-install-brew
geant4-install-mkdir
geant4-install-download
geant4-install-configure
geant4-install-configure-options
geant4-install-cmakelists
geant4-install-build
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
  |-- v11.4.0/    # バージョンごとの作業ディレクトリ（例：下の構成と同じ）
  |-- v11.4.3/
      |-- source/    # ソース一式
      |-- build/     # ビルド用のディレクトリ
      |-- install/   # インストール先のディレクトリ
```

zipを展開すると`geant4-v11.4.3/`ができ、それを`v11.4.3/source/`にリネームします。
展開後のzipファイルは`archives/`に残しておくと、やり直すときに使えます。
ディスク容量を節約したい場合は、削除しても問題ありません。

## インストールを確認したい

```console
// ステップ1：ディレクトリの構成を確認する
$ tree ~/geant4 -L 2

// ステップ2：使うバージョンの設定を読み込む
$ source ~/geant4/v11.4.3/install/bin/geant4.sh

// ステップ3：バージョンを確認する
$ geant4-config --version
11.4.3
```

`geant4-config --version`で、インストールしたバージョンが表示されれば完了です。

::: {seealso}

ここで紹介した手順を`Taskfile`を使って整理したリポジトリも作成しました。

- [qumasan/g4setup](https://gitlab.com/qumasan/g4setup)

:::
