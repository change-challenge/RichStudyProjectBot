import os
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import gspread

spreadsheet_url = "https://docs.google.com/spreadsheets/d/1doYowbfl1TJ3zn-QSGl8YMpr6P-0uUd_PPxrQGpAKLo/edit#gid=1934408757"

os.chdir("config/")
# hojin_key = "/Users/hojinjang/RichStudyProjectBot/config/goodmorningproject-657481cfc7b9.json"
# clust_key = ""
# aws_key = "/home/ubuntu/RichStudyProjectBot/config/goodmorningproject-657481cfc7b9.json"
json_key = os.getcwd() + "/goodmorningproject-657481cfc7b9.json"

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

def import_googlesheet(tab):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    credential = ServiceAccountCredentials.from_json_keyfile_name(json_key, scope)
    gc = gspread.authorize(credential)
    doc = gc.open_by_url(spreadsheet_url)
    return (doc.worksheet(tab))

credential = ServiceAccountCredentials.from_json_keyfile_name(json_key, scope)
gc = gspread.authorize(credential)
doc = gc.open_by_url("https://docs.google.com/spreadsheets/d/1doYowbfl1TJ3zn-QSGl8YMpr6P-0uUd_PPxrQGpAKLo/edit#gid=1934408757")

doc.add_worksheet("test", rows="100",cols="100")


# a = worksheet1.col_values(1)[3:]
# b = worksheet1.row_values(10)

# print(a)
# print("==============================")
# print(b)

# creds = None
# service = build('sheets', 'v4', credentials=creds)
