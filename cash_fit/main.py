import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta
import gspread
import src
from slack import WebClient
import time
from pytz import timezone

c_f_users = []
today = datetime.now(timezone('Asia/Seoul'))
client = WebClient(src.bot_token)

def import_googlesheet(tab):
    credential = ServiceAccountCredentials.from_json_keyfile_name(src.json_key_path, src.scope)
    gc = gspread.authorize(credential)
    doc = gc.open_by_url(src.spreadsheet_url)
    worksheet = doc.worksheet(tab)
    return (worksheet)

worksheet1 = import_googlesheet("현재 진행중")
g_date = worksheet1.find(src.Time.c_f_time())

def cash_fit_users():
	daily_ts = client.conversations_history(channel=src.c_f_channel)["messages"][0]["ts"]
	cash_fit_history = client.conversations_replies(channel=src.c_f_channel, ts=daily_ts)
	for user in cash_fit_history["messages"]:
		if (user["user"] == "U02D1UEL81Z"):
			continue
		c_f_users.append(src.UserID.users_id_to_name[user["user"]])
	return (c_f_users)

def get_g_users(row, col):
	return worksheet1.cell(row, col).value

def send_cashfit():
	print("===========send_cashfit()===========")
	name_col = 2
	date_col = g_date.col
	date_row = g_date.row + 1
	g_m_users = cash_fit_users()
	flag = False
	while (get_g_users(date_row, name_col) != None):
		value = get_g_users(date_row, name_col)
		check = get_g_users(date_row, date_col)
		if (check == '-'):
			date_row += 1
			continue
		for user in g_m_users:
			if (user == value):
				worksheet1.update_cell(date_row, date_col, 'O')
				date_row += 1
				flag = True
				break
		worksheet1.update_cell(date_row, date_col, 'X')
		if (flag == True):
			flag = False
			continue
		date_row += 1

if __name__ == "__main__":
	try:
		send_cashfit()
		client.chat_postMessage(channel=src.c_f_channel, blocks=src.c_f_state)
		print("==============================")
	except:
		print("오류가 발생하였습니다.")