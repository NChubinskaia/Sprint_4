# Проект автоматизации тестирования сервиса «Яндекс.Самокат»

*«Яндекс.Самокат» - сервис для заказа самокатов*</br>
*Основа для написания автотестов — фреймворк pytest*</br>
*Команда для запуска — pytest -v*</br>
*Установить зависимости — pip install -r requirements.txt*</br>
*Отчеты сформированы с помощью allure*



## Описание тестов

1. Файл tests_faq.py
+ **Class TestFaq** - содержит тесты для проверки соответствия ответов FAQ вопросам </br>
  - test_registration_true - проверка соответствия каждого ответа каждому вопросу. Тест параметризирован -
  данные для теста находятся в отдельном файле (test_data.py --> faq)
 
2. Файл test_header_logo.py
+ **Class TestHeaderLogo** - содержит тесты для проверки переходов на соответствующие страницы при нажатии на логотипы </br>
  - test_click_on_yandex_logo_go_to_yandex_true - клик на логотип Яндекс ведет на главную страницу Яндекс
  - test_click_on_scooter_logo_go_to_main_page_true - клик на логотип Самокат ведет на главную страницу приложения

3. Файл tests_order_scooter.py
+ **Class TestOrderScooter** - содержит тесты для проверки успешности заказа самоката. Тесты с параметризацией - проверка на 2-х наборах данных. Параметр scenario принимает индекс сценария (индекс локатора) 0 или 1 для каждого теста. 
  - test_order_scooter_by_header_button_success - успешный сценарий заказа самоката через кнопку "Заказать" в хэдере
  - test_order_scooter_by_order_main_page_button_success - успешный сценарий заказа самоката через кнопку "Заказать" на главной странице

## Директория pages

Каждый файл содержит класс определенной страницы приложения, конструктор класса и описание действий с элементами страницы, как методов класса

1. Файл header_page.py - **Class HeaderPage** - хэдер приложения
2. Файл scooter_main_page.py - **Class ScooterMainPage** - главная страница приложения
3. Файл client_data_page.py - **Class ClientDataPage** - страница с заголовком "Для кого самокат"
4. Файл about_rent_page.py - **Class AboutRentPage** - страница "Про аренду"


## Директория locators

Каждый файл содержит локаторы определенной страницы приложения

1. Файл header_page_locators.py - **Class HeaderPageLocators** - локаторы хэдера приложения
2. Файл scooter_main_page_locators.py - **Class ScooterMainPageLocators** - локаторы главной страница приложения
3. Файл client_data_page_locators.py - **Class ClientDataPageLocators** - локаторы страницы с заголовком "Для кого самокат"
4. Файл about_rent_page_locators.py - **Class AboutRentPageLocators** - локаторы страницы "Про аренду"
5. Файл external_locators.py -**Class ExternalLocators** - содержит необходимые для тестов внешние локаторы



## Дополнительные файлы и папки

1. Файл conftest.py - содержит следующие фикстуры:
   - **get_driver** - для открытия/инициализации/закрытия браузера
 

2. Файл test_data.py - вспомогательный файл, содержащий объемные тестовые данные
3. Файл requirements.txt - файл со списком внешних зависимостей
4. Папка allure_results - содержит файл с отчетами о тестировании

