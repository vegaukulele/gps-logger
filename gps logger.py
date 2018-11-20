import ui   
import location
import csv
import datetime, time

def shinki(sender):
	label = sender.superview['label1']
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 現時刻を取得
		
	location.start_updates() # 緯度、経度、高度などを取得 (辞書型)
	gps=location.get_location()
	location.stop_updates()

	gps_text = ''
	for g in gps:
		gps_text=gps_text + str(g)+':'+str(gps[g])+'\n'
	gps_dict = {'time':now}
	gps_dict.update(gps)
	gps_rows=[] # 空のリストを作成
	gps_rows.append(gps_dict)
	
	label.text=now + '\n' + gps_text
	
	parameters = ['time','latitude','longitude','altitude','timestamp','horizontal_accuracy','vertical_accuracy','speed','course']
	header = dict([(val,val) for val in parameters])
	
	# csvファイルを開いて、gps辞書を書き込む
	with open('gps_log.csv',mode='w', encoding='utf-8') as f:
		gps_rows.insert(0,header)
		writer = csv.DictWriter(f,parameters, extrasaction='ignore')
		writer.writerows(gps_rows)
		
def tuiki(sender):
	label = sender.superview['label1']
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 現時刻を取得
		
	location.start_updates() # 緯度、経度、高度などを取得 (辞書型)
	gps=location.get_location()
	location.stop_updates()
	gps_text = ''
	for g in gps:
		gps_text=gps_text + str(g)+':'+str(gps[g])+'\n'
	gps_dict = {'time':now}
	gps_dict.update(gps)
	gps_rows=[] # 空のリストを作成
	gps_rows.append(gps_dict)

	label.text=now + '\n' + gps_text
	parameters = ['time','latitude','longitude','altitude','timestamp','horizontal_accuracy','vertical_accuracy','speed','course']
	header = dict([(val,val) for val in parameters])

	# csvファイルを開いて、gps辞書を書き込む
	with open('gps_log.csv',mode='a', encoding='utf-8') as f:
		writer = csv.DictWriter(f,parameters, extrasaction='ignore')
		writer.writerows(gps_rows)
#-----------------------------------

v = ui.load_view()
v.present('sheet')
