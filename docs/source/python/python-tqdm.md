# 進捗バーしたい（``tqdm``）

```python
from tqdm import tqdm

for i in tqdm(range(3)):
   time.sleep(1)

100%|██████████| 3/3 [00:03<00:00,  1.00s/it]
```

``tqdm``パッケージを使って、ループ処理中の進捗バーを表示できます。
使い方がとても簡単で、イテラブルな変数を``tqdm(イテラブル)``の中にいれるだけです。
大きなループを回すときに設定すると、動作していることがぱっと見てわかるため安心です。

## 説明したい

```python
for i in tqdm(range(3), desc="進行状況):
    time.sleep(1)

進行状況: 100%|██████████| 3/3 [00:03<00:00,  1.00s/it]
```

``desc``オプションで、進捗バーのプレフィックスを変更できます。
ネストしたループで使うと、どのループにいるのか分かりやすくなります。

## 表示幅を変更したい

```python
for i in tqdm(range(10), ncols=80)
```

``ncols``オプションで、表示幅を変更できます。
デフォルトはターミナルの幅に合わせるようになっています。
ターミナルの大きさを途中で変更すると表示が崩れる場合があるので、
幅の上限値は指定しておくとよいと思います。

## rangeしたい（``tqdm.trange``）

```python
from tqdm import trange

for i in trange(10000):
    time.sleep(1)
```

`trange`は`tqdm(range)`を省略した形です。
少しだけタイピング量が減らせます。

## pandasしたい（``tqdm.pandas``）

```python
from tqdm import tqdm

tqdm.pandas(desc="プログレスバーの説明")
data.progress_apply(処理)
```

Pandasデータフレームに対する処理も進捗バーを表示できます。
``tqdm.pandas``を呼ぶことで、
``map``メソッド相当の``progress_map``、
``apply``メソッド相当の``progress_apply``が使えるようになります。

## ノートブックしたい（``tqdm.notebook``）

```python
from tqdm.notebook import tqdm

for i in tqdm(range(10)):
    time.sleep(1)
```

Jupyter Notebookで使う場合は``tqdm.notebook``を使うと、表示がおしゃれになります。

## リファレンス

- [tqdm documentation](https://tqdm.github.io/)
