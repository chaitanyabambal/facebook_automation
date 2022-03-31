import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
username=input("enter username")
password=input("enter password")
print("Test case started!")
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(1)
driver.find_element_by_name("email").send_keys(username)
time.sleep((1))
driver.find_element_by_name("pass").send_keys(password)
time.sleep(1)
driver.find_element_by_name("login").click()
time.sleep(30)
driver.close()
print("Test case has sucessfully completed!")