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
import time
import selenium as sl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import json 

def flighttracker(start_location_name,end_location_name, start_date, end_date,url='https://www.cheaptickets.com/',round_trip = True):
    cdr= sl.webdriver.Chrome(r'C:\Users\sg28r\Desktop\handon_ml\chromedriver.exe')
    action = ActionChains(cdr)
    cdr.set_page_load_timeout('10')    
    cdr.get(url)
    time.sleep(1)
    action.move_to_element(cdr.find_element_by_xpath("/html[1]/body[1]/meso-native-marquee[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/button[1]").send_keys(Keys.ENTER))
    list_fo_something=[cdr.find_element_by_xpath("/html[1]/body[1]/meso-native-marquee[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/form[1]/div[3]/div[1]/div[1]/div[1]/label[1]/input[1]"),cdr.find_element_by_xpath("/html[1]/body[1]/meso-native-marquee[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/form[1]/div[3]/div[2]/div[1]/div[1]/label[1]/input[1]"),cdr.find_element_by_xpath("/html[1]/body[1]/meso-native-marquee[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/form[1]/fieldset[2]/div[1]/div[2]/div[1]/label[1]/input[1]"),cdr.find_element_by_xpath("/html[1]/body[1]/meso-native-marquee[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/form[1]/fieldset[2]/div[1]/div[3]/div[1]/label[1]/input[1]")]
    somelist_fo_another_thing=[start_location_name,end_location_name,start_date,end_date]
    j=0
    for i in somelist_fo_another_thing:
        list_fo_something[j].send_keys(Keys.CONTROL + "a")
        list_fo_something[j].send_keys(Keys.DELETE)
        list_fo_something[j].send_keys(i) 

        j += 1 
        time.sleep(2)            
    cdr.find_element_by_xpath("//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']").send_keys(Keys.ENTER)
    time.sleep(20) 
flighttracker("New York","Kathmandu","05/20/2019","07/15/2019")
    