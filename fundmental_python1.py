import pandas as pd

df = pd.read_csv(
    "/home/tejas/ML_WORK/Nptel-Course/gapminder-unfiltered.tsv",
    sep="\t"
)

# Display the first 5 rows of the dataframe
print(df.head())
# ouptut
# country continent  year  lifeExp       pop   gdpPercap
# 0  Afghanistan      Asia  1952   28.801   8425333  779.445314
# 1  Afghanistan      Asia  1957   30.332   9240934  820.853030
# 2  Afghanistan      Asia  1962   31.997  10267083  853.100710
# 3  Afghanistan      Asia  1967   34.020  11537966  836.197138
# 4  Afghanistan      Asia  1972   36.088  13079460  739.981106


# get the number of rows and columns
print(df.shape )
# output
# (1704, 6)

# get the column names
print(df.columns)
# output
# Index(['country', 'continent', 'year', 'lifeExp', 'pop', '

# get the data dtype of each column
print(df.dtypes)
# output
# country       object
# continent     object
# year           int64
# lifeExp      float64
# pop            int64
# gdpPercap    float64
# dtype: object

# looking at colums, rows , and cells
# get the country column and save it to its own variable 
country_df = df["country"]

# show the first 5 observation
print(country_df.head())
# output
# 0    Afghanistan
# 1    Afghanistan
# 2    Afghanistan
# 3    Afghanistan
# 4    Afghanistan
# Name: country, dtype: object

# show the last 5 observation
print(country_df.tail())
# output
# 1699      Zimbabwe
# 1700      Zimbabwe
# 1701      Zimbabwe
# 1702      Zimbabwe
# 1703      Zimbabwe
# Name: country, dtype: object

# looking at country ,continent and year
subset = df[["country", "continent", "year"]]
print(subset.head())
# output
#      country continent  year
# 0  Afghanistan      Asia  1952
# 1  Afghanistan      Asia  1957
# 2  Afghanistan      Asia  1962
# 3  Afghanistan      Asia  1967
# 4  Afghanistan      Asia  1972

print(subset.tail())
# output
#        country continent  year
# 1699  Zimbabwe   Africa  2002 
# 1700  Zimbabwe   Africa  2007
# 1701  Zimbabwe   Africa  1952
# 1702  Zimbabwe   Africa  1957
# 1703  Zimbabwe   Africa  1962