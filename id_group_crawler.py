from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.common.keys import Keys
from fblogin import Login
import xlsxwriter
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

class ID_Crawler:
    def __init__(seft):
        seft.file = open("id.txt", "r")#
        #sua cach doc file
        seft.workbook = xlsxwriter.Workbook("id_result.xlsx")


    def run(self):
        login = Login("0817045653", "123456vn")
        login.loginFacebook()



        while(True):
            count = 0

            line = self.file.readline().encode('cp1252').decode('utf-8')
            line.replace(" ","%20")


            worksheet = self.workbook.add_worksheet(line)
            url0 = "https://www.facebook.com/search/groups/?q="+line+"&epa=FILTERS&filters=eyJncm91cHNfc2hvd19vbmx5Ijoie1wibmFtZVwiOlwicHVibGljX2dyb3Vwc1wiLFwiYXJnc1wiOlwiXCJ9In0%3D"
            login.browser.get(url0)
            m = 0
            while (m < 20):
                login.browser.find_element_by_tag_name('body').send_keys(Keys.END)
                time.sleep(1)
                m = m + 1

            name_list = login.browser.find_elements_by_class_name("_52eh._5bcu")
            url_list = [i.find_element_by_tag_name("a").get_attribute("href") for i in name_list]

            for i in url_list:

                try:
                    login.browser.get(str(i).replace("?ref=br_rs", 'about'))
                    time.sleep(1)
                    member = login.browser.find_element_by_xpath(
                        "//div[@class = '_1c-4 _6qq5 _63ok _1c-7 _6qqc']//div[@class = '_63om _6qq6']").text
                    todayPost = login.browser.find_element_by_xpath("//div[@class = '_63om _6qq6']").text
                    last30DayPost = login.browser.find_element_by_xpath(
                        "//div[@class = '_1c-4 _6qq5 _1c-7 _6qqc']//div[@class = '_63op _6qqa']").text.split()[0]
                    name = login.browser.find_element_by_xpath('//*[@id="seo_h1_tag"]').text
                    status = login.browser.find_element_by_class_name("_j1y").find_element_by_class_name("_2ieo").text
                    date_create_before = login.browser.find_element_by_xpath('//*[@class="_ifv"]').text[20:]

                    member = int(member.replace(".", ""))
                    todayPost = int(todayPost.replace(".", ""))
                    last30DayPost = int(last30DayPost.replace(".", ""))

                    worksheet.write(count, 0, url)
                    worksheet.write(count, 1, name)
                    worksheet.write(count, 2, member)
                    worksheet.write(count, 3, todayPost)
                    worksheet.write(count, 4, last30DayPost)
                    worksheet.write(count, 5, status)
                    worksheet.write(count, 6, date_create_before)

                    count = count + 1
                except:
                    print(count)
            if(not self.file.readline()):
                break
        self.workbook.close()
id_crawl = ID_Crawler()
id_crawl.run()