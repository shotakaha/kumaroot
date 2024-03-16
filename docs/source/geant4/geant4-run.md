# ランしたい（``G4Run``）

```cpp
aRun->GetNumberOfEvents()
```

[G4Run](https://geant4.kek.jp/Reference/11.2.0/classG4Run.html)はラン情報を管理するクラスです。
ユーザーアクション設定の``RunAction``や``EventAction``から情報を取得したいときに使います。

## ラン番号をしりたい（``GetRunID``）

```cpp
G4int run_id = aRun->GetRunID();
```

## イベント数をしりたい（``GetNumberOfEvents``）

```cpp
G4int n_events = aRun->GetNumberOfEvents();
```

ランのイベント数を取得できます。
イベントがないランはスキップできます。

```cpp
G4int n_events = aRun->GetNumberOfEvents();
if (n_events == 0 ) return;
```

## イベント一覧がほしい（``GetEventVector``）

```cpp
auto events = aRun->GetEventVector();
```
