from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

driver.save_screenshot("google_homepage.png")

driver.quit()
