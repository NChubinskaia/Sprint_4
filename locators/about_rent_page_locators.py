from selenium.webdriver.common.by import By


class AboutRentPageLocators:

    # заголовок Про аренду
    ABOUT_RENT_HEADER = [By.XPATH, '//div[text() = "Про аренду"]']

    # поле Когда привезти самокат
    RENT_START_DATE_FIELD = [By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]']

    # поле Срок аренды
    RENTAL_PERIOD_FIELD = [By.XPATH, '//div[text() = "* Срок аренды"]']

    # дропдаун Срок аренды (трое суток/сутки)
    RENTAL_PERIOD_DROPDOWN = [By.XPATH, ['//div[text() = "трое суток"]', '//div[text() = "сутки"]']]

    # чек-боксы Цвет самоката (Черный жемчуг/Серая безысходность)
    SCOOTER_COLOR_CHECK_BOX = [By.XPATH, ['//input[@id = "black"]', '//input[@id = "grey"]']]

    # кнопка Заказать после формы Про аренду
    ORDER_BUTTON_AFTER_FORM = [By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text() = "Заказать"]']

    # заголовок в попапе Хотите оформить заказ?
    CONFIRM_POPUP_HEADER = [By.XPATH, '//div[text() = "Хотите оформить заказ?"]']

    # кнопка Да в попапе Хотите оформить заказ?
    CONFIRM_POPUP_YES_BUTTON = [By.XPATH, '//button[text() = "Да"]']

    # заголовок в попапе Заказ оформлен
    SUCCESS_POPUP_HEADER = [By.XPATH, '//div[text() = "Заказ оформлен"]']
