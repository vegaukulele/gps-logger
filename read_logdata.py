# -*- coding:utf-8 -*-
import folium # 地図を作成するWebアプリ「Leaflet」を利用したライブラリ

# Pythonistaアプリgps loggerで記録したログデータを地図に反映させる

# あらかじめ空のリストを2つ用意する
gps_list = []
gps_data = []
# Dropboxに保存されているgps_log.csvを読み込みモードで開く
with open(r'C:\Users\tomo\Dropbox\Pythonista\gps_log.csv', mode = 'r', encoding = 'utf-8') as f:
# 0番目の要素['time','latitude','longitude']は要らない。
# pythonではファイルオブジェクトをイテレータとして扱うことができるので、
# next()で2番目から(csvでは2行目から)データを扱うことができる
# next()をn回実施すればn+1行目からデータを扱うことになる
    next(f)
# csvのrowそれぞれに対して、改行を省いてカンマで区切ってリストにする
# さらにリストのうち先頭3つ(取得時間、緯度、経度)を抽出する
    for line in f:
        gps_list = line.rstrip('\n').split(',')
        gps_data.append(gps_list[:3])
print(gps_data)# これは文字列のリスト
print('-----------------------------------------')
# folium.Map()の引数locationには数値のリストを入れる必要がある
gps_data_flt = []
time_data = []
for d in gps_data: # gps_dataリストの各要素(リスト型)に対して処理を実行
    time_data.append(d[0]) # 取得時間のリストを別途用意する
    d.pop(0) # 取得時間の要素を削除する
    for i in d: # 要素(リスト型)の中の要素[文字列型]を順に[小数型]に変換
        gps_data_flt.append([float(i) for i in d])
print(time_data)
print(gps_data_flt)
print(gps_data_flt[-1])

# ログデータをマップで見る
# 地図の基準として最後のログの位置を設定
last_log = gps_data_flt[-1]
# 基準地点と初期の倍率を指定し、地図を作成する
map = folium.Map(location=last_log, zoom_start=15)
# 記録した各ログをマークし、popupを自身の計測時間とする
for f,t in zip(gps_data_flt,time_data):
    marker = folium.Marker(f, popup=t)
    map.add_child(marker)

gps_line = folium.PolyLine(locations=gps_data_flt)
map.add_child(gps_line)

# 地図をhtml形式でDropboxのディレクトリに出力
map.save(outfile= r"C:\Users\tomo\Dropbox\Pythonista\gps_map.html")
