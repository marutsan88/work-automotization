from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Запустить сайт
driver.get(" http://the-internet.herokuapp.com/login")

# В поле username введите значение tomsmith
username = "#username"
username_input = driver.find_element(By.CSS_SELECTOR, username)
sleep(2)
username_input.send_keys("tomsmith")
sleep(2)

# В поле password введите значение SuperSecretPassword
password = "#password"
password_input = driver.find_element(By.CSS_SELECTOR, password)
sleep(2)
password_input.send_keys("SuperSecretPassword")
sleep(2)

# Нажмите кнопку Login
button = driver.find_element(By.CSS_SELECTOR, "button.radius").click()

sleep(10)

# Закрыть браузер
driver.quit()