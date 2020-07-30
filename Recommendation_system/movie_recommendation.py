#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the libraries
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


# In[3]:


#import the dataset
df=pd.read_csv("movie_dataset.csv")


# In[6]:


#initialize the features as a list 
features=['keywords','cast','genres','director']


# In[7]:


#creating a function for combining the values of these columns into a single string.
def combine_features(row):
    return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']


# In[8]:


#call this function over each row of our dataframe. 
#But, before doing that, we need to clean and preprocess the data for our use. 
#We will fill all the NaN values with blank string in the dataframe.
for feature in features:
    df[feature]=df[feature].fillna('') #filling all NaNs with blank string

df["combined_features"]=df.apply(combine_features,axis=1)


# In[11]:


ob=CountVectorizer() #creating new CountVectorizer() object
count_matrix=ob.fit_transform(df["combined_features"]) 
#feeding combined strings(movie contents) to CountVectorizer() object


# In[12]:


#Now, we need to obtain the cosine similarity matrix from the count matrix.
cosine_sim=cosine_similarity(count_matrix)


# In[13]:


#now we will define two functions to get movie title from movie index and vice-versa.
def get_title_from_index(index):
    return df[df.index==index]["title"].values[0]
def get_index_from_title(title):
    return df[df.title==title]["index"].values[0]


# In[15]:


print(df["original_title"])
user_likes=input('enter the movie name from the above list: ')
index=get_index_from_title(user_likes)
similar_movies=list(enumerate(cosine_sim[index]))


# In[16]:


#We will sort the list similar_movies according to similarity scores in descending order. 
#Since the most similar movie to a given movie will be itself, we will discard the first element after sorting the movies.
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]


# In[17]:


#we will run a loop to print first 5 entries from sorted_similar_movies list.
i=0
print("Top 5 similar movies to "+user_likes+" are as follows:\n")
for element in sorted_similar_movies:
    print(get_title_from_index(element[0]))
    i=i+1
    if i>5:
        break

