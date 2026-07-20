import pandas as pd

def clean_data(df):
    # create copy of original data 
    data = df.copy()

    # remove duplicate
    data = data.drop_duplicates()

    #removing missing values
    data = data.dropna(subset = ["name","rate","location","cuisines"])

    #clean space from text column
    data["name"] = data["name"].str.strip()
    data["location"] = data["location"].str.strip()
    data["cuisines"] = data["cuisines"].str.strip()

    #convert the rating valuess into number
    data["rate"]= (data["rate"].str.replace("/5","", regex = False).str.strip())
    data["rate"] = pd.to_numeric(data["rate"], errors="coerce")
    # remove ratings where not able to convert to numeric
    data = data.dropna(subset = ["rate"]) 



    return data