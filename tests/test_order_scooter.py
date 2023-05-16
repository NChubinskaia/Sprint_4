import pytest
import allure
from pages.client_data_page import ClientDataPage
from pages.about_rent_page import AboutRentPage
from pages.scooter_main_page import ScooterMainPage
from test_data import Person


@pytest.mark.parametrize('name, surname, address, phone, scenario', Person.scenarios)
class TestOrderScooter:

    @allure.title('Успешный сценарий заказа самоката через кнопку "Заказать" в хэдере')
    def test_order_scooter_by_header_button_success(self, driver, name, surname, address, phone, scenario):
        scooter_main_page = ScooterMainPage(driver)
        with allure.step('Переход на страницу "Для кого самокат" по кнопке "Заказать" в хэдере'):
            scooter_main_page.click_on_order_header_button()
        client_data_page = ClientDataPage(driver)
        client_data_page.wait_for_load_client_data_form()
        with allure.step('Заполнение формы на странице "Для кого самокат"'):
            client_data_page.fill_client_data_form(name, surname, address, scenario, phone)
        about_rent_page = AboutRentPage(driver)
        about_rent_page.wait_for_load_about_rent_header()
        with allure.step('Заполнение формы на странице "Про аренду"'):
            about_rent_page.fill_about_rent_form(scenario)
        about_rent_page.wait_for_load_confirm_popup()
        with allure.step('Нажатие на кнопку "Да" в попапе с подтверждением заказа'):
            about_rent_page.click_confirm_popup_yes_button()
        about_rent_page.wait_for_load_success_popup()
        with allure.step('Проверка, что заголовок попапа "Заказ оформлен" совпадает с ожидаемым результатом'):
            expected_result = 'Заказ оформлен'
            actual_result = about_rent_page.text_success_popup_header()
            assert expected_result in actual_result, f'Ожидалось значение: "{expected_result}", ' \
                                                     f'фактическое: "{actual_result}"'

    @allure.title('Успешный сценарий заказа самоката через кнопку "Заказать" на главной странице Яндекс.Самокат')
    def test_order_scooter_by_order_main_page_button_success(self, driver, name, surname, address, phone, scenario):
        scooter_main_page = ScooterMainPage(driver)
        with allure.step('Переход к кнопке "Заказать на главной странице Яндекс.Самокат"'):
            scooter_main_page.go_to_order_button_main_page()
        with allure.step('Клик по кнопке "Заказать на главной странице Яндекс.Самокат"'):
            scooter_main_page.click_on_order_button_main_page()
        client_data_page = ClientDataPage(driver)
        client_data_page.wait_for_load_client_data_form()
        with allure.step('Заполнение формы на странице "Для кого самокат"'):
            client_data_page.fill_client_data_form(name, surname, address, scenario, phone)
        about_rent_page = AboutRentPage(driver)
        about_rent_page.wait_for_load_about_rent_header()
        with allure.step('Заполнение формы на странице "Про аренду"'):
            about_rent_page.fill_about_rent_form(scenario)
        about_rent_page.wait_for_load_confirm_popup()
        with allure.step('Нажатие на кнопку "Да" в попапе с подтверждением заказа'):
            about_rent_page.click_confirm_popup_yes_button()
        about_rent_page.wait_for_load_success_popup()
        with allure.step('Проверка, что заголовок попапа "Заказ оформлен" совпадает с ожидаемым результатом'):
            expected_result = 'Заказ оформлен'
            actual_result = about_rent_page.text_success_popup_header()
            assert expected_result in actual_result, f'Ожидалось значение: "{expected_result}", ' \
                                                     f'фактическое: "{actual_result}"'
