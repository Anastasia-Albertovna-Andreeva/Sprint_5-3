import pytest
from selenium.webdriver.common.by import By

class Locator:
    # Страница регистрации
    input_name = By.XPATH, '//label[text()="Имя"]/following-sibling::input'  # Поле "Имя"
    input_email = By.XPATH, './/label[text()="Email"]/following-sibling::input'  # Поле Email
    input_password = By.XPATH, './/input[@name="Пароль"]' # Поле "Пароль"
    button_submit = By.XPATH, '//button[text() = "Зарегистрироваться"]' # Кнопка "Зарегистрироваться"
    notification_incorrect_password = By.XPATH, '//p[text() = "Некорректный пароль"]' # Сообщение об ошибке: пароль не прошел валидацию
    button_login_in_registration_form = By.XPATH, '//a[text() = "Войти"]' # Кнопка "Войти" на форме регистрации
    login_header_tag_h2 = By.XPATH, './/h2[text()="Вход"]'  # Заголовок "Вход"
    user_exists_message = By.XPATH, './/div/main/div/p[text()="Такой пользователь уже существует"]'

    # Страница авторизации
    input_email_auth = By.XPATH, '//label[text()="Email"]/following-sibling::input'  # Поле Email
    input_password_auth = By.XPATH, '//input[@name = "Пароль"]' # Поле "Пароль"
    button_login = By.XPATH, '//button[text()="Войти"]' # Кнопка "Войти"
    button_register = By.XPATH, '//a[text() = "Зарегистрироваться"]' # Кнопка "Зарегистрироваться"

    # Восстановление пароля
    button_forgot_password = By.XPATH, '//a[text() = "Восстановить пароль"]' # Кнопка "Восстановить пароль"
    button_login_passwd_recovery_form = By.XPATH, '//a[text() = "Войти"]' # Кнопка "Войти" в форме восстановления пароля

    # Личный кабинет
    profile = By.XPATH, '//a[@href = "/account/profile"]' # Профиль пользователя
    order_history = By.XPATH, '//a[@href = "/account/order-history"]' # История заказов
    button_logout = By.XPATH, '//button[@type = "button"]'  # Кнопка "Выйти"

    # Главная страница сервиса
    button_login_in_main = By.XPATH, './/button[text() = "Войти в аккаунт"]' # Кнопка "Войти в аккаунт" на главной
    button_personal_account = By.XPATH, '//p[text() = "Личный Кабинет"]' # Кнопка "Личный кабинет"
    button_make_the_order = By.XPATH, '//button[text()="Оформить заказ"]' # Кнопка "Оформить заказ"
    header_of_page_constructor = By.XPATH, '//p[text() = "Конструктор"]' # Кнопка "Конструктор" в шапке сайта
    bulki_block = By.XPATH, '//span[text() = "Булки"]' # Заголовок раздела "Булки" в конструкторе
    bulki_list = By.XPATH, './/h2[text()="Булки"]'  # Список "Булки"
    sauces_block = By.XPATH, '//span[text() = "Соусы"]' # Заголовок раздела "Соусы" в конструкторе
    souses_list = By.XPATH, './/h2[text()="Соусы"]'  # Список "Соусы"
    nachinki_block = By.XPATH, '//span[text() = "Начинки"]' # Заголовок раздела "Начинки" в меню конструктора
    nachinki_list = By.XPATH, './/h2[text()="Начинки"]'  # Список "Начинки"
    logo = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]' # Кликабельный логотип в шапке сайта