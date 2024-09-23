from selene import be, query, have
from selene.support.shared.jquery_style import s

from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self):
        super().__init__()
        self.text_in_url = '?promo='
        self.add_to_basket_button = s('button.btn-add-to-basket')
        self.success_message = s('.alertinner')
        self.product_name = s('h1')
        self.product_name_in_message = s('.alertinner strong')
        self.product_price = s('p.price_color')
        self.product_price_in_message = s('.alertinner p strong')

    def add_product_to_basket(self):
        self.url_should_contain_text(self.text_in_url)
        self.click_add_to_basket_button()
        self.solve_quiz_and_get_code()
        self.should_have_success_message()
        self.product_name_should_match_the_one_added()
        self.product_price_should_match_original_product_price()

    def click_add_to_basket_button(self):
        self.add_to_basket_button.click()

    def should_have_success_message(self):
        self.success_message.should(be.present)

    def should_not_have_success_message(self):
        self.success_message.should(be.hidden)

    def product_name_should_match_the_one_added(self):
        product_name_text = self.product_name.get(query.text)
        self.product_name_in_message.should(have.exact_text(product_name_text))

    def product_price_should_match_original_product_price(self):
        product_price = self.product_price.get(query.text)
        self.product_price_in_message.should(have.exact_text(product_price))
