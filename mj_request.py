import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from config import *


def connect_driver():
    """
    Function to connect to driver with Chrome Browser.
    :return:
    Chrome Webdriver
    """
    options = Options()
    # options.add_argument("--headless")  # Runs Chrome in headless mode.
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
        time.sleep(0.1)


class MJRequest:
    def __init__(self):
        self.driver = connect_driver()
        self.discord_login()

    def discord_login(self):
        print("Login processing...")
        self.driver.get("https://discord.com/channels/1088397804529000458/1088397805174927432")
        login = self.driver.find_element(By.XPATH, '//*[@id="uid_5"]')
        password = self.driver.find_element(By.XPATH, '//*[@id="uid_7"]')
        login.send_keys(DISCORD_EMAIL)
        password.send_keys(DISCORD_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        print("Login succeeded")

    def close_selenium_driver(self):
        self.driver.close()

    def mj_request(self):
        runnable = True
        while runnable:
            input_text = input("Enter text:")
            if input_text == "0":
                runnable = False
            else:
                print(f"Input: {input_text}")
                request_text = f"/imagine {input_text}"
                actions = ActionChains(self.driver)
                for i in request_text:
                    actions.send_keys(i)
                    actions.perform()
                    time.sleep(0.1)

                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ENTER)
                actions.perform()
                time.sleep(10)


try:
    a = MJRequest()
    a.mj_request()

finally:
    a.close_selenium_driver()
