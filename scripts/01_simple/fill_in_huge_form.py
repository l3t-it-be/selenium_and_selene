from selene import browser
from selene.support.shared.jquery_style import ss, s

from scripts.setup import define_browser_options, get_alert_text

browser.config.driver_options = define_browser_options()

browser.open('https://suninjuly.github.io/huge_form.html')

elements = ss('input')
for element in elements:
    element.type('stop the war')

s('button').click()

get_alert_text()
