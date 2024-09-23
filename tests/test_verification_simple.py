import pytest
from selene import browser, be, have
from selene.support.shared.jquery_style import s


class TestVerification:
    @pytest.mark.smoke
    def test_successful_verification(self):
        browser.open('https://suninjuly.github.io/wait2.html')
        s('#verify').should(be.clickable).click()
        s('#verify_message').should(have.text('successful'))
