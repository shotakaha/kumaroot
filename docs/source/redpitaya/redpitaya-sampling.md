# サンプリングレートしたい（``rp_AcqGetSamplingRateHz``）

```python
import rp
sampling_rate = rp.rp_AcqGetSamplingRateHz()
sampling_interval = 1./sampling_rate
```

``rp_AcqGetSamplingRateHz``で、サンプリングレートを確認できます。

サンプリングレートを設定するためのコマンドは存在しないようです。
代わりに``rp_AcqSetDecimationFactor``を使ってデシメーションを設定することで、サンプリングレートを変更できます。

デシメーションが``1``の場合、サンプリングレートは``125 MHz``となり、時間の目盛間隔は``8 ns``です。

## リファレンス

- [Sampling rate and decimations](https://redpitaya.readthedocs.io/en/latest/appsFeatures/examples/acquisition/acqRF-samp-and-dec.html)
