# launchctl

```bash
$ launchctl load ~/Library/LaunchAgents/ラベル.plist
$ launchctl unload ~/Library/LaunchAgents/ラベル.plist
```

定期的に実行したいスクリプトを``launchd``に登録するコマンドです。
設定は``plist``（property list）というXML形式で作成します。
``macOS``では、``contab``より``launchd``が推奨されています。

## ロードされているプロセスを確認したい

```bash
$ launchctl list | rg ラベル名
```

ロードされているプロセスの``PID``、``Status``、``Label``がずらーっと表示されます。
``grep``や``rg``などの検索コマンドにパイプして使うことが多いです。

## カスタムのplistを作成したい

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
        <key>キー</key>
        <string>値</string>
</dict>
</plist>
```

``plist``は、最初にXMLとDTDの宣言が必要です。
内容は、基本的にはキーと値のペアで記述します。
値には``<array>``や``<dict>``などを使うことができます。
詳しくはドキュメントを参照することをオススメします。

### ファイル置き場

1. {file}``~/Library/LaunchAgents/ラベル.plist``（ユーザーごと）
1. {file}``/Library/LaunchAgents/ラベル.plist``（ユーザーごと；sudoが必要）
1. {file}``/Library/LaunchDaemons/ラベル.plist``（システム全体；sudoが必要）

``plist``ファイルは上記のいずれかに作成します。
``LaunchDaemons``はシステム全体、``LaunchAgents``はユーザーに紐づいています。
基本的には、最初のパスに作成すればOKです。

## ラベルを作りたい（``Label``）

```xml
<key>Label</key>
<string>ラベル名</string>
```

ファイル名につける``ラベル``は、すでに存在している``plist``ファイルを参照して命名するとよいと思います。
たとえば``AdobeCC``に関係するファイルは``com.adobe.AdobeCreativeCloud.plist``となっています。
これに倣って、僕は``local.スクリプト名.plist``としています。

## スクリプトを指定したい（``ProgramArguments``）

```xml
<key>ProgramArguments</key>
<array>
    <string>実行したい/スクリプト/の/絶対/パス</string>
    <string>スクリプトのオプション</string>
    <string>スクリプトの引数</string>
</array>
```

実行するスクリプトは``ProgramArguments``で設定できます。
コマンドラインに打ち込む内容を、オプションや引数を含めて``array``の形式で並べて記述します。
複雑な内容を書くのは大変なので、別途シェルスクリプトなどにまとめておくのがよいと思います。

## ``KeepAlive``

```xml
<key>KeepAlive</key>
<true/>
```

## 定期実行したい（``StartCalendarInterval``）

```xml
<key>StartCalendarInterval</key>
<dict>
    <key>Minutes</key>
    <integer>20</integer>
    <key>Hour</key>
    <integer>13</integer>
    <key>Day</key>
    <integer>3</integer>
</dict>
```

日時を指定して定期実行したい場合は``StartCalendarInterval``を使って設定します。
頻度のキーとして``Minute``、``Hour``、``Day``、``Weekday``、``Month``があります。
毎週実行したい場合は、``Weekday``に0から7の値を指定します（0と7は日曜日に相当）。

実行した時刻を起点に定期実行する場合は``StartInterval``を使います。

## 環境変数を設定したい（``EnvironmentVariables``）

```xml
<key>EnvironmentVariables</key>
<dict>
    <key>PATH</key>
    <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
</dict>
```

## 実行ログを残したい（``StandardOutPath`` / ``StandardErrorPath``）

```xml
<key>StandardOutPath</key>
<string>/tmp/ラベル.stdout</string>
<key>StandardErrorPath</key>
<string>/tmp/ラベル.stderr</string>
```

定期実行した結果はファイルに保存できます。
``StandardOutPath``は標準出力、``StandardErrorPath``は標準エラー出力を保存するファイル名を指定します。
ログはずっと残っていなくてもよいと考えて、僕は``/tmp/``に保存しています。

## リファレンス

- [Creating Launch Daemons and Agents - Apple Developer](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html)
