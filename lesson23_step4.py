from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element(By.ID, "input_value").text
    x = int(x_element)
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    button1 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()