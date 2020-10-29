# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:48:47 2020

@author: user
"""


import string
from bs4 import BeautifulSoup
from pandas import DataFrame
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from tqdm import tqdm

emails=[]
mobiles=[]
ignored_exceptions=(StaleElementReferenceException)

def wdwfind(path):
    return WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.XPATH,(path))))

def wdwclick(path):
    return WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(
            EC.element_to_be_clickable((By.XPATH,(path))))



driver = webdriver.Chrome(ChromeDriverManager().install())

link="http://www.vkiassociation.com/associationmember.php?x="


for n in tqdm(string.ascii_uppercase):
    x=(link+n)    
    driver.get(x)    
    select_element = Select(wdwfind("//select[@name='example3_length']"))
    select_element.select_by_value('100')
    
    #Finding the total number of pages to be scraped
    
    soup=BeautifulSoup(driver.page_source)
       
    if True:
        try:
            pages=int(soup.find("a",{"class":"paginate_button next"})['data-dt-idx'])
        except:
            print("e")
    else:
        pages=int(soup.find("a",{"class":"paginate_button next disabled"})['data-dt-idx'])
        
    for running in range(pages):
        
        soup=BeautifulSoup(driver.page_source)
        for a in soup.findAll("p"):
            for n in a.findAll("i",{"class":"fa fa-envelope"}):
                emails.append(a.getText())
            
                
        for a in soup.findAll("p"):
            for n in a.findAll("i",{"class":"fa fa-mobile"}):
                mobiles.append(a.getText())
        
        wdwclick("//a[contains(text(),'Next')]").click()
        sleep(3)
    sleep(3)
    
df=DataFrame((emails,mobiles)).transpose()  
df.to_excel("C:\\Users\\user\\Documents\\Jaipur_Vki.xlsx")      





