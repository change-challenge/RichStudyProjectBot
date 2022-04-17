from datetime import datetime
from pytz import timezone
import os

c_f_channel = "C03AEMDJDRS"
bot_token = "xoxb-1830334374899-2443966688067-uYiR4dWVtj11GqJvE6D6ykBg"
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1Z_B2eYLwOOqU27yuQn6Mj68osJIT3og2XW4HFOSlHgM/edit#gid=147463382"

cur_dir = os.getcwd()
json_key_path = cur_dir + "/RichStudyProjectBot/cash_fit/config/cash-fit-347415-7076e46da026.json"

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

class Time:
	def c_f_post_time():
			return (datetime.now(timezone('Asia/Seoul'))).strftime('%Y년 %-m월 %-d일')
	def c_f_time():
		return (datetime.now(timezone('Asia/Seoul'))).strftime('%-m/%-d')

c_f_state = [
	{
		"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*[Cash-Fit 💪 인증 - " + Time.c_f_post_time() + "]* \n\n"
			}
	}
]

class UserID:
	users_name = [
				"강동운",
				"김가현",
				"김민수",
				"김범태",
				"김성훈",
				"김주영",
				"문건호",
				"박상아",
				"박상진",
				"박서지",
				"박재형",
				"박혜빈",
				"서수희",
				"신환종",
				"심혜빈",
				"양희재",
				"윤영주",
				"이재원",
				"이현정",
				"장호진",
				"전진표",
				"정하진",
				"정현진",
				"천지영",
				"최명원",
				"하승희",
				"한수경"
			]
	
	users_id_to_name = {
				"U02RL2XV4KH" : "강동운",
				"U02RTQ2NXKQ" : "김가현",
				"U02LE7HKCE6" : "김민수",
				"U027JQK00KB" : "김범태",
				"U01QT3KFU4D" : "김성훈",
				"U026RFKEN3H" : "김주영",
				"U02733TKY9K" : "문건호",
				"U02S33JRS9J" : "박상아",
				"U02S4TERJ5S" : "박상진",
				"U02S2LM4LP4" : "박서지",
				"U02S0M72N82" : "박재형",
				"U01QMTD1K37" : "박혜빈",
				"U02S2PVS3B6" : "서수희",
				"U01QSTF6M18" : "신환종",
				"U02RU9NTCA2" : "심혜빈",
				"U01QEPH2TP1" : "양희재",
				"U01QLRF7MJ6" : "윤영주",
				"U02AKLMDSRE" : "이재원",
				"U02RTS9357G" : "이현정",
				"U01R3U5FQL8" : "장호진",
				"U02S3UAPS9J" : "전진표",
				"U02SR22Q9MW" : "정하진",
				"U02727PASNS" : "정현진",
				"U032CUPKA95" : "천지영",
				"U02S0ER3W9H" : "최명원",
				"U02RU5T3KSS" : "하승희",
				"U027382N5K7" : "한수경"
			}
