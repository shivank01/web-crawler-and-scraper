from selnium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time

path = 'C:\Users\hp\Desktop\chromedriver.exe'


def page_is_loaded(driver):
    DVG=driver.find_element_by_tag_name("body")
    print "pojpo "+str(DVG)
    return DVG != None
driver = webdriver.Chrome(executable_path = path)

driver.get("https://hib.iiit-bh.ac.in/Hibiscus/Login/?client=iiit")

wait = ui.WebDriverWait(driver, 10)


wait.until(page_is_loaded)

email_field = driver.find_element_by_name("uid")

#for logging in to iiit hibiscus

email_field.send_keys("-----COLLEGE iD----")

password_field = driver.find_element_by_name("pwd")
password_field.send_keys("-----YOUR PASSWORD-----")

ans_field = driver.find_element_by_id("txtCaptchaDiv")
ans = driver.find_element_by_tag_name("span")
s = str(ans.text)
print(ans_field,s)
l = len(s)




if l == 5:
  summ = int(s[0]) + int(s[2])
  print 1
elif l == 6:
  if s[1] == '+':
    summ = int(s[0]) + int(s[2])*10 +(int(s[3]))
  else:
    summ = int(s[3]) +  int(s[0])*10 + int(s[1])
else:
  summ = int(s[0])*10 + int(s[1]) + int(s[3])*10 + int(s[4]) 



input_field = driver.find_element_by_id('txtInput')
input_field.send_keys(summ)

password_field.send_keys(Keys.RETURN)



driver.get("https://hib.iiit-bh.ac.in/Hibiscus/Start/menu.php")
print driver.window_handles
driver.find_element_by_xpath("""/html/body/div[5]/a""").click()
print driver.current_url+" o"
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
print driver.current_url+" op"


wait.until(page_is_loaded)
print driver.window_handles
tabs=driver.window_handles
print tabs[1]
driver.switch_to_window(tabs[1])
print driver.current_url+" o"

#for first notice

driver.find_element_by_xpath("""/html/body/div/div[2]/table/tbody/tr[1]/td[2]/a""").click()
wait.until(page_is_loaded)


for elem in driver.find_elements_by_xpath('/html/body/div/div[2]/table/tbody/tr/td/div'):
    message=elem.text

import urllib2
import cookielib
from getpass import getpass
import sys
import os
from stat import *


import csv
with open('C:\Users\hp\Desktop\shivank\official.csv') as csvfile:
    readCSV  = csv.reader(csvfile,delimiter = ',')
    numbers = []

    for row in readCSV:
        number = row[3]
        
        


        #login to way2sms

        if __name__ == "__main__":    
            username = "9938147181"
            passwd = "G3586B"

            message = "+".join(message.split(' '))

        #logging into the sms site
            url ='http://site24.way2sms.com/Login1.action?'
            data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
       

            cj= cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

        #Adding header details
            opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
            try:
                usock =opener.open(url, data)
            except IOError:
                print "error"
           

            jession_id =str(cj).split('~')[1].split(' ')[0]
            send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
            send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
            opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
            try:
                sms_sent_page = opener.open(send_sms_url,send_sms_data)
            except IOError:
                print "error"


            print "success" 
      
        print message


