from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import CorrectUsersData, TestUser2
from urls import URL
from locators import Locator

class TestLogin:
    def test_login_from_home_page(self, driver):
        driver.get(URL.home)  # Переход на главную домашнюю страницу
        driver.find_element(*Locator.button_login_in_main).click()  # Нажатие на кнопку "Войти в аккаунт" на главной странице
        driver.find_element(*Locator.input_email_auth).send_keys(CorrectUsersData.email)
        driver.find_element(*Locator.input_password_auth).send_keys(CorrectUsersData.password)
        driver.find_element(*Locator.button_login).click()  # Нажатие на кнопку "Войти" на странице входа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.button_make_the_order))
        assert driver.find_element(*Locator.button_make_the_order).is_displayed()

    def test_login_from_recovery_pass(self, driver):
        driver.get(URL.password_reset)  # Переход на страницу восстановления пароля
        driver.find_element(*Locator.button_login_passwd_recovery_form).click()  # Нажатие на кнопку "Войти"
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.button_login))  # Ожидание появления полей логина
        driver.find_element(*Locator.input_email_auth).send_keys(CorrectUsersData.email)
        driver.find_element(*Locator.input_password_auth).send_keys(CorrectUsersData.password)
        driver.find_element(*Locator.button_login).click()
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.button_make_the_order))  # Ожидание кнопки "Оформить заказ"
        assert driver.find_element(*Locator.button_make_the_order).is_displayed()  # Проверка отображения кнопки

    def test_login_from_registration_page(self, driver):
        driver.get(URL.signup)  # Переход на страницу регистрации
        driver.find_element(*Locator.button_login_in_registration_form).click()  # Нажатие на кнопку "Войти" на форме регистрации
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.button_login))
        driver.find_element(*Locator.input_email_auth).send_keys(CorrectUsersData.email)
        driver.find_element(*Locator.input_password_auth).send_keys(CorrectUsersData.password)
        driver.find_element(*Locator.button_login).click()
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.button_make_the_order))
        assert driver.find_element(*Locator.button_make_the_order).is_displayed()  # Проверка отображения кнопки

    def test_login_from_login_page(self, driver):
        driver.get(URL.login)  # Переход на страницу логина
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.input_email_auth))
        driver.find_element(*Locator.input_email_auth).send_keys(CorrectUsersData.email)  # Ввод email
        driver.find_element(*Locator.input_password_auth).send_keys(CorrectUsersData.password)  # Ввод пароля
        driver.find_element(*Locator.button_login).click()  # Нажатие на кнопку "Войти"
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.button_make_the_order))  # Ожидание кнопки "Оформить заказ"
        assert driver.find_element(*Locator.button_make_the_order).is_displayed()  # Проверка отображения кнопки "Оформить заказ"

    def test_login_after_registration(self, driver):
        user = TestUser2()# Генерация тестового пользователя
        driver.get(URL.signup) # Переход на страницу регистрации
        driver.find_element(*Locator.input_name).send_keys(user.username)
        driver.find_element(*Locator.input_email).send_keys(user.email)
        driver.find_element(*Locator.input_password).send_keys(user.password)
        driver.find_element(*Locator.button_submit).click()
        WebDriverWait(driver, 25).until(
                EC.visibility_of_element_located(Locator.button_login_in_registration_form))

        driver.find_element(*Locator.button_login_in_registration_form).click()
        WebDriverWait(driver, 25).until(
                EC.visibility_of_element_located(Locator.input_email_auth))
        driver.find_element(*Locator.input_email_auth).send_keys(user.email) # Вход с использованием зарегистрированных данных
        driver.find_element(*Locator.input_password_auth).send_keys(user.password)
        driver.find_element(*Locator.button_login).click()
        WebDriverWait(driver, 25).until(
                EC.visibility_of_element_located(Locator.button_make_the_order))
        assert driver.find_element(*Locator.button_make_the_order).is_displayed()