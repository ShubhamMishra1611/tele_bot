from selenium import webdriver
from bs4 import BeautifulSoup
import time

URL = "URL"
browser = webdriver.Chrome(executable_path="path_to_chromedriver.exe")
sada = browser.get(URL)
time.sleep(3)
source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')

file = open("words.txt", 'w')
for items in soup.find_all('li', attrs={'class': 'invert light'}):
    file.write(items.text)
    print(items.text)
