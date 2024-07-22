from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

from Page.InternetMagPage import InternetMagPage

def test_form_internet_mag():
    
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    
        internet_mag_page = InternetMagPage(driver)

        internet_mag_page.authorization("standard_user", "secret_sauce")
        to_be = internet_mag_page.add_products()
        internet_mag_page.go_to_cart()
        internet_mag_page.personal_data("Александр", "Семирунний", "234875")
        as_is = internet_mag_page.total_cost()

       
        assert as_is == to_be

        internet_mag_page.close()
