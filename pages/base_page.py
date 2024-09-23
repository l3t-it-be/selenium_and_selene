import math

from selene import browser, be, have
from selene.support.shared.jquery_style import s
from selenium.common import NoAlertPresentException


class BasePage:
    def __init__(self):
        self.login_link = s('#login_link')
        self.basket_link = s('.btn-group a')
        self.user_icon = s('.icon-user')
        self.user_email = s('//th[.="Email address"]/following-sibling::td')

    def go_to_basket(self):
        from pages.basket_page import BasketPage

        self.basket_link.click()
        return BasketPage()

    def go_to_login_page(self):
        from pages.login_page import LoginPage

        self.login_link.click()
        return LoginPage()

    @staticmethod
    def open(url: str):
        browser.open(url)

    def should_be_authorized_user(self, email):
        self.user_icon.click()
        self.user_email.should(have.exact_text(email))

    def should_have_login_link(self):
        self.login_link.should(be.present)

    @staticmethod
    def solve_quiz_and_get_code():
        alert = browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code: {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')

    @staticmethod
    def url_should_contain_text(text: str):
        browser.should(have.url_containing(text))
