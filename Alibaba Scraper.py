# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 22:33:38 2020

@author: user
"""


from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
from time import time
from tqdm import tqdm


s=time()
a="https://www.alibaba.com/products/Machinery.html?spm=a2700.galleryofferlist.0.0.18b09771MBoR62&IndexArea=product_en&page="
b="&Country=IN&ggs=GGS&param_order=CNTRY-IN"
company=[]
products=[]
prices=[]
index=[]

for n in tqdm(range(94,101)):
    x=(a+str(n)+b)  
      
    driver=urlopen(x)
    soup=BeautifulSoup(driver.read())
        
    for n in soup.findAll("div", {"class":"organic-list-offer-right"}):
        for name in n.find("a"):
            company.append(name)
    
    for n in soup.findAll("div",{"class":"organic-list-offer-center"}):
        products.append((n.find("a",{"class":"organic-gallery-title"})['title']))
        
    for n in soup.findAll("p",{"class":"gallery-offer-price"}):
        prices.append((n.getText()))
        
    

timetaken=time()-s
    
df=pd.DataFrame((products,prices,company)).transpose()
df.columns=["Products","Prices","Company"]

#df.to_excel()

