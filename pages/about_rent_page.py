from random import randint
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta
from locators.about_rent_page_locators import AboutRentPageLocators
from pages.base_page import BasePage


class AboutRentPage(BasePage):

    def wait_for_load_about_rent_header(self):
        self.wait_for_load(AboutRentPageLocators.ABOUT_RENT_HEADER)

    def set_random_rent_start_date(self):
        rent_date = str(date.today() + timedelta(days=(randint(1, 20))))
        self.driver.find_element(*AboutRentPageLocators.RENT_START_DATE_FIELD).send_keys(rent_date)
        self.driver.find_element(*AboutRentPageLocators.RENT_START_DATE_FIELD).send_keys(Keys.ENTER)

    def rental_period_field(self):
        return self.driver.find_element(*AboutRentPageLocators.RENTAL_PERIOD_FIELD)

    def click_rental_period_field(self):
        element = self.rental_period_field()
        self.click_on_element(element)

    def set_rental_period(self, days=0):
        self.driver.find_element(AboutRentPageLocators.RENTAL_PERIOD_DROPDOWN[0],
                                 AboutRentPageLocators.RENTAL_PERIOD_DROPDOWN[1][days]).click()

    def set_color_scooter_checkbox(self, color=0):
        self.driver.find_element(AboutRentPageLocators.SCOOTER_COLOR_CHECK_BOX[0],
                                 AboutRentPageLocators.SCOOTER_COLOR_CHECK_BOX[1][color]).click()

    def order_button_after_form(self):
        return self.driver.find_element(*AboutRentPageLocators.ORDER_BUTTON_AFTER_FORM)

    def click_order_button_after_form(self):
        element = self.order_button_after_form()
        self.click_on_element(element)

    def wait_for_load_confirm_popup(self):
        self.wait_for_load(AboutRentPageLocators.CONFIRM_POPUP_HEADER)

    def confirm_popup_yes_button(self):
        return self.driver.find_element(*AboutRentPageLocators.CONFIRM_POPUP_YES_BUTTON)

    def click_confirm_popup_yes_button(self):
        element = self.confirm_popup_yes_button()
        self.click_on_element(element)

    def wait_for_load_success_popup(self):
        self.wait_for_load(AboutRentPageLocators.SUCCESS_POPUP_HEADER)

    def text_success_popup_header(self):
        return self.driver.find_element(*AboutRentPageLocators.SUCCESS_POPUP_HEADER).text

    def fill_about_rent_form(self, scenario):
        self.set_random_rent_start_date()
        self.click_rental_period_field()
        self.set_rental_period(scenario)
        self.set_color_scooter_checkbox(scenario)
        self.click_order_button_after_form()
