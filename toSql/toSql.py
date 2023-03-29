import pymysql
import os
import glob
import pandas as pd
from sqlalchemy import create_engine

def findDbName():
    global DATABASE_NAME
    db = pymysql.connect(host=HOST, user=SQL_USER_ID, password=SQL_PASSWORD)
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES")
    result = cursor.fetchall()
    databases = {}
    print("資料庫列表: ")
    for i, database in enumerate(result, start=1):
        databases[i] = database[0]
        print(i, database[0])
    cursor.close()
    db.close()
    while True:
        ans = int(input("請選擇你要的資料庫: "))
        if ans in databases:
            return databases[ans]
        else:
            print("所選的資料庫不存在, 請重新選擇")


def newDbName(newName):
    # 創建MySQL數據庫連接
    db = pymysql.connect(host=HOST, user=SQL_USER_ID, password=SQL_PASSWORD)
    # 創建資料庫
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE {}".format(newName))
    cursor.close()
    db.close()


# 設置常數
PORT = '3306'
HOST = 'localhost'
SQL_USER_ID = str(input('請輸入你的MySql帳號: '))
SQL_PASSWORD = str(input('請輸入{}的密碼: '.format(SQL_USER_ID)))
DATABASE_NAME = str(input('請輸入您本次希望匯入到哪個Database(若為現有database請輸入N): '))

if DATABASE_NAME == '' or DATABASE_NAME == 'N':
    DATABASE_NAME = findDbName()
else:
    newDbName(DATABASE_NAME)

sqlTableName = str(input('請輸入資料庫中表的名稱: '))

# 創建資料庫連結，將資料匯入至MySql
engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(SQL_USER_ID, SQL_PASSWORD, HOST, PORT, DATABASE_NAME))
dataFolderName = input('請匯入的資料夾名稱: ')

for file in glob.glob(os.path.join(dataFolderName, '*.xlsx')):
    df = pd.read_excel(file)
    print(df)
    # 將DataFrame寫入MySQL中
    df.to_sql(sqlTableName, con=engine, if_exists='append', index=False)

engine.dispose()
