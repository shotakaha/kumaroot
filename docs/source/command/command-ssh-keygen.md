# SSH鍵したい（``ssh-keygen``）

SSH鍵（公開鍵と秘密鍵のペア）を生成するコマンドです。

```console
$ ssh-keygen -t ed25519 -C "コメント"
$ ssh-keygen -t ed25519 -C "メールアドレス (パソコンの名前)"
```

SSH鍵のペアは``~/.ssh/``に生成されます。
ファイル名に``.pub``がついているのが**公開鍵**、ついていないのが**秘密鍵**です。
各種サービスの認証に登録するのは必ず**公開鍵**です。
秘密鍵は誰にも渡してはいけないデータです。

ひとりで複数の端末を所有している場合でも、それぞれの端末同士は**赤の他人**と考え、端末ごとにSSH鍵のペアを生成するのがよいです。

## 暗号化アルゴリズムを指定したい（``-t``）

```console
// RSA鍵
$ ssh-keygen
id_rsa
id_rsa.pub

// DSA鍵（1024ビット推奨）
$ ssh-keygen -t dsa
id_dsa
id_dsa.pub

// ECDSA鍵（256ビット推奨）
$ ssh-keygen -t ecdsa
id_ecdsa
id_ecdsa.pub

// EdCSA鍵（256ビット推奨）
$ ssh-keygen -t ed25519
id_ed25519
id_ed25519.pub
```

暗号化アルゴリズムは``rsa`` / ``dsa`` / ``ecdsa`` / ``ed25519`` の4種類から選択できます。
デフォルトは``rsa``となっています。
サービスが``EdDSA``に対応しているなら``ed25519``を選択するのがよいと思います。
指定した暗号化アルゴリズム別にSSH鍵が{file}`~/.ssh/`に生成されます。

## 鍵の長さを指定したい（``-b``）

```console
// RSA鍵（2048ビット以上推奨）
$ ssh-keygen -b 4096

// DSA鍵（1024ビット推奨）
$ ssh-keygen -t dsa -b 1024

// ECDSA鍵（256ビット推奨）
$ ssh-keygen -t ecdsa -b 256

// EdCSA鍵（256ビット推奨）
$ ssh-keygen -t ed25519 -b 256
```

``-b``オプションを使って暗号鍵の長さ（＝ビット数）を指定できます。
それぞれの暗号化アルゴリズムの長さの推奨値を載せておきます。

## SSH鍵を登録したい（``ssh-add``）

```console
// 秘密鍵を登録する
$ ssh-add --apple-use-keychain ~/.ssh/id_ed25519
Identity added: 鍵のパス

// 登録を確認する
$ ssh-add -l
256 SHA256:鍵情報 (ED25519)
```

``ssh-agent``に登録することで、SSH鍵を使うときのマスターパスワード入力を省略できます。
``ssh-add -l``で登録してある鍵の情報を確認できます。

:::{seealso}

GitLabとGitHubはSSH鍵を登録してユーザー認証できます。
SSH鍵を登録する方法はそれぞれのサービスのヘルプなどを参照してください。
公開鍵をコピーする場合は[pbcopy](./command-pbcopy.md)を使うと便利です。

:::
