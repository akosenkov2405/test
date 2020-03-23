from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class StartPage():
    def __init__(self, driver):
        self.driver = driver
        self.start_url = 'урл проекта'

    def find_element(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не удается найти элемент {locator}")

    def open_site(self):
        return self.driver.get(self.start_url)

    def find_elements(self, locator, time=1.5):
        try:
            elements = [*WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                                message=f"Не удается найти элементы {locator}")]
        except TimeoutException:
            elements = []
        return elements

    def find_element_invisible_off(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator),
                                                      message=f"В течение {locator}с. элемент не исчез со страницы")

    def action_chains(self):
        return ActionChains(self.driver)
