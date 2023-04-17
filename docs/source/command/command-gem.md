# Rubyしたい（``gem``）

```console
$ brew install ruby
$ fish_add_path /opt/homebrew/opt/ruby/bin
```

``gem``はRubyのパッケージを管理するコマンドです。
（Pythonの``pip``、Nodeの``npm``に相当するイメージです）。
macOSにはデフォルトで``gem``がインストールされていますが、Homebrewを使って最新版を取得しておきます。
``gem``というフォーミュラはないので、``ruby``をインストールします。

``fish``の場合、パスを通す必要がありました。

```console
$ gem install パッケージ名
```
