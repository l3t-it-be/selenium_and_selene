from selene import browser, have
from selene.support.shared.jquery_style import s

from scripts.setup import define_browser_options

browser.config.driver_options = define_browser_options()

browser.open('https://suninjuly.github.io/wait1.html')
s('#verify').click()
s('#verify_message').should(have.text('successful'))
