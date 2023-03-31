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

    def discord_login(self) -> None:
        print("Login processing...")
        self.driver.get("https://discord.com/channels/1088397804529000458/1088397805174927432")
        time.sleep(5)
        login = self.driver.find_element(By.XPATH, '//*[@id="uid_5"]')
        password = self.driver.find_element(By.XPATH, '//*[@id="uid_7"]')
        login.send_keys(DISCORD_EMAIL)
        password.send_keys(DISCORD_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(15)
        print("Login succeeded")

    def close_selenium_driver(self) -> None:
        print('Driver closing')
        self.driver.close()

    def mj_request(self, request_text: str) -> None:
        mj_start_text = f"/imagine "
        actions = ActionChains(self.driver)
        for i in mj_start_text:
            actions.send_keys(i)
            actions.perform()
            time.sleep(0.3)

        actions = ActionChains(self.driver)
        actions.send_keys(request_text, Keys.ENTER)
        actions.perform()
        return
