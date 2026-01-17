import pandas as pd
df = pd.read_csv(
    "/home/tejas/ML_WORK/Nptel-Course/gapminder-unfiltered.tsv",
    sep="\t"
)

# get the first row
print(df.iloc[0])
# output
# country      Afghanistan
# continent          Asia
# year               1952
# lifeExp          28.801
# pop            8425333
# gdpPercap      779.445314
# Name: 0, dtype: object

# get the 100th row
# python count from 0
print(df.iloc[99])
# output
# country      Bangladesh
# continent          Asia
# year               1977
# lifeExp          54.490
# pop           81652000
# gdpPercap     620.280354
# Name: 99, dtype: object  

# get the last row
print(df.tail(n=1))
# output
#          country continent  year  lifeExp       pop   gdpPercap
# 1703  Zimbabwe      Africa  2007   43.487  12311143  469.709298

# subsetting multiple rows

# select the first ,100th and 1000th rows
print(df.iloc[[0, 99, 999]])
# output
#         country continent  year  lifeExp       pop   gdpPercap
# 0   Afghanistan      Asia  1952   28.801   8425333  779.445314
# 99   Bangladesh      Asia  1977   54.490  81652000  620.280354
# 999     Italy    Europe  1997   78.484  57680000  25885.009142


# subset rows by row number :ioc
# get the 2nd row
print(df.iloc[1])
# output
# country      Afghanistan
# continent          Asia
# year               1957
# lifeExp          30.332
# pop            9240934
# gdpPercap      820.853030
# Name: 1, dtype: object

# get the 100 row
print(df.iloc[99])
# output
# country      Bangladesh
# continent          Asia
# year               1977
# lifeExp          54.490
# pop           81652000
# gdpPercap     620.280354
# Name: 99, dtype: object

# using -1 to get the last row
print(df.iloc[-1])
# output
# country      Zimbabwe
# continent          Africa
# year               2007
# lifeExp          43.487
# pop           12311143
# gdpPercap     469.709298
# Name: 1703, dtype: object

# with iloc ,we can pass in th -1 to get the last row something we couldn't do with loc

# get the first ,100th and 1000th rows
print(df.iloc[[0, 99, 999]])
# output
#         country continent  year  lifeExp       pop   gdpPercap
# 0   Afghanistan      Asia  1952   28.801   842        5333  779.445314
# 99   Bangladesh      Asia  1977   54.490  81652000  620.280354
# 999     Italy    Europe  1997   78.484  57680000  25885.009142    

# subsetting column
#  * the python slicing syntx uses a colon:
# * if we have jsut a colon , the attribute refers to everything
#  * so,if we just want to get the first column using the loc or iloc syntax
# we can write something like this df.iloc[:,[columns]] to subset the column(s).

# subset column with loc
# note the position of colon
# it is used to select all rows

subset = df.loc[:,['year','pop']]
print(subset.head())
# output
#    year       pop
# 0  1952   8425333
# 1  1957   9240934
# 2  1962  10267083
# 3  1967  11537966
# 4  1972  13079460

# subset column with iloc
# iloc will alow us to use integers
# -1 will select the last column

subset = df.iloc[:,[2,4,-1]]
print(subset.head())
# output
#    year       pop   gdpPercap
# 0  1952   8425333  779.445314
# 1  1957   9240934  820.853030
# 2  1962  10267083  853.100710
# 3  1967  11537966  836.197138
# 4  1972  13079460  739.981106
# subset column with iloc
# iloc will alow us to use integres
# -1 will select the last column

subset = df.iloc[:, [2, 4, -1]]
print(subset.head())
# output
#    year       pop   gdpPercap
# 0  1952   8425333  779.445314
# 1  1957   9240934  820.853030
# 2  1962  10267083  853.100710 
# 3  1967  11537966  836.197138
# 4  1972  13079460  739.981106

# subsetting column by range
# create a range of integers from 0 to 4 inclusive
small_range = list(range(5))
print(small_range)
# output
# [0, 1, 2, 3, 4]

# subset the dataframe with the range
subset = df.iloc[:, small_range]
print(subset.head())
# output
#         country continent  year  lifeExp       pop   gdpPercap
# 0   Afghanistan      Asia  1952   28.801   842
# 1   Afghanistan      Asia  1957   30.332   9240934  820.853030
# 2   Afghanistan      Asia  1962   31.997  10267083  853.100710
# 3   Afghanistan      Asia  1967   34.020  11537966  836.197138
# 4   Afghanistan      Asia  1972   36.088  13079460  739.981106

# subsetting rows and columns
# using loc
print(df.loc[42,'country'])
# output
# Albania

# using iloc
print(df.iloc[42,0])
# output
# Albania

# subsetting multiple rows and columns
#get the 1st, 100th, and 1000th rows
# from the 1st, 4th, and 6th columns

print(df.iloc[[0,99,999],[0,3,5]])
# output
#         country   lifeExp   gdpPercap
# 0   Afghanistan   28.801  779.445314
# 99   Bangladesh   54.490  620.280354
# 999     Italy   78.484  25885.009142

# if we use the column names directly,
# it makes the code a bit easier to read
# note now we have to use loc, instead of iloc
print(df.loc[[0,99,999],['country','lifeExp','gdpPercap']])
# output
#         country   lifeExp   gdpPercap
# 0   Afghanistan   28.801  779.445314
# 99   Bangladesh   54.490  620.280354
# 999     Italy   78.484  25885.009142

print(df.loc[10:13,['country','year','pop'  ]])
# output
#        country  year       pop
# 10  Afghanistan  2002  25268405
# 11      Albania  1952   1282697
# 12      Albania  1957   1476505
# 13      Albania  1962   1728137

print(df.head(n=10))
# output
#         country continent  year  lifeExp       pop   gdpPercap
# 0   Afghanistan      Asia  1952   28.801   8425333  779.445314
# 1   Afghanistan      Asia  1957   30.332   9240934  820.853030
# 2   Afghanistan      Asia  1962   31.997  10267083  853.100710
# 3   Afghanistan      Asia  1967   34.020  11537966  836.197138
# 4   Afghanistan      Asia  1972   36.088  13079460  739.981106
# 5   Afghanistan      Asia  1977   38.438  14880372  786.113360
# 6   Afghanistan      Asia  1982   39.854  12881816  978.011439
# 7   Afghanistan      Asia  1987   40.822  16317921  852.395944
# 8   Afghanistan      Asia  1992   41.674  22227415  649.341395
# 9   Afghanistan      Asia  1997   41.763  25268405  635.341351        

# Grouped Means

# For each year in our data, what was the average life
# expectancy?
# To answer this question,
# we need to split our data into parts by year;
# then we get the 'lifeExp' column and calculate the mean


print(df.groupby('year')['lifeExp'].mean())
# output
# year
# 1952    48.451324
# 1957    50.548387
# 1962    52.631250
# 1967    54.735714
# 1972    57.051250
# 1977    59.471250
# 1982    61.903750
# 1987    64.663750
# 1992    67.275000
# 1997    69.516250
# 2002    71.603750
# 2007    72.995000
# Name: lifeExp, dtype: float64

multi_group_var = df.groupby(['year','continent'])['lifeExp'].mean()
print(multi_group_var)
# output
# year  continent
# 1952  Africa       39.613043
#       Americas     50.166667
#       Asia         44.901429
#       Europe       64.392500
#       Oceania      69.120000
# 1957  Africa       41.586957
#       Americas     52.233333
#       Asia         46.825714
#       Europe       65.900000
#       Oceania      70.366667
# 1962  Africa       43.891304
#       Americas     54.633333
#       Asia         49.325714
#       Europe       67.137500
#       Oceania      71.613333
# 1967  Africa       46.478261
#       Americas     56.866667
#       Asia         51.900000
#       Europe       68.737500
#       Oceania      72.786667
# 1972  Africa       49.282609
#       Americas     59.433333
#       Asia         54.514286
#       Europe       70.512500
#       Oceania      73.940000
# 1977  Africa       52.130435
#       Americas     62.100000
#       Asia         57.185714
#       Europe       72.162500
#       Oceania      75.073333
# 1982  Africa       55.173913     


# If you need to “flatten” the dataframe, you can use the
# reset_index method.
flat = multi_group_var.reset_index()
print(flat)
# output
#      year continent     lifeExp
# 0    1952    Africa  39.613043
# 1    1952  Americas  50.166667
# 2    1952      Asia  44.901429
# 3    1952    Europe  64.392500
# 4    1952   Oceania  69.120000
# 5    1957    Africa  41.586957
# 6    1957  Americas  52.233333
# 7    1957      Asia  46.825714
# 8    1957    Europe  65.900000
# 9    1957   Oceania  70.366667
# 10   1962    Africa  43.891304
# 11   1962  Americas  54.633333
# 12   1962      Asia  49.325714
# 13   1962    Europe  67.137500
# 14   1962   Oceania  71.613333


# Grouped Frequency Counts

# • use the nunique to get counts of unique values on a Pandas Series.

country_counts = df.groupby('continent')['country'].nunique()
print(country_counts)
# output
# continent
# Africa      53
# Americas    35
# Asia        33
# Europe      30
# Oceania      5
# Name: country, dtype: int64

# basic plot
import matplotlib.pyplot as plt

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)
# output
# year
# 1952    48.451324
# 1957    50.548387
# 1962    52.631250
# 1967    54.735714
# 1972    57.051250
# 1977    59.471250
# 1982    61.903750
# 1987    64.663750
# 1992    67.275000
# 1997    69.516250
# 2002    71.603750
# 2007    72.995000
# Name: lifeExp, dtype: float64

global_yearly_life_expectancy.plot()