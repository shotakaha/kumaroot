# SSH鍵したい（``ssh-keygen``）

```console
$ ssh-keygen -l
Enter file in which the key is (~/.ssh/id_ed25519):
```

``ssh-keygen``コマンドで、SSH鍵（公開鍵と秘密鍵のペア）を操作できます。
``-l``オプションでSSH鍵のフィンガープリントなどを確認できます。
すでにSSH鍵を作成したことがあるかどうか、どういう鍵を生成したのか、
などを確認したいときに、まず使ってみるとよいと思います。

## SSH鍵ペアを作りたい

```console
$ ssh-keygen -t ed25519 -C "コメント"
$ ssh-keygen -t ed25519 -C "メールアドレス (パソコンの名前)"
```

``ssh-keygen``コマンドでSSH鍵ペアを作成できます。
`-t`オプションで暗号化アルゴリズムを指定、
`-C`オプションでコメントを指定できます。
SSH鍵ペアは``~/.ssh/``に生成されます。

ファイル名に``.pub``がついているのが**公開鍵**、ついていないのが**秘密鍵**です。
各種サービスの認証に登録するのは必ず**公開鍵**です。
秘密鍵は絶対に誰にも渡してはいけないデータです。
もし、秘密鍵が漏洩してしまった場合は、その端末のSSH鍵を再作成したり、
外部に登録した公開鍵を削除したりする必要があります。

:::{hint}

職場と自宅で別々の端末を利用するなど、ひとりで複数の端末を所有している場合もあると思います。
その場合、端末同士は**別人**と考えて、端末ごとにSSH鍵ペアを生成し、各種サービスに公開鍵を登録すればOKです。
ある端末で作成したSSH鍵ペアを、別の端末で使い回すのは意味がありません。

:::

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

`-t`オプションで暗号化アルゴリズムを変更できます。
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

``-b``オプションで暗号鍵の長さ（＝ビット数）を変更できます。
それぞれの暗号化アルゴリズムの長さの推奨値を載せておきます。

## 秘密鍵をキーチェーンに登録したい（``ssh-add``）

```console
// 秘密鍵を登録する
$ ssh-add --apple-use-keychain ~/.ssh/id_ed25519（秘密鍵）
Identity added: 鍵のパス

// 登録を確認する
$ ssh-add -l
256 SHA256:鍵情報 (ED25519)
```

``ssh-add``コマンドを使って、秘密鍵を利用している端末の``ssh-agent``に登録できます。
``ssh-agent``に登録すると、SSH鍵を使うときのマスターパスワード入力を省略できます。
``ssh-add -l``で登録してある鍵の情報を確認できます。

:::{note}

GitHubなどを公開鍵認証にしていると、プッシュするたびにSSH鍵のマスターパスワードの入力が必要です。
SSHエージェントに登録しておくと、その入力が省略できます。

:::

## 公開鍵をリモートサーバ登録したい（``ssh-copy-id``）

```console
// 公開鍵をリモートサーバに登録する
$ ssh-copy-id -i ~/.ssh/id_ed25519.pub アカウント名@リモートサーバ
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "~/.ssh/id_ed25519.pub"
...（省略）...
アカウント名@リモートサーバ's password:    ## リモートサーバのログインパスワードを入力

Number of key(s) added:        1
...（省略）...
```

``ssh-copy-id``コマンドを使って、SSH公開鍵をリモートサーバに登録できます。
ひとつのリモートサーバに対して複数の公開鍵を登録できます。
職場と自宅で別々の端末を使っている場合は、端末ごとの公開鍵を登録できます。

```console
// すでに登録されている公開鍵を、追加しようとした場合
$ ssh-copy-id -i ~/.ssh/id_ed25519.pub アカウント名@リモートサーバ
...（省略）...
/usr/bin/ssh-copy-id: WARNING: All keys were skipped because they already exist on the remote system.
(if you think this is a mistake, you may want to use -f option)
```

公開鍵がすでに登録されている場合は、エラーを表示して教えてくれます。

## 公開鍵を外部サービスに登録したい

```console
// 公開鍵の内容をコピーする
$ cat ~/.ssh/id_ed25519.pub（公開鍵） | pbcopy
```

外部サービスには、SSH鍵ペアの**公開鍵を登録**してユーザー認証できるものがあります。
その際、手順のどこかで「公開鍵のコピー」が必要です。
ターミナルに表示して、マウスでドラグしてコピーしてもいいのですが、
余計な文字（空白や改行など）をうっかり含めてしまわないか心配です。

そのときは[pbcopy](./command-pbcopy.md)が便利です（macOSのみ）。
（Linuxでは`xclip`コマンドでできるそうです）

:::{note}

GitLabやGitHubなどのサービスでは、具体的な手順を記したページがあります。
それぞれのサービスのヘルプを参照してください。

- [GitHubアカウントへの新しいSSHキーの追加 - GiHub Docs](https://docs.github.com/ja/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
- [SSHキーを使ってGitLabと通信します - GitLab日本語マニュアル（クリエーションライン株式会社）](https://gitlab-docs.creationline.com/ee/user/ssh.html)
::

