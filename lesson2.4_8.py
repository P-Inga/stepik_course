from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
 
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

book = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))

book = browser.find_element(By.ID, 'book')
book.click()
   
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "[id = 'input_value']")
x = x_element.text
y = calc(x)

input = browser.find_element(By.CSS_SELECTOR, "[id = 'answer']")
input.send_keys(y) 

button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
button.click()

time.sleep(2)
browser.quit()