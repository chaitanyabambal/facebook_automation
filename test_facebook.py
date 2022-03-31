import pytest
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setUp():
    global product,driver
    username = input("enter username")
    password = input("enter password")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()
def test_searchproducts(setUp):

    driver.get("https://www.facebook.com/")
    time.sleep(1)
    driver.find_element_by_name("email").send_keys(username)
    time.sleep((1))
    driver.find_element_by_name("pass").send_keys(password)
    time.sleep(1)
    driver.find_element_by_name("login").click()
    time.sleep(30)