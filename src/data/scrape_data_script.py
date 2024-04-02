from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

url = 'https://developer.uspto.gov/product/patent-grant-full-text-dataxml#product-files'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

rows = driver.find_elements(by='xpath', value='//*[@id="table"]/tbody/tr/td/a')
print(len(rows))
links = []
for row in rows:
    links.append(row.get_attribute('href'))

print(links)
    
# page_link = driver.find_elements(by='xpath', value='/html/body/div[1]/div[3]/div/section/div[2]/article/div[2]/div[3]/div[1]/form[2]/div[1]/div[3]/div[1]/span[2]/span/button')
# page_link[0].click()
# time.sleep(5)
