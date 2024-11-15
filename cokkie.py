from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))


driver.get("https://orteil.dashnet.org/cookieclicker/")


cookie_id = "bigCookie"          
cookies_id = "cookies"            
product_price_prefix = "productPrice"
product_prefix = "product"        


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)
cookie = driver.find_element(By.ID, cookie_id)

while True:
    
    cookie.click()

    
    cookies_count_text = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count_text.replace(",", ""))

    
    for i in range(4):
        product_price_text = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
        
        
        if not product_price_text.isdigit():
            continue

        
        product_price = int(product_price_text)

        
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break  

    
    time.sleep(0.1)
