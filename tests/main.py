import time
from conftest import *
from config import *
from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
from page_objects.RegistrationPage import RegistrationPage


@allure.feature("Main picture")
@allure.title("Clicking right in picture")
def test_first_task(driver):
    time.sleep(3)
    MainPage(driver).click_product(0)
    ProductPage(driver).click_main_picture().right_arrow(3)


@allure.feature("Shopping Products")
@allure.title("Add products to cart")
def test_second_task(driver):
    time.sleep(3)
    main_Page = MainPage(driver)
    main_Page.click_products_buy([0, 1]).click(MainPage.BUTTON_CART)


@allure.feature("Main page navbar")
@allure.title("Check pc in store")
def test_third_task(driver):
    time.sleep(3)
    MainPage(driver).click(MainPage.DROPDOWN_PC).click(MainPage.LI_PC)


@allure.feature("Registration")
@allure.title("Check registration")
def test_forth_task(driver):
    time.sleep(3)
    MainPage(driver).open_registration()
    RegistrationPage(driver).registration().finish_reg()


@allure.feature("Search")
@allure.title("Input text in search")
def test_fifth_task(driver):
    time.sleep(3)
    MainPage(driver).click_search("random text!")


# Доп тесты
@allure.feature("Favorite")
@allure.title("Add random product to favorite list")
def test_first_dop_task(driver):
    time.sleep(3)
    index = MainPage(driver).random(MainPage.PRODUCTS)
    MainPage(driver).click(MainPage.PRODUCTS_BUTTON_FAVORITE[index])


@allure.feature("Last product")
@allure.title("Add last product to cart")
def test_second_dop_task(driver):
    time.sleep(3)
    MainPage(driver).click(MainPage(driver).LAST_INDEX)
    ProductPage(driver).click(ProductPage.SELECT_OPTION_COLOR)
    ProductPage(driver).click(ProductPage.BUTTON_BUY)


# дальше продолжить
@allure.feature("Tablet")
@allure.title("Add tablet to cart")
def test_third_dop_task(driver):
    time.sleep(3)
    MainPage(driver).click(MainPage.DROPDOWN_TABLET)
    MainPage(driver).click(MainPage.PRODUCT_TABLET)
    ProductPage(driver).click(ProductPage.BUTTON_BUY)


@allure.feature("Telephone")
@allure.title("Add telephone htc to cart")
def test_forth_dop_task(driver):
    time.sleep(3)
    MainPage(driver).click(MainPage.DROPDOWN_TELEPHONE_HTC)
    MainPage(driver).click(MainPage.PRODUCT_TELEPHONE_HTC)
    ProductPage(driver).click(ProductPage.BUTTON_BUY)


@allure.feature("Review")
@allure.title("Write review in product")
def test_fifth_dop_task(driver):
    time.sleep(3)
    MainPage(driver).click_product(0)
    ProductPage(driver).click(ProductPage.BUTTON_REVIEW)
    ProductPage(driver)._input(ProductPage.INPUT_NAME_REVIEW, firstname_text)
    ProductPage(driver)._input(ProductPage.INPUT_REVIEW, review_text)
    ProductPage(driver).click_review_mark(4)
    ProductPage(driver).click(ProductPage.BUTTON_NEXT_REVIEW)
