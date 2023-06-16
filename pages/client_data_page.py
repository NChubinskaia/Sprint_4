from locators.client_data_page_locators import ClientDataPageLocators
from pages.base_page import BasePage


class ClientDataPage(BasePage):

    def wait_for_load_client_data_form(self):
        self.wait_for_load(ClientDataPageLocators.CLIENT_DATA_HEADER)

    def set_name(self, name):
        self.driver.find_element(*ClientDataPageLocators.NAME_FIELD).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*ClientDataPageLocators.SURNAME_FIELD).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*ClientDataPageLocators.ADDRESS_FIELD).send_keys(address)

    def metro_field(self):
        return self.driver.find_element(*ClientDataPageLocators.METRO_FIELD)

    def click_on_metro_field(self):
        element = self.metro_field()
        self.click_on_element(element)

    def select_metro_station_in_dropdown(self, station=0):
        element = self.driver.find_element(ClientDataPageLocators.METRO_STATION[0],
                                           ClientDataPageLocators.METRO_STATION[1][station])
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def set_phone(self, phone):
        self.driver.find_element(*ClientDataPageLocators.PHONE_FIELD).send_keys(phone)

    def next_button(self):
        return self.driver.find_element(*ClientDataPageLocators.NEXT_BUTTON)

    def click_next_button(self):
        element = self.next_button()
        self.click_on_element(element)

    def fill_client_data_form(self, name, surname, address, scenario, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_on_metro_field()
        self.select_metro_station_in_dropdown(scenario)
        self.set_phone(phone)
        self.click_next_button()
