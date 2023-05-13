from selenium.webdriver.common.by import By


class ScooterMainPageLocators:

        # кнопка Заказать на главной странице
        ORDER_BUTTON_MAIN_PAGE = [By.XPATH, '//div[@class = "Home_FinishButton__1_cWm"]/button']

        # заголовок FAQ Вопросы о важном
        FAQ_HEADER = [By.XPATH, '//div[text() = "Вопросы о важном"]']

        # вопросы в FAQ
        FAQ_QUESTION = [By.XPATH, '//div[@id = "accordion__heading-{}"]']

        # ответы в FAQ
        FAQ_ANSWER = [By.XPATH, '//div[@id = "accordion__panel-{}"]']
