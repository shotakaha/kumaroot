# Xcodeしたい（`xcode-select`）

```console
$ xcode-select --version
xcode-select version 2408.

$ xcode-select --install

$ xcode-select --print-path
/Applications/Xcode.app/Contents/Developer

$ clang --version
Apple clang version 16.0.0 (clang-1600.0.26.6)
Target: arm64-apple-darwin23.6.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
```

`Command Line Tools`をインストールできます。
`clang`や`git`などが使えるようになります。

:::{note}

`Xcode.app`本体をインストールする容量が確保できない場合、この`Command Line Tools`のみをインストールすることもできます。

:::
