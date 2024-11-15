import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # Manages the Edge driver automatically
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Edge driver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.get("https://www.google.com/")


# Check if "Python" is in the page title
# assert "Goggle" in driver.title
# time.sleep(5)

# Find the search box by name
WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME,"gLFyf"))
)
elem = driver.find_element(By.CLASS_NAME, "gLFyf")
# time.sleep(5)
elem.clear()
time.sleep(3)
elem.send_keys("tech with tim"+Keys.RETURN)
time.sleep(3)


WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Tech with tim"))
)
time.sleep(4)
link=driver.find_element(By.PARTIAL_LINK_TEXT,"Tech with tim")
time.sleep(4)
link.click()
time.sleep(4)

# Ensure "No results found." is not in the page source
assert "No results found." not in driver.page_source

# Close the browser
driver.close()
