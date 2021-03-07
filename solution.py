import csv
import sys
import pandas as pd 

df = pd.read_csv('input.csv')
# print(df)
element_list = []
element = []
date = []
val = []
val_overlayed = []
final_val = []

for index, row in df.iterrows(): 
    #not getting value of F 
    if row['Value_overlayed'] == "N":
        T = row['Value']
        F = '?'
        element.append(row['Element'])
        date.append(row['Date'])
        val.append(row['Value'])
        val_overlayed.append(row['Value_overlayed'])
        final_val.append("Null")

    else:
        element.append(row['Element'])
        date.append(row['Date'])
        val.append(row['Value'])
        val_overlayed.append(row['Value_overlayed'])
        final_val.append(150)

print(element)
print(date)
print(val)
print(val_overlayed)
print(final_val)
element_dict = {"Element": element, "Date": date, "Value": val, "Value_overlayed": val_overlayed, "Final_value": final_val}
df = pd.DataFrame(element_dict)
print(df)
df.to_csv("output.csv", index=False)