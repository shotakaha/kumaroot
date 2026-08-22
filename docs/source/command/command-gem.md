# パッケージ管理したい（`gem`）

```console
$ gem
```

`gem`は、Rubyのパッケージ管理コマンドです。
開発言語のRuby（ルビー）にちなんで宝石（gem）と名付けられています。

## インストールしたい（`ruby`）

```console
$ brew install ruby

$ ruby --version
ruby 4.0.6 (2026-07-14 revision 03b6d3f889) +PRISM [arm64-darwin25]

$ gem --version
4.0.16

```

`gem`はHomebrewでインストールできます。
フォーミュラ名は`ruby`です。

```console
$ /usr/bin/ruby --version
ruby 2.6.10p210 (2022-04-12 revision 67958) [universal.arm64e-darwin25]

$ /usr/bin/gem --version
3.0.3.1
```

macOSにはデフォルトで`gem`がインストールされています、かなり古いです。
Homebrewを使って最新版を取得しておきます。

```console
$ fish_add_path /opt/homebrew/opt/ruby/bin
```

`fish`の場合、パスを通す必要がありました。
