from locators.scooter_main_page_locators import ScooterMainPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class ScooterMainPage(BasePage):

    def order_header_button(self):
        return self.driver.find_element(*BasePageLocators.ORDER_HEADER_BUTTON)

    def click_on_order_header_button(self):
        element = self.order_header_button()
        self.click_on_element(element)

    def yandex_logo(self):
        return self.driver.find_element(*BasePageLocators.YANDEX_LOGO)

    def click_on_yandex_logo(self):
        element = self.yandex_logo()
        self.click_on_element(element)

    def scooter_logo(self):
        return self.driver.find_element(*BasePageLocators.SCOOTER_LOGO)

    def click_on_scooter_logo(self):
        element = self.scooter_logo()
        self.click_on_element(element)

    def scooter_main_header(self):
        return self.driver.find_element(*ScooterMainPageLocators.SCOOTER_MAIN_HEADER)

    def order_button_main_page(self):
        return self.driver.find_element(*ScooterMainPageLocators.ORDER_BUTTON_MAIN_PAGE)

    def click_on_order_button_main_page(self):
        element = self.order_button_main_page()
        self.click_on_element(element)

    def go_to_faq_header_main_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        faq_header = self.driver.find_element(*ScooterMainPageLocators.FAQ_HEADER)
        self.driver.execute_script("arguments[0].scrollIntoView();", faq_header)

    def go_to_order_button_main_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button = self.driver.find_element(*ScooterMainPageLocators.ORDER_BUTTON_MAIN_PAGE)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
