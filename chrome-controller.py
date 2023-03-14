from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import keyboard
print('    Start')

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
print('Succesfully loaded chromedriver')

driver.get('https://www.python.org')

elem = driver.find_element(By.ID, 'id-search-field')
elem.send_keys('pip')
elem.send_keys(Keys.ENTER)

keyboard.wait('esc')
print('    End')
driver.quit