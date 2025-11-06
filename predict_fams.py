import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.impute import KNNImputer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC,NuSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

'''for regions outside of Europe, predict membership of
parties in political families using kNN'''

ignore = ["id","party_id","party","party_name","party_en","party_id","family","country","year","vote","seat",
          "country","country_en","epvote","lrecon_salience","galtan_salience","lrecon_blur","lrecon_dissent",
          "galtan_blur","galtan_dissent","galtan_salience","immigrate_salience","immigrate_dissent",
          "multicult_salience","redist_salience","climate_change_salience","environment_salience"]


files = ['CA_data.csv', 'CA_prov_data.csv', 'IL_data.csv', 'LA_data.csv']

def preprocess(df,columns): # function that renders data into form suitable for processing by dropping unwanted columns and
    # using imputation to fill in the blanks
    useful = pd.DataFrame()
    # creating training data
    for column in columns:
        if column not in ignore:
            useful = pd.concat([useful, df[column]], axis=1)
    # making it kNN-suitable by removing NaN
    imputer = KNNImputer(n_neighbors=3)
    useful = pd.DataFrame(imputer.fit_transform(useful), columns=list(useful.columns))
    return useful

europe_df = pd.concat([pd.read_csv("data/EU_data.csv"), pd.read_csv("data/EU_hist_data.csv")]) # dataset with EU data
europe_df = europe_df[europe_df.family != "Miscellaneous"] # too mixed, interferes

europe_fam = europe_df["family"] # families from EU data
europe_columns=list(europe_df.columns) # list of columns
euro_data = preprocess(europe_df,europe_columns) # data suitable for our needs
europe_columns=list(euro_data.columns) # new list of columns

# create classifier, check accuracy
euro_train,euro_test,fam_train,fam_test = train_test_split(euro_data, europe_fam, test_size=0.25, random_state=42)
RF_class = RandomForestClassifier(n_estimators=500,criterion="entropy")
RF_class.fit(euro_train,fam_train)
fam_pred = RF_class.predict(euro_test)
acc = accuracy_score(fam_test,fam_pred)
print("RF",acc)

for file in files:
    this_df = pd.read_csv("data/"+file)
    this_columns = list(this_df.columns)
    this_data = preprocess(this_df,this_columns)

    euro_train = pd.DataFrame()
    this_train = pd.DataFrame()
    for column in this_columns:
        if column in europe_columns:
            euro_train = pd.concat([euro_train, euro_data[column]], axis=1)
            this_train = pd.concat([this_train, this_data[column]], axis=1)

    RF_class.fit(euro_train, europe_fam)
    predicted_fam = RF_class.predict(this_train)
    this_df.insert(6,"family",predicted_fam)
    this_csv = "data_predicted/"+ file.split('.')[0]+"_p.csv"
    this_df.to_csv(this_csv, encoding='utf-8')

        
        

'''for file in files:
    this_df = pd.read_csv(file)
    this_columns = list(this_df.columns)'''
    
    