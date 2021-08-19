from .base_page import BasePage
from .locators import ProductPageLocators
import pytest

class ProductPage(BasePage):
    def add_to_cart_page(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_btn.click()
        #self.solve_quiz_and_get_code()
        #alert_name_product=self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME)
        #return alert_name_product.text

    def should_add_to_cart_page(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Add btn is not presented"
    def product_name(self):
        name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return name.text
    def product_price(self):
        price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return price.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"