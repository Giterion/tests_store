from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_not_bee_basket_link_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_LINK)

