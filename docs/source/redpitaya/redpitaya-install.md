# インストールしたい（``Red Pitaya OS``）

Red Pitaya OSをmicroSDカードに書き込みます。
使いたいOSのイメージをダンロードして、[balenaEtcher](https://etcher.balena.io/)などのイメージ書き込みソフトを使って、SDカードに書き込みます。

イメージを書き込んだmicroSDカードをRed Pitayaに差しこんで、電源をONにしたらインストールは完了です。

## タイムゾーンを設定する（``dpkg-reconfigure tzdata``）

```console
$ ssh rp-xxxxxx -l root
password: root
root@rp-xxxxxx:~# dpkg-reconfigure tzdata

Configuring tzdata
------------------
// （1）地域の設定
// （2）都市の設定
```

RedPitayaにSSHログインして、タイムゾーンを設定します。
ログイン直後の画面をよく読むと、設定方法が書いてあります。

### 地域を設定する

```console
// つづき
Please select the geographic area in which you live. Subsequent configuration questions will narrow this down by presenting a list of cities, representing the
time zones in which they are located.

  1. Africa  2. America  3. Antarctica  4. Australia  5. Arctic  6. Asia  7. Atlantic  8. Europe  9. Indian  10. Pacific  11. US  12. Etc
Geographic area: 6
```

地域を選択します。
「``6. Asia``」を選択しました。

### 都市を設定する

```console
// つづき
Please select the city or region corresponding to your time zone.

  1. Aden      11. Baku        21. Damascus     31. Hong_Kong  41. Kashgar       51. Makassar      61. Pyongyang  71. Singapore      81. Ujung_Pandang
  2. Almaty    12. Bangkok     22. Dhaka        32. Hovd       42. Kathmandu     52. Manila        62. Qatar      72. Srednekolymsk  82. Ulaanbaatar
  3. Amman     13. Barnaul     23. Dili         33. Irkutsk    43. Khandyga      53. Muscat        63. Qostanay   73. Taipei         83. Urumqi
  4. Anadyr    14. Beirut      24. Dubai        34. Istanbul   44. Kolkata       54. Nicosia       64. Qyzylorda  74. Tashkent       84. Ust-Nera
  5. Aqtau     15. Bishkek     25. Dushanbe     35. Jakarta    45. Krasnoyarsk   55. Novokuznetsk  65. Rangoon    75. Tbilisi        85. Vientiane
  6. Aqtobe    16. Brunei      26. Famagusta    36. Jayapura   46. Kuala_Lumpur  56. Novosibirsk   66. Riyadh     76. Tehran         86. Vladivostok
  7. Ashgabat  17. Chita       27. Gaza         37. Jerusalem  47. Kuching       57. Omsk          67. Sakhalin   77. Tel_Aviv       87. Yakutsk
  8. Atyrau    18. Choibalsan  28. Harbin       38. Kabul      48. Kuwait        58. Oral          68. Samarkand  78. Thimphu        88. Yangon
  9. Baghdad   19. Chongqing   29. Hebron       39. Kamchatka  49. Macau         59. Phnom_Penh    69. Seoul      79. Tokyo          89. Yekaterinburg
  10. Bahrain  20. Colombo     30. Ho_Chi_Minh  40. Karachi    50. Magadan       60. Pontianak     70. Shanghai   80. Tomsk          90. Yerevan
Time zone: 79
```

次に都市を選択します。「79. Tokyo」を選択しました。
アルファベット順に並んでいるので、根気よく探してください。

### 設定内容を確認する

```console
// つづき
Current default time zone: 'Asia/Tokyo'
Local time is now:      Mon Mar 25 11:29:23 JST 2024.
Universal Time is now:  Mon Mar 25 02:29:23 UTC 2024.
```

地域と都市の選択が終わると、設定内容が表示されます。
デフォルトのタイゾーンが「``Asia/Tokyo``」に変更できたことを確認しました。

## ファイルサイズをリサイズしたい（``resize.sh``）

```console
$ ssh rp-xxxxxx -l root
password: root
root@rp-xxxxxx:~# /opt/redpitaya/sbin/resize.sh
```

RedPitayaにSSHログインして、ファイルシステムをリサイズします。
``resize.sh``を実行すると、SDカードの容量をフルで使えるようになります。

### 現在の容量を確認する（``df -h``）

```console
redpitaya> $ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       6.6G  5.2G  1.1G  84% /
tmpfs           231M     0  231M   0% /dev/shm
tmpfs            93M  4.0M   89M   5% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
none            5.0M   16K  5.0M   1% /var/log
/dev/mmcblk0p1  484M  308M  177M  64% /boot
```

全体の容量が6.6GBくらいしか認識されていません。
32GBのmicroSDカードを使っているので、これはおかしい、と思いドキュメントを読んだら、リサイズコマンドが載っていました。

### リサイズコマンドを実行する

```console
root@rp-xxxx:~# /opt/redpitaya/sbin/resize.sh
```

``/opt/redpitaya/sbin/resize.sh``を実行します。
RedPitayaの中のどのパスからでも実行できます。

以下は、実際に実行したときに表示された内容です。

```console
Welcome to fdisk (util-linux 2.37.2).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

This disk is currently in use - repartitioning is probably a bad idea.
It's recommended to umount all file systems, and swapoff all swap
partitions on this disk.

Command (m for help):
Disk /dev/mmcblk0: 28.89 GiB, 31016878080 bytes, 60579840 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x4fbf5bff

Device         Boot  Start      End  Sectors  Size Id Type
/dev/mmcblk0p1        8192   999423   991232  484M  e W95 FAT16 (LBA)
/dev/mmcblk0p2      999424 15155199 14155776  6.8G 83 Linux

Command (m for help): Partition number (1,2, default 2):
Partition 2 has been deleted.

Command (m for help): Partition type
   p   primary (1 primary, 0 extended, 3 free)
   e   extended (container for logical partitions)
Select (default p): Partition number (2-4, default 2): First sector (2048-60579839, default 2048): Last sector, +/-sectors or +/-size{K,M,G,T,P} (999424-60579839, default 60579839):
Created a new partition 2 of type 'Linux' and of size 28.4 GiB.
Partition #2 contains a ext4 signature.

Command (m for help):
Disk /dev/mmcblk0: 28.89 GiB, 31016878080 bytes, 60579840 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x4fbf5bff

Device         Boot  Start      End  Sectors  Size Id Type
/dev/mmcblk0p1        8192   999423   991232  484M  e W95 FAT16 (LBA)
/dev/mmcblk0p2      999424 60579839 59580416 28.4G 83 Linux

Command (m for help): The partition table has been altered.
Syncing disks.

Root partition has been resized. The filesystem will be enlarged upon the next reboot
```

とくにNoと答えるような選択肢はなく、勝手に進んでいきました。
念のため、これまで測定したデータとDAQコードのバックアップは取得しておきましたが、そのまま残っていました。

### リサイズ後の容量を確認する

```console
root@rp-xxxxxx:~# reboot
root@rp-xxxxxx:~# Connection to rp-xxxxxx.local closed by remote host.

$ Connection to rp-xxxxxx.local closed.
```

コマンドを実行しただけでは容量が増えないため再起動（``rebooot``）します。

```console
root@rep-xxxxxx:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        28G  5.3G   22G  20% /
tmpfs           231M     0  231M   0% /dev/shm
tmpfs            93M  4.0M   89M   5% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
none            5.0M  8.0K  5.0M   1% /var/log
/dev/mmcblk0p1  484M  308M  177M  64% /boot
```

再度SSHログインして容量を確認します。
容量が28GBに増えていることを確認しました。

## リファレンス

- [Prepare SD card](https://redpitaya.readthedocs.io/en/latest/quickStart/SDcard/SDcard.html)
