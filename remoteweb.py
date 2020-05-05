from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
driver = webdriver.Chrome()
url = 'http://localhost:8080/wd/hub'
descaps = {'browserName': 'chrome', 'loggingPrefs': {'performance': 'INFO'}}

driver = webdriver.Remote(command_executor=url, desired_capabilities=descaps)

driver.get("http://www.youtube.com")

print("Page URL: "+driver.current_url)
print("Page title: "+driver.title)
x =driver.title

assert x == "YouTube"


driver.quit()
