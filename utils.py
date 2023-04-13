import time
import logging

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def connect_driver():
    """
    Function to connect to driver with Chrome Browser.
    :return:
    Chrome Webdriver
    """
    options = Options()
    options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def slow_typing(element, text):
    """
    Function to send keys by elements, with sleep.
    Text will be sent to web element by characters
    :param element: Web element when the text shall be sent
    :param text:
    :return: None
    """

    for character in text:
        element.send_keys(character)
        time.sleep(0.3)




