from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import CorrectUsersData
from urls import URL
from locators import Locator


class TestOpenPersonalAccountFromHome:
    def test_go_to_account_from_main(self, driver):
        driver.get(URL.home)  # Переход на главную страницу
        driver.find_element(*Locator.button_personal_account).click()
        driver.find_element(*Locator.input_email_auth).send_keys(CorrectUsersData.email)
        driver.find_element(*Locator.input_password_auth).send_keys(CorrectUsersData.password)
        driver.find_element(*Locator.button_login).click()
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.button_make_the_order))
        driver.find_element(*Locator.button_personal_account).click()
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(Locator.profile))
        assert driver.find_element(*Locator.profile).is_displayed()