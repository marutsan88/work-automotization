from time import sleep
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Запустить сайт
driver.get(" http://uitestingplayground.com/dynamicid/")

# Кликнуть на синюю кнопку(нажать) и в поле, любое место(отжать)
button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()
sleep(5)
field = driver.find_element(By.CSS_SELECTOR, "div[class='container']").click()
sleep(5)

# Повторение нажатия три раза
for _ in range(3):
    button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()
    sleep(5)
    field = driver.find_element(By.CSS_SELECTOR, "div[class='container']").click()
    
sleep(10)

# Закрыть браузер
driver.quit()