import allure
import pytest
from pages.scooter_main_page import ScooterMainPage
from locators.scooter_main_page_locators import ScooterMainPageLocators
from test_data import faq


class TestFaq:
    @allure.title('Проверка соответствия ответа вопросу в FAQ на главной странице Яндекс.Самокат')
    @allure.description('На странице кликаем на вопрос в FAQ и проверяем, что открывается соответствующий текст"')
    @pytest.mark.parametrize('question, answer, result', faq)
    def test_question_match_answer_true(self, driver, question, answer, result):
        scooter_main_page = ScooterMainPage(driver)
        with allure.step('Прокрутка страницы до заголовка "Вопросы о важном"'):
            scooter_main_page.go_to_faq_header_main_page()
        with allure.step('Выбор вопроса в FAQ и клик на него'):
            method1, locator1 = ScooterMainPageLocators.FAQ_QUESTION
            locator1 = locator1.format(question)
            question = driver.find_element(method1, locator1)
            question.click()
        with allure.step('Сравнение текста появившегося ответа с ожидаемым результатом'):
            method2, locator2 = ScooterMainPageLocators.FAQ_ANSWER
            locator2 = locator2.format(answer)
            answer = driver.find_element(method2, locator2).text
            assert result == answer, f'Ожидалось значение: "{result}", фактическое: "{answer}"'
