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
for song in driver.find_elements_by_class_name("o-chart-results-list-row-container"):
    print(song.text)
    for img in song.find_elements_by_tag_name("img"):
        print(img.get_attribute("src"))
        urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".jpg")
        i = i+1
        songList.append(
            {
                "No" :song.text.split("\n")[0],
                "Judul" : song.text.split("\n")[1],
                "Produser" : song.text.split("\n")[2],
                "Genre" : song.text.split("\n")[3],
                "Waktu Scraping" : now.strftime("%d %B %Y %H:%M:%S"),
                "Gambar" : img.get_attribute("src")
            }
        )
hasil_scraping = open("hasilscraping.json", "w")
json.dump(songList, hasil_scraping, indent = 6)
hasil_scraping.close()
driver.close()
