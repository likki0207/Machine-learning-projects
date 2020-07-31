# Machine learning:
Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for themselves.

## Project-1 - Recommendation system
A simple Movie Recommendation Python Recommendation is done using "cosine similarity" between certain features of the movies. In this we are having a huge dataset consisiting of 4809 movies and we have 24 different columns. The name of the dataset is "movie_dataset.csv"

![a](https://user-images.githubusercontent.com/68856803/89008744-d2fa6800-d328-11ea-83a8-1fb07d3dded5.png)

### -> Steps to implement this project:
(a) Read CSV File

(b) Select Features

(c) Create a column in df which combines all selected features

(d) Create count matrix from this new combined column

(e) Compute the Cosine Similarity based on the count_matrix

(f) Get index of this movie from its title

(g) Get a list of similar movies in descending order of similarity score

(h) Print titles of first 5 movies

## Project-2 - To find the advertisememnt which was clicked maximum number of times by the users

Upper Confidence Bound, One of the simplest policies for making decisions based on action values estimates is greedy action selection. This means, that in order to choose an action we compute an estimated value of all the possible actions and pick the one which has the highest estimate.
In this project we will be using the same approach to estimate the advertisement which was clicked maximum number of times by the user.
The dataset which we will be using for this is "Ads_CTR_Optimisation.csv". In this dataset we are given the information of 10 ADs and 10000 users. If the user clicks on a particular Advertisement then it will be marked as 1 else 0.

### -> Steps to implement this project:

![b](https://user-images.githubusercontent.com/68856803/89013310-4acc9080-d331-11ea-96b6-f3257339d1fd.png)


## Project-3 - Predicting the salary of an employee based on his/her years of experience
In this project we will be using Simple linear regression model. In statistics, simple linear regression is a linear regression model with a single explanatory variable. That is, it concerns two-dimensional sample points with one independent variable and one dependent variable (conventionally, the x and y coordinates in a Cartesian coordinate system) and finds a linear function (a non-vertical straight line) that, as accurately as possible, predicts the dependent variable values as a function of the independent variable.
In this we are using a very small datset having only 2 columns, i.e., YearsExperience	and the Salary.

Following is the plot obtained for training set results:

![a](https://user-images.githubusercontent.com/68856803/89012376-c299bb80-d32f-11ea-9a2d-0d821b58d250.png)

### -> Steps to implement this project:
(a) Importing the required libraries

(b) Importing the dataset

(c) Splitting the dataset into the Training set and Test set

(d) Training the Simple Linear Regression model on the Training set

(e) Predicting the Test set results

(f) Visualising the Training set results

(g) Visualising the Test set results

(h) predicting the salary based upon the value entered by the user



