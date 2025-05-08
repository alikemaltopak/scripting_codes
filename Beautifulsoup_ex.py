import requests
from bs4 import BeautifulSoup
url = "https://www.trendyol.com/telefon-x-c104025"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers).content
soup = BeautifulSoup(response,"html.parser")
liste = soup.find_all("div",{"class":"prdct-cntnr-wrppr"},limit = 1)
for i in liste:
    pname = i.find_all(" title")
    print(pname)

