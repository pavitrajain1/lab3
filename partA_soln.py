'''Question 1'''

# importing the important packages
import pandas as pd

# reading the csv file
df = pd.read_csv('pima-indians-diabetes.csv')

# dropping the class attribute
df = df.drop('class', axis = 1)

# creating the median series for df
median_data = df.median()

# creating a function which will delete the outliers of the passed attribute
def del_outliers(att):
    quart_data = df[att].quantile([0.25, 0.50, 0.75])
    lower_bound = quart_data[0.25] - 1.5*(quart_data[0.75] - quart_data[0.25])
    upper_bound = quart_data[0.75] + 1.5*(quart_data[0.75] - quart_data[0.25])
    for i in df.index:
        if(df.loc[i, att] < lower_bound or df.loc[i, att] > upper_bound):
            df.loc[i, att] = quart_data[0.50]

# deleting outliers
for att in df.columns:
    del_outliers(att)

# initial min max data
lst_ini = [df.min(), df.max()]
ini_minmax = pd.DataFrame(lst_ini, index = ['min', 'max'])
print("Minimum and maximum attribute values before normalization : \n")
print(ini_minmax)

# applying min max normalization to take data in range of 5 - 10
for att in df.columns:
    df[att] =( (df[att] - ini_minmax.loc['min', att])/(ini_minmax.loc['max',att] - ini_minmax.loc['min', att]) )*7 + 5;
    
# final min max data
lst_fin = [df.min(), df.max()]
fin_minmax = pd.DataFrame(lst_fin, index = ['min', 'max'])
print("\nMinimum and maximum attribute values after normalization : \n")
print(fin_minmax)

# mean and std data before standardization
lst = [df.mean(), df.std()]
mean_std_ini = pd.DataFrame(lst, index = ['mean', 'std'])
print("\nMean and standard deviation before standardization : \n")
print(mean_std_ini)

# standardizing the data by z-standardization method
for att in df.columns:
    df[att] = (df[att] - mean_std_ini.loc['mean', att])/mean_std_ini.loc['std', att]

# mean and std after standardization
lst2 = [df.mean(), df.std()]
mean_std_fin = pd.DataFrame(lst2, index = ['mean', 'std'])
print("\nMean and standard deviation before and after standardization : \n")
print(mean_std_fin)
