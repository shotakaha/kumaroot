# ECMAScriptのバージョン

| ECMAScript | 通称 | V8エンジン | Node.js |
| --- | --- | --- |
| (1999) | ES3 | | |
| (2009) | ES5 | v3.19 (2012) | |
| ES2015 | ES6 | v4.9 (2013) | 4.x - 6.x |
| ES2016 | ES7 | v5.1 (2016) | 6.x - 8.x |
| ES2017 | ES8 | v5.8 (2017) | 8.x - 10.x |
| ES2018 | ES9 | v6.6 (2018) | 10.x - 12.x |
| ES2019 | ES10 | v7.1 (2019) | 12.x - 14.x |
| ES2020 | ES11 | v8.0 (2020) | 14.x - 16.x |
| ES2021 | ES12 | v8.7 (2021) | 16.x - 18.x |
| ES2022 | ES13 | v9.1 (2022) | 18.x - 20.x |

ECMAScriptは、ECMA（エクマ；European Computer Manufacturers Association）によって策定される言語仕様です。
ES2015以降、毎年6月に新しいバージョンがリリースされています。

ECMAScriptの正式名（ES20xx）と通称（ESx）で番号が1つずれているので、
解説記事などを読むときに注意が必要です。

:::{note}

JavaScriptは、ECMAScriptの実装例のひとつです。
他にもMozillaのSpiderMonkeyやAppleのJavaScriptCoreなどがあります。

:::

V8エンジンはGoogleが中心となって開発しているJavaScript／WebAssemblyのランタイム環境です。
ECMAScriptの最新版に追随する形で、随時機能追加されているようです。

:::{note}

Node.jsはV8を搭載したサーバー向けランタイムです。
GAS環境と比べて、こちらがよく使われます。
他にも、DenoやBunなど、Node.jsと同様にサーバー向けに使えるECMASCriptランタイムがあります。

:::

## リファレンス

- [V8 Runtime Overview](https://developers.google.com/apps-script/guides/v8-runtime)
