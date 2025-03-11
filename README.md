# Data Cleaning with Python and Pandas

In this project, I discuss useful techniques to clean a messy dataset with Python and Pandas. I discuss EDA and present ways to deal with duplicates and missing datas. I present how to reshape data using the Pandas function.

## 1. Introduction to Python data cleaning

Whenever we have to work with a real world dataset, the first problem that we face is to clean it. The real world dataset never comes clean. It consists lot of discrepancies in the dataset. So, we have to clean the dataset for further processing.

Cleaning data is the process of preparing the dataset for analysis. It is very important because the accuracy of machine learning or data mining models are affected because of poor quality of data.

So, data scientists spend a large amount of their time cleaning the dataset and transform them into a format with which they can work with. In fact, data scientists spend 80% of their time cleaning the data.

A very common scenario is that the dataset contains missing values coded as NaN. Also, the missing values are coded in different ways. The dataset may contain negative or invalid values. It may contain outliers. It may be in the untidy format. All of these are examples of a messy dataset.

In this project, I present several useful ways to handle these discrepancies in the dataset.

## 2. Tidy data format
Data comes in a wide variety of shapes and formats. Hadley Wickham, the Chief Scientist at RStudio, write a paper about tidy data in 2014 that formalizes the shape of the data. So, it gives us a goal when formatting the data.

He states in his paper that –

Tidy data provides a standard way to organize data values within a dataset.

There are three principles of tidy data. These are as follows:-

**• Columns represent separate variables**

**• Rows represent individual observations**

**• Observational units form tables.**

Tidy data makes it easier to fix common data problems. So, we need to transform the untidy dataset into tidy data.

Before we look into the details of cleaning the dataset, we have to understand what constitutes an untidy data. We need to diagnose our data and find common signs of a messy dataset.

## 3. Signs of an untidy dataset

We have to take a closer look to find common signs of a messy dataset. These common signs are as follows:-

**• Missing numerical data**

Missing numerical data needs to be identified and addressed. Either they need to be deleted or replaced with a suitable test statistic.

**• Untidy data**

Untidy dataset can contain multiple problems. They prevent us from transforming the messy dataset into a clean dataset that is suitable for analysis.

**• Unexpected data values**

Mismatched data types of a column and data values can cause potential problems. They need to be investigated and solved.

**• Inconsistent column names**

Column names contain inconsistent capitalizations and bad characters. They need to be addressed properly.

**• Outliers**

Outliers need to be detected. They pose potential problems needs to be investigated and removed.

**• Duplicate rows and columns**

Duplicate rows and columns make data redundant. They can bias an analysis. Hence, they needs to be found and dropped.

## 4. Python data cleaning - prerequisites

We need three Python libraries for the data cleaning process – NumPy, Pandas and Matplotlib.

**• NumPy** – NumPy is the fundamental Python library for scientific computing. It adds support for large and multi-dimensional arrays and matrices. It also supports large collection of high-level mathematical functions to operate on these arrays.

**• Pandas** - Pandas is a software library for Python programming language which provide tools for data manipulation and analysis tasks. It will enable us to manipulate numerical tables and time series using data structures and operations.

**• Matplotlib** - Matplotlib is the core data visualization library of Python programming language. It provides an object-oriented API for embedding plots into applications.

## 5. Import Python libraries

We have seen that we need three Python libraries – NumPy, Pandas and Matplotlib for the data cleansing process. We need to import these libraries before we actually start using them. We can import them with their usual shorthand notation as follows:-

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

%matplotlib inline

## 6. Exploratory data analysis
Now, it is time to understand the data. We should diagnose the data for any discrepancies by doing exploratory data analysis. We should proceed as follows:-

• **df.shape** attribute

We can check the dimensions of the data with **df.shape** attribute.

• **df.head()** and **df.tail()** methods

We can view the top five and bottom five rows of the dataset with **df.head()** and **df.tail()** methods respectively.

• **df.info()** method

We can get a concise summary of the dataset with **df.info()** method. This method prints information about a DataFrame including the index dtype and column dtypes, non-null values and memory usage.

• **df.dtypes** attribute

We can check the data types of each column in the dataframe with **df.dtypes** attribute. The above command returns the data type of each column.

• **df.describe()** method

We can view the summary statistics of numerical columns with **df.describe()** method. It enable us to detect outliers in the data which require further investigation.

• **df.columns** attribute

We can get the column labels of the dataframe with **df.columns** attribute.

## 7. Visual exploratory data analysis

Now, we should conduct data visualization to find discrepancies in the data. Data visualization is a great way to find errors in the data and detect outliers. They help us to detect patterns in the data.

We can use various types of plots for data visualization purpose. These plots are listed below:-

**• Bar plot**

A bar plot is a plot that presents data with rectangular bars with lengths proportional to the values that they represent.

**• Histograms**

We use histograms for plotting continuous data counts. A histogram is a representation of the distribution of data.

In this case, we use histograms for plotting distribution of data values of height (cm) and weight (kg) columns.

**• Box plot**

We can visualize basic summary statistics with box plot. Box plot let us to detect outliers in the data. They help us to find minimum and maximum values. They present 25th, 50th, 75th percentiles. 50th percentile value is the median value.

**• Scatter plot**

Scatter plot help us to explore relationship between two numeric variables. It help us to identify potentially bad data. We should draw a scatter plot of height(cm) and weight(kg) column.

## Author - Antonio Reshme

This project is part of my portfolio, showcasing the dta clening skills essential for data analyst roles. If you have any questions, feedback, or would like to collaborate, feel free to get in touch!
