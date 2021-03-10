# importing datetime module 
from datetime import *
import pandas as pd 
import numpy as np
import datetime as dt
import math

df = pd.read_csv('input.csv')
print(df)
element = []
date = []
val = []
val_overlayed = []
final_val = []


#function for filter dataframe for selected year with Value-overlayed=="N"

def filt_df(year,df):
    df['Date'] = pd.to_datetime(df['Date'])
    df_date = df['Date']
    print(df['Date'])
    df_w_y = df.loc[df_date.dt.year == int(year)]
    return df_w_y

#iteration on dataframe to find value-ovelayed=="N" and to find Final_value

for index,row in df.iterrows():
    T = row['Value']
    
    # calculate final_value if value-ovelayed=="N"

    if row['Value_overlayed'] == "N":
        dy = pd.to_datetime(row['Date'])
        print(dy.year)
        
        df_f = filt_df(int(dy.year),df)
        print(df_f)
        
        df_li = []
        for i, r in df_f.iterrows():
            if r['Value_overlayed'] == "Y" and r['Date'] < dy:    
                df_li.append(r)
                print(df_li)
                
        if df_li:
            print(df_li[0])
            F = df_li[0]['Value']
            n = dy-df_li[0]['Date']
            n = n.days 
            f_value = T-((F-150)/365)*(365-n)
            f_value = round(f_value)

            #Append all values with list 
            element.append(row['Element'])
            date.append(row['Date'])
            val.append(row['Value'])
            val_overlayed.append(row['Value_overlayed'])
            final_val.append(f_value)
        else:
            f_value = row['Value']
            element.append(row['Element'])
            date.append(row['Date'])
            val.append(row['Value'])
            val_overlayed.append(row['Value_overlayed'])
            final_val.append(f_value)

    else:
        element.append(row['Element'])
        date.append(row['Date'])
        val.append(row['Value'])
        val_overlayed.append(row['Value_overlayed'])
        final_val.append(150)

# make dict of header with list and make dataframe to write csv 

element_dict = {"Element": element, "Date": date, "Value": val, "Value_overlayed": val_overlayed, "Final_value": final_val}
df = pd.DataFrame(element_dict)
print(df)

#write output.csv file  
df.to_csv("output.csv", index=False)