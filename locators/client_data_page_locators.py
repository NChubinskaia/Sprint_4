from selenium.webdriver.common.by import By


class ClientDataPageLocators:

    # заголовок "Для кого самокат"
    CLIENT_DATA_HEADER = [By.XPATH, '//div[text() = "Для кого самокат"]']

    # поле Имя
    NAME_FIELD = [By.XPATH, '//input[@placeholder = "* Имя"]']

    # поле Фамилия
    SURNAME_FIELD = [By.XPATH, '//input[@placeholder = "* Фамилия"]']

    # поле Адрес: куда привезти заказ
    ADDRESS_FIELD = [By.XPATH, '//input[@placeholder = "* Адрес: куда привезти заказ"]']

    # поле Станция метро
    METRO_FIELD = [By.XPATH, '//input[@placeholder = "* Станция метро"]']

    # дропдаун со станциями метро (станция Чеховская/последняя станция в списке)
    METRO_STATION = [By.XPATH, ['//div[text() = "Чеховская"]', '//li[last()]']]

    # поле Телефон
    PHONE_FIELD = [By.XPATH, '//input[@placeholder = "* Телефон: на него позвонит курьер"]']

    # кнопка Далее
    NEXT_BUTTON = [By.XPATH, '//button[text() = "Далее"]']
