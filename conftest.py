import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from BaseFunc import StartPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


class UsersData:
    domain = 'test_inc'
    user_login = 'us1'
    user_password = '12345'
    approver_login = 'utv1'
    approver_password = '12345'
    financier_login = 'fin1'
    financier_password = '12345'
    assistant_login = 'as1'
    assistant_password = '12345'
    admin_login = 'admin'
    admin_password = '12345'
    super_admin_login = 'admin'
    super_admin_password = '12345'
    reports_login = 'ois1'
    reports_password = '12345'


# Firefox Fixtures
@pytest.fixture(scope="module")
def browser_login():
    driver = webdriver.Firefox()
    driver.maximize_window()
    base = StartPage(driver)
    base.open_site()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def browser_super_admin():
    driver = webdriver.Firefox()
    driver.maximize_window()
    base = StartPage(driver)
    base.open_site()
    login = base.find_element((By.NAME, 'username'))
    login.send_keys(UsersData.super_admin_login)
    password = base.find_element((By.NAME, 'password'))
    password.send_keys(UsersData.super_admin_password)
    login_button = base.find_element((By.XPATH, "//button[text()='Войти']"))
    login_button.click()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def browser_admin():
    driver = webdriver.Firefox()
    driver.maximize_window()
    base = StartPage(driver)
    base.open_site()
    domain = base.find_element((By.NAME, 'domain'))
    domain.send_keys(UsersData.domain)
    login = base.find_element((By.NAME, 'username'))
    login.send_keys(UsersData.admin_login)
    password = base.find_element((By.NAME, 'password'))
    password.send_keys(UsersData.admin_password)
    login_button = base.find_element((By.XPATH, "//button[text()='Войти']"))
    login_button.click()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def browser_user():
    driver = webdriver.Firefox()
    driver.maximize_window()
    base = StartPage(driver)
    base.open_site()
    domain = base.find_element((By.NAME, 'domain'))
    domain.send_keys(UsersData.domain)
    login = base.find_element((By.NAME, 'username'))
    login.send_keys(UsersData.user_login)
    password = base.find_element((By.NAME, 'password'))
    password.send_keys(UsersData.user_password)
    login_button = base.find_element((By.XPATH, "//button[text()='Войти']"))
    login_button.click()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def browser_approver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    base = StartPage(driver)
    base.open_site()
    domain = base.find_element((By.NAME, 'domain'))
    domain.send_keys(UsersData.domain)
    login = base.find_element((By.NAME, 'username'))
    login.send_keys(UsersData.approver_login)
    password = base.find_element((By.NAME, 'password'))
    password.send_keys(UsersData.approver_password)
    login_button = base.find_element((By.XPATH, "//button[text()='Войти']"))
    login_button.click()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def browser_financier():
    driver = webdriver.Firefox()
    driver.maximize_window()
    base = StartPage(driver)
    base.open_site()
    domain = base.find_element((By.NAME, 'domain'))
    domain.send_keys(UsersData.domain)
    login = base.find_element((By.NAME, 'username'))
    login.send_keys(UsersData.financier_login)
    password = base.find_element((By.NAME, 'password'))
    password.send_keys(UsersData.financier_password)
    login_button = base.find_element((By.XPATH, "//button[text()='Войти']"))
    login_button.click()
    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def login_logout():
    driver = webdriver.Firefox()
    driver.maximize_window()
    base = StartPage(driver)
    base.open_site()
    yield driver
    driver.quit()
