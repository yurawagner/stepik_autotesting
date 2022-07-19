from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:
    #current_dir = os.path.abspath(os.path.dirname('lesson22_step8.py'))    # получаем путь к директории текущего исполняемого файла 
    #file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    #element.send_keys(file_path)
    #print(os.path.abspath('lesson22_step8.py'))
    #print(" ")
    #print(os.path.abspath(os.path.dirname('lesson22_step8.py')))
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('Pavel')
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('Gutierres')
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys('PG_Mexico@gmail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    load = browser.find_element(By.ID, "file")
    load.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.close()