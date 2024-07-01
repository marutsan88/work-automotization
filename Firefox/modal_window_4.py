from time import sleep
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Запустить сайт
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

#В модальном окне нажмите на кнопку Сlose.
driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()

sleep(10)

driver.quit()