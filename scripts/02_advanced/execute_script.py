from selene import browser, query
from selene.support.shared.jquery_style import s

from scripts.setup import define_browser_options, calculation, get_alert_text

browser.config.driver_options = define_browser_options()

browser.open('https://suninjuly.github.io/execute_script.html')

formula_text = s('label .nowrap').get(query.text).strip()
x_text = s('#input_value').get(query.text).strip()
result = calculation(formula_text, x_text)

s('#answer').type(result)
browser.execute_script('window.scrollBy(0, 100);')

s('#robotCheckbox').click()
s('#robotsRule').click()
s('button').click()

get_alert_text()
