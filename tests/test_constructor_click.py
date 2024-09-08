from data import CorrectUsersData  # Импорт данных пользователя
from urls import URL  # Импорт URL из файла urls.py
from locators import Locator  # Импорт локаторов
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestConstructorRedirects:
    def test_go_to_constructor_from_account(self, driver):
        driver.get(URL.login)  # Переход на страницу авторизации пользователя
        driver.find_element(*Locator.input_email_auth).send_keys(CorrectUsersData.email)
        driver.find_element(*Locator.input_password_auth).send_keys(CorrectUsersData.password)
        driver.find_element(*Locator.button_login).click()  # Нажимаем кнопку Входа
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.button_make_the_order)
        )
        driver.find_element(*Locator.button_personal_account).click() # Переход в ЛК
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.profile)
        )
        driver.find_element(*Locator.header_of_page_constructor).click() # Переход в конструктор
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.bulki_block)
        )
        assert driver.find_element(*Locator.bulki_block).is_displayed() # Булки отображаются в конструкторк

    def test_go_to_home_from_account_logo_click(self, driver):
        driver.get(URL.login)
        driver.find_element(*Locator.input_email_auth).send_keys(CorrectUsersData.email)
        driver.find_element(*Locator.input_password_auth).send_keys(CorrectUsersData.password)
        driver.find_element(*Locator.button_login).click()  # Нажимаем кнопку входа
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.button_make_the_order)
        )
        driver.find_element(*Locator.button_personal_account).click() # Переход в личный кабинет
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.profile)
        )
        driver.find_element(*Locator.logo).click() # Клик по логотипу Stellar Burgers для возврата на главную страницу
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.header_of_page_constructor)
        )
        assert driver.current_url == URL.home # Проверка, что пользователь на главной странице