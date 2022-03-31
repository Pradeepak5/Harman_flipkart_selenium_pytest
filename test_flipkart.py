from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def setUp():
    global driver,product
    product = input("Enter the product to be searched :")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(15)
    driver.close()
    print("Tested Successfully")

def test_search_product(setUp):
    driver.get("https://www.flipkart.com/")
    driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    driver.find_element_by_name("q").send_keys(product)
    driver.find_element_by_class_name("L0Z3Pu").click()

