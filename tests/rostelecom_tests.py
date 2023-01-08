import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing(selenium):
    selenium.get('https://b2c.passport.rt.ru')
    yield
    selenium.quit()


def test_1_login_valid_phone_valid_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с валидными номером телефона и паролем"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "телефон" используя явное ожидание "кликабельности" элемента
    btn_phone = WebDriverWait(selenium,
                              5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    btn_phone.click()
    # очищаем поле ввода телефона и вводим валидный телефон
    field_phone = selenium.find_element_by_id('username')
    field_phone.clear()
    field_phone.send_keys('79373860001')
    # очищаем поле ввода пароля и вводим валидный пароль
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('0Okm*uhb')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем что после успешной авторизации мы оказались в личном кабинете
    assert selenium.find_element_by_id('lk-btn').text == "Личный кабинет", "login error"


def test_2_login_valid_email_valid_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с валидными email и паролем"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "почта" используя явное ожидание "кликабельности" элемента
    btn_email = WebDriverWait(selenium,
                              10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-mail"]')))
    btn_email.click()
    # очищаем поле ввода email и вводим валидный email
    field_email = selenium.find_element_by_id('username')
    field_email.clear()
    field_email.send_keys('japanflower@rambler.ru')
    # очищаем поле ввода пароля и вводим валидный пароль
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('0Okm*uhb')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем что после успешной авторизации мы оказались в личном кабинете
    assert selenium.find_element_by_id('lk-btn').text == "Личный кабинет", "login error"


def test_3_login_valid_phone_invalid_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с валидным номером телефона и
    невалидным паролем в 7 символов"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "телефон" используя явное ожидание "кликабельности" элемента
    btn_phone = WebDriverWait(selenium,
                              5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    btn_phone.click()
    # очищаем поле ввода телефона и вводим валидный телефон
    field_phone = selenium.find_element_by_id('username')
    field_phone.clear()
    field_phone.send_keys('79373860001')
    # очищаем поле ввода пароля и вводим невалидный пароль
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('0Okm*uh')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем что появляется сообщение "Неверный логин или пароль"
    assert selenium.find_element_by_xpath('//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_4_login_valid_email_invalid_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с валидным email и
    невалидным паролем в 7 символов"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "почта" используя явное ожидание "кликабельности" элемента
    btn_email = WebDriverWait(selenium,
                              10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-mail"]')))
    btn_email.click()
    # очищаем поле ввода email и вводим валидный email
    field_email = selenium.find_element_by_id('username')
    field_email.clear()
    field_email.send_keys('japanflower@rambler.ru')
    # очищаем поле ввода пароля и вводим невалидный пароль
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('0Okm*uh')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем что появляется сообщение "Неверный логин или пароль"
    assert selenium.find_element_by_xpath('//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_5_login_invalid_phone_valid_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с невалидным номером телефона и валидным паролем"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "телефон" используя явное ожидание "кликабельности" элемента
    btn_phone = WebDriverWait(selenium,
                              5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    btn_phone.click()
    # очищаем поле ввода телефона и вводим невалидный телефон
    field_phone = selenium.find_element_by_id('username')
    field_phone.clear()
    field_phone.send_keys('7937386000')
    # очищаем поле ввода пароля и вводим валидный пароль
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('0Okm*uhb')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем наличие сообщения под полем ввода телефона: "Неверный формат телефона"
    assert selenium.find_element_by_xpath('//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == \
           "Неверный формат телефона"


def test_6_login_invalid_email_valid_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с невалидным email и валидным паролем"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "почта" используя явное ожидание "кликабельности" элемента
    btn_email = WebDriverWait(selenium,
                              10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-mail"]')))
    btn_email.click()
    # очищаем поле ввода email и вводим невалидный email
    field_email = selenium.find_element_by_id('username')
    field_email.clear()
    field_email.send_keys('japanflower@rambler.com')
    # очищаем поле ввода пароля и вводим валидный пароль
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('0Okm*uhb')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем что появляется сообщение "Неверный логин или пароль"
    assert selenium.find_element_by_xpath('//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_7_login_empty_phone_empty_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с пустыми полями ввода номера телефона и пароля"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "телефон" используя явное ожидание "кликабельности" элемента
    btn_phone = WebDriverWait(selenium,
                              5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    btn_phone.click()
    # очищаем поле ввода телефона и оставляем его пустым
    field_phone = selenium.find_element_by_id('username')
    field_phone.clear()
    field_phone.send_keys('')
    # очищаем поле ввода пароля и оставляем его пустым
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем наличие сообщения под полем ввода телефона: "Введите номер телефона"
    assert selenium.find_element_by_xpath('//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == \
           "Введите номер телефона"


def test_8_login_empty_email_empty_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с пустыми полями ввода email и пароля"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "почта" используя явное ожидание "кликабельности" элемента
    btn_email = WebDriverWait(selenium,
                              10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-mail"]')))
    btn_email.click()
    # очищаем поле ввода email и оставляем его пустым
    field_email = selenium.find_element_by_id('username')
    field_email.clear()
    field_email.send_keys('')
    # очищаем поле ввода пароля и оставляем его пустым
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем что появляется сообщение "Введите адрес, указанный при регистрации"
    assert selenium.find_element_by_xpath('//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text\
           == "Введите адрес, указанный при регистрации"


def test_9_login_empty_phone_valid_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с пустым полем ввода номера телефона и валидным паролем"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "телефон" используя явное ожидание "кликабельности" элемента
    btn_phone = WebDriverWait(selenium,
                              5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    btn_phone.click()
    # очищаем поле ввода телефона и оставляем его пустым
    field_phone = selenium.find_element_by_id('username')
    field_phone.clear()
    field_phone.send_keys('')
    # очищаем поле ввода пароля и вводим валидный пароль
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('0Okm*uhb')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем наличие сообщения под полем ввода телефона: "Введите номер телефона"
    assert selenium.find_element_by_xpath('//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == \
           "Введите номер телефона"


def test_10_login_empty_email_valid_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с пустым полем ввода email и валидным паролем"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "почта" используя явное ожидание "кликабельности" элемента
    btn_email = WebDriverWait(selenium,
                              10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-mail"]')))
    btn_email.click()
    # очищаем поле ввода email и оставляем его пустым
    field_email = selenium.find_element_by_id('username')
    field_email.clear()
    field_email.send_keys('')
    # очищаем поле ввода пароля и вводим валидный пароль
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('0Okm*uhb')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем что появляется сообщение "Введите адрес, указанный при регистрации"
    assert selenium.find_element_by_xpath('//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text\
           == "Введите адрес, указанный при регистрации"


def test_11_login_invalid_phone_invalid_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с невалидным телефоном и
    невалидным паролем в 9 символов"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "телефон" используя явное ожидание "кликабельности" элемента
    btn_phone = WebDriverWait(selenium,
                              5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    btn_phone.click()
    # очищаем поле ввода телефона и вводим невалидный телефон
    field_phone = selenium.find_element_by_id('username')
    field_phone.clear()
    field_phone.send_keys('7937386000')
    # очищаем поле ввода пароля и вводим невалидный пароль
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('Okm*uhbb')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем наличие сообщения под полем ввода телефона: "Неверный формат телефона"
    assert selenium.find_element_by_xpath('//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == \
           "Неверный формат телефона"


def test_12_login_invalid_email_invalid_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с невалидным email и
    невалидным паролем в 9 символов"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "почта" используя явное ожидание "кликабельности" элемента
    btn_email = WebDriverWait(selenium,
                              10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-mail"]')))
    btn_email.click()
    # очищаем поле ввода email и вводим невалидный email
    field_email = selenium.find_element_by_id('username')
    field_email.clear()
    field_email.send_keys('japanflower@rambler.com')
    # очищаем поле ввода пароля и вводим невалидный пароль
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('Okm*uhbb')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем что появляется сообщение "Неверный логин или пароль"
    assert selenium.find_element_by_xpath('//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_13_login_valid_phone_pass_symbols(selenium):
    """ Данный тест проверяет процедуру авторизации с валидным номером телефона и паролем из спецсимволов"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "телефон" используя явное ожидание "кликабельности" элемента
    btn_phone = WebDriverWait(selenium,
                              5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    btn_phone.click()
    # очищаем поле ввода телефона и вводим валидный телефон
    field_phone = selenium.find_element_by_id('username')
    field_phone.clear()
    field_phone.send_keys('79373860001')
    # очищаем поле ввода пароля и вводим пароль из спецсимволов
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('£€¶§©®™ΔΞψ½')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем что появляется сообщение "Неверный логин или пароль"
    assert selenium.find_element_by_xpath('//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_14_login_valid_email_pass_symbols(selenium):
    """ Данный тест проверяет процедуру авторизации с валидным email и паролем из спецсимволов"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "почта" используя явное ожидание "кликабельности" элемента
    btn_email = WebDriverWait(selenium,
                              10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-mail"]')))
    btn_email.click()
    # очищаем поле ввода email и вводим валидный email
    field_email = selenium.find_element_by_id('username')
    field_email.clear()
    field_email.send_keys('japanflower@rambler.ru')
    # очищаем поле ввода пароля и вводим пароль из спецсимволов
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('£€¶§©®™ΔΞψ½')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем что появляется сообщение "Неверный логин или пароль"
    assert selenium.find_element_by_xpath('//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_15_login_valid_phone_pass_256symbols(selenium):
    """ Данный тест проверяет процедуру авторизации с валидным номером телефона и паролем из 256 символов"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "телефон" используя явное ожидание "кликабельности" элемента
    btn_phone = WebDriverWait(selenium,
                              5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    btn_phone.click()
    # очищаем поле ввода телефона и вводим валидный телефон
    field_phone = selenium.find_element_by_id('username')
    field_phone.clear()
    field_phone.send_keys('79373860001')
    # очищаем поле ввода пароля и вводим пароль 256 символов
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем что появляется сообщение "Ошибка", и после нескольких секунд происходит redirect
    # на страницу авторизации
    assert selenium.find_element_by_xpath('//*[@id="page-right"]/div/div/h1').text == "Ошибка"


def test_16_login_valid_email_pass_256symbols(selenium):
    """ Данный тест проверяет процедуру авторизации с валидным email и паролем из 256 символов"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "почта" используя явное ожидание "кликабельности" элемента
    btn_email = WebDriverWait(selenium,
                              10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-mail"]')))
    btn_email.click()
    # очищаем поле ввода email и вводим валидный email
    field_email = selenium.find_element_by_id('username')
    field_email.clear()
    field_email.send_keys('japanflower@rambler.ru')
    # очищаем поле ввода пароля и вводим пароль 256 символов
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем что появляется сообщение "Ошибка", и после нескольких секунд происходит redirect
    # на страницу авторизации
    assert selenium.find_element_by_xpath('//*[@id="page-right"]/div/div/h1').text == "Ошибка"


def test_17_login_valid_phone_space_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с валидным номером телефона и
    содержащим вначале пробелы паролем"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "телефон" используя явное ожидание "кликабельности" элемента
    btn_phone = WebDriverWait(selenium,
                              5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    btn_phone.click()
    # очищаем поле ввода телефона и вводим валидный телефон
    field_phone = selenium.find_element_by_id('username')
    field_phone.clear()
    field_phone.send_keys('79373860001')
    # очищаем поле ввода пароля и вводим содержащий вначале пробелы пароль
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('  0Okm*uhb')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # Система автоматически удаляет пробелы при вводе поэтому осуществляется успешный вход в систему
    assert selenium.find_element_by_id('lk-btn').text == "Личный кабинет", "login error"


def test_18_login_valid_email_space_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с валидными email и
    содержащим вначале пробелы паролем"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "почта" используя явное ожидание "кликабельности" элемента
    btn_email = WebDriverWait(selenium,
                              10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-mail"]')))
    btn_email.click()
    # очищаем поле ввода email и вводим валидный email
    field_email = selenium.find_element_by_id('username')
    field_email.clear()
    field_email.send_keys('japanflower@rambler.ru')
    # очищаем поле ввода пароля и вводим содержащий вначале пробелы пароль
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('  0Okm*uhb')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # Система автоматически удаляет пробелы при вводе поэтому осуществляется успешный вход в систему
    assert selenium.find_element_by_id('lk-btn').text == "Личный кабинет", "login error"


def test_19_login_valid_caps_email_pass(selenium):
    """ Данный тест проверяет процедуру авторизации с валидными email написанным заглавными буквами и
    валидным паролем"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "почта" используя явное ожидание "кликабельности" элемента
    btn_email = WebDriverWait(selenium,
                              10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-mail"]')))
    btn_email.click()
    # очищаем поле ввода email и вводим валидный email из заглавных букв
    field_email = selenium.find_element_by_id('username')
    field_email.clear()
    field_email.send_keys('JAPANFLOWER@RAMBLER.RU')
    # очищаем поле ввода пароля и вводим содержащий вначале пробелы пароль
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('0Okm*uhb')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # Система автоматически заменяет заглавные буквы на строчные поэтому осуществляется
    # успешный вход в систему
    assert selenium.find_element_by_id('lk-btn').text == "Личный кабинет", "login error"


def test_20_login_valid_phone_pass_with_sql(selenium):
    """ Данный тест проверяет процедуру авторизации с валидным номером телефона и
    паролем содержащим SQL injections"""
    selenium.maximize_window()
    # выполняем нажатие вкладки "телефон" используя явное ожидание "кликабельности" элемента
    btn_phone = WebDriverWait(selenium,
                              5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    btn_phone.click()
    # очищаем поле ввода телефона и вводим валидный телефон
    field_phone = selenium.find_element_by_id('username')
    field_phone.clear()
    field_phone.send_keys('79373860001')
    # очищаем поле ввода пароля и вводим пароль содержащий SQL запрос
    field_pass = selenium.find_element_by_id('password')
    field_pass.clear()
    field_pass.send_keys('DROP TABLE user')
    # нажимаем оранжевую кнопку "Войти"
    btn_login = selenium.find_element_by_id('kc-login')
    btn_login.click()
    # проверяем что появляется сообщение "Неверный логин или пароль"
    assert selenium.find_element_by_xpath('//*[@id="form-error-message"]').text == "Неверный логин или пароль"

# python -m pytest -v --driver Chrome --driver-path C:/WebDriver/chromedriver.exe rostelecom_tests.py
