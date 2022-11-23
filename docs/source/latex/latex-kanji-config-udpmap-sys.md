# 和文フォントを設定したい（``kanji-config-udpmap-sys``）

```bash
$ kanji-config-udpmap-sys [オプション] フォント名
```

(u)pLaTeXの場合、``kanji-config-udpmap-sys``コマンドを使って、システム全体の和文フォントを変更できます。
詳細は``texdoc kanji-config-udpmap``してドキュメントを参照してください。

```{note}
TeX Live 2020以降は和文デフォルトが原ノ味フォントになっているため、わざわざ変更する必要はないかなと思っています。
```

## 現在の設定を確認したい

```bash
$ kanji-config-updmap-sys --ja status
Cannot find ptex-fontmaps-macos-data.dat, skipping!
CURRENT family for ja: haranoaji (variant: -04)
Standby family : haranoaji
Standby family : ipa
Standby family : ipaex
```

日本語（``--ja``）、簡体中国語（``--sc``）、繁体中国語（``--tc``）、韓国語（``--ko``）に設定されているフォントを確認できます。
日本語には[原の味フォント](https://github.com/trueroad/HaranoAjiFonts)が使われていることが分かります。

## フォントを変更したい

```bash
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
``kanji-config-udpmap-sys``はデフォルトで**JIS90字系**を選択するため、``--jis2004``オプションを追加しています。
