import pytest
from selene import browser, have
from selene.support.shared.jquery_style import s

url1 = 'https://suninjuly.github.io/registration1.html'
url2 = 'https://suninjuly.github.io/registration2.html'
welcome_text_expected = 'Congratulations! You have successfully registered!'


class TestRegistration:
    @staticmethod
    def fill_registration_form(url, random):
        browser.open(url)

        s('.first_block input.first').type(random.first_name())
        s('.first_block input.second').type(random.last_name())
        s('.first_block input.third').type(random.email())
        s('button').click()

        s('h1').should(have.exact_text(welcome_text_expected))

    @pytest.mark.smoke
    def test_successful_registration(self, random):
        self.fill_registration_form(url1, random)

    @pytest.mark.xfail
    @pytest.mark.regression
    def test_registration_failed(self, random):
        self.fill_registration_form(url2, random)
