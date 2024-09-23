import pytest
from selene import browser, be
from selene.support.shared.jquery_style import s

link = 'https://selenium1py.pythonanywhere.com/'


@pytest.mark.parametrize('language', ['ru', 'en-gb'])
class TestMainPage:
    @staticmethod
    def open_main_page(language):
        browser.open(link + f'{language}')

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, language):
        self.open_main_page(language)
        s('#login_link').should(be.enabled)

    @pytest.mark.skip
    @pytest.mark.regression
    def test_guest_should_see_basket_link(self, language):
        self.open_main_page(language)
        s('.basket-mini a.btn').should(be.enabled)

    @pytest.mark.xfail(reason='fixing this bug right now')
    def test_guest_should_see_search_button(self, language):
        self.open_main_page(language)
        s('input.btn').should(be.enabled)
