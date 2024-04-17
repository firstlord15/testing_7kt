import time
from conftest import *
from config import *
from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
from page_objects.RegistrationPage import RegistrationPage

@allure.feature("Main picture")
@allure.title("Clicking right in picture")
def test(driver):
    time.sleep(100)
    MainPage(driver).click_product(0)
    ProductPage(driver).click_main_picture().right_arrow(3)

