# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:59:46 2019

@author: Big data
"""

from yahooupdate import start_clawer_new_movie
from theater_func import theater_num
from gtrend_0701 import trends
from model_auto import predict_loss,predict_gain
from model_fun_yesno import model_yn
import numpy as np

m_dict = start_clawer_new_movie()
m_dict = trends(m_dict[0:2])

for m in m_dict[0:2]:#先跑三個
    m_dict = theater_num(m,m_dict) #此階段回傳新的m_dict(加了theater_num,Domestic_box_office,International_box_office,Worldwide Box Office,moive_name_thenumbers,budget_in_USD)
for m in m_dict[0:2]:
    if m["Runtime"] == "N/A":
        m["Runtime"]="100"
#    if np.isnan(m["budget_in_USD"]):
#        m["budget_in_USD"]="2000000"
    output = model_yn(m) #馮哥model output
    if output == False:
        print("ok")
        m=predict_loss(m)
    else:
        m=predict_gain(m)
        
    
    