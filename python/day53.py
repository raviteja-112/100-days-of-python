from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests

forms_URL = "https://forms.gle/a91DvmZHYyEBfjXf6"
URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(url=URL).text
soup = BeautifulSoup(response,"html.parser")
links_address = [[item["href"],item.text.replace(" | ","").strip()]for item in soup.find_all(name ="a",class_ = "StyledPropertyCardDataArea-anchor")]

prices = [price.text.replace("/mo","").split("+")[0] for price in soup.find_all(name="span",class_ ="PropertyCardWrapper__StyledPriceLine")]



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=forms_URL)

for n in range(len(prices)):
    time.sleep(3)
    input = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address = links_address[n][1]
    link = links_address[n][0]
    price = prices[n]
    input.send_keys(address,Keys.TAB,price,Keys.TAB,link)
    time.sleep(3)
    
    
    submit = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    time.sleep(3)

    another_submit = driver.find_element(By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    another_submit.click()
    time.sleep(5)
    

