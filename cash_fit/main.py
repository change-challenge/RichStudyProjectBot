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
	daily_ts = client.conversations_history(channel=src.g_m_channel)["messages"][0]["ts"]
	cash_fit_history = client.conversations_replies(channel=src.g_m_channel, ts=daily_ts)
	for user in cash_fit_history["messages"]:
		if (user["user"] == "U02D1UEL81Z"):
			continue
		c_f_users.append(src.UserID.users_id_to_name[user["user"]])
	return (c_f_users)

#print(worksheet1)

if __name__ == "__main__":
	try:

		client.chat_postMessage(channel=src.c_f_channel, blocks=src.c_f_state)
		print("==============================")
	except:
		print("오류가 발생하였습니다.")