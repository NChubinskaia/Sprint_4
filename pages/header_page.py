from locators.header_page_locators import HeaderPageLocators


class HeaderPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_order_header_button(self):
        self.driver.find_element(*HeaderPageLocators.ORDER_HEADER_BUTTON).click()

    def click_on_yandex_logo(self):
        self.driver.find_element(*HeaderPageLocators.YANDEX_LOGO).click()

    def click_on_scooter_logo(self):
        self.driver.find_element(*HeaderPageLocators.SCOOTER_LOGO).click()



