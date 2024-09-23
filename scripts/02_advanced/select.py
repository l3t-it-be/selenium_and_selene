from selene import browser, query, Collection, be, Element, have
from selene.support.shared.jquery_style import s

from scripts.setup import define_browser_options, get_alert_text

browser.config.driver_options = define_browser_options()

browser.open('https://suninjuly.github.io/selects1.html')

num1 = int(s('#num1').get(query.text))
num2 = int(s('#num2').get(query.text))
result = num1 + num2


class Select:
    def __init__(self, element):
        self.element = element

    @classmethod
    def by(cls, selector: str):
        return cls(browser.element(selector))

    @property
    def options(self) -> Collection:
        return self.element.all('option')

    @property
    def all_selected_options(self) -> Collection:
        return self.options.by(be.selected)

    @property
    def first_selected_option(self) -> Element:
        return self.all_selected_options.first

    def select_by_value(self, value):
        self.element.click()
        self.options.element_by(have.value(value)).click()
        return self

    def select_by_index(self, index):
        self.element.click()
        self.options[index].click()
        return self

    def select_by_visible_text(self, text):
        self.element.click()
        self.options.element_by(have.text(text)).click()
        return self


Select(s('select')).select_by_visible_text(str(result))
s('button').click()

get_alert_text()
