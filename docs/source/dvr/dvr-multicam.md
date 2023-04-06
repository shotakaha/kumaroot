# マルチカメラ編集したい

ATEM Miniを使ってISO録画したり、複数のカメラで同時に撮影したりしたプロジェクトを**マルチカム編集**できます。
ここでは、マルチカム編集可能なタイムラインの作成方法と切り替え方を整理します。

## マルチカムクリップを作成したい

0. ``Edit``ページで作業します
1. クリップを``メディアプール``に読み込みます
2. 同期させたいクリップをすべて選択し、``右クリック`` -> ``Create New Multicam Clip Using Selected Bin ...``を選択します
3. ``New Multicam Clip``のダイアログに必要な情報を入力します

Start Timecode（開始タイムコード）
: マルチカムクリップの開始タイムコードです。
  デフォルトの値（``01:00:00:00``）でOKです。

Multicam Clip Name（マルチカムクリップ名）
: クリップ名を入力します。名前は自由に指定できます。僕や``multicam``をよく使います。

Frame Rate（フレームレート）
: 選択したクリップに関連するフレームレートが自動的にリストされます。
  ドロップダウンリストから選択します。

Drop Frame:

Angle Sync（アングルの同期）
: すべてのアングルを同期させる基準を選択します。
  ``[In/Out]``は各クリップに設定したイン点／アウト点を使用します。ATEM MiniでISO収録したクリップは``[In]``を選択すればよいと思います。
  ``[Sound]``は各クリップのオーディオ波形を使用します。複数台のカメラで個別収録したクリップは、この方法を選択するとよいかもしれません。

Angle Name（アングル名）
: マルチカムクリップのアングル名を作成する方法を選択します。
  ``[Sequential]``でOKです。

Detect Clips from Same Camera（同じカメラのクリップを検出）
: 同じカメラで撮影したクリップを検出する場合は、チェックボックスをONにします。
  検出方法は``Detect using:``から選択します。

Move Source Clips to "Original Clips' Bin"
: マルチカムクリップの作成に使ったクリップを``Original Clips' Bin``に移動します。
  （たぶん）デフォルトのままONでいいのだと思います。




## タイムラインを作成したい

## カメラを切り替えたい