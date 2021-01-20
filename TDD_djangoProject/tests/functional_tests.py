# 功能测试
from selenium import webdriver

chromedriver = 'C:\\Users\\ShionLee\\chromedriver_win32\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.get('http://localhost:8000')

assert 'Django' in browser.title