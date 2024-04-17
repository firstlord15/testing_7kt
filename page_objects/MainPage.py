from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from config import *
import time


class MainPage(BasePage):
    INPUT_SEARCH = (
        By.CSS_SELECTOR, "div.container div.row div.col-sm-5 div.input-group > input.form-control.input-lg")
    BUTTON_CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")
    BUTTON_CART = (
        By.XPATH, "//body/nav[@id='top']/div[1]/div[1]/ul[1]/li[4]/a[1]")
    BUTTON_REGLOG = (
        By.CSS_SELECTOR, "div.container div.nav.pull-right ul.list-inline li.dropdown:nth-child(2) > a.dropdown-toggle"
    )
    BUTTON_REGISTER = (By.LINK_TEXT, "Регистрация")
    BUTTON_LOGIN = (By.LINK_TEXT, "Авторизация")
    BUTTON_HOME = (By.LINK_TEXT, "Интернет магазин Opencart")

    DROPDOWN_TABLET = (By.LINK_TEXT, "Планшеты")
    PRODUCT_TABLET = (By.LINK_TEXT, "Samsung Galaxy Tab 10.1")

    DROPDOWN_TELEPHONE_HTC = (By.LINK_TEXT, "Телефоны")
    PRODUCT_TELEPHONE_HTC = (By.LINK_TEXT, "HTC Touch HD")

    DROPDOWN_PC = (By.LINK_TEXT, "Компьютеры")
    LI_PC = (By.LINK_TEXT, "PC (0)")

    PRODUCTS = [
        (By.CSS_SELECTOR, product.format(str(i), product_element))
        for i in range(1, 5)
    ]

    PRODUCTS_BUTTON_BUY = [
        (By.CSS_SELECTOR, product.format(str(i), product_button_buy))
        for i in range(1, 5)
    ]

    PRODUCTS_BUTTON_FAVORITE = [
        (By.CSS_SELECTOR, product.format(str(i), product_button_favorite))
        for i in range(1, 5)
    ]

    LAST_INDEX = PRODUCTS[len(PRODUCTS) - 1]

    def click_product(self, index: int):
        self.click(self.PRODUCTS[index])
        time.sleep(3)
        return self

    def click_products_buy(self, count):
        for i in count:
            self.click(self.PRODUCTS_BUTTON_BUY[i])

        time.sleep(3)
        return self

    def open_registration(self):
        self.click(self.BUTTON_REGLOG)
        self.click(self.BUTTON_REGISTER)

        time.sleep(3)
        return self

    def click_search(self, text: str):
        self._input(self.INPUT_SEARCH, text)
        self.enter()
