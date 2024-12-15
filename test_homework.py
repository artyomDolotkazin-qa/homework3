from selene import browser, have
import pytest

@pytest.fixture(scope='function')
def setup_browser():
    browser.open('https://school.qa.guru/cms/system/login')
    browser.driver.set_window_size(375, 700)
    yield
    browser.quit()

def test_valid_login(setup_browser):
    browser.element('[name=email]').type('qagurubot@gmail.com')
    browser.element('[name=password]').type('somepasshere').press_enter()
    browser.element('.logined-form').should(have.text('QA_GURU_BOT'))

def test_wrong_password(setup_browser):
    browser.element('[name=email]').type('qagurubot@gmail.com')
    browser.element('[name=password]').type('assdaff').press_enter()
    browser.element('.btn-error').should(have.text('Неверный пароль'))


def test_empty_password(setup_browser):
    browser.element('[name=email]').type('qagurubot@gmail.com').press_enter()
    browser.element('.btn-error').should(have.text('Не заполнено поле Пароль'))


def test_empty_login(setup_browser):
    browser.element('[name=password]').type('assdaff').press_enter()
    browser.element('.btn-error').should(have.text('Не заполнено поле E-Mail'))