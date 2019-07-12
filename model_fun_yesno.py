# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:02:20 2019

@author: Big data
"""
import pandas as pd
import xgboost as xgb
import numpy as np
from xgboost import plot_importance
from sklearn.preprocessing import Imputer
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score


def model_yn(movielist):
    
    movielist['release_date_USA']=movielist['Released']
    

    want_keys={
            'classification', 'Runtime', 'budget_in_USD', 'gross_na',
           'release_date_USA', 'Genre', 'imdbVotes', 'IMDBscore', 'TomatoesScore',
           'Metascore', 'Theater_num', 'movie_2_before',
           'movie_1_before', 'movie_0_before', 'Actor_2_before',
           'Actor_1_before', 'Actor_0_before'}

    wanted_dict = {key : [val] for key ,val in movielist.items() if key in want_keys }   
    df = pd.DataFrame.from_dict(wanted_dict)

    for i in df.columns:
#        print(i)
        if df[i].isna().any():
            df[i][0] = str(0)
    
    df["runtime"] = df["Runtime"]
    df["runtime"] = df["runtime"].str.replace("min","")
    df["runtime"] = df["runtime"].astype("float")
    df = df.drop(["Runtime"],axis= 1)
    try:
        df["budget_in_USD"] = df["budget_in_USD"].str.replace('$',"").str.replace(",","")   
    except:
        pass
    df["budget_in_USD"] = df["budget_in_USD"].astype("float")
    
    
    df["imdbVotes"] = df["imdbVotes"][0].replace(",","")
    df["imdbVotes"] = df["imdbVotes"].astype("float")
    
    
    df['release_date_USA'] = df.release_date_USA.str.split(' ',expand=True)[1]
    
    #df["Cmovie_3_before"] = df["Cmovie_3_before"].astype("str").replace("error","0").astype("float")
    #df["Cmovie_2_before"] = df["Cmovie_2_before"].astype("str").replace("error","0").astype("float")
    #df["Cmovie_1_before"] = df["Cmovie_1_before"].astype("str").replace("error","0").astype("float")
    #df["Cmovie_0_before"] = df["Cmovie_0_before"].astype("str").replace("error","0").astype("float")
#    df["movie_3_before"] = df["movie_3_before"].astype("str").replace("error","0").astype("float")
    df["movie_2_before"] = df["movie_2_before"].astype("str").replace("error","0").astype("float")
    df["movie_1_before"] = df["movie_1_before"].astype("str").replace("error","0").astype("float")
    df["movie_0_before"] = df["movie_0_before"].astype("str").replace("error","0").astype("float")
#    df["Actor_3_before"] = df["Actor_3_before"].astype("str").replace("error","0").astype("float")
    df["Actor_2_before"] = df["Actor_2_before"].astype("str").replace("error","0").astype("float")
    df["Actor_1_before"] = df["Actor_1_before"].astype("str").replace("error","0").astype("float")
    df["Actor_0_before"] = df["Actor_0_before"].astype("str").replace("error","0").astype("float")
    df= df.join(pd.get_dummies(df["classification"]).astype("bool"))
    df = df.drop(["classification"], axis=1)
    
    df= df.join(pd.get_dummies(df["release_date_USA"]).astype("bool"))
    df = df.drop(["release_date_USA"], axis=1)
    
    
    #onhot encoding
    
    
    
    model_wanted_keys=[
            'runtime', 'budget_in_USD', 'imdbVotes', 'IMDBscore', 'TomatoesScore',
           'Metascore', 'Theater_num', 'movie_2_before',
           'movie_1_before', 'movie_0_before', 'Actor_2_before',
           'Actor_1_before', 'Actor_0_before', 'G', 'NC-17', 'NotRated', 'PG',
           'PG-13', 'R', 'TV-14', 'TV-G', 'TV-MA', 'TV-PG', 'TV-Y', 'TV-Y7',
           'TV-Y7-FV', 'Unrated', 'Apr', 'Aug', 'Dec', 'Feb', 'Jan', 'Jul', 'Jun',
           'Mar', 'May', 'Nov', 'Oct', 'Sep', 'Action', 'Adventure', 'Animation',
           'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
           'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery',
           'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']
    data = [0]*len(model_wanted_keys)
    
    df_model = pd.DataFrame(data=[data],columns= model_wanted_keys)
    df_model.update(df)
    
    with open('RandomForest.pickle', 'rb') as f:
        clf2 = pickle.load(f)
        #测试读取后的Model
    return clf2.predict(df_model)[0]
if __name__=="__main__":
    for i in m_dict:
        print(model_yn(i))