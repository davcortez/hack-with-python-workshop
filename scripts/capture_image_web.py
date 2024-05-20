## Dependencies: Selenium and Gecko Driver
### pip install selenium
### Gecko Driver -> https://github.com/mozilla/geckodriver/releases

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from time import sleep

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

# Enter URL here
URL = "http://example.com"

driver.get(URL)
sleep(30)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
driver.find_element(By.TAG_NAME,'body').screenshot('web_screenshot.png')

driver.quit()
print("end")