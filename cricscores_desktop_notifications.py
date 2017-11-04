from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import requests
import gi
from threading import Thread

gi.require_version('Notify', '0.7')  #to avoid unwanted warnings

from gi.repository import Notify
from playsound import playsound
import time

Notify.init("Test App")  #desktop notification initialization

Notify.Notification.new(
    "Cric Notify!!!",
    "WELCOME",
    "/home/shivank/python/cric.jpeg"
).show()
playsound('/home/shivank/python/pop.mp3')

def check():
    time.sleep(2)
    if answer=='exit':
    	return 0	
    elif answer == None:
        return 1
    
    print "Too Slow"

from Tkinter import *

x=0

def value(val,root):
	global x
	x=val
	root.destroy()


def gui_show(s1,s2,s3,s4):
	root=Tk()

	button1=Button(root,text=s1,bg='light blue',fg='red',command= lambda: value(1,root))
	button2=Button(root,text=s2,bg='light blue',fg='red',command= lambda: value(2,root))
	button3=Button(root,text=s3,bg='light blue',fg='red',command= lambda: value(3,root))
	button4=Button(root,text=s4,bg='light blue',fg='red',command= lambda: value(4,root))
	button1.pack(fill=X)
	button2.pack(fill=X)
	button3.pack(fill=X)
	button4.pack(fill=X)

	root.mainloop()






# chromeOptions = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chromeOptions.add_experimental_option("prefs",prefs)
#to prevent images from loading

# driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver",chrome_options=chromeOptions)
#opening Chrome
driver=webdriver.PhantomJS(service_args=['--load-images=no'])
driver.get("http://www.cricbuzz.com/")  #specifying the website


matches=driver.find_elements_by_class_name("cb-font-12")   

count =0
a = ["" for x in range(4)]
for element in matches:
    if (count<=3):
        #print str(count+1) + "." + element.text     #display the matches going on
        a[count]=element.text
        count=count+1
gui_show(a[0],a[1],a[2],a[3])
# x=int(input())
#print "x:",x		
#driver.save_screenshot('testing.png')			 #selecting the match we want to display the score for
matches[x-1].click()
exit=0

while(1):
	score=driver.find_element_by_xpath('//*[@id="matchCenter"]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/h2')
	#score=driver.find_element_by_xpath('//*[@id="matchCenter"]/div[3]/div[2]/div[2]')
	curr=driver.find_element_by_xpath('//*[@id="matchCenter"]/div[3]/div[2]/div[1]/div[2]')
	#message = score.text+curr.text
	# print "score",score.text
	# print "curr",curr.text.replace('\n',' ')

	curr=curr.text.replace('\n',' ')

	message=curr[:18]+'\n'+curr[18:]

	Notify.Notification.new(
    "Cric Notify!!!",
    score.text,
    "/home/shivank/python/cric.jpeg"
	).show()
	Notify.Notification.new(
    "Cric Notify!!!",
    message,
    "/home/shivank/python/cric.jpeg"
	).show()
	playsound('/home/shivank/python/pop.mp3')

	# answer = None
	# Thread(target = check).start()

	# answer = raw_input("Input something: ")
	# if answer==0:
	# 	break
	
	# print "success" 
	# try:
	# 	answer = input_with_timeout(prompt, 10)
	# except TimeoutExpired:
	# 	print('Sorry, times up')
	# else:
	# 	print('Got %r' % answer)
	time.sleep(50)
	driver.refresh()

driver.quit()

