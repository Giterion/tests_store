from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "a#login_link"), "Login link is not presented"

    def can_add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
        add_to_basket_button.click()

    def correctly_book_name_in_allert_about_add_to_basket(self):
        assert self.browser.find_element(By.XPATH, '//strong[text()="Coders at Work"]')

    def go_to_basket(self):
        go_to_basket_button = self.browser.find_element(By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
        go_to_basket_button.click()

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_CART)

    def no_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_CART)

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_IN_CART)

    def should_not_be_message_product_in_cart(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_CART)

    def should_not_be_product_name_in_basket_opened_from_main_page(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME)

    def should_be_your_cart_is_empty(self):
        assert self.is_element_present(*MainPageLocators.YOUR_CART_IS_EMPTY)




