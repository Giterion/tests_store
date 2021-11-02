from pages.main_page import MainPage
from pages.locators import ProductPageLocators
from pages.locators import MainPageLocators
from pages.product_page import ProductPage
from pages .base_page import BasePage
from pages .login_page import LoginPage
from pages .basket_page import BasketPage

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

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.correctly_book_name_in_allert_about_add_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    page.can_add_product_to_basket()
    page.guest_cant_see_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(3)
    assert page.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_CART)

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    page.can_add_product_to_basket()
    assert page.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_IN_CART)

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/'
    page = ProductPage(browser,link)
    page.open()
    page.go_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_NAME)
    assert page.is_element_present(*MainPageLocators.YOUR_CART_IS_EMPTY)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_go_to_login_link()

def test_guest_should_not_see_basket_link_in_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    time.sleep(1)
    page.to_basket()
    page.should_not_bee_basket_link_in_basket()

def test_guest_should_see_empty_basket_message(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    time.sleep(1)
    page.to_basket()
    page.basket_should_be_empty()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        #time.sleep(2)
        email = str(time.time()) + '@fakemail.org'
        password = str(time.time()) + 'S2312124ss3212d'
        page.register_new_user(email, password)
        #time.sleep(2)
        page.should_be_authorized_user()
        #time.sleep(2)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = MainPage(browser, link)
        page.open()
        #time.sleep(1)
        assert page.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_CART)

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = MainPage(browser, link)
        page.open()
        page.can_add_product_to_basket()
        #page.solve_quiz_and_get_code()
        #time.sleep(1)
        page.correctly_book_name_in_allert_about_add_to_basket()



















