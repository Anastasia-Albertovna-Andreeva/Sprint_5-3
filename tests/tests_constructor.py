from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locator
from urls import URL
from data import CorrectUsersData


class TestConstructorSectionNavigation:
    def login(self, driver):
        # Переход на страницу авторизации и вход
        driver.get(URL.login)
        driver.find_element(*Locator.input_email_auth).send_keys(CorrectUsersData.email)
        driver.find_element(*Locator.input_password_auth).send_keys(CorrectUsersData.password)
        driver.find_element(*Locator.button_login).click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locator.button_make_the_order))

    def test_navigate_to_buns_section(self, driver):
        self.login(driver)
        # Переход в конструктор
        driver.find_element(*Locator.header_of_page_constructor).click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locator.bulki_block))
        # Проверка, что раздел "Булки" отображается
        assert driver.find_element(*Locator.bulki_block).is_displayed()

    def test_navigate_to_sauces_section(self, driver):
        self.login(driver)
        # Переход в конструктор
        driver.find_element(*Locator.header_of_page_constructor).click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locator.sauces_block))
        # Проверка, что раздел "Соусы" отображается
        assert driver.find_element(*Locator.sauces_block).is_displayed()

    def test_navigate_to_fillings_section(self, driver):
        self.login(driver)
        # Переход в конструктор
        driver.find_element(*Locator.header_of_page_constructor).click()
        WebDriverWait(driver, 25).until(EC.visibility_of_element_located(Locator.nachinki_block))
        # Проверка, что раздел "Начинки" отображается
        assert driver.find_element(*Locator.nachinki_block).is_displayed()

    def test_switch_between_sections(self, driver):
        self.login(driver)
        # Переход в конструктор
        driver.find_element(*Locator.header_of_page_constructor).click()
        WebDriverWait(driver, 25).until(EC.visibility_of_element_located(Locator.bulki_block))

        # Переход из "Булки" в "Соусы"
        driver.find_element(*Locator.bulki_block).click()
        WebDriverWait(driver, 25).until(EC.visibility_of_element_located(Locator.sauces_block))
        driver.find_element(*Locator.sauces_block).click()
        assert driver.find_element(*Locator.sauces_block).is_displayed()

        # Переход из "Соусы" в "Начинки"
        driver.find_element(*Locator.sauces_block).click()
        WebDriverWait(driver, 25).until(EC.visibility_of_element_located(Locator.nachinki_block))
        driver.find_element(*Locator.nachinki_block).click()
        assert driver.find_element(*Locator.nachinki_block).is_displayed()

        # Переход из "Начинки" в "Булки"
        driver.find_element(*Locator.nachinki_block).click()
        WebDriverWait(driver, 25).until(EC.visibility_of_element_located(Locator.bulki_block))
        driver.find_element(*Locator.bulki_block).click()
        assert driver.find_element(*Locator.bulki_block).is_displayed()