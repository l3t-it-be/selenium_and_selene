from selene import browser
from selene.support.shared.jquery_style import s

from scripts.setup import (
    define_browser_options,
    create_random_generator,
    get_alert_text,
)

browser.config.driver_options = define_browser_options()
random = create_random_generator()

browser.open('https://suninjuly.github.io/find_xpath_form')

s('//input[@name="first_name"]').type(random.first_name())
s('//input[@name="last_name"]').type(random.last_name())
s('//input[@class="form-control city"]').type(random.city())
s('//input[@id="country"]').type(random.country())
s('//button[text()="Submit"]').click()

get_alert_text()
