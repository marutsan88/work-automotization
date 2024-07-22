from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InternetMagPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

   # Авторизация пользователя
    def authorization(self, name = "standard_user", password = "secret_sauce"):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    # Добавление товара в корзину
    def add_products(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        counter = 'Total: $58.29'
        return counter

    # Переход в корзину интернет-магазина
    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    # Ввод персональных данных пользователя
    def personal_data(self, name: str, last_name: str, index: int):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="postalCode"]').send_keys(index)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="continue"]').click()

    # Вызов метода для ожидания элемента в течение 10 секунд
    def total_cost(self):
        txt = WebDriverWait(self.driver, "10").until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
        return txt

    # Закрытие браузера
    def close(self):
        self.driver.find_element(By.CSS_SELECTOR, "#finish").click()
        self.driver.quit()
