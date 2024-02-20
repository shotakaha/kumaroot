# op

```bash
$ brew install --cask 1password-cli
```

パスワード管理ソフト``1password``を操作するコマンドです。
Homebrew Caskを使ってインストールできます。

## バージョンを確認したい

```bash
$ op --version
2.12.0
```

## サインインしたい

``op``コマンドをはじめて使う場合、まずアカウントのサインインが必要です。
設定は[公式ドキュメント](https://developer.1password.com/docs/cli/get-started/)を参照してください。
ここに書いてある通りに進めるとTouchIDを使って認証できるようになります。

## 保管庫を一覧したい

```bash
$ op vault ls
```
