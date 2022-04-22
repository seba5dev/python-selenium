from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ie_options = webdriver.IeOptions()
ie_options.attach_to_edge_chrome = True
ie_options.edge_executable_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe --app=https://www.google.com"
ie_options.ignore_zoom_level = True
ie_options.ignore_protected_mode_settings = True

driver = webdriver.Ie(options=ie_options)
try:
    driver.get("https://www.google.com")

    driver.find_element(By.NAME, "q").send_keys("Selenium")
    driver.find_element(By.NAME, "btnK").click()

    driver.find_element(By.NAME, "q").get_attribute("value")  # => "Selenium"
except Exception as e:
    print(e)
