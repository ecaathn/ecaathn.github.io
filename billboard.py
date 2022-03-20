from selenium import webdriver
import urllib.request
import json
from datetime import datetime

PATH = "C:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.billboard.com/charts/hot-100/")

songList = []
now = datetime.now()
i = 1

while i<=100:
    for song in driver.find_elements_by_class_name("o-chart-results-list-row-container"):
        print(song.text)
        for img in song.find_elements_by_tag_name("img"):
            print(img.get_attribute("src"))
            urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".jpg")
            i = i+1
            songList.append(
                {
                    "Pos" :song.text.split("\n")[0],
                    "Title" : song.text.split("\n")[1],
                    "Artist": song.text.split("\n")[2],
                    "PeakPos" : song.text.split("\n")[3],
                    "WksonChart": song.text.split("\n")[4],
                    "ScrapingTime" : now.strftime("%d %B %Y %H:%M:%S"),
                    "Image" : song.get_attribute("src")
                    }
                )
            
hasil_scraping = open("hasilscraping.json", "w")
json.dump(songList, hasil_scraping, indent = 6)
hasil_scraping.close()

driver.close()
