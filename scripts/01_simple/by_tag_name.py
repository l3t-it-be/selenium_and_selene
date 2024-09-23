from selene import browser
from selene.support.shared.jquery_style import s

from scripts.setup import define_browser_options

browser.config.driver_options = define_browser_options()

browser.open('https://suninjuly.github.io/text_input_task.html')
s('input').type('get()')
s('button').click()
