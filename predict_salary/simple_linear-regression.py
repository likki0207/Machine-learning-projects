#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the required libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


# Importing the dataset
df=pd.read_csv('Salary_Data.csv')
X=df.iloc[:, :-1].values
y=df.iloc[:, -1].values


# In[4]:


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)


# In[5]:


# Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
ob=LinearRegression()
ob.fit(X_train,y_train)


# In[6]:


# Predicting the Test set results
y_pred=ob.predict(X_test)


# In[7]:


# Visualising the Training set results
plt.scatter(X_train,y_train,color='blue')
plt.plot(X_train,ob.predict(X_train),color='red')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# In[8]:


# Visualising the Test set results
plt.scatter(X_test,y_test,color='blue')
plt.plot(X_train,ob.predict(X_train),color='red')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# In[22]:


# predicting the salary
x=int(input('enter your total years of experience..'))
a=ob.predict([[x]])
print(f"So you will get a salary of ${a[0]}")


# In[ ]:




