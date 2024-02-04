Python  Pandas and SQlite3 :

pandas tutorial : 
https://www.w3schools.com/python/pandas/default.asp



add-total-row-to-pandas-dataframe

filter-pandas-dataframe


import pandas as pd
import sqlite3

connection = sqlite3.connect("dental.db")


# to select all data from the table called patient :

df = pd.read_sql("select * from patient",connection)
print(df)      # print(df.head(2)) or tail(2) for first 2 or last 2 row

# to select the row containing “Houssam Rassi” from the collumn called “Name” :

filtered_row = df[ df[“Name"] == "Houssam Rassi"]
print(filtered_row)

# to select the row containing a part of “Houssam Rassi”
# and case insensitive  from the collumn called “Name” :

filtered_row = df.query("Name.str.contains ('houss',case = False)")

# to select a row by its index number:

filtered_row = df.filter(items = [2], axis=0) # or item=[1,3] for 2 row 1 and 3
or:
print(df.loc[2])  # use location 2 to print row 2
or:
print(df.loc[1,2,3])  # use location 1,2,3 to print row 1,2,3


# to remove the row nbr 3 from the data frame :

df = df.drop(3)
or :
df.drop(x, inplace = True) # where x is the index
                                                        # inplace true correct
                                                        # directly the same file

# to set in the 3rd row in the ‘paid’ column the value 100  
    use df.loc :

df.loc [3, ’paid’ ] = 100


# from pandas to sqlite db file : 
 
filtered_row.to_sql("Patient",con=connection,if_exists='replace')
connection.commit()  # save
connection.close()

# to open old excel file from old access db (sepcify engine ‘xlrd’) :
pip install xlrd

df = pd.read_excel("patient.xlsx",engine='xlrd')
print(df)

# then to save the file : 
df.to_csv("patientxlrd.csv")

# to read the saved csv file :
df = pd.read_csv("patientxlrd.csv")

# SQLITE3 CREATING EMPTY db file and POPULATING IT:

### CONNECTING TO DATABASE.db FILE OR CREATING (IF THE FILE DOES NOT EXIST WILL CREATE AN EMPTY DATABASE.db )
connection = sqlite3.connect("dentabase1.db")
### SAVING TABLE NAMED PATIENT TO THE FILE dentalbase1.db
df.to_sql("Patient",con=connection,if_exists='replace')
connection.commit()  # save
### LOADING ALL PATIENT TABLE FROM dentalbase1.db TO THE DATAFRAME df
df = pd.read_sql("select * from patient",connection)
print (df)
connection.close()


PANDAS Functions WIth Examples: 
**********************************************

import pandas as pd


# to read excel file in dataframe :
data=pd.read_excel("in_out_eval.xlsx")
data.to_csv("inouteval.csv",sep="\t")
print(data)


# to read xlsx excel file and save it to csv using xlrd engine (pip install xlrd):
df=pd.read_excel("patient.xlsx",engine='xlrd')
# to save dataframe df to .csv file :
df.to_csv("patientxlrd.csv")
print(df)


# load .csv file to dataframe df :
# the optional index_col to remove 
# duplicate index collumn 
df = pd.read_csv("patientxlrd.csv", index_col=[0])
print (df)

print(df.head()) # or head(2) for first 2
print(df.tail()) # or tail(1) for last one

# to print the type of dataframe
print(df.dtypes)

print(df['name'])

# to print a specific row example for index 4
print(df.loc[4]) 

# set the index to be the name and overwrite the df : 
df=df.set_index('name') 
# then print index Moubarak Eliana :
print(df.loc['Moubarak Eliana']) 

# to print all available column :
print(df.columns) :

# to select only theses rows :
df=df[['Unnamed: 0', 'name', 'tel', 'referby', 'address']] 
print(df)

# to print idex row between 100 and 110
print (df.query('index > 100 and index < 110'))

# to all row contaning case sensitif eliana :
print (df.query("name.str.contains ('eliana',case = False)")) 

# to change data type of name column as interger:
df['name']=df['name'].astype('int') 

# put last row in a variable called:df_to_append 
df_to_append=df.tail(1)
# add a new row to df with append command containing the data of the variable df_to_append:
df=pd.concat([df,df_to_append])
print (df)

#insert a new row in position 3 with value hello:
df.insert(2, "Age", "hello", True) 
print (df)

# to get the nmbr of the last available row to put data inside
last=(len(df.index))
print (last)
# to remove collumns from dataframe and leave only first 3 collumn :
df=df[['Unnamed: 0', 'name', 'tel']]
print (df)
# to add a row to the last available row in the dataframe name chakib....
df.loc[len(df.index)]=['5008','chakib','234234'] 
print (df)

#display max columns or rows, instead of none u can put the nbr of column
pd.set_option('display.max_columns',None) 
pd.set_option('display.max_rows',None)

# to read a single cell using index 1 and column"name"
x=df.at[1,'name'] 
print(x)

# to write a single entry using index 1 and column"name"
df.at[1,'name']='tralla laa'
# save to file( the optional index=False  is to remove the double index column):
df.to_csv("patientxlrd.csv", index=False) 
print (df)


#  read cvs file and specifying datatype:
(csv dont store data type when saving file)
df=pd.read_csv(´patientxlrd.csv’, 
                           dtype={‘name’ :´category ’ ,
                                         ‘tel ‘ : ´ int64 ‘ , 
                                           ….. } )
                                          
