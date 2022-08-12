"""
This is a test module
"""


def test_simple(config, browser):
    browser.get(config['url'])
    # raise Exception('Failed test')
