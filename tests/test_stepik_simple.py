import math
import time

import pytest
from selene import browser, have, be, query
from selene.support.shared.jquery_style import s


@pytest.mark.stepik
class TestStepik:
    @pytest.mark.smoke
    def test_successful_login(self):
        browser.open('https://stepik.org/')

        s('a[href="/catalog?auth=login"]').click()
        s('input[name="login"]').type('stepikstudent@yandex.ru')
        s('input[name="password"]').type('stepikpassword')
        s('button[type="submit"]').click()
        time.sleep(2)

        s('button[aria-label="Profile"]').click()
        s('[data-qa="menu-item-profile"]').click()

        s('h1').should(have.exact_text('Stepik Student'))

    @pytest.mark.parametrize(
        'num',
        [
            '236895',
            '236896',
            '236897',
            '236898',
            '236899',
            '236903',
            '236904',
            '236905',
        ],
    )
    def test_stepik_puzzle(self, num):
        link = f'https://stepik.org/lesson/{num}/step/1'
        browser.open(link)
        time.sleep(2)

        login_button = s(f'a[href="/lesson/{num}/step/1?auth=login"]')
        login_button.click()
        time.sleep(2)

        s('input[name="login"]').type('stepikstudent@yandex.ru')
        s('input[name="password"]').type('stepikpassword')
        s('button[type="submit"]').click()
        time.sleep(2)

        answer = math.log(int(time.time()))

        input_field = s('textarea')

        if not input_field.matching(be.enabled):
            try_again_button = s('button.again-btn').with_(timeout=12)
            try_again_button.click()
            time.sleep(2)

        input_field.clear().type(str(answer))
        time.sleep(2)

        send_button = s('button.submit-submission').with_(timeout=12)
        send_button.click()
        time.sleep(2)

        feedback = s('p.smart-hints__hint').get(query.text)
        if feedback != 'Correct!':
            print('', feedback, sep='\n')
