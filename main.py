from oauth2client.service_account import ServiceAccountCredentials
import gspread

spreadsheet_url = "https://docs.google.com/spreadsheets/d/1doYowbfl1TJ3zn-QSGl8YMpr6P-0uUd_PPxrQGpAKLo/edit#gid=1934408757"

hojin_key = "/Users/hojinjang/RichStudyProjectBot/config/goodmorningproject-657481cfc7b9.json"
aws_key = "/home/ubuntu/RichStudyProjectBot/config/goodmorningproject-657481cfc7b9.json"
json_key_path = hojin_key
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

def import_googlesheet(tab):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    credential = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)
    gc = gspread.authorize(credential)
    doc = gc.open_by_url(spreadsheet_url)
    worksheet = doc.worksheet(tab)
    return (worksheet)

worksheet1 = import_googlesheet('2기 : 2022년 2월28일-')
#a = worksheet1.col_values(1)[3:]
b = worksheet1.row_values(10)
#print(a)
print("==============================")
print(b)