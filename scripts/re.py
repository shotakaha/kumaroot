# ---
# jupyter:
#   jupytext:
#     formats: notebooks//ipynb,mystmd//md:myst,scripts//py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: 'Python 3.10.8 (''.venv'': poetry)'
#     language: python
#     name: python3
# ---

# # 正規表現したい（re）
#
# - Apacheのログをパースしてみる

# Apacheログの形式
#
# - https://httpd.apache.org/docs/2.4/ja/logs.html#accesslog
#
# ---
#
# Commonログ
#
# ```
# LogFormat "%h %l %u %t \"%r\" %>s %b" common
# ```
#
# ---
#
# Combinedログ
#
# - combinedにはリファラーとユーザーエージェント（＝ブラウザ）の情報が追加される
#
# ```
# LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\"" combined
# ```
#
# ---
#
# LTSVログ
#
# - パースしやすいように名前付きタブ区切りにする形式も、最近ある
# - 読みやすいように``\t``のあとに改行をいれた。運用するならこの改行は不要
#
# ```
# LogFormat "
# remote_host:%h\t
# ident:%l\t
# user:%u\t
# time:%{%d/%b/%Y:%H:%M:%S %z}t\t
# request:\"%r\"\t
# status:%>s\t
# size:%b\t
# referer:\"%{Referer}i\"\t
# user_agent:\"%{User-Agent}i
# " apache_ltsv
# ```

# 実サンプル

s01 = """64.124.8.47 - - [01/Oct/2022:03:17:08 +0900] "GET /proffice/archives/intra-j/images/safty.gif HTTP/1.1" 200 241 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/
537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36" www2.kek.jp"""
s01

s02 = """24.129.70.237 - - [01/Oct/2022:03:21:19 +0900] "GET /ja/news/highlights/2011/images/Aerosol2s.jpg HTTP/1.1" 200 24799 "https://www.kek.jp/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15" www2.kek.jp"""
s02

s03 = """114.119.144.65 - - [01/Oct/2022:03:17:55 +0900] "GET /engineer/oho/giken/procedng/paper/met063.pdf HTTP/1.1" 200 34855 "https://www2.kek.jp/engineer/oho/giken/pr
ocedng/html/kwall.htm" "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://webmaster.pe
talsearch.com/site/petalbot)" www2.kek.jp"""
s03

# ホスト名（IPアドレス）を抽出したい
#
# - IPv4 : ``xxx.xxx.xxx.xxx``
#   - 4組の数字をピリオドで結合した文字列
#   - それぞれの数字は8ビットを10進数で表したもの（0 - 255）
#   - 正規表現 : ``(\d{1,3}\.){3}\d{1,3}`` でOK
# - IPv6は``xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx``
#   - 8組の文字列を``:``で結合した文字列
#   - それぞれの文字列は16ビットを16進数で表したもの
#   - 正規表現 : ``([0-9A-Fa-f]{0,4}\:){7}[0-9A-Fa-f]{0,4}`` でOKなはず

import re

ipv4 = re.compile("(\d{1,3}\.){3}\d{1,3}")
ipv4

ipv6 = re.compile("([0-9A-Fa-f]{0,4}:){7}[0-9A-Fa-f]{0,4}")
ipv6

m = ipv4.match(s01)
m

m = ipv6.match(s01)
m

m.re

m.group()



# アクセス日時を抽出したい
#
# - 時刻は``[``と``]``で囲まれた内容
# - 正規表現は``\[.*?\]``

tm = re.compile("\[.*?\]")
tm

m = tm.search(s01)
m

m.group()

# リクエストを取得したい
#
# - リクエストは``"GET /ja/news/highlights/2011/images/Aerosol2s.jpg HTTP/1.1"``のように``"``と``"``で挟まれた部分
# - 正規表現は``\".*?\"``

rq = re.compile('".*?"')
rq

m = rq.search(s01)
m

m.group()

# Combinedログ全部盛りの正規表現を作ってみる

s03

# _regex_str = """"(\d{1,3}\.){3}\d{1,3} (\s+|-) (\s+|-) (\[.*?\]) (\".*?\") (\d+) (\d+|-) (\".*?\") (\".*?\")"""
# _regex_str = '(?P<remote_host>(\d{1,3}\.){3}\d{1,3}) (?P<ident>(\S+|-)) (?P<user>(\S+|-)) (?P<time>(\[.*?\])) (?P<request_first_line>(\"[\S\s]+?\")) (?P<status>(\d+)) (?P<size>(\d+|-)) (?P<referer>(\S+)) (?P<ua>(\"[\S\s]+?\"))'
# _regex_str = '(?P<remote_host>(\d{1,3}\.){3}\d{1,3}) (?P<ident>(\S+|-)) (?P<user>(\S+|-)) (?P<time>(\[[\S\s]+?\])) (?P<request_first_line>(\"[\S\s]+?\")) (?P<status>(\d+)) (?P<size>(\d+|-)) (?P<referer>([\S\s]+)) (?P<ua>(\"[\S\s]+?\"))'
_regex_str = '(?P<remote_host>(\d{1,3}\.){3}\d{1,3}) (?P<ident>(\S+|-)) (?P<user>(\S+|-)) (?P<time>(\[[\S\s]+?\])) (?P<request_first_line>("[\S\s]+?")) (?P<status>(\d+)) (?P<size>(\d+|-)) (?P<referer>([\S\s]*)) (?P<ua>("[\S\s]+?"))'
# _regex_str

m = re.search(_regex_str, s02)
m

m.group()

m.group("remote_host")

m.group("ident")

m.group("user")

m.group("time")

m.group("request_first_line")

m.group("status")

m.group("size")

m.group("referer")

m.group("ua")


