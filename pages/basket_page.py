from selene import be, have
from selene.support.shared.jquery_style import ss, s

from pages.base_page import BasePage


class BasketPage(BasePage):
    def __init__(self):
        super().__init__()
        self.basket_items = ss('.basket-items')
        self.empty_basket_message = s('#content_inner p')

    def basket_should_be_empty(self):
        self.basket_items.should(have.size(0))

    def empty_basket_should_have_message_about_it(self):
        self.empty_basket_message.should(be.present)
