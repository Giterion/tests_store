from selenium.webdriver.common.by import By



class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BOOK_NAME_IN_MESSAGE_ABOUT_ADD = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    YOUR_CART_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_CONFIRM_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-success.fade.in")
    MESSAGE_PRODUCT_IN_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR,"div.alertinner>strong")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")

class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")