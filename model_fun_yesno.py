# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:02:20 2019

@author: Big data
"""

#movielist={'Title': 'Yesterday', 
#'Year': '2019', 
#'classification': 'PG-13', 
#'Released': '08 Aug 2019', 
#'runtime': '116 min', 
#'Genre': 'Comedy, Fantasy, Music, Musical, Romance', 
#'Director': 'Danny Boyle', 
#'Writer': 'Jack Barth (story by), Richard Curtis (screenplay), Richard Curtis (story by)', 
#'Actors': 'Himesh Patel, Lily James, Sophia Di Martino, Ellise Chappell', 
#'Plot': "A struggling musician realizes he's the only person on Earth who can remember The Beatles after waking up in an alternate timeline where they never existed.", 
#'Language': 'English', 
#'Country': 'UK', 
#'Awards': 'N/A', 
#'Poster': 'https://m.media-amazon.com/images/M/MV5BYzE4MGU0MTYtYTYwNS00ZTljLWEwYTItNmNlYTg2MTViZWExXkEyXkFqcGdeQXVyMjUxMTY3ODM@._V1_SX300.jpg', 
#'Ratings': [{'Source': 'Internet Movie Database', 'Value': '6.7/10'}, 
#{'Source': 'Rotten Tomatoes', 'Value': '65%'}, 
#{'Source': 'Metacritic', 'Value': '54/100'}], 
#'Metascore': '0.54', 
#"TomatoesScore": "0.65", 
#'IMDBscore': '0.67', 
#'imdbVotes': '717', 
#'imdbID': 'tt8079248', 
#'Type': 'movie', 
#'DVD': 'N/A', 
#'BoxOffice': 'N/A', 
#'Production': 'Universal Pictures', 
#'Website': 'N/A', 
#'Response': 'True', 
#"Theater_num":20, 
#"budget_in_USD":15000,
#'movie_8_before': 30, 
#'movie_7_before': 36, 
#'movie_6_before': 100, 
#'movie_5_before': 99, 
#'movie_4_before': 0, 
#'movie_3_before': 0, 
#'movie_2_before': 0, 
#'movie_1_before': 0, 
#'movie_0_before': 0, 
#'movie_1_after': 0, 
#'movie_2_after': 0, 
#'movie_3_after': 0, 
#'movie_4_after': 0, 
#'movie_5_after': 0, 
#'movie_6_after': 0, 
#'movie_7_after': 0, 
#'movie_8_after': 0, 
#'Actor_8_before': 26.25, 
#'Actor_7_before': 5.0, 
#'Actor_6_before': 30.0, 
#'Actor_5_before': 54.0, 
#'Actor_4_before': 0.0, 
#'Actor_3_before': 0.0, 
#'Actor_2_before': 0.0, 
#'Actor_1_before': 0.0, 
#'Actor_0_before': 0.0, 
#'Actor_1_after': 0.0, 
#'Actor_2_after': 0.0, 
#'Actor_3_after': 0.0, 
#'Actor_4_after': 0.0, 
#'Actor_5_after': 0.0, 
#'Actor_6_after': 0.0, 
#'Actor_7_after': 0.0, 
#'Actor_8_after': 0.0, 
#'moive_name_thenumbers': 404, 
#"Domestic_box_office": np.nan, 
#'International Box Office': np.nan, 
#'Worldwide Box Office': np.nan}
def model_yn(movielist):
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
    movielist['release_date_USA']=movielist['Released']
    want_keys={
            'classification', 'Runtime', 'budget_in_USD', 'gross_na',
           'release_date_USA', 'Genre', 'imdbVotes', 'IMDBscore', 'TomatoesScore',
           'Metascore', 'Theater_num', 'movie_3_before', 'movie_2_before',
           'movie_1_before', 'movie_0_before', 'Actor_3_before', 'Actor_2_before',
           'Actor_1_before', 'Actor_0_before'}
    
    wanted_dict = {key : [val] for key ,val in movielist.items() if key in want_keys }
    

    if wanted_dict["classification"] == "N/A":
        wanted_dict["classification"]= "Action"
    if wanted_dict["Runtime"] == "N/A":
        wanted_dict["Runtime"] = "100min"
    if wanted_dict["budget_in_USD"] == "N/A":
        wanted_dict["budget_in_USD"] = 100000
    if wanted_dict["release_date_USA"] == "N/A": 
        wanted_dict["release_date_USA"]
    if wanted_dict["Genre"] == "N/A":
        wanted_dict = "21 Jul 2019"
    if wanted_dict["imdbVotes"] == "N/A":
        wanted_dict["imdbVotes"] = 1000
    if wanted_dict["IMDBscore"] == "N/A":
        wanted_dict["IMDBscore"] = 5
    if wanted_dict["TomatoesScore"] == "N/A":
        wanted_dict["TomatoesScore"] = 5
    if wanted_dict["Metascore"] == "N/A":        
        wanted_dict["Metascore"]= 5
    if wanted_dict["Theater_num"] == "N/A":
        wanted_dict["Theater_num"] = 1000
    
    
    df = pd.DataFrame.from_dict(wanted_dict)
    
    for i in df.columns:

        if df[i].isna().any() == True :
            df[i][0] = 0
            continue
    if df["Runtime"][0] =="N/A":
        df["Runtime"] = "100min" 
    if df["classification"][0] =="N/A":
        df["classification"] = ""
            
    df["runtime"]= df["Runtime"]
    df["runtime"] = df["runtime"].str.replace("min","")
    df["runtime"] = df["runtime"].astype("float")
    df["budget_in_USD"] = df["budget_in_USD"].astype("float")
    df["imdbVotes"] = df["imdbVotes"].str.replace(",","")
    df["imdbVotes"] = df["imdbVotes"].astype("float")
    
    
    df['release_date_USA'] = df.release_date_USA.str.split(' ',expand=True)[1]
    
    #df["Cmovie_3_before"] = df["Cmovie_3_before"].astype("str").replace("error","0").astype("float")
    #df["Cmovie_2_before"] = df["Cmovie_2_before"].astype("str").replace("error","0").astype("float")
    #df["Cmovie_1_before"] = df["Cmovie_1_before"].astype("str").replace("error","0").astype("float")
    #df["Cmovie_0_before"] = df["Cmovie_0_before"].astype("str").replace("error","0").astype("float")
    df["movie_3_before"] = df["movie_3_before"].astype("str").replace("error","0").astype("float")
    df["movie_2_before"] = df["movie_2_before"].astype("str").replace("error","0").astype("float")
    df["movie_1_before"] = df["movie_1_before"].astype("str").replace("error","0").astype("float")
    df["movie_0_before"] = df["movie_0_before"].astype("str").replace("error","0").astype("float")
    df["Actor_3_before"] = df["Actor_3_before"].astype("str").replace("error","0").astype("float")
    df["Actor_2_before"] = df["Actor_2_before"].astype("str").replace("error","0").astype("float")
    df["Actor_1_before"] = df["Actor_1_before"].astype("str").replace("error","0").astype("float")
    df["Actor_0_before"] = df["Actor_0_before"].astype("str").replace("error","0").astype("float")
    df= df.join(pd.get_dummies(df["classification"]).astype("bool"))
    df = df.drop(["classification"], axis=1)
    
    df= df.join(pd.get_dummies(df["release_date_USA"]).astype("bool"))
    df = df.drop(["release_date_USA","Runtime"], axis=1)
    
    
    #onhot encoding
    
    
    
    model_wanted_keys=[
            'runtime', 'budget_in_USD', 'imdbVotes', 'IMDBscore', 'TomatoesScore',
           'Metascore', 'Theater_num', 'movie_3_before', 'movie_2_before',
           'movie_1_before', 'movie_0_before', 'Actor_3_before', 'Actor_2_before',
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

