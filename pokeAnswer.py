from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from secret import usr
from secret import passwd
from time import sleep
from random import randint

email = usr[0]
hasło = passwd[0]

class Bot:

    @staticmethod
    def rNum():
        var = []

        def draw(x, a, b):
            for i in range(x):
                var.append(randint(a, b))

        draw(5, 1, 30)
        draw(10, 30, 60)
        draw(5, 60, 90)
        return var

    Path = "chromedriver.exe"

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(self.Path)
        self.card = self.driver.get(self.url)

    def confirm(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "login"))).click()

    def login(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)

    def passwd(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "pass"))).send_keys(hasło)

    def confCookies(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "t"))).click()

    def poke(self):
        while True:
            self.driver.refresh()
            sleep(1)
            var = self.driver.find_elements_by_partial_link_text("Poke Back")
            if len(var) > 0:
                x = randint(0,len(self.rNum())-1)
                y = self.rNum()[x]
                print(y)
                for i in range(y):
                    sleep(1)
                    self.driver.refresh()
                var = self.driver.find_elements_by_partial_link_text("Poke Back")
                for i in range(len(var)):
                    self.driver.find_element_by_partial_link_text("Poke Back").click()

    def open(self):
        self.confCookies()
        self.login()
        self.passwd()
        self.confirm()


u1 = Bot('https://mbasic.facebook.com/pokes/?ref_component=mbasic_bookmark&ref_page=XMenuController')
u1.open()
sleep(2)
u1.poke()
