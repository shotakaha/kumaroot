# インストールしたい（``spack install geant4``）

```console
$ brew install spack
$ spack install geant4
```

公式ドキュメントの[Install Geant4 via a Package Manager](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/#install-geant4-via-a-package-manager)に書いてあるようにパッケージ管理ツールでインストールできるようになっています。

以前はHomebrewにもフォーミュラがあったのですが、いまはなくなってしまいました。
なので、[Spack](https://spack.io/)というスパコン向けのパッケージ管理ツールを使います。
``Spack``は``Homebrew``でインストールできます。

Geant4に必要な関連パッケージすべてのビルドが必要なため、それなりに時間がかかりました。

## 環境変数したい

```console
$ source /usr/local/Cellar/spack/0.21.1/share/spack/setup-env.fish
$ spack load geant4
```

シェルの環境変数を設定します。
まず、``setup-env.fish``を読み込みSpackを設定します。
次に``spack load geant4``を実行し、Geant4を設定します。

:::{hint}

``setup-env``はシェルごとに用意されています。
未設定の場合、``spack load geant4``を実行すれば、どのパスを読み込めばよいか、エラーメッセージで教えてくれます。

:::

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

## 利用可能なバージョン

```console
$ spack versions geant4
==> Safe versions (already checksummed):
  11.1.2  11.1.0  11.0.3  11.0.1  10.7.4  10.7.2  10.7.0  10.6.2  10.6.0  10.4.3  10.3.3
  11.1.1  11.0.4  11.0.2  11.0.0  10.7.3  10.7.1  10.6.3  10.6.1  10.5.1  10.4.0
==> Remote versions (not yet checksummed):
  11.2.1  11.2.0.beta  11.2.0  11.1.3  11.1.0.beta  11.0.0.beta
```

``spack versions``コマンドで利用できるバージョンを確認できます。
チェックサムが確認済みの``Safe versions``と、まだ確認できてない``Remote versions``があります。
