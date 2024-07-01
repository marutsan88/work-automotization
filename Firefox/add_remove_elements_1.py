from time import sleep
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Запустить сайт
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликнуть на кнопку Add Element
for _ in range(5):
    add_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()

# Собрать со страницы список кнопок Delete  
add_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')

print(len(add_buttons))

# Вывести на экран размер списка
for add_button in add_buttons:
    elements = driver.find_element(By.CSS_SELECTOR, "button.added-manually").text
    
    print(elements)    

sleep(10)

# Закрыть браузер
driver.quit()