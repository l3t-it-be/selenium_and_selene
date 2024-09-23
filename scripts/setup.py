import os

from faker import Faker
from selene import browser
from selenium import webdriver
from sympy import sympify, symbols


def define_browser_options():
    browser_options = webdriver.ChromeOptions()
    browser_options.page_load_strategy = 'eager'
    browser_options.add_argument('--headless')

    return browser_options


def create_random_generator():
    random = Faker()
    return random


def get_alert_text():
    alert_text = browser.switch_to.alert.text

    num_in_alert = ''
    for symbol in alert_text:
        if symbol.isdigit() or symbol == '.':
            num_in_alert += symbol

    print(num_in_alert)


def calculation(formula_text, x_text):
    formula_start = formula_text.find('ln')
    formula_end = formula_text.find(',')
    formula_text = formula_text[formula_start:formula_end]
    formula = sympify(formula_text)

    x_int = int(x_text)
    x_symbol = symbols('x')

    return str(formula.subs(x_symbol, x_int).evalf())


def get_file_path(file_name):
    file_path = os.path.abspath(file_name)
    return file_path
