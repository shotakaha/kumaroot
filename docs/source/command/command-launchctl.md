# launchctl

定期的にスクリプトを実行するためのコマンドです。
``macOS``では、``contab``より``launchd``が推奨されています。
設定は``plist``（property list）というXML形式で記述します。

## ファイル置き場

1. {file}``~/Library/LaunchAgents/ラベル.plist``
1. {file}``/Library/LaunchAgents/ラベル.plist``
1. {file}``/Library/LaunchDaemons/ラベル.plist``

``plist``ファイルは上記のいずれかに作成します。
それぞれ実行者が異なりますが、一般ユーザーならば最初のパスでOKです。

## plistの書き方

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

## 定期実行したい（``StartCalendarInterval``）

```xml
<key>StartCalendarInterval</key>
<dict>
    <key>Minutes</key>
    <integer>20</integer>
    <key>Hour</key>
    <integer>13</integer>
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
ログは永遠に残っていなくてもよいと考え、僕は``/tmp/``に保存しています。

## リファレンス

- [Creating Launch Daemons and Agents - Apple Developer](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html)
