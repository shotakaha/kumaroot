# イベント一覧がほしい（``G4Run::EventVector``）

```cpp
// G4Run *aRun
auto events = aRun->GetEventVector();
```

ランの含まれるすべての``G4Event``を取得できます。
返り値は``std::vector<const G4Event>``型ですが、
型名が長いので`auto`でもらうのがよいと思います。
