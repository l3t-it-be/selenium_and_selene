import pytest
from faker import Faker
from selene import browser
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help='Choose browser: chrome or firefox',
    )
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help="Choose language: ",
        choices=(
            'ar',
            'ca',
            'cs',
            'da',
            'de',
            'en',
            'el',
            'es',
            'fi',
            'fr',
            'it',
            'ko',
            'nl',
            'pl',
            'pt',
            'pt-br',
            'ro',
            'ru',
            'sk',
            'uk',
            'zh-hans',
        ),
    )


@pytest.fixture(scope='function', autouse=True)
def browser_options(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')

    if browser_name == 'chrome':
        print('\nStart Chrome browser for test')
        browser_options = webdriver.ChromeOptions()
        browser_options.add_experimental_option(
            'prefs', {'intl.accept_languages': language}
        )
    elif browser_name == 'firefox':
        print('\nStart Firefox browser for test')
        browser_options = webdriver.FirefoxOptions()
        browser_options.set_preference('intl.accept_languages', str(language))

    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    browser_options.page_load_strategy = 'eager'
    browser_options.add_argument('--headless')
    browser.config.driver_options = browser_options

    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser
    print('\nQuit browser after test')
    browser.quit()


@pytest.fixture()
def random():
    random = Faker()
    return random
