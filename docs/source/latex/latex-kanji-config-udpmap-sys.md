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
