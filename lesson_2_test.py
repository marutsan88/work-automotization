from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
from time import sleep

def test_form_calculator():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.implicitly_wait(10)
    driver.maximize_window()

    input_delay = driver.find_element(By.CSS_SELECTOR, 'input[id = "delay"]')
    input_delay.clear()
    input_delay.send_keys('3')
    driver.find_element(By.XPATH, '//span[contains(text(),"7")]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//span[contains(text(),"+")]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//span[contains(text(),"8")]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//span[contains(text(),"=")]').click()
    sleep(3)
    WebDriverWait(driver, "48").until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))

    assert driver.find_element(By.CSS_SELECTOR, "div.screen").text == "15"
     
    driver.quit()
# чтобы зыпустить Pytest, нужно в терминале ввести команду python -m pytest и  нажать Enter
