from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "C:/Program Files/Google/Chrome Beta/Application/chrome.exe"

driver = webdriver.Chrome(chrome_options=options)
link = " http://SunInJuly.github.io/execute_script.html"
driver.get(link)
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    x_element = driver.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    element = driver.find_element_by_id('answer')
    element.send_keys(y)

    option1 = driver.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = driver.find_element_by_id("robotsRule")
    driver.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option2.click()

    button = driver.find_element_by_tag_name("button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(5)
    driver.quit()