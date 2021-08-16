from pages.locators import ProductPageLocators
from .pages.main_page import MainPage
from .pages.base_page import BasePage
import time
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])


# def test_guest_can_add_product_to_basket(browser, link):
#     page = MainPage(browser, link)
#     page.open()
#     page.can_add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     time.sleep(1)
#     page.correctly_book_name_in_allert_about_add_to_basket()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(3)
    page.can_add_product_to_basket()
    time.sleep(3)
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(3)
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(3)
    page.can_add_product_to_basket()
    time.sleep(3)
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)








