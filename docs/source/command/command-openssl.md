# SSL証明書したい（`openssl`）

```console
$ openssl version
OpenSSL 3.4.0 22 Oct 2024 (Library: OpenSSL 3.4.0 22 Oct 2024)
```

`openssl`コマンドで、暗号化やSSL/TLS、証明書操作、鍵作成など、
OpenSSLを使ったさまざまな操作ができます。

## 証明書したい（`openssl x509`）

```console
# 証明書を表示
$ openssl x509 -in 証明書.pem -noout -text

# 証明書の有効期限を確認
$ openssl x509 -in 証明書.pem -noout -dates
```

`openssl x509`コマンドで証明書の操作ができます。
`-in`オプションでPEM形式の証明書を指定します。
`-noout`オプションで出力内容に証明書自身を非表示にできます。

:::{note}

**PEM形式**（Privacy Enhanced Mail）は、Base64でエンコードされたテキスト形式で、秘密鍵／公開鍵や証明書、証明書チェーンを保存する汎用的な形式です。
ファイルの内容は
`-----BEGIN`と
`-----END`で囲まれています。

同じPEM形式でも、用途によって次のような拡張子を使用します。

| 用途 | 秘密鍵 | 公開鍵 | ファイル名 |
|---|---|---|---|
| 汎用 | `.key` | `.pem` / `.pub` | |
| SSH公開鍵認証 | `.key` / なし | `.pub` | `id_ed25519` / `id_ed25519.pub` |
| SSL/TLS証明書 | `.key` | `.crt` / `.cer` | `server.key` / `server.crt` |
| 証明書チェーン | `.pem` | `.pem` | |

**X.509証明書** は公開鍵基盤（PKI; Public Key Infrastructure）で使用される標準形式のデジタル証明書です。
サーバー証明書の公開鍵は、Linux環境では`.crt`、Windows環境では`.cer`を利用します。

:::

## CSRしたい（`openssl req`）

```console
$ openssl req -new -key 秘密鍵.key -out CSR証明書.pem
```

`openssl req`コマンドと秘密鍵を使ってCSR証明書を作成できます。

```console
$ openssl req -new -key 秘密鍵.key -out 自己証明書.pem -x509 -nodes -sha256 -days 365
```
