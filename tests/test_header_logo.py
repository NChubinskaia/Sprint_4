import allure
from pages.header_page import HeaderPage
from locators.external_locators import ExternalLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestHeaderLogo:

    @allure.title('Проверка перехода на главную страницу Яндекса при клике на логотип "Яндекс" в хэдере')
    def test_click_on_yandex_logo_go_to_yandex_true(self, driver):
        header_page = HeaderPage(driver)
        with allure.step('Клик на логотип "Яндекс" в хэдере'):
            header_page.click_on_yandex_logo()
        with allure.step('Переход на последнюю открывшуюся вкладку в браузере'):
            header_page.driver.switch_to.window(header_page.driver.window_handles[-1])
        WebDriverWait(header_page.driver, 3).until(
                expected_conditions.visibility_of_element_located(ExternalLocators.DZEN_LOGO))
        with allure.step('Сравнение, что фактический URL равен ожидаемому'):
            expected_url = 'https://dzen.ru/?yredirect=true'
            actual_url = header_page.driver.current_url
            assert expected_url == actual_url, f'Ожидалось значение: "{expected_url}", фактическое: "{actual_url}"'

    @allure.title('Проверка перехода на главную страницу Яндекс.Самоката при клике на логотип "Самокат" в хэдере')
    def test_click_on_scooter_logo_go_to_main_page_true(self, driver):
        header_page = HeaderPage(driver)
        with allure.step('Переход на страницу "Для кого самокат" по кнопке "Заказать" в хэдере'):
            header_page.click_on_order_header_button()
        with allure.step('Клик на логотип "Самокат" в хэдере'):
            header_page.click_on_scooter_logo()
        with allure.step('Сравнение, что фактический URL равен ожидаемому'):
            expected_url = 'https://qa-scooter.praktikum-services.ru/'
            actual_url = header_page.driver.current_url
            assert expected_url == actual_url, f'Ожидалось значение: "{expected_url}", фактическое: "{actual_url}"'
