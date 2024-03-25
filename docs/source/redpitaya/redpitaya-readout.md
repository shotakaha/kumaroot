# データを読み出したい

```python
def single_daq_readout():

    channels = [rp.RP_CH_1, rp.RP_CH_2]
    N = 16384

    # データを保存するための辞書型オブジェクト
    wv = {}
    for ich in channels:

        # RAW
        ibuff = rp.i16Buffer(N)
        res = rp.rp_AcqGetOldestDataRaw(ich, N, ibuff.cast())

        # Volts
        fbuff = rp.fBuffer(N)
        res = rp.rp_AcqGetDataV(ich, N, fbuff)

        # Get data
        data_raw = np.zeros(N, dtype=int)
        data_volts = np.zeros(N, dtype=float)

        for i in range(0, N):
            data_raw[i] = ibuff[i]
            data_volts[i] = fbuff[i]

        wv[f"raw{ich+1}"] = data_raw
        wv[f"v{ich+1}"] = data_volts

    # wvの内容
    # wv = {
    #    "raw1": [...],
    #    "v1": [...],
    #    "raw2": [...],
    #    "v2": [...],
    #    }

    # pd.DataFrameに変換する
    waves = pd.DataFrame.from_dict(wv, orient="index")
    # or
    # waves = pd.DataFrame(wv.values(), index=wv.keys()).T

    return waves
```

トリガーにかかった波形データを読み出すために必要な要素をサンプルコードから抜粋してみました。
波形データは``RAW``形式（＝ADC値）と電圧値で読み出すことができます。
が、正直、どういうオブジェクトで読み出されているのかよく分かりません。

``ibuff``、``fbuff``はそのままではどうにもできないので、
``for``ループを使ってバッファーサイズの大きさの``numpy``配列に移し替えています。
``numpy``配列にしておけば、``dict``や``pd.DataFrame``にも簡単に変換できます。

## リファレンス

- [Triggering with a threshold on channel](https://redpitaya.readthedocs.io/en/latest/appsFeatures/examples/acquisition/acqRF-exm1.html)
