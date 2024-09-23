from selene import browser
from selene.support.shared.jquery_style import s

from scripts.setup import (
    define_browser_options,
    create_random_generator,
    get_file_path,
    get_alert_text,
)

browser.config.driver_options = define_browser_options()
random = create_random_generator()

browser.open('https://suninjuly.github.io/file_input.html')

s('[name="firstname"]').type(random.first_name())
s('[name="lastname"]').type(random.last_name())
s('[name="email"]').type(random.email())

s('#file').send_keys(get_file_path('../../python_autotests_courses_on_stepik.txt'))
s('button').click()

get_alert_text()
