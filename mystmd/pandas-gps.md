---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: .venv
  language: python
  name: python3
---

---
title: 位置情報したい（GeoPandas）
---

- [pandas.DataFrameからgeopandas.GeoDataFrameに変換する方法](https://geopandas.org/en/stable/gallery/create_geopandas_from_pandas.html)
- ``pd.DataFrame``で位置情報を扱う場合、``geopandas.GeoDataFrame``に変換が必要です。
- ``geopandas.GeoDataFrame``は``pd.DataFrame``のサブクラスです。
- ``geopandas.points_from_xy(緯度のカラム名、経度のカラム名、高度のカラム名)``を使って、該当カラムを``POINT``オブジェクトに変換します。
- ``POINT``オブジェクトに変換するときに、空間座標系を指定する必要があります。GPSの場合は``EPSG:4326``（地理座標系）にしておけばよいようです。

```{code-cell} ipython3
from pathlib import Path
import pandas as pd
import geopandas as gpd
import geodatasets
import hvplot.pandas

print(f"Pandas: {pd.__version__}")
print(f"GeoPandas: {gpd.__version__}")
print(f"GeoDataSets: {geodatasets.__version__}")
print(f"HvPlot: {hvplot.__version__}")
```

GPSを記録したファイル名を指定します。

```{code-cell} ipython3
read_from = Path("./_static/phyphox/_GPS_2024-04-21_14-00-07/RawData.csv")
read_from.exists()
```

CSVファイルを``pd.DataFrame``として読み込みます。

```{code-cell} ipython3
names = [
    "time",
    "latitude",  # 緯度
    "longitude",  # 経度
    "altitude",  # 高度
    "altitude_wgs84",  # 高度（地理座標系）
    "speed",
    "direction",
    "distance",
    "horizontal_accuracy",
    "vertical_accuracy",
    "satellites",
]

data = pd.read_csv(read_from, names=names, skiprows=1)
len(data)
```

読み込んだデータフレームを確認します。
緯度、経度、高度がただの数値として読み込まれていることが分かります。
このままでも、位置座標としてプロットできます。

```{code-cell} ipython3
data.head()
```

```{code-cell} ipython3
data.hvplot.scatter(x="time", y="latitude")
data.hvplot.scatter(x="time", y="longitude")
data.hvplot.scatter(x="longitude", y="latitude")
```

```{code-cell} ipython3
data.hvplot.scatter(x="altitude", y="altitude_wgs84")
```

経過時間と移動速度をプロットしてみました。
速度が0になっている場所は、新幹線が停止した駅です。

また、ぽつぽつと`370 km/h`に近いピークがありますが、トンネルなどでGPS情報を受信できない状態が続いたあとで、トンネルから抜けた後の地点です。

```{code-cell} ipython3
data["speed_kmh"] = data["speed"] * 3.6
data.hvplot.scatter(x="time", y="speed_kmh", c="altitude")
```

```{code-cell} ipython3
data.hvplot.scatter(
    x="time",
    y="latitude",
)
data.hvplot.errorbars(x="time", y="latitude", yerr1="horizontal_accuracy")
data.hvplot.errorbars(x="time", y="altitude", yerr1="vertical_accuracy", c="speed_kmh")
```

# GeoDataFrameに変換する

- `GeoDataFrame`には`shapely`オブジェクトが必要
- `points_from_xy()`を使って経度／緯度のデータを`shapely.Point`オブジェクトのリストに変換する
- 上で作成したデータを`geometry`に設定する

---

- [geopandas.points_from_xy](https://geopandas.org/en/stable/docs/reference/api/geopandas.points_from_xy.html)
- [EPSG:4326](https://epsg.io/4326) : WGS84 / 地理座標系（緯度経度） / GPSで利用される座標系
  - European Petroleum Survey Group（現在 International Association of Oil & Gas Producers)

```{code-cell} ipython3
gps = gpd.GeoDataFrame(
    data,
    geometry=gpd.points_from_xy(
        data.longitude, data.latitude, data.altitude, crs="EPSG:4326"
    ),
    crs="EPSG:4326",
)
gps
```

``geometry``というカラムが追加されています。

```{code-cell} ipython3
gps.plot()
```

```{code-cell} ipython3
data.plot.scatter(x="longitude", y="latitude", c="altitude")
```

```{code-cell} ipython3
data.plot.scatter(x="longitude", y="latitude", c="time")
```

```{code-cell} ipython3
# nybb = geodatasets.get_path("nybb")
cities = gpd.datasets.get_path("naturalearth_cities")
geo = gpd.read_file(cities)
```

```{code-cell} ipython3
q = "name == 'Tokyo' or name == 'Kyoto'"
geo.query(q).plot()
```

```{code-cell} ipython3
geo.hvplot(tiles="EsriTerrain")
```

```{code-cell} ipython3
import cartopy.crs as ccrs
```

```{code-cell} ipython3
geo.hvplot(
    coastline=True,
    projection=ccrs.Geostationary(central_longitude=-30),
    global_extent=True,
)
```

```{code-cell} ipython3
countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
countries
```

```{code-cell} ipython3
countries.value_counts("continent")
countries.value_counts("name")

q = "name == 'Japan'"
```

```{code-cell} ipython3
import matplotlib.pyplot as plt

fig, axs = plt.subplots()

countries.query(q).plot(ax=axs)
gps.plot.scatter(x="longitude", y="latitude", c="altitude_wgs84", ax=axs)
```
