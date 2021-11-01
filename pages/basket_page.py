from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_bee_basket_link_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_LINK)

    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY)

