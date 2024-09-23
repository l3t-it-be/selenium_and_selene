from selene import browser, have, command, query
from selene.support.shared.jquery_style import s

from scripts.setup import define_browser_options, calculation, get_alert_text

browser.config.driver_options = define_browser_options()

browser.open('https://suninjuly.github.io/explicit_wait2.html')

s('#price').with_(timeout=12).should(have.text('100'))
s('#book').click()

input_field = s('#answer')
input_field.perform(command.js.scroll_into_view)

formula_text = s('label .nowrap').get(query.text).strip()
x_text = s('#input_value').get(query.text).strip()
result = calculation(formula_text, x_text)

input_field.type(result)
s('#solve').click()

get_alert_text()
