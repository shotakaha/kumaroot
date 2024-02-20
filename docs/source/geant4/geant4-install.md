# インストールしたい（``geant4``）

```console
$ brew install spack
$ spack install geant4
```

公式ドキュメントの[Install Geant4 via a Package Manager](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/#install-geant4-via-a-package-manager)に書いてあるようにパッケージ管理ツールでインストールできるようになっています。

``Homebrew``にはフォームラがないので、[Spack](https://spack.io/)というスパコン向けのパッケージ管理ツールを使います。
``Spack``は``Homebrew``でインストールできます。

``spack install geant4``すると、関連パッケージ／ツールすべてのコンパイルがはじまるので、それなりに時間がかかります。

## 関連パッケージ

```console
$ spack list | rg geant4
geant4
geant4-data
geant4-vmc
```

``geant4``関係のパッケージを確認しました。
``geant4-data``は本体の依存パッケージとしてインストールされるようです。

過去に手動インストールしたときは、数種類のデータファイルを、指定されたパスに配置してからコンパイルした覚えがあります。
かなり簡素化されていることに感激しました。

