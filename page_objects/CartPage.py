from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from config import *


class CartPage(BasePage):
    BUTTON_UPDATE = (By.XPATH, "//tbody/tr[1]/td[4]/div[1]/span[1]/button[1]")
    BUTTON_DELETE = (By.XPATH, "//tbody/tr[1]/td[4]/div[1]/span[1]/button[2]")
    BUTTON_PRODUCT = (By.LINK_TEXT, "MacBook")
    INPUT_COUNT = (By.XPATH, "//tbody/tr[1]/td[4]/div[1]/input[1]")

    BUTTON_NEXT = (By.LINK_TEXT, "Продолжить покупки")
    BUTTON_MAKE_PURCHASES = (By.LINK_TEXT, "Оформление заказа")

    BUTTON_OPEN_COUPON = (By.PARTIAL_LINK_TEXT, "Использовать куп")
    BUTTON_CONFIRM_COUPON = (By.CSS_SELECTOR, "#button-coupon")
    INPUT_COUPON = (By.CSS_SELECTOR, "#input-coupon")

    BUTTON_OPEN_VOUCHER = (By.PARTIAL_LINK_TEXT, "Использовать Подароч")
    BUTTON_CONFIRM_VOUCHER = (By.CSS_SELECTOR, "#button-voucher")
    INPUT_VOUCHER = (By.CSS_SELECTOR, "#input-voucher")
