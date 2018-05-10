from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "http://indiatoday.intoday.in/section/114/1/india.html"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
box = page_soup.findAll ("div", {"class" : "box"})

filename = "indiatodaynews.csv"
f = open(filename, "w")
headers = "news_title, news"

f.write(headers)
for box in box:
	news = box.div.a.img["title"]
	newstitle = box.findAll("div",{"class":"innerbox"})
	title_name = newstitle[0].text
	
	
print("title_name: "+ title_name)
print("news: "+ news)

f.write(news + "," + title_name +"\n")
f.close()
