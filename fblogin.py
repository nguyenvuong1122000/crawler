from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Login :

    # 1. Khai bao bien browser

    def __init__(self, name, password ):
        self.name  = name
        self.password = password;
        self.browser = webdriver.Chrome(executable_path="./chromedriver")

    def loginFacebook(self):
        option = Options()

        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        self.browser = webdriver.Chrome(chrome_options=option, executable_path='./chromedriver.exe')

        self.browser.get("http://facebook.com")
        txtUser = self.browser.find_element_by_id("email")
        txtUser.send_keys("0817045952") # <---  Điền username thật của các bạn vào đây

        txtPass = self.browser.find_element_by_id("pass")
        txtPass.send_keys("123456vn")

        # 2b. Submit form

        txtPass.send_keys(Keys.ENTER)


        # 3. Dừng chương trình 5 giây
        sleep(2)
        # 4. Đóng trình duyệt