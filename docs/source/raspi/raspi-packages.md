```{tags} raspi, apt
```

# パッケージ管理したい（`apt`）

Raspberry Piではパッケージマネージャー`apt`を使用してソフトウェアをインストール・管理します。

## パッケージリストを更新したい

```bash
sudo apt update
```

パッケージリストを更新して、最新のパッケージ情報を取得します。
他のコマンドを実行する前に実行することが推奨されます。

## 初回アップグレードしたい

```bash
sudo apt update
sudo apt full-upgrade
```

初回起動後は`full-upgrade`でシステム全体をアップグレードします。
`full-upgrade`は`upgrade`より多くのパッケージを更新し、古いパッケージを削除することもあります。

## 定期的に更新したい

```bash
sudo apt update
sudo apt upgrade
```

定期的なセキュリティアップデートには`upgrade`を使用します。
`upgrade`は依存関係に影響しないパッケージのみを更新します。

## パッケージを検索したい

```bash
apt-cache search <パッケージ名>
apt-cache search <キーワード>
```

リポジトリ内で利用可能なパッケージを検索できます。

**パッケージの詳細情報を確認：**

```bash
apt-cache show <パッケージ名>
```

## パッケージをインストールしたい

```bash
sudo apt install <パッケージ名>
```

単一パッケージをインストール：

```bash
sudo apt install vim
```

複数パッケージを一度にインストール：

```bash
sudo apt install vim git curl
```

## パッケージを削除したい

```bash
sudo apt remove <パッケージ名>
```

パッケージを削除します。設定ファイルは保持されます。

**設定ファイルも含めて削除：**

```bash
sudo apt purge <パッケージ名>
```

## 不要なパッケージを削除したい

```bash
sudo apt autoremove
```

依存関係がなくなったパッケージを自動削除します。

## パッケージのバージョンを固定したい

```bash
sudo apt-mark hold <パッケージ名>
```

パッケージのアップデートを防ぎます。

**固定を解除：**

```bash
sudo apt-mark unhold <パッケージ名>
```

## 推奨パッケージしたい

個人的に推奨する開発ツールやユーティリティです。

```bash
# Rustで書かれた高速コマンドラインツール
sudo apt install ripgrep
sudo apt install bat
sudo apt install fd-find
sudo apt install lsd

# その他のユーティリティ
sudo apt install tealdeer        # manコマンドの簡潔版
sudo apt install fish            # ユーザーフレンドリーなシェル
sudo apt install vim             # テキストエディタ
sudo apt install code            # Visual Studio Code
```

**Rust代替コマンドの説明：**

- `ripgrep` - `grep`の高速な代替（正規表現検索）
- `bat` - `cat`の改良版（構文ハイライト付き）
- `fd-find` - `find`の高速な代替（ファイル検索）
- `lsd` - `ls`の改良版（カラー表示＆ツリー表示）

## Python開発環境をセットアップしたい

```bash
sudo apt install python3-pip python3-venv python3-dev
```

Pythonの基本的な開発ツールをインストール：

- `python3-pip` - パッケージマネージャー
- `python3-venv` - 仮想環境作成ツール
- `python3-dev` - Python開発用ヘッダーファイル

**さらに高度な環境構築：**

```bash
sudo apt install pipx
```

`pipx`を使うと、Pythonツールをシステム全体に影響を与えずにインストールできます。

詳細は[Python環境構築](../python/)を参照してください。

## SSHサーバーをインストールしたい

```bash
sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
```

SSHサーバーをインストールして有効化します。

詳細は[SSH設定](raspi-ssh.md)を参照してください。

## キャッシュをクリアしたい

```bash
sudo apt clean
```

ダウンロード済みのパッケージキャッシュを削除してディスク容量を解放します。

**より積極的にクリア：**

```bash
sudo apt autoclean
```

不要になったパッケージのキャッシュのみを削除します。

## アップグレード時の問題をデバッグしたい

```bash
# 依存関係の問題を確認
sudo apt check

# 設定ファイルの差分を表示
sudo apt install -s <パッケージ名>
```

`-s`（シミュレーション）オプションで、実際に変更を加えずに動作を確認できます。

## リファレンス

- [Debian Package Management](https://wiki.debian.org/PackageManagement)
- [apt Manual](https://manpages.debian.org/apt)
- [Raspberry Pi Official Documentation](https://www.raspberrypi.com/documentation/)
