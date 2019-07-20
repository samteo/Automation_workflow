import json
from urllib.request import urlopen,urlretrieve
from urllib.parse import quote
import string
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csv
import json
import ssl
import requests
import pymongo
import datetime
import pandas as pd
ssl._create_default_https_context = ssl._create_unverified_context

def yahoo_new_movie_list(p=1):
    url = "https://movies.yahoo.com.tw/movie_intheaters.html?page=" + str(p)

    # req = urllib.request.Request(
    #     url,
    #     data=None,
    #     headers={
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    #     }
    # )
    #
    # f = urllib.request.urlopen(req)
    response = urlopen(url)
    html = BeautifulSoup(response, from_encoding="utf-8")
    html = html.find("div", class_="release_box")
    html = html.find_all("div", class_="release_info_text")
    # 拿取中文名稱、英文名稱、上映日期
    d = dict()
    new_movie_list = []

    for each_movie in html:
        chinese_name = each_movie.find("a").text.replace(" ", "").replace("\n", "")
        english_name = each_movie.find("div", class_="en").text.replace("\n", "")[20:]
        TaiwanRelease = each_movie.find("div", class_="release_movie_time")
        TaiwanRelease = each_movie.find("div", class_="release_movie_time").text.split(" ： ")[1].replace("-", "/")


        x = each_movie.find("div", class_="release_movie_name")
        x = x.find("a")
        movie_url = x.get('href')
        chinese_info = requests.get(movie_url)
        chinese_info = BeautifulSoup(chinese_info.text, from_encoding="utf-8")
        chinese_info = chinese_info.find("div", class_="gray_infobox_inner")
        chinese_info = chinese_info.find("span").text.replace("\r\n", "").replace("\n", "").replace(" ", "").replace(
            "\xa0", "")
        # print(chinese_info)
        #電影時刻表
        id = movie_url.split("-")[-1]
        movietime = "https://movies.yahoo.com.tw/movietime_result.html/id="+str(id)

        d = {"chinese_name": chinese_name, "yahoo_english_name": english_name,
             "TaiwanRelease": TaiwanRelease, "yahoo_movie_url": movie_url,"movietime":movietime, "chinese_info": chinese_info}
        new_movie_list.append(d)
    return new_movie_list

def yahoo_thisweek(p=1):
    url = "https://movies.yahoo.com.tw/movie_thisweek.html?page=" + str(p)
    response = urlopen(url)
    html = BeautifulSoup(response, from_encoding="utf-8")
    html = html.find("div", class_="release_box")
    html = html.find_all("div", class_="release_info_text")
    # 拿取中文名稱、英文名稱、上映日期
    d = dict()
    new_movie_list = []

    for each_movie in html:
        chinese_name = each_movie.find("a").text.replace(" ", "").replace("\n", "")
        english_name = each_movie.find("div", class_="en").text.replace("\n", "")[20:]
        TaiwanRelease = each_movie.find("div", class_="release_movie_time")
        TaiwanRelease = each_movie.find("div", class_="release_movie_time").text.split(" ： ")[1].replace("-", "/")

        x = each_movie.find("div", class_="release_movie_name")
        x = x.find("a")
        movie_url = x.get('href')
        chinese_info = requests.get(movie_url)
        chinese_info = BeautifulSoup(chinese_info.text, from_encoding="utf-8")
        chinese_info = chinese_info.find("div", class_="gray_infobox_inner")
        chinese_info = chinese_info.find("span").text.replace("\r\n", "").replace("\n", "").replace(" ", "").replace(
            "\xa0", "")
        # print(chinese_info)
        # 電影時刻表
        id = movie_url.split("-")[-1]
        movietime = "https://movies.yahoo.com.tw/movietime_result.html/id=" + str(id)

        d = {"chinese_name": chinese_name, "yahoo_english_name": english_name,
             "TaiwanRelease": TaiwanRelease, "yahoo_movie_url": movie_url, "movietime": movietime,
             "chinese_info": chinese_info}
        new_movie_list.append(d)
    return new_movie_list

def movie_name_imdbID(english_name):
    imdb_url = "https://www.imdb.com/find?ref_=nv_sr_fn&q=" + english_name + "&s=all"
    response = requests.get(imdb_url)
    html = BeautifulSoup(response.text, from_encoding="utf-8")
    movie = html.find("td", class_="result_text")
    IMDB_number = movie.find("a").get("href").split('/')[2]
    return IMDB_number

def update_movie_OMDB(IMDB_number="tt0446029", apikey="5ab10f1c"):
    url = "http://www.omdbapi.com/?i=" + IMDB_number + "&apikey=" + apikey  # 5ab10f1c(免費)
    response = urlopen(url)

    info = json.load(response)
    info['plot'] = Plot_to_story(info['imdbID'])
    info['year'] = info['year'].replace('-','')
    json.dumps(info)

    return info

def run_movie():
    update_list = []
    MovieInfoList = []
#yahoo this week
    for j in range(1,3):
        thisweek = yahoo_thisweek(p=j)
        update_list += thisweek
# yahoo到第幾頁
    for i in range(1, 3):
        a = yahoo_new_movie_list(p=i)
        update_list += a

    with open("update_list.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(update_list)
    for j in update_list:
        english_name = j['yahoo_english_name']
        # english_name = english_name.split(":")[0]
        try:
            IMDB_number = movie_name_imdbID(english_name=english_name)
            movie_json = update_movie_OMDB(IMDB_number=IMDB_number)
            if movie_json != "":
                movie_json.update(j)
            else:
                continue
        except:
            continue
        MovieInfoList.append(movie_json)
    return MovieInfoList

def update(data = ""):
    i = 0
    data_old = []
    for i in range(len(data)):
        try:
            dict1 = data[i]
            #title = data[i]['Title']
        except  KeyError:
            continue
        data_old.append(dict1)

    data1 = data_old
    for r in range(len(data1)):
        data1[r]['IMDBscore'] = 0
        data1[r]['TomatoesScore'] = 0
        try:
            if data1[r]['Ratings'][1]['Source'] == 'Rotten Tomatoes':
                data1[r]['Ratings'] = [{"Source": "Internet Movie Database", "Value": "N/A"},
                                       {"Source": "Rotten Tomatoes", "Value": data1[r]['Ratings'][1]['Value']},
                                       {"Source": "Metacritic", "Value": "N/A"},
                                       ]
            else:
                data1[r]['Ratings'] = [{"Source": "Internet Movie Database", "Value": "N/A"},
                                       {"Source": "Rotten Tomatoes", "Value": "N/A"},
                                       {"Source": "Metacritic", "Value": "N/A"},
                                       ]
        except IndexError:
            data1[r]['Ratings'] = [{"Source": "Internet Movie Database", "Value": "N/A"},
                                   {"Source": "Rotten Tomatoes", "Value": "N/A"},
                                   {"Source": "Metacritic", "Value": "N/A"},
                                   ]
    for j in range(len(data1)):
        # for k in range(1):
        # j = 68
        imdbID = data1[j]['imdbID']
        metacritic = data1[j]['Title'].lower().replace(" ", "-").replace("é", "e").replace(":", "").replace("!",
                                                                                                            "").replace(
            "'", "").replace(",", "")
        tomato = data1[j]['Title'].lower().replace(" ", "_").replace("é", "e").replace("!", "").replace(":",
                                                                                                        "").replace("'",
                                                                                                                    "").replace(
            ",", "")
        # print(metacritic)
        # imdbID
        url_imdb = 'https://www.imdb.com/title/' + imdbID
        # metacritic
        url_metacritic = 'https://www.metacritic.com/movie/' + metacritic
        url_metacritic = quote(url_metacritic, safe=string.printable)  # 處理特殊字元é
        # tomato
        url_tomato = 'https://www.rottentomatoes.com/m/' + tomato
        url_tomato = quote(url_tomato, safe=string.printable)  # 處理特殊字元é
        year = '_' + str(data1[j]['Year'])
        year = quote(year, safe=string.printable).replace("–", "")
        # print(url_metacritic)
        ############## imdb
        try:
            response_imdb = urlopen(url_imdb)
        except HTTPError:
            # print('有問題的資料imdb', imdbID)
            continue

        html_imdb = BeautifulSoup(response_imdb, from_encoding="utf-8")
        source = html_imdb.find_all("div", class_="imdbRating")  # 找職業   他是list
        try:
            tag3 = html_imdb.find("div", class_="metacriticScore").text  # Metacritic
        except AttributeError:
            tag3 = 'N/A'
        ############## metacritic

        try:
            response_metacritic = urlopen(url_metacritic)
        except HTTPError:
            # print('有問題的資料metacritic', metacritic, '      ', data1[j]['Title'])
            response_metacritic = 'N/A'

        if response_metacritic != 'N/A' and tag3 == 'N/A':
            html_metacritic = BeautifulSoup(response_metacritic, from_encoding="utf-8")
            try:
                tag3 = html_metacritic.find("span", class_="metascore_w").text  # Metacritic
            except AttributeError:
                tag3 = 'N/A'
        if tag3 == 'tbd':
            tag3 = 'N/A'
        ############## tomato
        tag4 = data1[j]['Ratings'][1]['Value']
        # print(data1[j]['Ratings'])
        try:
            response_tomato = urlopen(url_tomato + year)
        except HTTPError:
            url_tomato = url_tomato
            url_tomato = quote(url_tomato, safe=string.printable)  # 處理特殊字元é
            try:
                response_tomato = urlopen(url_tomato)
            except HTTPError:
                # print('有問題的資料tomato', tomato, '      ', data1[j]['Title'])
                response_tomato = 'N/A'
            # print('有問題的資料tomato',tomato,'      ',data1[j]['Title'])
            # response_tomato = 'N/A'

        # if response_tomato != 'N/A' and tag4 == 'N/A':
        if response_tomato != 'N/A':
            html_tomato = BeautifulSoup(response_tomato, from_encoding="utf-8")
            # source_tomato = html_tomato.find("span", class_="mop-ratings-wrap__percentage")
            # print(source_tomato)
            try:
                # for ss in source_tomato:
                #     tag4 = ss.find("span", class_="mop-ratings-wrap__percentage").text  # tomato
                # print(tag4)
                tag4 = html_tomato.find("span", class_="mop-ratings-wrap__percentage").text.replace("\n", "").replace(
                    " ", "")
                # print(tag4)
            except AttributeError:
                tag4 = 'N/A'
        # 避免掉應該加上2019的資料才是正確的，但在沒有2019的狀況下抓到資料，保留原本資料
        if tag4 != 'N/A':
            tag4 = tag4
        elif tag4 == 'N/A' and data1[j]['Ratings'][1]['Value'] == 'N/A':
            tag = 'N/A'
        else:
            tag4 = data1[j]['Ratings'][1]['Value']
            # print('應該要抓的到')

        tag = 0  # Internet Movie Database
        tag1 = 0  # Internet Movie Database
        tag2 = 0  # imdbVotes

        for s in source:
            tag = s.find("span", itemprop="ratingValue").text  # Internet Movie Database
            tag1 = s.find("span", itemprop="bestRating").text  # Internet Movie Database
            tag2 = s.find("span", itemprop="ratingCount").text  # imdbVotes
        # print(tag, tag1, tag2, tag3, tag4)
        # data1[j]['Ratings'][j]['Value'] = str(tag) + '/' +str(tag1)
        data1[j]['Ratings'][0]['Value'] = str(tag) + '/' + str(tag1)
        data1[j]['imdbRating'] = str(tag)
        data1[j]['imdbVotes'] = str(tag2)
        if tag3 == 'N/A':
            data1[j]['Ratings'][2]['Value'] = tag3  # str(lambda x:x+1 if tag3 == 'N/A' else '')
            data1[j]['Metascore'] = tag3
        else:
            data1[j]['Ratings'][2]['Value'] = str(tag3.replace("\n", "")) + '/100'
            data1[j]['Metascore'] = str(tag3.replace("\n", ""))

        data1[j]['Ratings'][1]['Value'] = tag4

        #########################2019-07-08
        try:
            data1[j]['classification'] = data1[j].pop('Rated')
            score = data1[j]['Ratings']
        except:
            continue
        try:
            IMDBscore = round(float(score[0]['Value'].split('/')[0]) / float(score[0]['Value'].split('/')[1]), 2)
        except:
            IMDBscore = 0
        try:
            TomatoesScore = round(float(score[1]['Value'].replace('%', '')) / 100, 2)
        except:
            TomatoesScore = 0
        try:
            Metascore = round(float(score[2]['Value'].split('/')[0]) / float(score[2]['Value'].split('/')[1]), 2)
        except:
            Metascore = 0
        data1[j]['IMDBscore'] = IMDBscore
        data1[j]['TomatoesScore'] = TomatoesScore
        data1[j]['Metascore'] = Metascore

        data1[j].pop('imdbRating')
        data1[j].pop('Ratings')

        # print(type(data1[j]['Ratings']))
    return data1

def change_col_rating(list):
    output_list=[]
    for i in list:
        dic = i
        try:
            dic['classification']= dic.pop('Rated')
            score = dic['Ratings']
        except:
            continue
        try:
            IMDBscore = round(float(score[0]['Value'].split('/')[0]) / float(score[0]['Value'].split('/')[1]),2)
        except:
            IMDBscore - 0
        try:
            TomatoesScore = round(float(score[1]['Value'].replace('%','')) / 100,2)
        except:
            TomatoesScore = 0
        try:
            Metascore = round(float(score[2]['Value'].split('/')[0]) / float(score[2]['Value'].split('/')[1]),2)
        except:
            Metascore = 0
        dic['IMDBscore']= IMDBscore
        dic['TomatoesScore']= TomatoesScore
        dic['Metascore']= Metascore

        dic.pop('imdbRating')
        dic.pop('Ratings')
        output_list.append(dic)
    return output_list

def Plot_to_story(ID):
    url = "https://www.imdb.com/title/"+ID+"/?ref_=fn_al_tt_1"
    res = requests.get(url)
    html = BeautifulSoup(res.text)
    #Plot
    storyline = html.find("div",id="titleStoryLine")
    story = storyline.find("div",class_="canwrap")
    story_str = repr(story.text).split("\\n")[2].replace("   ","")
    return story_str

def start_clawer_new_movie():
    starttime = datetime.datetime.now()
    data = run_movie()
    print("run_movie()花費:",datetime.datetime.now()-starttime)
    all_data = update(data)
    print("update()花費:",datetime.datetime.now()-starttime)



    # with open("update_movie_yahoo1.json", "w", encoding="utf-8")as final:
    #     json.dumps(all_data, final)
    return all_data






if __name__=="__main__":
    #all_new_movie為最後output
    all_new_movie = start_clawer_new_movie()



