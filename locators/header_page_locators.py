from selenium.webdriver.common.by import By


class HeaderPageLocators:

    # кнопка Заказать в хэдере
    ORDER_HEADER_BUTTON = [By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]']

    # логотип Яндекс
    YANDEX_LOGO = [By.XPATH, '//a[@class = "Header_LogoYandex__3TSOI"]']

    # логотип Самокат
    SCOOTER_LOGO = [By.XPATH, '//a[@class = "Header_LogoScooter__3lsAR"]']
