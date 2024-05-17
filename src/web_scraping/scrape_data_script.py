from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load existing links from file
existing_links = set()
try:
    with open('links.txt', 'r') as file:
        for line in file:
            existing_links.add(line.strip())
except FileNotFoundError:
    pass

url = 'https://developer.uspto.gov/product/patent-grant-full-text-dataxml#product-files'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(20)

rows = driver.find_elements(by='xpath', value='//*[@id="table"]/tbody/tr/td/a')
print("Number of links extracted:", len(rows))


# Extract new links
new_links = set()
for row in rows:
    new_links.add(row.get_attribute('href'))

# Combine existing links with new links
links = existing_links.union(new_links)

# Write all links to file
with open('links.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')

print("Links saved to links.txt")

driver.quit()
