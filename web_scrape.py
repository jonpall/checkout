import selenium

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)



url = "https://www.bestbuy.ca/en-ca/product/asus-geforce-gtx-1650-4gb-gddr5-video-card-dual-gtx1650-o4g/14180222"

driver.get(url)

driver.maximize_window()

click.click()    



