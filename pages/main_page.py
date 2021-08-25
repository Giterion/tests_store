# from .base_page import BasePage
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from .base_page import BasePage


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



# messages > div:nth-child(1) > div > strong
# def should_be_login_link(self):
#     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"