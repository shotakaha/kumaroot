# ひとり認証局したい（``mkcert``）

```bash
$ brew install mkcert
$ mkcert --version
v1.4.4
```

ローカルのウェブ開発で``https``を使いたい場合に、SSLの自己証明書（いわゆる「オレオレ証明書」）を作成する必要があります。
``mkcert``コマンドを使うと、簡単にローカル認証局を作成できます。

## ローカル認証局を登録する（``-install``）

```bash
$ mkcert -install
```
自分のパソコン（＝システム）のトラストストアにローカル認証局を登録します。
この認証局を使って、ローカル開発用の証明書を認証できるようになります。

登録されているルート認証局は``Keychain Access.app``で確認（``System Keychains`` -> ``System Roots`` -> ``Certificates``）できます。
