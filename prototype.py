# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:59:46 2019

@author: Big data
"""
import pymongo
from yahooupdate import start_clawer_new_movie
from theater_func import theater_num
from gtrend_0711 import trends
from model_auto import predict_loss,predict_gain
from model_fun_yesno import model_yn
import numpy as np

m_dict = start_clawer_new_movie(end_page=5)
m_dict = trends(m_dict)
wanted_keys={"Runtime","budget_in_USD","Production","imdbVotes","IMDBscore","TomatoesScore","Metascore","Theater_num",
                 "movie_2_before","movie_1_before","movie_0_before","Actor_2_before","Actor_1_before","Actor_0_before",
                 "Genre","Language","Country","classification"}
for m in m_dict:#先跑三個
    theater_num(m,m_dict) #此階段回傳新的m_dict(加了theater_num,Domestic_box_office,International_box_office,Worldwide Box Office,moive_name_thenumbers,budget_in_USD)
    keyslist = list(m.keys()) 
    for key in wanted_keys:
        if key not in keyslist:
            del m_dict[m_dict.index(m)]
            break
    
    if m["Runtime"] == "N/A":
        m["Runtime"]="100"
#    if np.isnan(m["budget_in_USD"]):
#        m["budget_in_USD"]="2000000"
    try:
        output = model_yn(m) #馮哥model output

        if output == False:
            predict_loss(m)
        else:
            predict_gain(m)
    except:
        print(m)
        
myclient = pymongo.MongoClient("mongodb://10.120.28.26:27017/")
db = myclient["movies"]
dblist = myclient.list_database_names()
collist = db.list_collection_names()
onlinedb = db["online"]
inserted = onlinedb.insert_many(m_dict)