import undetected_chromedriver as uc
import os
import pandas as pd
from unidecode import unidecode
class Crawl:
    def __init__(self):
        self.driver = uc.Chrome(headless=True,use_subprocess=False)
    
    def crawl_data(self, url):
        self.driver.get(url)
        self.filename = f'{url.replace("/","_").replace(".","_").replace(":","_").replace('''"''',)}'
        el = self.driver.find_element('tag name','html')
        with open("./text/" + self.filename + ".txt",'w', encoding='utf-8') as file:
            file.write(el.text) 
        with open("./html/" + self.filename+'.html','w', encoding='utf-8') as file:
            file.write(self.driver.page_source)
        self.driver.save_screenshot("./images/" + self.filename +'.png')

class ReadInput:
    def __init__(self, filename):
        self.filename = filename
    
    def convert(self):
        pass

    def read_convert(self, type):
        if(type == "xlsx"):
            file = pd.read_excel(self.filename)
        elif(type == "csv") :
            file = pd.read_csv(self.filename)
        else:
            return
        self.file = file
        title = file["Tên bài"].values
        url = [f"https://www.trelangblog.com/2023/12/{unidecode(c_tit).lower().replace(' ', '-')}" for c_tit in title]

        return url
    # def url(self, type):
    #     if(type == "xlsx"):
    #         file = pd.read_excel(self.filename)
    #     elif(type == "csv") :
    #         file = pd.read_csv(self.filename)
    #     else:
    #         return
    #     self.file = file
    #     url = file["URL"].values
    #     return url


        

        


if(__name__ == '__main__'):
    crawl = Crawl()
    read = ReadInput("./input/template.xlsx")
    urls = read.read_convert("xlsx")
    print(urls)
    for url in urls:
        # print("Crawling: " + url)
        if(type(url) == str and url != float('nan') and url != None):
            print(f"Crawling : {url}")
            crawl.crawl_data(url)