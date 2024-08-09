import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage

@allure.id("Calculator")
@allure.epic("калькулятор")
@allure.severity("blocker")
@allure.suite("Тесты на работу с калькулятором")
@allure.story("Выполнение математических операций на калькуляторе")
@allure.title("Сложение чисел на калькуляторе")
@allure.feature("CREATE")
def test_form_calculator():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Создание переменной, которая хранит экзампляр класса CalculatorPage"):
        calculator_page = CalculatorPage(driver)

    calculator_page.delay()
    calculator_page.sum_of_the_numbers()
    calculator_page.get_result()
    calculator_page.close_driver()
