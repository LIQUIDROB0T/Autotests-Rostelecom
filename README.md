Описание
--------
Данный репозиторий содержит автотесты тестирования формы авторизации на странице [Ростелеком](https://b2c.passport.rt.ru)

[Документация](https://docs.google.com/spreadsheets/d/1_y5dEBcIX9OW30eGUw-xQoXByDqCuTOWCVuwG2hnmmM/edit?usp=sharing) содержит:
* Чек-лист тестирования требований
* Чек-лист тестирования атрибутивного состава форм авторизации, регистрации, восстановления пароля
* Тест-кейсы тестирования формы авторизации
* Баг-репорты
* Описание

Как запустить тест?
----------------

1) Установить необходимые библиотеки:

    ```bash
    pip install -r requirements.txt
    ```

2) Скачать Selenium WebDriver с https://chromedriver.chromium.org/downloads (выбрать версию подходящую под ваш браузер)

3) Запуск теста:

    ```bash
    python -m pytest -v --driver Chrome --driver-path ~путь/driver.exe tests/rostelecom_tests.py
    ```
