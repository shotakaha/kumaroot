# インストールしたい（``geant4``）

```console
$ brew install spack
$ spack install geant4
```

公式ドキュメントの[Install Geant4 via a Package Manager](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/#install-geant4-via-a-package-manager)に書いてあるようにパッケージ管理ツールでインストールできるようになっています。

``Homebrew``にはフォームラがないので、[Spack](https://spack.io/)というスパコン向けのパッケージ管理ツールを使います。
``Spack``は``Homebrew``でインストールできます。

``spack install geant4``すると、関連パッケージ／ツールすべてのコンパイルがはじまるので、それなりに時間がかかります。

## 依存パッケージ

```console
$ spack spec geant4
Input spec
--------------------------------
 -   geant4

Concretized
--------------------------------
 -   geant4@11.1.2
 -       ^clhep@2.4.6.4
 -       ^cmake@3.27.7
 -           ^curl@8.4.0
 -               ^nghttp2@1.57.0
 -               ^pkgconf@1.9.5
 -           ^ncurses@6.4
 -       ^expat@2.5.0
 -       ^geant4-data@11.1.0
 -           ^g4abla@3.1
 -           ^g4emlow@8.2
 -           ^g4ensdfstate@2.3
 -           ^g4incl@1.0
 -           ^g4ndl@4.7
 -           ^g4particlexs@4.0
 -           ^g4photonevaporation@5.7
 -           ^g4pii@1.3
 -           ^g4radioactivedecay@5.6
 -           ^g4realsurface@2.2
 -           ^g4saiddata@2.0
 -       ^gmake@4.4.1
 -       ^xerces-c@3.2.4
 -       ^zlib-ng@2.1.4
```

``spack info``コマンドで関係するパッケージや``variant``を確認できます。
また、``spack spec``コマンドでインストールされるパッケージ一覧を確認できます（少し時間がかかりました）。

``geant4-data``もインストールされることが確認できました。
過去に手動インストールしたときは、数種類のデータファイルを、指定されたパスに配置してからコンパイルした覚えがあります。
かなり簡素化されていることに感激しました。

