from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org/")
dates = [date.text for date in driver.find_elements(By.CSS_SELECTOR,".event-widget time")]
titles = [title.text for title in driver.find_elements(By.CSS_SELECTOR,".event-widget li a")]
# not required to change to list with text because function return a object we can iterate through it 

events = {

}

for i in range(len(dates)):
    events.update({f"{i}": {"Date": f"{dates[i]}", "Event name": f"{titles[i]}"}})
    # events[i] = {
    #     "time":dates[i].text,
    #     "name":titles[i].text
    # }

print(events)
driver.close()