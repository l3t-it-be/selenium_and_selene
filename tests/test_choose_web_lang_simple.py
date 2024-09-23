import time

from selene import browser, be
from selene.support.shared.jquery_style import s


def test_add_to_cart_button_is_present():
    browser.open(
        'https://selenium1py.pythonanywhere.com/catalogue/the-art-of-the-start_169/'
    )
    add_to_basket_button = s('button.btn-add-to-basket')
    add_to_basket_button.should(be.present)

    time.sleep(2)

    print(
        '\nFor running in console: ',
        'pytest --language=en .\\tests\\test_choose_web_lang_simple.py',
        'or pytest --language=ru .\\tests\\test_choose_web_lang_simple.py',
        'or pytest --language=uk .\\tests\\test_choose_web_lang_simple.py',
        'or pytest --language=pt-br .\\tests\\test_choose_web_lang_simple.py',
        sep='\n',
    )
