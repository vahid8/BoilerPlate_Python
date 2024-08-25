# first pip install lxml
import pandas as pd
import matplotlib.pyplot as plt

# read HTML using pd -> output is a list of dataframes
URL_address = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Sweden'
Table = pd.read_html(URL_address)
# example of covid 19
Table_covid = pd.read_html(URL_address,match='New COVID-19 cases in Sweden by county')
# get dataframe
df = Table_covid [0]
print(df.head())

# Delete unrelevant data first rows and last row
b= list(range (df.shape[0]-23,df.shape[0]))
df.drop(df.index[b], inplace=True)

b= list(range (0,5))
df.drop(df.index[b], inplace=True)

print(df.tail())
# get rid of 3 rows header
print(df.tail())
df.columns = df.columns.get_level_values(1)
df['Date'] = df['Date'].str.replace(r"\[.*?\]","")
# change date dtime to series and makke its column as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# fill nan values with 0 for plot and convert values from str to numeric
df.fillna(0, inplace=True)
df = df.iloc[:,0:21].apply(pd.to_numeric)

df = df.cumsum()
print('finish')

f = plt.figure()

plt.title('Covid cases Sweden', color='black')
df.iloc[:,0:21].plot(ax=f.gca())

plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()
