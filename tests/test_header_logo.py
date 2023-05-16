import allure
from locators.external_locators import ExternalLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from pages.scooter_main_page import ScooterMainPage
from urls import dzen_url, base_url


class TestHeaderLogo:

    @allure.title('Проверка перехода на главную страницу Яндекса при клике на логотип "Яндекс" в хэдере')
    def test_click_on_yandex_logo_go_to_yandex_true(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        with allure.step('Клик на логотип "Яндекс" в хэдере'):
            scooter_main_page.click_on_yandex_logo()
        with allure.step('Переход на последнюю открывшуюся вкладку в браузере'):
            scooter_main_page.driver.switch_to.window(scooter_main_page.driver.window_handles[-1])
        WebDriverWait(scooter_main_page.driver, 3).until(
                expected_conditions.visibility_of_element_located(ExternalLocators.DZEN_LOGO))
        with allure.step('Сравнение, что фактический URL равен ожидаемому и страница загрузилась'):
            actual_url = scooter_main_page.driver.current_url
            try:
                driver.find_element(*ExternalLocators.DZEN_LOGO)
                dzen_logo_found = True
            except NoSuchElementException:
                dzen_logo_found = False
            assert dzen_logo_found == True and dzen_url == actual_url, \
                f'Ожидалось значение: "{dzen_url}", фактическое: "{actual_url}"'

    @allure.title('Проверка перехода на главную страницу Яндекс.Самоката при клике на логотип "Самокат" в хэдере')
    def test_click_on_scooter_logo_go_to_main_page_true(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        with allure.step('Переход на страницу "Для кого самокат" по кнопке "Заказать" в хэдере'):
            scooter_main_page.click_on_order_header_button()
        with allure.step('Клик на логотип "Самокат" в хэдере'):
            scooter_main_page.click_on_scooter_logo()
        with allure.step('Сравнение, что фактический URL равен ожидаемому и страница загрузилась'):
            actual_url = scooter_main_page.driver.current_url
            try:
                scooter_main_page.scooter_main_header()
                main_header_found = True
            except NoSuchElementException:
                main_header_found = False
            assert main_header_found == True and base_url == actual_url, \
                f'Ожидалось значение: "{base_url}", фактическое: "{actual_url}"'
