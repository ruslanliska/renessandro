import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config import *
from utils import connect_driver


class MJRequest:
    def __init__(self):
        self.driver = connect_driver()
        self.discord_login()

    def discord_login(self):
        print("Login processing...")
        self.driver.get("https://discord.com/channels/1088397804529000458/1088397805174927432")
        time.sleep(10)
        login = self.driver.find_element(By.XPATH, '//*[@id="uid_5"]')
        password = self.driver.find_element(By.XPATH, '//*[@id="uid_7"]')
        login.send_keys(DISCORD_EMAIL)
        password.send_keys(DISCORD_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(15)
        print("Login succeeded")

    def close_selenium_driver(self):
        self.driver.close()
        print('Driver closed')

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
                    time.sleep(0.3)

                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ENTER)
                actions.perform()
