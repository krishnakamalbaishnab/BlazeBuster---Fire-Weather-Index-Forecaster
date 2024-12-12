import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

dataset=pd.read_csv('Algerian_forest_fires_dataset_UPDATE.csv' ,header=1)

dataset.head()

dataset.info()

#Data Cleaning

## missing values
dataset[dataset.isnull().any(axis=1)]

dataset.loc[:122,"Region"]=0
dataset.loc[122:,"Region"]=1
df=dataset

df.info()

df.head()

df[['Region']]=df[['Region']].astype(int)

df.head()

df.isnull().sum()

## Removing the null values
df=df.dropna().reset_index(drop=True)

df.head()

df.isnull().sum()

df.iloc[[122]]

##remove the 122nd row
df=df.drop(122).reset_index(drop=True)

df.iloc[[122]]

df.columns
## fix spaces in columns names
df.columns=df.columns.str.strip()
df.columns

df.info()


#Change the required columns as integer data types

df.columns

df[['month','day','year','Temperature','RH','Ws']]=df[['month','day','year','Temperature','RH','Ws']].astype(int)

df.info()

df.head()


#chaaning the other columns to float data types

objects=[features for features in df.columns if df[features].dtypes=='O']

objects



for i in objects:
    if i!='Classes':
        df[i]=df[i].astype(float)


df.info()

objects

df.describe()


df.head()

#EDA Starts Here

## drop day,month and year
df_copy=df.drop(['day','month','year'],axis=1)

df_copy.head()



## categories in classes
df_copy['Classes'].value_counts()


## Encoding of the categories in classes
df_copy['Classes']=np.where(df_copy['Classes'].str.contains('not fire'),0,1)

df_copy.head()

df_copy.tail()

df_copy['Classes'].value_counts()



## Plot desnity plot for all features

sns.set_style("darkgrid")  # Example: Seaborn style


# plt.style.use('seaborn')
df_copy.hist(bins=50,figsize=(20,15))
plt.show()


# import matplotlib.pyplot as plt
# print(plt.style.available)



import seaborn as sns
import matplotlib.pyplot as plt
print(plt.style.available)



## Percentage for Pie Chart
percentage=df_copy['Classes'].value_counts(normalize=True)*100

# plotting piechart
classlabels=["Fire","Not Fire"]
plt.figure(figsize=(12,7))
plt.pie(percentage,labels=classlabels,autopct='%1.1f%%')
plt.title("Pie Chart of Classes")
plt.show()



#Correlation

df_copy.corr()

# sns.heatmap(df.corr())

## Box Plots
sns.boxplot(df['FWI'],color='green')

df.head()

df['Classes']=np.where(df['Classes'].str.contains('not fire'),'not fire','fire')

## Monthly Fire Analysis
dftemp=df.loc[df['Region']==1]
plt.subplots(figsize=(13,6))
sns.set_style('whitegrid')
sns.countplot(x='month',hue='Classes',data=df)
plt.ylabel('Number of Fires',weight='bold')
plt.xlabel('Months',weight='bold')
plt.title("Fire Analysis of Sidi- Bel Regions",weight='bold')

## Monthly Fire Analysis
dftemp=df.loc[df['Region']==0]
plt.subplots(figsize=(13,6))
sns.set_style('whitegrid')
sns.countplot(x='month',hue='Classes',data=df)
plt.ylabel('Number of Fires',weight='bold')
plt.xlabel('Months',weight='bold')
plt.title("Fire Analysis of Brjaia Regions",weight='bold')



















