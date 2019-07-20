# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:56:10 2019

@author: Big data
"""  
import numpy as np 
#m={'Title': 'Yesterday',
#     'Year': '2019',
#     'classification': 'PG-13',
#     'Released': '08 Aug 2019',
#     'runtime': '116 min',
#     'Genre': 'Comedy, Fantasy, Music, Musical, Romance',
#     'Director': 'Danny Boyle',
#     'Writer': 'Jack Barth (story by), Richard Curtis (screenplay), Richard Curtis (story by)',
#     'Actors': 'Himesh Patel, Lily James, Sophia Di Martino, Ellise Chappell',
#     'Plot': "A struggling musician realizes he's the only person on Earth who can remember The Beatles after waking up in an alternate timeline where they never existed.",
#     'Language': 'English',
#     'Country': 'UK',
#     'Awards': 'N/A',
#     'Poster': 'https://m.media-amazon.com/images/M/MV5BYzE4MGU0MTYtYTYwNS00ZTljLWEwYTItNmNlYTg2MTViZWExXkEyXkFqcGdeQXVyMjUxMTY3ODM@._V1_SX300.jpg',
#     'Ratings': [{'Source': 'Internet Movie Database', 'Value': '6.7/10'},
#      {'Source': 'Rotten Tomatoes', 'Value': '65%'},
#      {'Source': 'Metacritic', 'Value': '54/100'}],
#     'Metascore': '54',
#     "TomatoesScore": "0.65",
#     'IMDBscore': '6.7',
#     'imdbVotes': '717',
#     'imdbID': 'tt8079248',
#     'Type': 'movie',
#     'DVD': 'N/A',
#     'BoxOffice': 'N/A',
#     'Production': 'Universal Pictures',
#     'Website': 'N/A',
#     'Response': 'True',
#     "Theater_num":20,
#     'movie_8_before': 30,
#     'movie_7_before': 36,
#     'movie_6_before': 100,
#     'movie_5_before': 99,
#     'movie_4_before': 0,
#     'movie_3_before': 0,
#     'movie_2_before': 0,
#     'movie_1_before': 0,
#     'movie_0_after': 0,
#     'movie_1_after': 0,
#     'movie_2_after': 0,
#     'movie_3_after': 0,
#     'movie_4_after': 0,
#     'movie_5_after': 0,
#     'movie_6_after': 0,
#     'movie_7_after': 0,
#     'movie_8_after': 0,
#     'Actor_8_before': 26.25,
#     'Actor_7_before': 5.0,
#     'Actor_6_before': 30.0,
#     'Actor_5_before': 54.0,
#     'Actor_4_before': 0.0,
#     'Actor_3_before': 0.0,
#     'Actor_2_before': 0.0,
#     'Actor_1_before': 0.0,
#     'Actor_0_after': 0.0,
#     'Actor_1_after': 0.0,
#     'Actor_2_after': 0.0,
#     'Actor_3_after': 0.0,
#     'Actor_4_after': 0.0,
#     'Actor_5_after': 0.0,
#     'Actor_6_after': 0.0,
#     'Actor_7_after': 0.0,
#     'Actor_8_after': 0.0,
#     'moive_name_thenumbers': 404,
#     "Domestic_box_office": np.nan,
#     'International Box Office': np.nan,
#     'Worldwide Box Office': np.nan}
t={'Title': 'Wild Rose',
 'Year': '2018',
 'Released': '21 Jun 2019',
 'Runtime': '100 min',
 'Genre': 'Drama, Music',
 'Director': 'Tom Harper',
 'Writer': 'Nicole Taylor',
 'Actors': 'Jessie Buckley, Matt Costello, Jane Patterson, Lesley Hart',
 'Plot': 'A musician from Glasgow dreams of becoming a Nashville star.',
 'Language': 'English',
 'Country': 'UK',
 'Awards': 'N/A',
 'Poster': 'https://m.media-amazon.com/images/M/MV5BYjBkOTZlNmYtN2NjOS00YWM2LTk0MzMtOTEwMmIyNWIwMDA5XkEyXkFqcGdeQXVyNjg3MDMxNzU@._V1_SX300.jpg',
 'Metascore': 0.79,
 'imdbVotes': '1,972',
 'imdbID': 'tt5117428',
 'Type': 'movie',
 'DVD': 'N/A',
 'BoxOffice': 'N/A',
 'Production': 'NEON',
 'Website': 'https://www.wildrose-movie.com/',
 'Response': 'True',
 'plot': " Rose-Lynn Harlan is bursting with raw talent, charisma and cheek. Fresh out of prison and reunited with her son and daughter, all she wants is to get out of Glasgow and make it as a country singer in Nashville. Rose's mother Marion, on the other hand, has had a bellyful of her worthless nonsense. Forced to take strict responsibility, Rose gets a cleaning job, only to find an unlikely champion in the middle-class lady of the house.",
 'chinese_name': '鏗鏘玫瑰',
 'yahoo_english_name': 'Wild Rose',
 'TaiwanRelease': '2019/07/12',
 'yahoo_movie_url': 'https://movies.yahoo.com.tw/movieinfo_main/%E9%8F%97%E9%8F%98%E7%8E%AB%E7%91%B0-wild-rose-9914',
 'movietime': 'https://movies.yahoo.com.tw/movietime_result.html/id=9914',
 'chinese_info': '★繼《一個巨星的誕生》之後，今年最動人的音樂電影！★《美人心機》製作團隊，打造又一經典女性電影！★溫柔樂觀、細膩描繪家庭與夢想之間的動人情感，深具魅力！★年度新星潔西伯克利，大展充滿渲染力的絕美歌喉，驚豔影壇代表作！★強勢入選多倫多影展、翠貝卡影展、台北電影節等各大國際影展！★國際影迷熱烈追捧，「爛番茄」新鮮度89%好評如潮！★權威媒體《綜藝》盛讚：「一部讓人感動流淚的作品！」站在人生交叉點，傾聽夢想最真實的聲音年輕有活力、性格奔放不羈的蘿絲琳（潔西伯克利飾演），她天生有副絕美嗓音，一心夢想成為鄉村音樂天后。然而她剛出獄、身無分文，又有兩個小孩要照顧；就連始終在背後幫助她的母親（茱莉華特絲飾演），都希望她能改頭換面、成為一個負責任的大人。有案底的蘿絲琳，困於現實壓力，只好到有錢人家幫傭。就當她的雇主（蘇菲歐克妮飾演）發現她驚人的歌唱才華，並積極籌錢助她逐夢時，好不容易與孩子消除隔閡的她，將面臨家庭與夢想的艱難抉擇…。究竟，蘿絲琳能否找到夢想中最真實的聲音，唱出屬於自己的歌曲呢？【關於電影】繼《一個巨星的誕生》之後，今年最動人的音樂電影本片除了找來驚艷影壇的亮眼新人潔西伯克利領銜主演之外，更請來獲獎無數的英國演技派女星茱莉華特絲（JulieWalters）、以及曾入圍奧斯卡的性格女星蘇菲歐克妮多（SophieOkonedo）共同飆戲。憑藉真誠的劇本、精湛的演技，以及直探靈魂的動人音樂，讓本片強勢入選多倫多影展、翠貝卡影展、舊金山影展、台北電影節等各大國際影展，並持續獲得影迷熱烈追捧。本片不但在「爛番茄網站」的新鮮度始終居高不下，更被國際媒體推爆好評，權威媒體《綜藝》（Variety）更盛讚：「這是一部令人著迷的悲喜劇，讓人沉浸在感動的熱淚當中！」',
 'IMDBscore': 0.74,
 'TomatoesScore': 0.94,
 'classification': 'R',
 'moive_name_thenumbers': 'Wild Rose (2019)',
 'Domestic Box Office': '$381,154',
 'International Box Office': '$3,230,568',
 'Worldwide Box Office': '$3,611,722',
 'budget_in_USD': np.nan,
 'Theater_num': 63}
def predict_loss(m):
    import pymongo
    import pandas as pd
    import numpy as np
    import re
    import xgboost as xgb

    
    wanted_keys={"Runtime","budget_in_USD","Production","imdbVotes","IMDBscore","TomatoesScore","Metascore","Theater_num",
                 "movie_2_before","movie_1_before","movie_0_before","Actor_2_before","Actor_1_before","Actor_0_before",
                 "Genre","Language","Country","classification"}
    
    wanted_dict  = {key : [val] for key ,val in m.items() if key in wanted_keys}
    df_company = pd.read_csv("company_detail.csv")
    company_dict = {}
    for i, s in df_company.iterrows():
        company_dict[s["company"]] = s["avg"]
    key = list(company_dict.keys())
    
    regex_pat = re.compile(r"[^a-zA-Z0-9]+", flags=re.IGNORECASE)
    wanted_dict["Production"][0] = re.sub(regex_pat,'', wanted_dict["Production"][0]).lower()
    wanted_dict["Production"] = wanted_dict["Production"][0]
    print(wanted_dict["Production"])
    for x in key:
        if wanted_dict["Production"].find(x) != -1:
           wanted_dict["Production"] = company_dict[wanted_dict["Production"]] 
           break 
    print("type",type(wanted_dict["Production"]),type(wanted_dict["Production"]) == 'str',wanted_dict["Production"])
    if type(wanted_dict["Production"]) == str:
        wanted_dict["Production"]= 200000
    
    df = pd.DataFrame.from_dict(wanted_dict)        
    cleaned = df.Genre.str.split(',', expand=True).stack()
    cleaned = cleaned.apply(lambda x:x.replace(" ",""))
    genre_enc = pd.get_dummies(cleaned, prefix='g').groupby(level=0,sort=False).sum()
    
    cleaned = df.Language.str.split(',', expand=True).stack()
    cleaned = cleaned.apply(lambda x:x.replace(" ",""))
    #drop_lang = (cleaned.value_counts()[cleaned.value_counts()<=5]).index.tolist()
    #for l in range(len(cleaned)):
    #    if cleaned.iloc[l] in drop_lang:
    #        cleaned.iloc[l] = "Other_language"
    language_enc = pd.get_dummies(cleaned, prefix='L').groupby(level=0,sort=False).sum()
    
    cleaned = df.Country.str.split(',', expand=True).stack()
    cleaned = cleaned.apply(lambda x:x.replace(" ",""))
    country_enc = pd.get_dummies(cleaned, prefix='L').groupby(level=0,sort=False).sum()
    try:
        df["budget_in_USD"] = df["budget_in_USD"].str.replace("$","").str.replace(",","")
    except:
        pass
    if  pd.isnull(df["budget_in_USD"]).any():
        df["budget_in_USD"] = 5000000   
    df["Runtime"] = df["Runtime"].str.replace("min","")
    df["imdbVotes"]=df["imdbVotes"].str.replace(",","")
    for e in df.columns:
        if "movie" or "Actor" in e:
            df[e] = df[e].replace("error","0")
    cla_enc = pd.get_dummies(df["classification"])
    df = df.drop(["classification","Genre","Language","Country"],axis=1)
    
    for i in df.columns:
        print(i)
        try:
            df[i] =pd.to_numeric(df[i], downcast='float')
            #df["budget_in_USD"] = np.log(df["budget_in_USD"])
        except:
            pass
                
    
    #df["Production"] = np.log(df["Production"])   
    df["Theater_num"] = np.log(df["Theater_num"]) 
    df = pd.concat([df.reset_index(drop=True),genre_enc.reset_index(drop=True),
                    country_enc.reset_index(drop=True),language_enc.reset_index(drop=True),
                    cla_enc.reset_index(drop=True)
                    ],
                    axis=1) 
    
    
    
    feature = ['budget_in_USD','Production','imdbVotes','IMDBscore','TomatoesScore','Metascore','Theater_num',
 'movie_2_before','movie_1_before','movie_0_before',
 'Actor_2_before','Actor_1_before','Actor_0_before','Runtime','g_Action','g_Adventure','g_Animation','g_Biography',
 'g_Comedy','g_Crime','g_Drama','g_Family','g_Fantasy','g_History',
 'g_Horror','g_Music','g_Musical','g_Mystery','g_Romance','g_Sci-Fi',
 'g_Sport','g_Thriller','g_War','g_Western','L_Algeria','L_Angola','L_Argentina','L_Australia',
 'L_Austria','L_Belgium','L_BosniaandHerzegovina','L_Botswana','L_Brazil','L_BritishVirginIslands','L_Bulgaria','L_Cambodia',
 'L_Canada','L_CaymanIslands','L_Chile','L_China','L_Colombia',
 'L_Croatia','L_Cyprus','L_CzechRepublic','L_Denmark','L_Egypt','L_Estonia','L_Finland','L_France','L_Georgia',
 'L_Germany','L_Greece','L_HongKong','L_Hungary','L_Iceland','L_India','L_Indonesia','L_Iran',
 'L_Ireland','L_IsleOfMan','L_Israel','L_Italy','L_Japan','L_Jordan','L_Kazakhstan','L_Kenya','L_Lebanon','L_Liechtenstein',
 'L_Lithuania','L_Luxembourg','L_Malta','L_Mexico','L_Monaco','L_Mongolia','L_Morocco',
 'L_Myanmar','L_Nepal','L_Netherlands','L_NewZealand','L_Nigeria','L_Norway','L_Palestine','L_Panama','L_Paraguay','L_Peru',
 'L_Philippines','L_Poland','L_Portugal','L_PuertoRico','L_Qatar','L_Romania','L_Russia','L_SaudiArabia','L_Serbia','L_Singapore','L_Slovakia',
 'L_Slovenia','L_SouthAfrica','L_SouthKorea','L_Spain','L_Sweden','L_Switzerland','L_Taiwan','L_Thailand',
 'L_Tunisia','L_Turkey','L_UK','L_USA','L_Ukraine','L_UnitedArabEmirates','L_Uruguay','L_Venezuela','L_Vietnam','G','NC-17','NotRated','PG',
 'PG-13','R','TV-14','TV-MA','TV-PG','Unrated']
    
    #feature2 = ['IMDBscore','TV-MA','g_Action','L_Canada','L_HongKong','L_Mexico','L_Jordan','L_India','movie_2_before','L_Chile','L_Peru',
    # 'g_Crime','g_Comedy','L_Denmark','L_Venezuela','L_Mongolia','L_Portugal','Actor_1_before','g_Music','L_Iran','L_Cyprus','NotRated',
    # 'L_BritishVirginIslands','L_CaymanIslands','L_Iceland','L_Kazakhstan','L_Romania','L_Palestine','TomatoesScore','L_Philippines','L_SaudiArabia',
    # 'L_Argentina','budget_in_USD','L_Italy','L_Netherlands','L_Spain','L_UK','g_Drama','L_Malta','Unrated','L_Singapore','L_France',
    # 'L_Austria','L_Egypt','L_Kenya','runtime','g_Romance','L_Switzerland','L_SouthAfrica','imdbVotes','L_Lithuania','g_Sport',
    # 'movie_0_before','TV-14','L_Slovenia','movie_1_before','L_Nigeria','L_PuertoRico','Actor_2_before','L_Japan','L_Indonesia','g_Fantasy',
    # 'L_Israel','NC-17','L_Bulgaria','L_Luxembourg','L_Estonia','L_Algeria','g_Musical','L_IsleOfMan','L_Poland','L_Ireland','Actor_0_before',
    # 'g_War','L_Paraguay','L_Cambodia','Metascore','L_Monaco','L_Angola','L_Turkey','L_Georgia','L_Serbia','L_Panama','Production','L_Australia',
    # 'L_Colombia','g_Adventure','PG','L_Uruguay','PG-13','g_History','L_Morocco','L_Hungary','L_Myanmar','L_Ukraine','G','TV-PG','g_Horror',
    # 'L_Brazil','R','L_Vietnam','L_Lebanon','L_Belgium','g_Sci-Fi','L_Botswana','g_Western','L_Tunisia','L_BosniaandHerzegovina','L_Qatar',
    # 'g_Thriller','L_Finland','L_Russia','g_Biography','L_SouthKorea','L_Germany','L_Liechtenstein','L_NewZealand','L_Thailand','g_Animation',
    # 'L_Croatia','L_Greece','L_Sweden','L_UnitedArabEmirates','L_CzechRepublic','L_USA','g_Mystery','L_Taiwan','L_Nepal','L_Slovakia',
    # 'L_Norway','g_Family','Theater_num','L_China']
    
    data = [0]*len(feature)
    df_model = pd.DataFrame(data=[data],columns=feature)
    df_model.update(df)
#    feature_list = ["f"+str(i) for i in range(len(feature))]
#    df_model.columns = feature_list
    #for f in feature2:
    #    if f not in df.columns.tolist():
    #        df_append = pd.DataFrame.from_dict({f:[0]})
    #        df=pd.concat([df,df_append],axis=1)
    #import joblib
    #xgb = joblib.load("modeltest")
    import pickle
    loaded_model = pickle.load(open("loss.pickle.dat", "rb"))
    y_pred = loaded_model.predict(df_model)
    y_pred = np.exp(y_pred)
    print("Prediction (loss)=",y_pred[0])
    m["Predict"]= y_pred[0]
    return m

def predict_gain(m):
    import pymongo
    import pandas as pd
    import numpy as np
    import re
    import xgboost as xgb

    
    wanted_keys={"Runtime","budget_in_USD","Production","imdbVotes","IMDBscore","TomatoesScore","Metascore","Theater_num",
                 "movie_2_before","movie_1_before","movie_0_before","Actor_2_before","Actor_1_before","Actor_0_before",
                 "Genre","Language","Country","classification"}
    
    wanted_dict  = {key : [val] for key ,val in m.items() if key in wanted_keys}
    df_company = pd.read_csv("company_detail.csv")
    company_dict = {}
    for i, s in df_company.iterrows():
        company_dict[s["company"]] = s["avg"]
    key = list(company_dict.keys())
    
    regex_pat = re.compile(r"[^a-zA-Z0-9]+", flags=re.IGNORECASE)
    wanted_dict["Production"][0] = re.sub(regex_pat,'', wanted_dict["Production"][0]).lower()
    wanted_dict["Production"] = wanted_dict["Production"][0]
    print(wanted_dict["Production"])
    for x in key:
        if wanted_dict["Production"].find(x) != -1:
           wanted_dict["Production"] = company_dict[wanted_dict["Production"]] 
           break 
    print("type",type(wanted_dict["Production"]),type(wanted_dict["Production"]) == 'str',wanted_dict["Production"])
    if type(wanted_dict["Production"]) == str:
        wanted_dict["Production"]= 200000
    
    df = pd.DataFrame.from_dict(wanted_dict)        
    cleaned = df.Genre.str.split(',', expand=True).stack()
    cleaned = cleaned.apply(lambda x:x.replace(" ",""))
    genre_enc = pd.get_dummies(cleaned, prefix='g').groupby(level=0,sort=False).sum()
    
    cleaned = df.Language.str.split(',', expand=True).stack()
    cleaned = cleaned.apply(lambda x:x.replace(" ",""))
    #drop_lang = (cleaned.value_counts()[cleaned.value_counts()<=5]).index.tolist()
    #for l in range(len(cleaned)):
    #    if cleaned.iloc[l] in drop_lang:
    #        cleaned.iloc[l] = "Other_language"
    language_enc = pd.get_dummies(cleaned, prefix='L').groupby(level=0,sort=False).sum()
    
    cleaned = df.Country.str.split(',', expand=True).stack()
    cleaned = cleaned.apply(lambda x:x.replace(" ",""))
    country_enc = pd.get_dummies(cleaned, prefix='L').groupby(level=0,sort=False).sum()   
    try:
        df["budget_in_USD"] = df["budget_in_USD"].str.replace("$","").str.replace(",","")
    except:
        pass
    if  pd.isnull(df["budget_in_USD"]).any():
        df["budget_in_USD"] = 5000000   
    df["Runtime"] = df["Runtime"].str.replace("min","")
    df["imdbVotes"]=df["imdbVotes"].str.replace(",","")
    for e in df.columns:
        if "movie" or "Actor" in e:
            df[e] = df[e].replace("error","0")
    cla_enc = pd.get_dummies(df["classification"])
    df = df.drop(["classification","Genre","Language","Country"],axis=1)
    
    for i in df.columns:
        print(i)
        try:
            df[i] =pd.to_numeric(df[i], downcast='float')
            #df["budget_in_USD"] = np.log(df["budget_in_USD"])
        except:
            pass
        
    
    #df["Production"] = np.log(df["Production"])   
    df["Theater_num"] = np.log(df["Theater_num"]) 
    df = pd.concat([df.reset_index(drop=True),genre_enc.reset_index(drop=True),
                    country_enc.reset_index(drop=True),language_enc.reset_index(drop=True),
                    cla_enc.reset_index(drop=True)
                    ],
                    axis=1) 
    
    
    
    feature = ['budget_in_USD', 'Production', 'imdbVotes', 'IMDBscore',
       'TomatoesScore', 'Metascore', 'Theater_num', 'movie_2_before',
       'movie_1_before', 'movie_0_before', 'Actor_2_before', 'Actor_1_before',
       'Actor_0_before', 'Runtime', 'g_Action', 'g_Adventure', 'g_Animation',
       'g_Biography', 'g_Comedy', 'g_Crime', 'g_Drama', 'g_Family',
       'g_Fantasy', 'g_History', 'g_Horror', 'g_Music', 'g_Musical',
       'g_Mystery', 'g_Romance', 'g_Sci-Fi', 'g_Sport', 'g_Thriller', 'g_War',
       'g_Western', 'L_Argentina', 'L_Australia', 'L_Austria', 'L_Bahamas',
       'L_Belgium', 'L_Brazil', 'L_Bulgaria', 'L_Cambodia', 'L_Canada',
       'L_Chile', 'L_China', 'L_Colombia', 'L_CzechRepublic', 'L_Denmark',
       'L_DominicanRepublic', 'L_Finland', 'L_France', 'L_Germany', 'L_Greece',
       'L_HongKong', 'L_Hungary', 'L_Iceland', 'L_India', 'L_Indonesia',
       'L_Iran', 'L_Ireland', 'L_IsleOfMan', 'L_Israel', 'L_Italy', 'L_Japan',
       'L_Kenya', 'L_Luxembourg', 'L_Malaysia', 'L_Malta', 'L_Mexico',
       'L_Morocco', 'L_Netherlands', 'L_NewZealand', 'L_Norway',
       'L_Philippines', 'L_Poland', 'L_Romania', 'L_Russia', 'L_Serbia',
       'L_Singapore', 'L_Slovakia', 'L_SouthAfrica', 'L_SouthKorea', 'L_Spain',
       'L_Sweden', 'L_Switzerland', 'L_Taiwan', 'L_Thailand', 'L_Turkey',
       'L_UK', 'L_USA', 'L_Ukraine', 'L_UnitedArabEmirates', 'G', 'NotRated',
       'PG', 'PG-13', 'R', 'Unrated']
    
    #feature2 = ['IMDBscore','TV-MA','g_Action','L_Canada','L_HongKong','L_Mexico','L_Jordan','L_India','movie_2_before','L_Chile','L_Peru',
    # 'g_Crime','g_Comedy','L_Denmark','L_Venezuela','L_Mongolia','L_Portugal','Actor_1_before','g_Music','L_Iran','L_Cyprus','NotRated',
    # 'L_BritishVirginIslands','L_CaymanIslands','L_Iceland','L_Kazakhstan','L_Romania','L_Palestine','TomatoesScore','L_Philippines','L_SaudiArabia',
    # 'L_Argentina','budget_in_USD','L_Italy','L_Netherlands','L_Spain','L_UK','g_Drama','L_Malta','Unrated','L_Singapore','L_France',
    # 'L_Austria','L_Egypt','L_Kenya','runtime','g_Romance','L_Switzerland','L_SouthAfrica','imdbVotes','L_Lithuania','g_Sport',
    # 'movie_0_before','TV-14','L_Slovenia','movie_1_before','L_Nigeria','L_PuertoRico','Actor_2_before','L_Japan','L_Indonesia','g_Fantasy',
    # 'L_Israel','NC-17','L_Bulgaria','L_Luxembourg','L_Estonia','L_Algeria','g_Musical','L_IsleOfMan','L_Poland','L_Ireland','Actor_0_before',
    # 'g_War','L_Paraguay','L_Cambodia','Metascore','L_Monaco','L_Angola','L_Turkey','L_Georgia','L_Serbia','L_Panama','Production','L_Australia',
    # 'L_Colombia','g_Adventure','PG','L_Uruguay','PG-13','g_History','L_Morocco','L_Hungary','L_Myanmar','L_Ukraine','G','TV-PG','g_Horror',
    # 'L_Brazil','R','L_Vietnam','L_Lebanon','L_Belgium','g_Sci-Fi','L_Botswana','g_Western','L_Tunisia','L_BosniaandHerzegovina','L_Qatar',
    # 'g_Thriller','L_Finland','L_Russia','g_Biography','L_SouthKorea','L_Germany','L_Liechtenstein','L_NewZealand','L_Thailand','g_Animation',
    # 'L_Croatia','L_Greece','L_Sweden','L_UnitedArabEmirates','L_CzechRepublic','L_USA','g_Mystery','L_Taiwan','L_Nepal','L_Slovakia',
    # 'L_Norway','g_Family','Theater_num','L_China']
    
    data = [0]*len(feature)
    df_model = pd.DataFrame(data=[data],columns=feature)
    df_model.update(df)
#    feature_list = ["f"+str(i) for i in range(len(feature))]
#    df_model.columns = feature_list
    #for f in feature2:
    #    if f not in df.columns.tolist():
    #        df_append = pd.DataFrame.from_dict({f:[0]})
    #        df=pd.concat([df,df_append],axis=1)
    #import joblib
    #xgb = joblib.load("modeltest")
    import pickle
    loaded_model = pickle.load(open("gain.pickle.dat", "rb"))
    y_pred = loaded_model.predict(df_model)
    y_pred = np.exp(y_pred)
    print("Prediction (gain)=",y_pred[0])
    m["Predict"]= y_pred[0]
    return m

if __name__ == "__main__":
    predict_loss(t)














