import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics as st
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

#creating a data frame with dropped class attribute
df=pd.read_csv('pima-indians-diabetes.csv')
df.drop(['class'],axis=1,inplace=True)
cols=['pregs','plas','pres','skin','test','BMI','pedi','Age']
median=[df[cols[i]].median() for i in range(len(cols))]

for i in range(len(cols)):
    q1=np.quantile(df[cols[i]],0.25)
    q3=np.quantile(df[cols[i]],0.75)
    iqr=q3-q1
    upper_bound=q3+1.5*iqr
    lower_bound=q1-1.5*iqr
    for j in range(len(df)):
       if((df.loc[j,cols[i]]>upper_bound) or (df.loc[j,cols[i]]<lower_bound)):
           df.loc[j,cols[i]]=median[i]

foo=df
import statistics as st
for i in range(len(cols)):
    foo[cols[i]]=(foo[cols[i]]-(foo[cols[i]]).mean())/st.stdev(foo[cols[i]])
print(foo)
#Que3 a  
pca = PCA(n_components=2)
pca_data = pca.fit_transform(foo)
pca_data_df = pd.DataFrame(pca_data,columns = ['PCA-1','PCA-2'])
cov1 = pca_data_df.cov()
e = np.linalg.eig(cov1)
plt.figure()
plt.figure(figsize=(10,10))
plt.xticks(fontsize=12)
plt.yticks(fontsize=14)
plt.xlabel('Principal Component - 1',fontsize=20)
plt.ylabel('Principal Component - 2',fontsize=20)
plt.title("Principal Component Analysis of Pmca Dataset",fontsize=20)
plt.scatter(pca_data_df['PCA-1'], pca_data_df['PCA-2'], c = 'Red', s = 50)
plt.show()


#Que b
cov_ori = foo.cov()
eigen_value,eigen_vector = np.linalg.eig(cov_ori)
evalue = list(eigen_value)
lis = []
for i in range(1,9): 
    lis.append('value'+str(i))
evalue.sort(reverse = True)
plt.bar(lis,evalue)
plt.show()


#Que3 c
error_list = []
df1 = np.array(foo)
for i in range(1,9):
    pca1=PCA(n_components=i)
    pca2=pca1.fit_transform(foo)
    data_proj=pca1.inverse_transform(pca2)
    error = 0
    for j in range(len(foo)):
        sum=0
        for k in range(8):
            sum+=(data_proj[j][k]-df1[j][k])**2
        error+=sum**0.5
    error_list.append(error/(len(foo)))
    cov_mat=np.cov(pca2,rowvar = False)
    print("Covariance Matrix for l =",i,"\n",cov_mat)
l=["l=1","l=2","l=3","l=4","l=5","l=6","l=7","l=8"]
plt.bar(l,error_list,color="blue",edgecolor="black")
plt.title("Plot of Euclidean distance for different Lower dimensions")
plt.xlabel("Lower dimensions")
plt.ylabel("Value of Euclidean distance")
plt.show()

#Que3 d
print("Ques.3-(d)")
print("Covariance matrix of original Data -\n",cov_ori)
pca1=PCA(n_components=8)
pca2=pca1.fit_transform(foo)
cov_recons = pd.DataFrame(pca2).cov()
print("Covariance matrix for 8-dimensional representation obtained using PCA with l = 8 -\n",cov_recons)
