# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:46:04 2019

@author: Big data
"""
def theater_num(m,m_dict):
    import pandas as pd
    import numpy as np
    from bs4 import BeautifulSoup
    import requests
    result=[404,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN]
    try:
        name = m["Title"].replace(":","").replace(" ","-")
        list_theater= []
        notheater=[]
        url= "https://www.the-numbers.com/movie/"+str(name)
        response = requests.get(url)
        html = BeautifulSoup(response.text)
        moviename =html.find("h1") 
        content = html.find_all("table",id="movie_finances")
        for c in content:
            if "Domestic Box Office" in c.text: 
                    content1 = c.find_all("tr")
                    result[0]=moviename.text
        
    except:
         if result[0] == 404:
            url= "https://www.the-numbers.com/movie/"+str(name)+"-("+m["Year"]+")"
            print(url)
            response = requests.get(url)
            html = BeautifulSoup(response.text)
            moviename =html.find("h1") 
            content = html.find_all("table",id="movie_finances")
            print(content)
            for c in content:
                if "Domestic Box Office" in c.text: 
                        content1 = c.find_all("tr")
                        result[0]=moviename.text
            print(content)
    try:
       Dos = content1[1].find("td")
       if "Domestic Box Office" in Dos.text:
           result[1]=content1[1].find("td",class_="data").text
    except:
       pass
    try:
        Int = content1[2].find("td")
        if "International Box Office" in Int.text:
            result[2]=content1[2].find("td",class_="data").text
    except:
        pass
    try:
        Wor = content1[3].find("td")
        if "Worldwide Box Office" in Wor.text:
            result[3]=content1[3].find("td",class_="data").text
    except:
        pass  
    try:
        budget = html.find("div",id="summary")
        budget1 = budget.find_all("tr")
        for i in budget1:
            if "Production\xa0Budget" in i.text:
                budget2 = i.find_all("td")[1]
                budget2 = budget2.text
                result[4]=budget2
                print('ok')
    except:
        pass
    
    try:
        theater = html.find("div",id="box_office_chart")
        list_td = theater.find_all("tr")[1:]
        for i in list_td:
            theater_num=i.find_all('td')
            list_theater.append(theater_num[4].text)
        list_theater = [a.replace(',','') for a in list_theater]
        list_theater = [int(a) for a in list_theater if a.isdigit()]
        list_theater = max(list_theater)
        #print(list_theater)
        result[5]=list_theater
        #print(result)
    except:
        if result[1]!= "$0":
            notheater.append(moviename.text)
    print(result)
    m_dict[m_dict.index(m)]["moive_name_thenumbers"] = result[0]
    m_dict[m_dict.index(m)]["Domestic Box Office"] = result[1]
    m_dict[m_dict.index(m)]["International Box Office"] = result[2]
    m_dict[m_dict.index(m)]["Worldwide Box Office"] = result[3]
    m_dict[m_dict.index(m)]["budget_in_USD"] = result[4]
    m_dict[m_dict.index(m)]["Theater_num"] = result[5]
    return m_dict

if __name__=="__main__":
    m_dict = theater_num(m,m_dict)
    
    