import pandas as pd
import sqlite3

#data=pd.read_excel("in_out_eval.xlsx")
#data.to_csv("inouteval.csv",sep="\t")
#print(data)


# to read xlsx excel file and save it to csv using xlrd engine (pip install xlrd):
#df = pd.read_excel("patient.xlsx",engine='xlrd')
# to save dataframe df to .csv file :
#df.to_csv("patientxlrd.csv")
#print(df)


# load .csv file to dataframe df :
df = pd.read_csv("patientxlrd.csv")#, index_col=[0])
#print (df)

#print(df.head()) # or head(2) for first 2
#print(df.tail()) # or tail(1) for last one

# to print the type of dataframe
#print(df.dtypes)

#print(df['name'])

# to print a specific row example for index 4
#print(df.loc[4])

# set the index to be the name and overwrite the df :
#df=df.set_index('name')
# then print index Moubarak Eliana :
#print(df.loc['Moubarak Eliana'])

# to print all available column :
#print(df.columns)

# to select only theses rows :
#df=df[['Unnamed: 0', 'name', 'tel', 'referby', 'address']]
#print(df)

# to print idex row between 100 and 110
#print (df.query('index > 100 and index < 110'))

# to all row contaning case sensitif eliana :
#print (df.query("name.str.contains ('eliana',case = False)"))

# to change data type of name column as interger:
#df['name']=df['name'].astype('int')

# put last row in a variable called:df_to_append
#df_to_append=df.tail(1)
# add a new row to df with append command containing the data of the variable df_to_append
#df=pd.concat([df,df_to_append])
#print (df)

#insert a new row in position 3 with value hello:
#df.insert(2, "Age", "hello", True)
#print (df)

# to get the nmbr of the last available row to put data inside
#last=(len(df.index))
#print (last)
# to remove collumns from dataframe and leave only first 3 collumn :
#df=df[['Unnamed: 0', 'name', 'tel']]
#print (df)
# to add a row to the last available row in the dataframe name chakib....
#df.loc[len(df.index)]=['5008','chakib','234234']
#print (df)

#display max columns or rows, instead of none u can put the nbr of column
#pd.set_option('display.max_columns',2)
#pd.set_option('display.max_rows',None)

# to read a single cell using index 1 and column"name"
#x=df.at[1,'name']
#print(x)

# to write a single entry using index 1 and column"name"
#df.at[1,'name']='Fadi KHazin'
#df.to_csv("patientxlrd.csv",index=False) # saved to file
#print (df)

#print(df)


# number of item in column_list :
#n= (len(column_list))

'''
# getting index row in a variable called seq of  a name containing ghazi and case insensitive,
# if many result : seq[0] and seq[1] .... 
search=(df.query("name.str.contains ('ghazi',case = False)"))
print('search result: ')
print(search)
seq=(search.index)
print(seq)
print ("ID= ",(seq[0])) # seq[0] is the first index of the search then seq[1] if 2 result for the search ...


# creating a list for all column called column_list :
column_list=(['id','name', 'tel', 'profession', 'address', 'birth', 'date', 'note','birth2', 'date2', 'referby','precaution'])

# printing row (for selected above collumns) for search result name containing "GHAZI"
for i in column_list:      # i will be equal 'name' then 'tel' then 'profession'...till the end of column_list
    data_field=df.at[seq[0],i]  # will give to variable data_field the [index 1,'i value' each increment]
    print(i," ",data_field)    # print( i value from column_list:name..tel... , data_field:value in row 1 for each column)

'''

### CONNECTING TO DATABASE.db FILE OR CREATING (IF THE FILE DOES NOT EXIST WILL CREATE AN EMPTY DATABASE.db )
connection = sqlite3.connect("dentabase1.db")
### SAVING TABLE NAMED PATIENT TO THE FILE dentalbase1.db
df.to_sql("Patient",con=connection,if_exists='replace')
connection.commit()  # save
### LOADING ALL PATIENT TABLE FROM dentalbase1.db TO THE DATAFRAME df
df = pd.read_sql("select * from patient",connection)
print (df)
connection.close()





'''
'title', 'id', 'headersfile', 'pagenb', 'rank', 'rankalb', 'fichnb','rankfich', 'remindme', 'reminddate', 'birth2', 'date2', 'referby',
'tcolora', 'tcolorp', 'chevery', 'precaution', 'maiden', 'father',
'mother', 'height', 'weight', 'motif', 'previous', 'datelastdet',
'personalid', 'SNA', 'SNB', 'IF', 'IM', 'TW', 'Sx', 'Sy', 'Nx', 'Ny',
'Ax', 'Ay', 'Bx', 'By', 'I1x', 'I1y', 'I2x', 'I2y', 'pi1x', 'pi1y',
'pi2x', 'pi2y', 'F1x', 'F1y', 'F2x', 'F2y', 'M1x', 'M1y', 'M2x', 'M2y',
'telerank', 'personal', 'fam', 'smoker', 'smokersince', 'cofee','whisky'

'''