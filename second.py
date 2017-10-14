from bs4 import BeautifulSoup
import requests
url="https://its.pku.edu.cn/cas/webLogin"
username=input("请输入学号：")
password=input("请输入密码：")
postdata={"username":username,"password":password,"iprange":"no"}
r=requests.post(url,data=postdata)
HTMLData=r.text
HTMLData=BeautifulSoup(HTMLData,"html.parser")
a=HTMLData.find_all("li")[0]
print(a.get_text())


