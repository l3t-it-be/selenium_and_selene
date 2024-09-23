from selene import browser, query
from selene.support.shared.jquery_style import s

from scripts.setup import define_browser_options, calculation, get_alert_text

browser.config.driver_options = define_browser_options()

browser.open('https://suninjuly.github.io/get_attribute.html')

formula_text = s('h2 .nowrap').get(query.text).strip()
x_text = s('#treasure').get(query.attribute('valuex')).strip()
result = calculation(formula_text, x_text)

s('#answer').type(result)
s('#robotCheckbox').click()
s('#robotsRule').click()
s('button').click()

get_alert_text()
