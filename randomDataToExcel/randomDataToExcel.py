import random
import string
import pandas as pd
import hashlib

# 取得使用者輸入的需產生的檔案數量、欄位名稱、每份檔案的筆數和檔名
numFiles = int(input('要產生幾份檔案？'))
columns = input('請輸入欄位名稱，以逗號分隔： (ex. name,phoneNumber,address,...)').split(',')
numRows = int(input('每份檔案要產生幾筆資料？'))
filenamePrefix = input('請輸入檔名：')

# 產生指定數量的亂數資料
for i in range(numFiles):
    # 產生每個欄位的亂數資料
    data = {}
    for column in columns:
        # 產生隨機字串並進行SHA1加密
        values = [''.join(random.choice(string.ascii_letters + string.digits) for j in range(10)) for k in
                  range(numRows)]
        sha1Values = [hashlib.sha1(v.encode('utf-8')).hexdigest() for v in values]
        data[column] = sha1Values

    # 將資料組成dataframe
    df = pd.DataFrame(data)

    # 檔案名稱
    filename = f'{filenamePrefix}{i + 1:03d}'

    # 將資料存成Excel檔案
    df.to_excel(filename + '.xlsx', index=False)

    print(f'產生檔案: {filename}')
