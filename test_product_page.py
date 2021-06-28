from .pages.main_page import MainPage
from .pages.base_page import BasePage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    page.can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(60)
