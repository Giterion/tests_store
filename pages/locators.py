from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BOOK_NAME_IN_MESSAGE_ABOUT_ADD = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")