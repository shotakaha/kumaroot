# WSLしたい（``wsl --install``）

```console
$ wsl --install
インストール中: Linux用Windowsサブシステム
Linux用Windowsサブシステムはインストールされました。
インストール中: Ubuntu
Ubuntuはインストールされました。
要求された操作は正常に終了しました。
変更を有効にするには、システムを再起動する必要があります。
```

PowerShellを起動し``wsl --install``を実行します。
デフォルトでUbuntuがインストールされます。
インストールした後はパソコン自体の再起動が必要です。

再起動したあとにUbuntuを起動します。
初回のみユーザー設定（ユーザー名／パスワード）の設定が必要です。

```console
Ubuntuはすでにインストールされています。
Ubuntuを起動しています。
Installing, this may take a few minutes...

Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers

Enter new UNIX username: #入力
New password: #入力
Retype new password: #再入力

... いろいろ表示

Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.145.1-microsoft-standard-WSL2 x86_64)
```

ユーザー設定が終わり、ログインできたら、パッケージを更新しておきます。

```console
$ sudo apt update
$ sudo apt full-upgrade
```

## インストールできるLinuxをしりたい（``wsl --list --online``）

```console
$ wsl --list --online
インストールできる有効なディストリビューションの一覧を次に示します
NAME        FRIENDLY NAME
Ubuntu    Ubuntu
Debian    Debian GNU/Linux
kali-linux    Kali Linux Rolling
Ubuntu-18.04    Ubuntu 18.04 LTS
Ubuntu-20.04    Ubuntu 20.04 LTS
Ubuntu-22.04    Ubuntu 22.04 LTS
OracleLinux_7_9    Oracle Linux 7.9
OracleLinux_8_7    Oracle Linux 8.7
OracleLinux_9_1    Oracle Linux 9.1
openSUSE-Leap-15.5    openSUSE Leap 15.5
SUSE-Linux-Enterprise-Server-15-SP4    SUSE Linux Enterprise Server 15 SP4
SUSE-Linux-Enterprise-15-SP5    SUSE Linux Enterprise 15 SP5
openSUSE-Tumbleweed    openSUSE Tumbleweed
```

## AlmaLinuxしたい

```console
$ winget search almalinux
// インストールしたいバージョンのIDを確認する
$ winget install <ID>
```

Alma Linux は上記のリストにないですが、``winget``でインストールできます。
インストール後に再起動が必要なことと、初回起動時にユーザー設定をすることはUbuntuのと同じです。
パッケージ管理は``dnf``を使います。

```console
$ dnf check-update
$ dnf upgrade
```

## リファレンス

- [WSLを使用してWindowsにLinuxをインストールする方法 - MS Learn](https://learn.microsoft.com/ja-jp/windows/wsl/install)
