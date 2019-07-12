# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 18:25:38 2019

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
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc


df_origin = pd.read_csv(r"movie628_1.csv",encoding='utf-8')
df = df_origin
pd.options.display.max_rows


df = df.drop(["movie_1_after","movie_2_after",'movie_3_after',"movie_4_after","movie_5_after","movie_6_after","movie_7_after","movie_8_after",
              "Actor_1_after","Actor_2_after","Actor_3_after","Actor_4_after","Actor_5_after","Actor_6_after","Actor_7_after","Actor_8_after",
              "Cmovie_1_after","Cmovie_2_after","Cmovie_3_after","Cmovie_4_after","Cmovie_5_after","Cmovie_6_after","Cmovie_7_after","Cmovie_8_after",
              "Unnamed: 0","id","Cmovie_8_before","Cmovie_7_before","Cmovie_6_before","Cmovie_5_before","Cmovie_4_before",
              "Actor_8_before","Actor_7_before","Actor_6_before","Actor_5_before","Actor_4_before",
              "movie_8_before","movie_7_before","movie_6_before","movie_5_before","movie_4_before",
              "Cmovie_3_before","Cmovie_2_before","Cmovie_1_before","Cmovie_0_before","movie_3_before","Actor_3_before"
                     ],axis = 1)
df["runtime"] = df["runtime"].str.replace("min","")
df["runtime"] = df["runtime"].astype("float")

df.loc[(df[df['budget_in_USD']=='5353754?'].index),"budget_in_USD"] = "7000000"
df["budget_in_USD"] = df["budget_in_USD"].astype("float")


df["imdbVotes"] = df["imdbVotes"].str.replace(",","")
df["imdbVotes"] = df["imdbVotes"].astype("float")

df["gross_na"] = df["gross_na"].str.replace("$","").str.replace(",","").astype('float')
df['release_date_USA'] = df.release_date_USA.str.split('-',expand=True)[1]

#df["Cmovie_3_before"] = df["Cmovie_3_before"].astype("str").replace("error","0").astype("float")
#df["Cmovie_2_before"] = df["Cmovie_2_before"].astype("str").replace("error","0").astype("float")
#df["Cmovie_1_before"] = df["Cmovie_1_before"].astype("str").replace("error","0").astype("float")
#df["Cmovie_0_before"] = df["Cmovie_0_before"].astype("str").replace("error","0").astype("float")
#df["movie_3_before"] = df["movie_3_before"].astype("str").replace("error","0").astype("float")
df["movie_2_before"] = df["movie_2_before"].astype("str").replace("error","0").astype("float")
df["movie_1_before"] = df["movie_1_before"].astype("str").replace("error","0").astype("float")
df["movie_0_before"] = df["movie_0_before"].astype("str").replace("error","0").astype("float")
#df["Actor_3_before"] = df["Actor_3_before"].astype("str").replace("error","0").astype("float")
df["Actor_2_before"] = df["Actor_2_before"].astype("str").replace("error","0").astype("float")
df["Actor_1_before"] = df["Actor_1_before"].astype("str").replace("error","0").astype("float")
df["Actor_0_before"] = df["Actor_0_before"].astype("str").replace("error","0").astype("float")


df = df.drop(["name","year","opening_weekend","Domestic_box_office","gross_g","release_date","gross_tw","gross_cn","gross_hk","gross_my",
              "gross_sg","Director","Writer","Actors","Language","Awards","Country","Production",
              "ChineseName","TaiwanRelease","International_box_office","Worldwide_box_office","gross_xndom"
                     ],axis = 1)

df= df.join(pd.get_dummies(df["classification"]).astype("bool"))
df = df.drop(["classification"], axis=1)

df= df.join(pd.get_dummies(df["release_date_USA"]).astype("bool"))
df = df.drop(["release_date_USA"], axis=1)

genretrans = df.Genre.str.split(',', expand=True).stack()
genretrans = genretrans.apply(lambda x:x.replace(" ",""))
genretrans = pd.get_dummies(genretrans).groupby(level=0).sum()
df =df.join(genretrans)
df = df.drop(["Genre"], axis=1)


df = df.dropna(subset=['budget_in_USD'])
df = df.dropna(subset=['gross_na'])
df["TomatoesScore"] = df["TomatoesScore"].fillna(df["TomatoesScore"].median())
df["Metascore"] = df["Metascore"].fillna(df["Metascore"].median())
df["Theater_num"] = df["Theater_num"].fillna(df["Theater_num"].median())

df = df.rename(columns={'gross_na':'Domestic_box_office'})



a = df["Domestic_box_office"]/df["budget_in_USD"] > 1
df_1 = pd.concat([df,a],axis =1)
df_1 = df_1.drop(["Domestic_box_office"],axis = 1)


y = df_1[0]
df_1 = df_1.drop([0],axis =1 )

x_train, x_test, y_train, y_test = train_test_split(df_1,
                                                    y,
                                                    test_size=0.2,random_state=93)

clf = RandomForestClassifier(n_estimators=64, max_depth=20,random_state=86)
clf.fit(x_train, y_train)


pre = clf.predict(x_test)

#            from sklearn.preprocessing import MinMaxScaler
#            scaler = MinMaxScaler()
#            x_train_norm = scaler.fit_transform(x_train)
#            x_test_norm = scaler.transform(x_test)
#            
#            from sklearn.neighbors import KNeighborsClassifier
#            clf = KNeighborsClassifier(n_neighbors=6)
#            np.average(cross_val_score(clf, x_train_norm, y_train, cv=50))
#            
#            clf.fit(x_train_norm, y_train)
#            pre = clf.predict(x_test_norm)
ans = (pre == y_test).sum()/y_test.count()


with open('RandomForest.pickle', 'wb') as f:
    pickle.dump(clf, f)

#读取Model
#with open('clf.pickle', 'rb') as f:
#    clf2 = pickle.load(f)
#    #测试读取后的Model
#    print(clf2.predict(x_test))



#for i in range(4,8):
#    for j in range(4500,5500,10):
#        for k in range(4,12):
#            for l in range(3,7):
#                
#                model = xgb.XGBRegressor(
#                    colsample_bylevel=0.8,
#                    colsample_bytree = 0.33,
#                    max_depth = i, 
#                    gamma=0,
#                    min_child_weight=l,
#                    learning_rate = 0.033,
#                    max_delta_step=k,
#                    missing=None,
#                    n_estimators = j,
#                    nthread= -1,
#                    silent = True,
#                    objective = 'reg:gamma', #'reg:linear', 'reg:linear' 
#                    reg_lambda = 0.8,
#                    scale_pos_weiht = 1,
#                    seed = 1234,
#                    subsample = 1,
#                    default='cpu_predictor',
#                    )
#                #
#                model.fit(x_train, y_train)
#                
#                
#                preds = model.predict(x_test)
#                #
#                ans = (pre == y_test).sum()/y_test.count()
#                if ans >0.8:
#                    print(i,j,k,l,ans)
#                #
                #
#               畫圖
s = clf.fit(x_train, y_train) # 训练模型
r = clf.score(x_test,y_test) #评估模型准确率

predict_y_validation = clf.predict(x_test)#直接给出预测结果，每个点在所有label的概率和为1，内部还是调用predict——proba()
# print(predict_y_validation)
prob_predict_y_validation = clf.predict_proba(x_test)#给出带有概率值的结果，每个点所有label的概率和为1
predictions_validation = prob_predict_y_validation[:, 1]
fpr, tpr, _ = roc_curve(y_test, predictions_validation)
    #
roc_auc = auc(fpr, tpr)
plt.title('ROC Validation')
plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
plt.legend(loc='lower right')
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
