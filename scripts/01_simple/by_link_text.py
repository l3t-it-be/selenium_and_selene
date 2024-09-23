import math

from selene import browser, by
from selene.support.shared.jquery_style import s

from scripts.setup import (
    define_browser_options,
    create_random_generator,
    get_alert_text,
)

browser.config.driver_options = define_browser_options()
random = create_random_generator()

browser.open('https://suninjuly.github.io/find_link_text')

text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
s(by.link_text(text)).click()

s('[name="first_name"]').type(random.first_name())
s('[name="last_name"]').type(random.last_name())
s('input.city').type(random.city())
s('#country').type(random.country())
s('button[type="submit"]').click()

get_alert_text()
