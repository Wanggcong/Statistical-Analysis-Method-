import numpy as np
import math
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import pandas as pd

df=pd.read_csv('data.txt',header=0)
df=df.dropna()
age=np.array(df['age'])
bmi=np.array(df['bmi'])
children=np.array(df['children'])
Y=np.array(df['charges']).astype(float)

X=np.zeros((1338,1))
X=age
X=np.column_stack((X,bmi))
X=np.column_stack((X,children))

def problem1(X1,Y1):
    Xtrain=X1[0:1333]
    a = np.ones((Xtrain.shape[0],1))
    Xtrain=np.column_stack((a,Xtrain))
    Xtest=X1[1333:]
    b = np.ones((Xtest.shape[0], 1))
    Xtest = np.column_stack((b, Xtest))
    Ytrain=Y1[0:1333]


    B=np.zeros((4,1))
    B=np.dot(np.dot(np.linalg.inv(np.dot(Xtrain.T,Xtrain)),Xtrain.T),Ytrain)
    print(B)

    Ytest=np.dot(Xtest,B)
    print(Ytest)

    Q=np.sum([i * i for i in Ytrain-np.dot(Xtrain,B)])
    sigma=np.sqrt(Q/(Xtrain.shape[0]-2))

    #confidence interval
    result=np.zeros((5,2))
    for i in range(5):
        se = sigma * math.sqrt(1+np.dot(np.dot(Xtest[i],np.linalg.inv(np.dot(Xtrain.T,Xtrain))),Xtest[i].T))
        result[i,0]=Ytest[i]-2*se
        result[i,1]=Ytest[i]+2*se
    print(result)

def problem2():
    model = ols('charges ~ sex', df).fit()
    anovat = anova_lm(model)
    print(anovat)

    formula = 'charges ~ sex + smoker + sex:smoker'
    anova_results = anova_lm(ols(formula, df).fit())
    anova_results.to_csv('anova_result.csv')
    print(anova_results)

if __name__=='__main__':
    problem1(X,Y)
    problem2()

