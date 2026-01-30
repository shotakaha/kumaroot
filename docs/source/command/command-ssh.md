# SSH接続したい（`ssh`）

```console
$ ssh ユーザー名@接続先ホスト名
$ ssh 接続先ホスト名 -l ユーザー名
```

`ssh`はリモートサーバーに安全にログインして操作するためのコマンドです。
ユーザー名とホスト名を指定してログインします。通信は暗号化されます。

接続元と接続先でユーザー名が同じ場合、ユーザー名の指定を省略できます。
また、設定ファイル（`~/.ssh/config`）に接続情報やエイリアスを保存できます。

## 秘密鍵したい（`ssh -i`）

```console
$ ssh -i ~/.ssh/id_ed25519 ユーザー名@接続先ホスト名
```

`-i`オプションで秘密鍵のパスを変更できます。
サーバーごとに秘密鍵を使い分けている場合に使用するオプションです。

管理している端末と鍵が多い場合には、
それぞれ`IdentityFile`を設定しておくと便利です。

```unixconfig
Host *
    AddKeysToAgent yes    # 秘密鍵をssh-agentに自動登録
    UseKeychain yes       # パスフレーズをkeychainに保存（macOSのみ）

Host github
    IdentityFile ~/.ssh/id_ed25519_github    # 秘密鍵のパス
    IdentitiesOnly yes    # 指定した鍵だけを使用

Host gitlab
    IdentityFile ~/.ssh/id_ed25519_gitlab    # 秘密鍵のパス
    IdentitiesOnly yes    # 指定した鍵だけを使用
```

このサンプルは、GitHubとGitLabで別々の秘密鍵を想定しています。

:::{note}

`IdentitiesOnly`は`IdentityFile`で指定した鍵のみを使って認証するためのオプションです。
SSHはデフォルトで、ssh-agentに登録されている鍵や、デフォルト鍵など、
利用可能な手持ちの鍵をすべて順番に試す挙動となっています。

`IdentitiesOnly yes`の設定は必須ではありませんが、
使用する鍵を明示的に制御したい場合や、
セキュリティ・安定性を重視する場合には有効にするとよい設定です。

:::

## エイリアスを設定したい（`~/.ssh/config`）

```unixconfig
# ~/.ssh/config
Host aliasname    # エイリアス名
HostName host.example.com  # ホスト名
User example   # ログイン名
```

SSH接続の設定は`~/.ssh/config`で変更できます。
頻繁にログインするサーバーは「エイリアス」を設定しておくとよいです。
エイリアスを設定すると、好きな名前でSSH接続できます。
ログイン先のサーバー名が長い場合は、打ち間違いを少なくできます。
また、ローカルPCの名とリモート環境のログインユーザー名が異なる場合も、この設定で吸収できます。

## 一時的に設定したい（`ssh -o`）

```console
$ ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no ユーザー@ホスト名
Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
```

`-o`オプションで、設定ファイルのオプションを一時的に上書きできます。
上記サンプルは、パスワード認証をOFFにしたサーバーに対して、
パスワード認証でログインできないことを確認したときのコマンドです。
パスワード認証を優先させて、念のために公開鍵認証も無効にして、ログインできないことを確認しています。
