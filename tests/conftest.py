"""
Configuration module for PyTest
"""

import json
import pytest
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def config():
    with open('../config.json') as config_file:
        config = json.load(config_file)

    return config


@pytest.fixture
def browser(config):
    # Initialize browser instance
    manager = ChromeDriverManager()
    service = Service(manager.install())

    # Configure driver options
    options = webdriver.ChromeOptions()
    if config['browser'].lower() == 'headless':
        options.add_argument("headless")
    options.add_argument("disable-gpu")
    options.add_argument("no-default-browser-check")
    options.add_argument("no-first-run")
    options.add_argument("no-sandbox")

    capabilities = DesiredCapabilities.CHROME
    capabilities["loggingPrefs"] = {"browser": "ALL"}

    driver = webdriver.Chrome(service=service, options=options, desired_capabilities=capabilities)

    # Set a wait time for calls
    driver.implicitly_wait(30)

    # Return a browser instance for each setup
    yield driver

    # Quit every instance of web driver
    driver.quit()
