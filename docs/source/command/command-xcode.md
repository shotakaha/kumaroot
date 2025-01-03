# Xcodeしたい（`xcode-select`）

```console
$ xcode-select --print-path
/Applications/Xcode.app/Contents/Developer

$ xcode-select --version
xcode-select version 2408.
```

`xcode-select`はXcodeの開発ツールやコマンドラインツールを管理するコマンドです。
`--print-path`や`--version`オプションでで現在利用している情報を確認できます。

```console
$ xcode-select --install
```

`--install`オプションでコマンドラインツールをインストールできます。
`Xcode.app`本体をインストールする容量が確保できない場合、
この`Command Line Tools`のみをインストールすることもできます。
SDKsは`/Library/Developer/CommandLineTools/`の中に追加されます。

```console
$ clang --version
Apple clang version 16.0.0 (clang-1600.0.26.6)
Target: arm64-apple-darwin23.6.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
```

`Command Line Tools`をインストールすると`clang`や`git`などが使えるようになります。
