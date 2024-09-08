from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import CorrectUsersData, RegisteredUserData, TestUser, InvalidData, InvalidData_2
from locators import Locator
from urls import URL


class TestRegistrationPage:
    def test_registration_success(self, driver):
        driver.get(URL.signup) # Переход на страницу регистрации
        driver.find_element(*Locator.input_name).send_keys(CorrectUsersData.username) # Заполнение формы регистрации
        driver.find_element(*Locator.input_email).send_keys(CorrectUsersData.email)
        driver.find_element(*Locator.input_password).send_keys(CorrectUsersData.password)
        driver.find_element(*Locator.button_submit).click()
        WebDriverWait(driver, 25).until(EC.url_to_be(URL.login)) # Ожидание перенаправления на страницу входа


    def test_registration_with_existing_user(self, driver):
        driver.get(URL.signup) # Переход на страницу регистрации
        driver.find_element(*Locator.input_name).send_keys(RegisteredUserData.username) # Заполнение формы данными уже существующего пользователя
        driver.find_element(*Locator.input_email).send_keys(RegisteredUserData.email)
        driver.find_element(*Locator.input_password).send_keys(RegisteredUserData.password)
        driver.find_element(*Locator.button_submit).click()
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.user_exists_message)
        ) # Ожидание появления сообщения об ошибке
        error_message = driver.find_element(*Locator.user_exists_message).text
        assert error_message == 'Такой пользователь уже существует'

    def test_registration_without_name(self, driver):
        test_user = TestUser() # Создаем случайного пользователя
        driver.get(URL.signup) # Переход на страницу регистрации
        driver.find_element(*Locator.input_name).send_keys('')  # Пустое имя
        driver.find_element(*Locator.input_email).send_keys(test_user.email)
        driver.find_element(*Locator.input_password).send_keys(test_user.password)
        driver.find_element(*Locator.button_submit).click()
        assert driver.find_element(*Locator.button_submit).is_displayed() # Проверка, что кнопка отправки формы всё ещё отображается

    def test_registration_without_email(self, driver):
            test_user = TestUser() # Создаем случайного пользователя
            driver.get(URL.signup) # Переход на страницу регистрации
            driver.find_element(*Locator.input_name).send_keys(test_user.username)
            driver.find_element(*Locator.input_email).send_keys('')  # Пустой email
            driver.find_element(*Locator.input_password).send_keys(test_user.password)
            driver.find_element(*Locator.button_submit).click()
            assert driver.find_element(*Locator.button_submit).is_displayed() # Проверка, что кнопка отправки формы всё ещё отображается

    def test_registration_without_password(self, driver):
            test_user = TestUser() # Создаем случайного пользователя
            driver.get(URL.signup) # Переход на страницу регистрации
            driver.find_element(*Locator.input_name).send_keys(test_user.username)
            driver.find_element(*Locator.input_email).send_keys(test_user.email)
            driver.find_element(*Locator.input_password).send_keys('')  # Пустой пароль
            driver.find_element(*Locator.button_submit).click()
            assert driver.find_element(*Locator.button_submit).is_displayed()  # Проверка, что кнопка отправки формы всё ещё отображается

    def test_registration_with_short_password(self, driver):
        driver.get(URL.signup) # Переход на страницу регистрации
        driver.find_element(*Locator.input_name).send_keys(InvalidData.username)
        driver.find_element(*Locator.input_email).send_keys(InvalidData.email)
        driver.find_element(*Locator.input_password).send_keys(InvalidData.password)
        driver.find_element(*Locator.button_submit).click()
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.notification_incorrect_password)) # Ожидание и проверка наличия сообщения об ошибке
        error_message = driver.find_element(*Locator.notification_incorrect_password).text
        assert 'Некорректный пароль' in error_message # Проверка текста сообщения об ошибке

    def test_registration_with_too_short_password(self, driver):
        driver.get(URL.signup) # Открытие страницы регистрации
        driver.find_element(*Locator.input_name).send_keys(InvalidData_2.username)
        driver.find_element(*Locator.input_email).send_keys(InvalidData_2.email)
        driver.find_element(*Locator.input_password).send_keys(InvalidData_2.password)
        driver.find_element(*Locator.button_submit).click()
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.notification_incorrect_password)) # Ожидание и проверка наличия сообщения об ошибке
        error_message = driver.find_element(*Locator.notification_incorrect_password).text
        assert 'Некорректный пароль' in error_message # Проверка текста сообщения об ошибке