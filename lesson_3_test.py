from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
from time import sleep


driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(10)
driver.maximize_window()
    # Авторизация
    
user = "standard_user"
password = "secret_sauce"

    
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(user)
sleep(3)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
sleep(3)   
driver.find_element(By.CSS_SELECTOR, "#login-button").click()
sleep(3)  
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
sleep(3) 
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
sleep(3)   
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
sleep(3) 
driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()
sleep(3) 
driver.find_element(By.CSS_SELECTOR, "#checkout").click()
sleep(3)  
driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]').send_keys("Александр")
sleep(3) 
driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').send_keys("Семирунний")
sleep(3) 
driver.find_element(By.CSS_SELECTOR, 'input[name="postalCode"]').send_keys("250056")
sleep(3) 
driver.find_element(By.CSS_SELECTOR, 'input[name="continue"]').click()
txt = WebDriverWait(driver, "10").until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
    
driver.find_element(By.CSS_SELECTOR, "#finish").click()
    
driver.quit()
assert txt == "Total: $58.29"



