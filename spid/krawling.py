import requests
# import urllib
import lxml
from lxml.html.soupparser import fromstring
import selenium as sl
import time
import bs4 as bs
# import tk
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from PIL import ImageTk, Image
 

def lets_go(username, password,root):
    # op = Options()
    # op.headless = True
    # rep = sl.webdriver.Firefox(options=op)
    rep = sl.webdriver.Firefox()
    print("lets go bitch")
    rep.set_page_load_timeout('20')
    rep.get("https://cunyfirst.cuny.edu")
    time.sleep(4)
    u_path = rep.find_element_by_xpath("//input[@id='CUNYfirstUsernameH']")
    pass_path = rep.find_element_by_xpath("//input[@id='CUNYfirstPassword']")
    u_path.send_keys(Keys.CONTROL + "a")
    time.sleep(4)
    u_path.send_keys(Keys.DELETE)
    u_path.send_keys(username)
    pass_path.send_keys(password)
    rep.find_element_by_xpath(
            "//button[@id='submit']").send_keys(Keys.ENTER)
    time.sleep(10)    
    if rep.current_url == "https://home.cunyfirst.cuny.edu/psp/cnyepprd/EMPLOYEE/EMPL/h/?tab=DEFAULT":
        # got_in("GOT IN BITCH","Good")
        print("gotin")
        time.sleep(10)
        rep.find_element_by_xpath(
            "//ul[@id='ptnav2tree']//a[contains(text(),'Student Center')]").click()
        try:
            
            element = WebDriverWait(rep, 10).until(
                EC.presence_of_element_located((By.ID, "ptifrmtgtframe")))
            rep.switch_to.frame(element)
            rep.find_element_by_xpath(
                "//a[@class='PSHYPERLINK' and @id='DERIVED_SSS_SCR_SSS_LINK_ANCHOR3']").click()
            table = WebDriverWait(rep, 10).until(
                EC.presence_of_element_located((By.ID, "SSR_DUMMY_RECV1$scroll$0")))
            row = table.find_elements(By.TAG_NAME, 'tr')
            term_text_list = []
            term_list = []
            for i in range(2,len(row)):          
                # col_0 = row[i].find_elements(By.TAG_NAME, "td")[0]
                col_1 = row[i].find_elements(By.TAG_NAME, "td")[1]
                col_2 = row[i].find_elements(By.TAG_NAME, "td")[2]
                term_list.append((col_1, col_2))
                term_text_list.append((col_1.text, col_2.text))
            # print(term_text_list)
            root.destroy()
            laa = term_windows(term_text_list)
            for i in laa.values():
                print(f"{i}")
            
            
        finally:
            rep.quit()
    else:
        got_in("you fucking idiot something doesn't match",
               "fuck you, But i will try again!")

def got_in(some_text,buttontxt):
     rat = tk.Tk()
     two_so = tk.Label(rat, text=some_text, font=(
         "Comic Sans MS", 20, 'bold')).grid(row=0)
     retch = tk.Button(rat, text=buttontxt,
                       command=lambda: rat.destroy()).grid(columnspan=6)
     rat.mainloop()
def term_windows(some_list):
    rat = tk.Tk()
    chek_frame = tk.Frame(rat).grid(sticky=tk.W)
    dic = {}
    for i in range(0, len(some_list)):
        name = f"{some_list[i][0]}|{some_list[i][1]}"
        dic[name] = tk.IntVar()
        tk.Checkbutton(chek_frame, text=name, variable=dic[name]).grid(row=i + 1)

    tk.Button(rat, text="end_this",
              command=lambda: rat.destroy()).grid(sticky=tk.SW)
              
    rat.mainloop()
    return dic

    

def return_some_dic(dic, rat):    
    return dic 

    

    




