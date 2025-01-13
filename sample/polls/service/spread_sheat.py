import pandas as pd
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pytz
from google.cloud import storage
import os

# 認証情報を作成
Auth = "./polls/service/sample_sheet.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Auth

# 認証情報をもとにクライアントを作成
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(Auth, scope)
Client = gspread.authorize(credentials)

SpreadSheet = Client.open_by_key("14JiPn02nCSXhh7gwJIjUcV-PfMI6Kt6Gw_rA8cKgSds")

# SpreadSheetから指定の名前のデータを取得
def get_spread_sheet_data(sheet_name):    
    RawData = SpreadSheet.worksheet(sheet_name)
    Data = RawData.get_all_records()
    name_column = []
    for row in Data:
        print(row['name'])
        name_column.append(row['name'])
    return name_column
