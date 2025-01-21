# 和文フォントしたい（``kanji-config-udpmap-sys``）

:::{note}

これは2011年ころの(u)pLaTeXで必要だった設定です。
TeX Live 2020以降は和文のデフォルトが原ノ味フォントになっているため、わざわざ変更する必要はないと思います。

:::

```console
$ kanji-config-udpmap-sys [オプション] フォント名
```

`kanji-config-udpmap-sys`コマンドで、システム全体の和文フォントを変更できます。
詳細はドキュメントを参照してください（`texdoc kanji-config-udpmap`）。

## 設定を確認したい（`status`）

```console
$ kanji-config-updmap-sys --ja status
Cannot find ptex-fontmaps-macos-data.dat, skipping!
CURRENT family for ja: haranoaji (variant: -04)
Standby family : haranoaji
Standby family : ipa
Standby family : ipaex
```

日本語（`--ja`）、
簡体中国語（`--sc`）、
繁体中国語（`--tc`）、
韓国語（`--ko`）
に設定されているフォントを確認できます。
日本語には[原の味フォント](https://github.com/trueroad/HaranoAjiFonts)が使われていることが分かります。

## フォントを変更したい

```console
$ kanji-config-updmap-sys -n --ja haranoaji --jis2004
Cannot find ptex-fontmaps-macos-data.dat, skipping!
Setting up ... haranoaji for ja
updmap --quiet --nomkmap --nohash --setoption jaEmbed haranoaji
updmap --quiet --nomkmap --nohash --setoption jaVariant -04
updmap
```

```{note}
`-n`をつけてドライランモードで確かめています。
```

フォントには**JIS90字系**と**JIS2004字系**があります。
フォントセットによりますが、原の味フォントは両方の字系セットに対応しています。
`kanji-config-udpmap-sys`はデフォルトで**JIS90字系**を選択するため、`--jis2004`オプションを追加しています。
