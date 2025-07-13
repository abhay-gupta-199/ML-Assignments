import pandas as pd
import numpy as np

# Task 1: Working with Series ------------------------------------

data = [25, 30, 35, 40, 45]

s = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'])
print(s)
# A    25
# B    30
# C    35
# D    40
# E    45
# dtype: int64

print(s.head(3))
# A    25
# B    30
# C    35
# dtype: int64

print(s.mean())
print(s.median())
print(s.std())
# 35.0
# 35.0
# 7.905694150420948

# Task 2: Creating and Inspecting DataFrames ---------------------

data = {
    'Name': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Age': [20, 22, 19, 21, 20],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female'],
    'Marks': [85, 78, 92, 74, 88]
}
df = pd.DataFrame(data)

print(df.head(2))
#     Name  Age  Gender  Marks
# 0  Alice   20  Female     85
# 1    Bob   22    Male     78

# Column names and Data types:
print(df.columns)
print(df.dtypes)
# Index(['Name', 'Age', 'Gender', 'Marks'], dtype='object')
# Name      object
# Age        int64
# Gender    object
# Marks      int64
# dtype: object

# Summary Statistics:
print(df.describe())
#              Age      Marks
# count   5.000000   5.000000
# mean   20.400000  83.400000
# std     1.140175   7.334848
# min    19.000000  74.000000
# 25%    20.000000  78.000000
# 50%    20.000000  85.000000
# 75%    21.000000  88.000000
# max    22.000000  92.000000

df['Passed'] = df['Marks'] >= 80
print(df)
#     Name  Age  Gender  Marks  Passed
# 0  Alice   20  Female     85    True
# 1    Bob   22    Male     78   False
# 2  Carol   19  Female     92    True
# 3  David   21    Male     74   False
# 4    Eve   20  Female     88    True

# Task 3: Data Selection and Filtering ---------------------------

print(df[['Name', 'Marks']])
#     Name  Marks
# 0  Alice     85
# 1    Bob     78
# 2  Carol     92
# 3  David     74
# 4    Eve     88

print(df[df['Marks'] > 80])
#     Name  Age  Gender  Marks  Passed
# 0  Alice   20  Female     85    True
# 2  Carol   19  Female     92    True
# 4    Eve   20  Female     88    True

print(df[df['Marks'] == df['Marks'].max()])
#     Name  Age  Gender  Marks  Passed
# 2  Carol   19  Female     92    True

# Task 4: Handling Missing Data ----------------------------------

df.loc[1, 'Marks'] = None
df.loc[4, 'Age'] = None
print(df)
#     Name   Age  Gender  Marks  Passed
# 0  Alice  20.0  Female   85.0    True
# 1    Bob  22.0    Male    NaN   False
# 2  Carol  19.0  Female   92.0    True
# 3  David  21.0    Male   74.0   False
# 4    Eve   NaN  Female   88.0    True

print(df.isnull().sum())
# Name      0
# Age       1
# Gender    0
# Marks     1
# Passed    0
# dtype: int64

df['Marks'].fillna(df['Marks'].mean(), inplace=True)
df.dropna(subset=['Age'], inplace=True)
print(df)
#     Name   Age  Gender  Marks  Passed
# 0  Alice  20.0  Female  85.00    True
# 1    Bob  22.0    Male  84.75   False
# 2  Carol  19.0  Female  92.00    True
# 3  David  21.0    Male  74.00   False

# Task 5: Grouping and Aggregation -------------------------------

df2 = pd.DataFrame(data)
grouped = df2.groupby('Gender')
print(grouped[['Age', 'Marks']].mean())
#               Age      Marks
# Gender                      
# Female  19.666667  88.333333
# Male    21.500000  76.000000

print(grouped.size())
# Gender
# Female    3
# Male      2
# dtype: int64

# Task 6: Reading and Writing Data -------------------------------

df.to_csv('students_data.csv', index=False)
new_df = pd.read_csv('students_data.csv')
print(new_df.head())
#     Name   Age  Gender  Marks  Passed
# 0  Alice  20.0  Female  85.00    True
# 1    Bob  22.0    Male  84.75   False
# 2  Carol  19.0  Female  92.00    True
# 3  David  21.0    Male  74.00   False

# Task 7: General ------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# Using the iris dataset from seaborn
iris = sns.load_dataset('iris')

# Displaying the first 5 rows of the dataset:
print(iris.head())
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 3           4.6          3.1           1.5          0.2  setosa
# 4           5.0          3.6           1.4          0.2  setosa

# Summary Statistics:
print(iris.describe())
#        sepal_length  sepal_width  petal_length  petal_width
# count    150.000000   150.000000    150.000000   150.000000
# mean       5.843333     3.057333      3.758000     1.199333
# std        0.828066     0.435866      1.765298     0.762238
# min        4.300000     2.000000      1.000000     0.100000
# 25%        5.100000     2.800000      1.600000     0.300000
# 50%        5.800000     3.000000      4.350000     1.300000
# 75%        6.400000     3.300000      5.100000     1.800000
# max        7.900000     4.400000      6.900000     2.500000

# Checking for missing values:
print(iris.isnull().sum())
# sepal_length    0
# sepal_width     0
# petal_length    0
# petal_width     0
# species         0
# dtype: int64

# Visualizing relationships between features using pairplot
# 'hue' differentiates species using colors
sns.pairplot(iris, hue='species')
plt.show()

# Summary of Findings:
# -> No missing values in the dataset.
# -> Setosa is clearly separable from other species.
# -> Petal length and petal width are highly correlated.
