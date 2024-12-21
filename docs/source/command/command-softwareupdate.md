# macOSの更新を確認したい（`softwareupdate`）

```console
$ softwareupdate --list

Software Update Tool

Finding available software
Software Update found the following new or updated software:
* Label: Safari18.2SonomaAuto-18.2
    Title: Safari, Version: 18.2, Size: 179043KiB, Recommended: YES,
* Label: Command Line Tools for Xcode-16.2
    Title: Command Line Tools for Xcode, Version: 16.2, Size: 751786KiB, Recommended: YES,
* Label: macOS Sonoma 14.7.2-23H311
    Title: macOS Sonoma 14.7.2, Version: 14.7.2, Size: 1727102KiB, Recommended: YES, Action: restart,
* Label: macOS Sequoia 15.2-24C101
    Title: macOS Sequoia 15.2, Version: 15.2, Size: 7300295KiB, Recommended: YES, Action: restart,
```

`softwareupdate`コマンドで、macOSの更新を確認できます。
`System Settings` → `General` → `Software Update`で確認できる内容と同じです。
