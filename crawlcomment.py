from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.common.keys import Keys
from fblogin import Login
import xlsxwriter
import pandas as pd

class Crawler :
    def __init__(seft) :
        seft.file = open("file_4500.txt","r")

    def run(self):
        self.file.readline()
        login = Login("0817045653", "123456vn")
        login.loginFacebook()
        workbook = xlsxwriter.Workbook('result.xlsx')
        worksheet = workbook.add_worksheet()
        row = 0

        while(True):
            id = self.file.readline()
            url = "https://www.facebook.com/" + "groups/" + id + "/about/"
            login.browser.get(url)

            # worksheet.write(0, 0, 'id_group')
            # worksheet.write(0, 1, 'name')
            # worksheet.write(0, 2, 'member')
            # worksheet.write(0, 3, 'todayPost')
            # worksheet.write(0, 4, 'last30DayPost')
            # worksheet.write(0, 5, 'status')
            # worksheet.write(0, 6, 'date_create_before')

            try :
                member = login.browser.find_element_by_xpath("//div[@class = '_1c-4 _6qq5 _63ok _1c-7 _6qqc']//div[@class = '_63om _6qq6']").text
                todayPost = login.browser.find_element_by_xpath("//div[@class = '_63om _6qq6']").text
                last30DayPost = login.browser.find_element_by_xpath("//div[@class = '_1c-4 _6qq5 _1c-7 _6qqc']//div[@class = '_63op _6qqa']").text.split()[0]
                name = login.browser.find_element_by_xpath('//*[@id="seo_h1_tag"]').text
                status = login.browser.find_element_by_class_name("_j1y").find_element_by_class_name("_2ieo").text
                date_create_before = login.browser.find_element_by_xpath('//*[@class="_ifv"]').text[20:]

                member = int(member.replace(".",""))
                todayPost = int(todayPost.replace(".",""))
                last30DayPost =int(last30DayPost.replace(".",""))


                worksheet.write(row , 0, id  )
                worksheet.write(row , 1, name  )
                worksheet.write(row , 2, member  )
                worksheet.write(row , 3, todayPost  )
                worksheet.write(row , 4, last30DayPost  )
                worksheet.write(row , 5, status  )
                worksheet.write(row , 6, date_create_before)


                row = row + 1
                print(name)
            except:
                if(not self.file.readline()):
                    break
                pass

        workbook.close()

craw = Crawler()
print()
craw.run()
