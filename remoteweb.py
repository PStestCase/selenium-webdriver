from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
driver = webdriver.Chrome()
url = 'http://localhost:8080/wd/hub'



driver.get('http://codepad.org')


python_link = driver.find_elements_by_xpath(
    "//input[@name='lang' and @value='Python']")[0]
python_link.click()


text_area = driver.find_element_by_id('textarea')
text_area.send_keys("print 'Hello,' + ' World!'")


submit_button = driver.find_element_by_class_name('g-recaptcha')
submit_button.click()


assert "Hello, World!" in driver.get_page_source()

# driver.quit()
