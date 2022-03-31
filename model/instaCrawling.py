from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from model import sheet
import datetime

driver = wd.Chrome(executable_path='/Users/ain/Desktop/Desktop/instaCrolling/model/chromedriver')

day = ['월','화','수','목','금','토','일']
Day_of_the_week = day[datetime.datetime.today().weekday()]
date = datetime.datetime.today().day

class instagram:
    def __init__(self,id,pwd,targets):
        self.id = id
        self.pwd = pwd
        self.targets = targets

    def login(self):
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(1)
        try:
            driver.find_element(by=By.NAME, value="username").send_keys(self.id)
            driver.find_element(by=By.NAME, value="password").send_keys(self.pwd)
            time.sleep(1)
            driver.find_element(by=By.CSS_SELECTOR, value=".sqdOP.L3NKy.y3zKF").click()
            time.sleep(4)

            driver.find_element(by=By.CSS_SELECTOR, value=".sqdOP.L3NKy.y3zKF").click()
            time.sleep(3)
            driver.find_element(by=By.CSS_SELECTOR, value=".aOOlW.HoLwm").click()
        except:
            print("로그인 실패")
            return

    def getFollowers(self):
        for person in self.targets:
            time.sleep(3)
            find = driver.find_element(by=By.CSS_SELECTOR, value=".XTCLo.d_djL.DljaH")
            find.send_keys(person)
            for _ in range(2):
                time.sleep(1)
                find.send_keys(Keys.RETURN)
            time.sleep(2)
            try:
                followers = driver.find_element(by=By.XPATH, value="//span[@title]")
                print(person,"의 팔로워는 ",value := int(followers.get_property("title")))
                sheet.inputSheet(person, [date, Day_of_the_week, value])
            except:
                print(person,"의 팔로워 가져오기 실패")
                print(type(person),type(value))

    def __del__(self):
        print("참조 해제 완료")


# def login(user_id,user_passwd):
#     try:
#         instagram_id_fom = driver.find_element(by=By.NAME,value="username")
#         instagram_id_form.send_keys(user_id)
#
#         instagram_pw_form = driver.find_element(by=By.NAME, value="password")
#         instagram_pw_form.send_keys(user_passwd)
#         driver.find_element(by=By.CSS_SELECTOR,value=".sqdOP.L3NKy.y3zKF").click()
#         is_login_success = True
#         time.sleep(2)
#         driver.find_element(by=By.CSS_SELECTOR,value=".sqdOP.yWX7d.y3zKF").click()
#     except:
#         print("로그인 실패")
#         is_login_success = False
#
# def get(id):
#     try:
#         driver.find_element(by=By.CLASS_NAME,value="eyXLr").send_keys(id)
#     except:
#         print("aa")
#
# login(user_id,user_passwd)
# time.sleep(4)
# searchId("merumichandayo")