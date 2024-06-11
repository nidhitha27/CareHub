!pip install numpy

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

AIQ=pd.read_excel("C:\\Users\\hansh\\OneDrive\\Desktop\\AIQ_Data.xlsx")
AIQ.head()

AIQ["Month"].unique()
AIQ.columns

# Correlation

sns.heatmap(AIQ[['NowCast Conc.','AQI', 'Year', 'Month', 'Day', 'Hour']].corr(),annot=True)

plt.savefig("Correlation",dpi=300)

from ydata_profiling import ProfileReport

Profile=ProfileReport(AIQ,title="Air Quality Index report",explorative=True)

Profile

Profile.to_file("Air Quality Index report.html")

AIQ.info()

a=AIQ[['NowCast Conc.','AQI']]

a

sns.boxplot(a)


a[a['NowCast Conc.']<0]

# Outlier Detection (IQR)

# NowCast Conc

Q1=a['NowCast Conc.'].quantile(0.25)
Q2=a['NowCast Conc.'].quantile(0.50)
Q3=a['NowCast Conc.'].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR


outliers=(a["NowCast Conc."]<lower_bound)|(a["NowCast Conc."]>upper_bound)

a.loc[outliers,"NowCast Conc."]=np.mean(a["NowCast Conc."])

a.loc[outliers,"NowCast Conc."]

# AQI

Q1=a['AQI'].quantile(0.25)
Q2=a['AQI'].quantile(0.50)
Q3=a['AQI'].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR


outliers1=(a["AQI"]<lower_bound)|(a["AQI"]>upper_bound)

a.loc[outliers1,"AQI"]

a.loc[outliers1,"AQI"]=np.mean(a["AQI"])

a.loc[outliers1,"AQI"]

sns.boxplot(a["AQI"])

sns.boxplot(a)

a.isnull().sum()

a.info()

a.describe()

sns.scatterplot(a)

sns.jointplot(a)

sns.pairplot(a)

Profile1=ProfileReport(a,title="Air Quality Index report1",explorative=True)

Profile1

a.shape

#a.drop_duplicates()

a.shape

Profile2=ProfileReport(a,title="Air Quality Index report1",explorative=True)

Profile2

from autoviz.AutoViz_Class import AutoViz_Class

AV=AutoViz_Class()

report=AV.AutoViz(filename="",dfte=a)

# Normalization

from sklearn.preprocessing import MinMaxScaler

mm=MinMaxScaler()

a1=mm.fit_transform(a)

a1

a.columns

a2=pd.DataFrame(a1,columns=['NowCast Conc.', 'AQI'])
a2

a2.describe()

sns.pairplot(a2)

#  Linear Reg Model

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error

lr=LinearRegression()

a2

X=a2[["NowCast Conc."]]

Y=a2[["AQI"]]

X_train, X_test, Y_train, Y_test =train_test_split(X,Y,test_size=0.3,random_state=21)


X_train.shape

Y_train.shape

X_test.shape

Y_test.shape

print(X_train.mean())
print(X_test.mean())

print(Y_train.mean())
print(Y_test.mean())

lr.fit(X_train,Y_train)

# Make predictions on the training set 

Y_train_pred=lr.predict(X_train)

Y_test_pred=lr.predict(X_test)

r2_train=r2_score(Y_train,Y_train_pred)

r2_test=r2_score(Y_test,Y_test_pred)

r2_train

r2_test

lr.predict([[65]])

print(classificat)

print(Y_test)



sns.scatterplot(Y_tse)

