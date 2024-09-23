from selene import be, browser
from selene.support.shared.jquery_style import s

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.text_in_url = 'login'
        self.login_form = s('#login_form')
        self.register_form = s('#register_form')
        self.email_field = s('#id_registration-email')
        self.password_field = s('#id_registration-password1')
        self.confirm_password_field = s('#id_registration-password2')
        self.submit_registration_button = s('button[name="registration_submit"]')

    def should_be_on_login_page(self):
        self.url_should_contain_text(self.text_in_url)
        self.login_form.should(be.visible)
        self.register_form.should(be.visible)

    def should_have_login_form(self):
        self.login_form.should(be.visible)

    def should_have_register_form(self):
        self.register_form.should(be.visible)

    def register_new_user(self, email, password):
        browser.execute_script('window.scrollBy(0, 100);')

        self.email_field.type(email)
        self.password_field.type(password)
        self.confirm_password_field.type(password)
        self.submit_registration_button.click()

        return BasePage()
