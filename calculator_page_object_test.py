from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
from Page.CalculatorPage import CalculatorPage


def test_form_calculator():
    
        driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))


        calculator_page = CalculatorPage(driver)

        calculator_page.delay()
        calculator_page.sum_of_the_numbers()
        calculator_page.get_result()
        calculator_page.close_driver()
