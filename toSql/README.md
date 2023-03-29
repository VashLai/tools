# ToSql(mySQL)

## 文件說明
在某份職缺上看到 JD (Job Description) 寫著 __『需要會將EXCEL匯入到SQL』__，

想著這沒有很難啊，以往都是只透過 pymysql 的方式去寫入，只是這樣非常的慢，

這次換用 SQLalchemy 搭配 Pandas 的 DataFram 使用 tosql() 的方式匯入，幾萬筆的資料一下就寫入了，覺得非

常的快，不過因為是隨意寫的程式，所以若有一些 bug 請見諒。





## 文件需求
因為會用到DataFram所以要把Pandas套件載下來。
```shell
pip install sqlalchemy
pip install pandas
```



## 使用說明
將要匯入的Excel放在同目錄下的一個資料夾中，啟用程式並依序輸入資料即可。

因為預設是存在本機，所以HOST：localhost，PORT：3306，若有其他需求的，請再自行修改。

若DATABASE_NAME沒輸入或輸入N，會自動抓取你的所有DBNAME並枚舉出來讓您選擇，請打上數字就好。



| Name           | Type | Description                                                  |
| -------------- | ---- | ------------------------------------------------------------ |
| SQL_USER_ID    | str  | Mysql登入帳號                                                |
| SQL_PASSWORD   | str  | Mysql登入密碼                                                |
| DATABASE_NAME  | str  | 若輸入為N或是空白會自動抓取現有DB並枚舉出來，若是要新增DB請直接輸入 |
| sqlTableName   | str  | 輸入要寫入的TABLE的名稱                                      |
| dataFolderName | str  | Excel檔案存放的資料夾名稱                                    |

