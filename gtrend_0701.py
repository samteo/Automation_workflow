from pytrends.request import TrendReq #API
import time
import random
import json
import pandas as pd
import numpy as np



def month(m):
    mon={
        "Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,
        "Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12
    }
    return mon.get(m)



def g_trend_movie(movie,release_date):
    s_movie=movie
    if "," in movie:          #Gooletrends不可使用"，" 分隔 所以將名稱有"，"的取代成空白
        s_movie = movie.replace(",", " ")
    if "：" in movie:
        s_movie = movie.split("：")[0]
        
    release_year=int(release_date.split(" ")[-1])   #取上映年分，還有前一年和後一年
    release_mon=release_date.split(" ")[1]
    release_mon=month(release_mon)
    release_day=int(release_date.split(" ")[0])
         
    
    front_year=int(release_year)-1
    next_year=int(release_year)+1
    timeframe = str(front_year) + "-01-01 " + str(next_year) + "-12-31"
    
    pytrend = TrendReq(tz=360)
    kw_list=[s_movie]
    pytrend.build_payload(kw_list=kw_list,cat=34,timeframe=timeframe,geo="US",gprop="")  #搜尋使用的參數,其中cat=34 為電影類別
    
    moviedata = pytrend.interest_over_time().get(kw_list)
    try:
        moviedata.rename(columns={moviedata.columns[0]: "Count" }, inplace=True)                   
        moviedata_list = json.loads(moviedata.to_json(orient='table'))['data']
        if release_mon==2:
            start_mon=12
            start_year=release_year -1
        elif release_mon==1:
            start_mon=11
            start_year=release_year -1
        else:
            start_mon=release_mon-2
            start_year=release_year  
        start_day=release_day
        for l in moviedata_list:
            tempdate=l["date"][0:10]
            l["date"]=tempdate
        node_day=0
        day_count=0
        node_count=0
        for l in moviedata_list:
            year_gt=int(l["date"].split("-")[0])
            mon_gt=int(l["date"].split("-")[1])
            day_gt=int(l["date"].split("-")[-1])
            if year_gt==start_year and  mon_gt==start_mon:
                if node_day <start_day:
                    node_day=day_gt
                    node_count=day_count
            day_count+=1
        #node_data= moviedata_list[node_count]
   
        output_list=[]
        for i in range (17):    
            try:
                #print(moviedata_list[node_count+i],i)
                output_list.append(moviedata_list[node_count+i]["Count"])
            except:
                output_list.append(0)
    except:
        output_list=[0,0,0,0,0,
                     0,0,0,0,0,
                     0,0,0,0,0,
                     0,0]
        
    output_df=pd.DataFrame([output_list])
        
    j=8
    for i in range(0,9,1):    
        output_df=output_df.rename(columns={i:"movie_"+str(j)+"_before"})
        j-=1
    j=1
    for i in range(9,17,1):    
        output_df=output_df.rename(columns={i:"movie_"+str(j)+"_after"})
        j+=1
    output_df=output_df.to_dict(orient='records')
    return output_df

def g_trend_actor(actor,release_date):
    actor_alist=actor.split(",")
        
    release_year=int(release_date.split(" ")[-1])  
    release_mon=release_date.split(" ")[1]
    release_mon=month(release_mon)
    release_day=int(release_date.split(" ")[0])
    
    timeframe=["2004-01-01 2007-12-31","2008-01-01 2011-12-31","2012-01-01 2015-12-31","2016-01-01 2019-12-31"]
    output_total= np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    for actor in actor_alist:
        actordata_list=[]
        for t in timeframe:
            time.sleep(random.randint(3,5))
            #print(actor,t)
            pytrend = TrendReq(tz=360)
            kw_list=[actor]
            pytrend.build_payload(kw_list=kw_list,cat=34,timeframe=t,geo="US",gprop="")  #搜尋使用的參數,其中cat=34 為電影類別
            
            actordata = pytrend.interest_over_time().get(kw_list)
            try:
                actordata.rename(columns={actordata.columns[0]: "Count" }, inplace=True)
            except:
                continue
            temp_actordata_list = json.loads(actordata.to_json(orient='table'))['data']
            actordata_list += temp_actordata_list
        
            
        for l in actordata_list:
            tempdate=l["date"][0:10]
            l["date"]=tempdate
            
        if release_mon==2:
            start_mon=12
            start_year=release_year -1
        elif release_mon==1:
            start_mon=11
            start_year=release_year -1
        else:
            start_mon=release_mon-2
            start_year=release_year  
        start_day=release_day
        node_day=0
        day_count=0
        node_count=0
        for l in actordata_list:
            year_gt=int(l["date"].split("-")[0])
            mon_gt=int(l["date"].split("-")[1])
            day_gt=int(l["date"].split("-")[-1])
            if year_gt==start_year and  mon_gt==start_mon:
                if node_day <start_day:
                    node_day=day_gt
                    node_count=day_count
            day_count+=1
        #print(actordata_list[node_count],"rr")
        
        output_list=[]
        for i in range (17):
            try:
                #print(actordata_list[node_count+i],i)
                output_list.append(actordata_list[node_count+i]["Count"])
            except:
                output_list.append(0)
        output_list=np.array(output_list)
        
        output_total=output_total+output_list
    output_avg=output_total/len(actor_alist)
    output_avg=pd.DataFrame([output_avg])
    j=8
    for i in range(0,9,1):    
        output_avg=output_avg.rename(columns={i:"Actor_"+str(j)+"_before"})
        j-=1
    j=1
    for i in range(9,17,1):    
        output_avg=output_avg.rename(columns={i:"Actor_"+str(j)+"_after"})
        j+=1
    output_avg=output_avg.to_dict(orient='records')
    return output_avg

def trends(input_json):
    i=1
    output=[]
    for m in input_json:
        #m=input_data[1]
        try: 
            movie=m["Title"]
            release_date=m["Released"]
            actor=m["Actors"]
        except:
            output.append(m)
#            with open("testqwe.json", 'a',encoding="utf-8") as outfile:
#                if i==1:
#                    outfile.write("["+json.dumps(m,ensure_ascii= False)+"\n")
#                else:
#                    outfile.write(","+json.dumps(m,ensure_ascii= False) + "\n")
            continue
        col_movie=g_trend_movie(movie,release_date)
        col_actor=g_trend_actor(actor,release_date)
        m=dict(m,**col_movie[0])
        m=dict(m,**col_actor[0])
        output.append(m)
#        with open("testqwe.json", 'a',encoding="utf-8") as outfile:
#            if i==1:
#                outfile.write("["+json.dumps(m,ensure_ascii= False)+"\n")
#            else:
#                outfile.write(","+json.dumps(m,ensure_ascii= False) + "\n")
#        outfile.close()
        
#    with open("testqwe.json", 'a',encoding="utf-8") as outfile:
#        outfile.write("]")
#    outfile.close()
    i+=1
    return output
 
