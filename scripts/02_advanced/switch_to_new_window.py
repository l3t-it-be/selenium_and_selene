from selene import browser, query
from selene.support.shared.jquery_style import s

from scripts.setup import define_browser_options, calculation, get_alert_text

browser.config.driver_options = define_browser_options()

browser.open('https://suninjuly.github.io/redirect_accept.html')

s('button.trollface').click()
browser.switch_to_next_tab()

formula_text = s('label .nowrap').get(query.text).strip()
x_text = s('#input_value').get(query.text).strip()
result = calculation(formula_text, x_text)

s('#answer').type(result)
s('button').click()

get_alert_text()
