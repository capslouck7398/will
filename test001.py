import requests
from bs4 import BeautifulSoup
response = requests.get("https://travel.ettoday.net/category/%E5%8F%B0%E5%8C%97/")
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find("div", class_ ='part_pictxt_1').find_all("a", class_="pic")
for obj in result:
    print(obj.get("title") + "\n" + "\n")
for obj2 in soup.select("em"):
    obj2.decompose()
for obj1 in soup.find("div", class_ ='part_pictxt_1').find_all("p", class_="summary"):
    print(obj1.text + "\n")
 
import requests
from bs4 import BeautifulSoup
response = requests.get("https://travel.ettoday.net/category/%E5%8F%B0%E5%8C%97/")
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find("div", class_ ='part_pictxt_1').find_all("a", class_="pic")
for obj in result:
    print(obj.get("title") + "\n" + "\n")
for obj2 in soup.select("em"):
    obj2.decompose()
for obj1 in soup.find("div", class_ ='part_pictxt_1').find_all("p", class_="summary"):
    print(obj1.text + "\n")
 


