from data import CorrectUsersData
from locators import Locator
from urls import URL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestLogout:
    def test_logout(self, driver):
        driver.get(URL.home)  # Переход на главную страницу
        driver.find_element(*Locator.button_login_in_main).click()  # Переход на страницу входа
        driver.find_element(*Locator.input_email_auth).send_keys(CorrectUsersData.email)  # Ввод email
        driver.find_element(*Locator.input_password_auth).send_keys(CorrectUsersData.password)  # Ввод пароля
        driver.find_element(*Locator.button_login).click()  # Нажатие кнопки "Войти"
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(Locator.button_make_the_order)
        )
        driver.find_element(*Locator.button_personal_account).click()  # Переход в личный кабинет
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(Locator.profile)
        )
        driver.find_element(*Locator.button_logout).click()  # Нажатие кнопки "Выйти"
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(Locator.button_login)
        )
        assert driver.find_element(*Locator.button_login).is_displayed()  # Проверка, что кнопка "Войти" отображается