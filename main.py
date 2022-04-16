# 매일 0시 : 인증 글 올리기
# 매일 8시 11분 : 기상 인증 체크
# 매일 13시 : 오전 활동 인증 체크

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date, datetime
import gspread
import src
from slack import WebClient
import os
from pytz import timezone

today = datetime.now(timezone('Asia/Seoul'))

g_m_users = []
client = WebClient(src.bot_token)



def get_ts():
	daily_thread = client.conversations_history(channel=src.g_m_channel)["messages"][0]
	return (daily_thread["ts"])
daily_history = client.conversations_replies(channel=src.g_m_channel, ts=get_ts())

for user in daily_history["messages"]:
	if (user["user"] == "U02D1UEL81Z"):
		continue
	g_m_users.append(src.UserID.users_id_to_name[user["user"]])

def import_googlesheet(tab):
    credential = ServiceAccountCredentials.from_json_keyfile_name(src.json_key_path, src.scope)
    gc = gspread.authorize(credential)
    doc = gc.open_by_url(src.spreadsheet_url)
    worksheet = doc.worksheet(tab)
    return (worksheet)

worksheet1 = import_googlesheet("4/18~5/15")
g_date = worksheet1.find(src.Time.g_m_time())

def get_g_users(row, col):
	return worksheet1.cell(row, col).value

def send_morning():
	name_col = 1
	date_col = g_date.col
	date_row = g_date.row + 1
	while (get_g_users(date_row, name_col) != None):
		value = get_g_users(date_row, name_col)
		for user in g_m_users:
			if (user == value):
				worksheet1.update_cell(date_row, date_col, 'O')
				date_row += 1
				break
		worksheet1.update_cell(date_row, date_col, 'X')
		print(value)
		date_row += 1



if __name__ == "__main__":
	try:
		if (today.hour == 23):
			client.chat_postMessage(channel=src.g_m_channel, blocks=src.g_m_state)
		if (today.hour == 23):
			send_morning()
		if (today.hour == 13):
			send_morning()
		print("==============================")
	except:
		print("오류가 발생하였습니다.")





#print(b)
#a = worksheet1.col_values(2)[3:]
#b = worksheet1.row_values(10)