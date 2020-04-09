import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=94635433'


req = requests.get(url)
    


html = req.content
html_doc=str(html,'utf-8')
#修改成utf-8 #解析
soup = BeautifulSoup(html_doc,"lxml")
results = soup.find_all('d')
contents = [x.text for x in results] #保存结果
table_dict = {"contents":contents}
df = pd.DataFrame(table_dict)
df=df.drop_duplicates(['contents'])
df.to_csv("bibi.csv",encoding='utf_8_sig')
