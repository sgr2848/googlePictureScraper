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

#import bs4 as bs 

import urllib.parse
import time, os, re, requests
import shutil
import json 
from selenium.webdriver.common.keys import Keys
from selenium import webdriver as sl
from selenium.common.exceptions import ElementNotInteractableException

#logging.basicConfig(level = logging.DEBUG)


class google_image_dwn:
    def __init__(self):
         
        self.set_of_links = set()# A set is also a type of data set it is kinda like list but only has unique entries and is unordered(
    def download_link(self, link, fpath):
        '''
        The following function dowloads the image image in the link 
        '''
        rspn = requests.get(link,stream = True)
        with open(fpath,'wb') as file:
            shutil.copyfileobj(rspn.raw,file)
    def download_image(self, keyword, url = 'https://www.google.co.in/search?{}'):
                                        
        chrome_drive = sl.Chrome(r'C:\Users\sg28r\Desktop\handon_ml\chromedriver.exe')#setting path for the driver
        chrome_drive.set_page_load_timeout('5')

        #https://www.google.com/search?q=doge source=lnms tbm=isch sa=X ved=0ahUKEwjR_9-q5rjfAhUOjlkKHeAWCCkQ_AUIDigB biw=1280 bih=648
        #here q is the query, lnms is the source(in our case browser) & tbm  is the type of file we are searching for (images for us)
        # if you want to read more https://www.reddit.com/r/explainlikeimfive/comments/2ecozy/eli5_when_you_search_for_something_on_google_the/
        
        search_url_params = {'q': keyword, 'source' : 'lnms', 'tbm' : 'isch' }
        parsed_source = urllib.parse.urlencode(search_url_params)# parsing the url 

        chrome_drive.get(url.format(parsed_source))
        #soup = bs.BeautifulSoup(chromeSl.get(source),'lxml')
        time.sleep(3)
        
        '''
        **** THIS IS JUST A COMMENT****
        window.scrollTo(0,document.body.scrollHeight);
        var height = document.body.scrollHeight;
        return height;
        '''
        #the following js code snippet is executed by the browser and get the height
        # so if we scroll more results are displayed 
        #height = chrome_drive.execute_script('window.scrollTo(0,document.body.scrollHeight);var height = document.body.scrollHeight; return height')

        
        image_meta = chrome_drive.find_elements_by_xpath(".//div[contains(@class,'rg_meta')]")# this tag get the dictionary of meta data(image url) for the current page
        
        for data in image_meta:
            json_meta = json.loads(data.get_attribute('innerHTML'))
            print(type(json_meta))
            url = json_meta['ou']#here ou is the key for the url
           
            self.set_of_links.add(url)# adds url to the lsit
        chrome_drive.close()# closes the driver
        links_regExp = re.compile(r'.*\.(\w+)')#using regular expression to check if there pattern for the extension 
        link_d_c = 0
        for i, link in enumerate(list(self.set_of_links)):
            link_ext_exists = links_regExp.search(link.lower())#searching for pattern in the above links                
            if link_ext_exists:
                link_ext = link_ext_exists.groups()[0]
                valid_extension = not {'jpg','png'} or link_ext in {'jpg','png'}#only taking jpg and png file
                if valid_extension:
                    filename = '{}.{}'.format(keyword,i,link_ext)
                    fpath = os.path.join('C:/Users/sg28r/Desktop/handon_ml/webscarping',filename)# dpwloading paths
                    try:
                        self.download_link(link,fpath)
                    except Exception as e:

                        link_d_c += 1
                else:
                    link_d_c += 1
   
       
if __name__ == '__main__':
    g = google_image_dwn()
    g.download_image('hodor')
