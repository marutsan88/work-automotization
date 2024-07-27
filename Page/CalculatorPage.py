from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:

    def __init__(self, driver: bool):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(1)
        self._driver.maximize_window()

    def delay(self):
        input_delay = self._driver.find_element(By.CSS_SELECTOR, 'input[id = "delay"]')
        input_delay.clear()
        input_delay.send_keys('3')
# Ввод чисел в калькулятор и запуска операции сложения
    def sum_of_the_numbers(self):
        self._driver.find_element(By.XPATH, '//span[contains(text(),"7")]').click()
        self._driver.find_element(By.XPATH, '//span[contains(text(),"+")]').click()
        self._driver.find_element(By.XPATH, '//span[contains(text(),"8")]').click()
        self._driver.find_element(By.XPATH, '//span[contains(text(),"=")]').click()

    # Получениt результата сложения
    def get_result(self):
            WebDriverWait(self._driver, "48").until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
            return self._driver.find_element(By.CSS_SELECTOR, "div.screen").text == "15"

    # Закрытие браузера
    def close_driver(self):
        self._driver.quit()
