# -*- coding: utf-8 -*-
r'''
Confusion is the key
    v^v^v^v^v^v^
     \    |   /
      \   |  /
       \  | / 
        mmmm
      <|o  o|>
        \~~/
         ""  
k vnay fw qyws jmul qg ucdcjhavu
folpce-uotflkpfruhuf   
'''
# this script is written to check the price of a flight and return an email if it dips below some threshold price

import time
#from bs4 import BeautifulSoup 
import selenium as sl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import json 
import requests
from lxml import html
import smtplib
 
def flight_tracker(start_location_name,end_location_name, start_date, end_date,url='https://www.cheaptickets.com/',round_trip = True):
    cdr= sl.webdriver.Chrome(r'C:\Users\sg28r\Desktop\handon_ml\chromedriver.exe')
    action = ActionChains(cdr)
    cdr.set_page_load_timeout('15')    
    cdr.get(url)
    time.sleep(1)
    action.move_to_element(cdr.find_element_by_xpath("/html[1]/body[1]/meso-native-marquee[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/button[1]").send_keys(Keys.ENTER))
    list_fo_something=[cdr.find_element_by_xpath("/html[1]/body[1]/meso-native-marquee[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/form[1]/div[3]/div[1]/div[1]/div[1]/label[1]/input[1]"),cdr.find_element_by_xpath("/html[1]/body[1]/meso-native-marquee[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/form[1]/div[3]/div[2]/div[1]/div[1]/label[1]/input[1]"),cdr.find_element_by_xpath("/html[1]/body[1]/meso-native-marquee[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/form[1]/fieldset[2]/div[1]/div[2]/div[1]/label[1]/input[1]"),cdr.find_element_by_xpath("/html[1]/body[1]/meso-native-marquee[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/form[1]/fieldset[2]/div[1]/div[3]/div[1]/label[1]/input[1]")]
    somelist_fo_another_thing=[start_location_name,end_location_name,start_date,end_date]
    j=0
    for i in somelist_fo_another_thing:
        if(j==3):
          
          list_fo_something[j].send_keys(Keys.CONTROL + "a")
          list_fo_something[j].send_keys(Keys.DELETE)
          list_fo_something[j].send_keys(i)
        else:
          list_fo_something[j].send_keys(i) 

        j += 1 
        time.sleep(2)            
    cdr.find_element_by_xpath("//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']").send_keys(Keys.ENTER)    
    time.sleep(20)
    priceList=[]
    for i in range(1,20):
      try: 
        listing_for_flights = cdr.find_element_by_xpath("/html[1]/body[1]/div[2]/div[11]/section[1]/div[1]/div[10]/ul[1]/li[{}]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]".format(i))
        whole_listing = cdr.find_element_by_xpath('/html[1]/body[1]/div[2]/div[11]/section[1]/div[1]/div[10]/ul[1]/li[{}]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]'.format(i))
        priceList.append(((whole_listing.text),(listing_for_flights.text)))
      else:
        i += 1      
    print(priceList)
    for tupal in priceList:
      if('tupal[1]' <= 800):
        send_email(tupal[1])
      else:
        send_email('not there yet')
        pass

def send_email(some_string):
#This function checks the login and sends mail
         
    print('Something')
    gmail_user = ''
    gmail_password = '******'

    sent_f =gmail_user
    subject ='PriceIsRight
    to =[ 'sg28r8@gmail.com']
    body = some_string

    email_text = """\
    From:%s
    To:%s
    Subject:%s
    %s
    """%(sent_f,",".join(to),subject,body)
  
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo()
        server.login(gmail_user,gmail_password)
        server.sendmail(sent_f,to,email_text)
        server.close()
        print('Well')       
          
    except:
        print('Did not work')


    
flight_tracker("New York","Kathmandu","05/20/2019","07/15/2019")
    