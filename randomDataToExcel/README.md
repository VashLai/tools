# RandomDataToExcel

## 文件說明
本來是在某份職缺上看到的 JD (Job Description) 上寫到  __『需要會將EXCEL 匯入到 SQL』__ ，
於是自己心血來潮，心想我也來試著寫寫看好了，但寫完了另一份名叫 __toSql.py__ 的程式後忽然想到
__『啊，我沒有檔案可以匯入啊！』__。
於是乎，就試著寫了一個產生隨機字串並對該字串進行SHA1加密(透過SHA1加密純粹只是為了好玩)，使用者只要輸入相關的資料即可於當前目錄下產生Excel的檔案。



## 文件需求
因為會用到DataFram所以要把Pandas套件載下來。
```shell 
pip install pandas
```



## 使用說明
程式會以input()的方式向使用者索取資料

| Name           | Type | Description                                          |
| -------------- | ---- | ---------------------------------------------------- |
| numFiles       | int  | 需要產生幾份檔案                                     |
| columns        | str  | Excel欄位的名稱，並用半形逗點隔開 ex.Name,Phone,.... |
| numRows        | int  | 每份檔案產生幾筆的資料                               |
| filenamePrefix | str  | Excel的檔案名稱                                      |

