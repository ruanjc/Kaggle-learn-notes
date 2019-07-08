#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Data visulization beginner


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
print("Setup Complete")


# In[ ]:


#csv file--comma-separated value file


# In[ ]:


#Hello seaborn

#.head--show the top few rows of the data
fifa_data.head()

#read the data
museum_data = pd.read_csv(museum_filepath, 
                          index_col = "Date", 
                          parse_dates = True) 
#Data is the name of the column to use as row labels

#force legend to appear
plt.legend()

#plot the data
#1.set the width and height
plt.figure(figsize = (16,6))
#2.line chart
sns.lineplot(data = fifa_data)


# In[ ]:


#Line charts

#.tail()--print the last five rows of the data

#set up the size
plt.figure(figsize=(14,6))

#add title
plt.title("......")

#line chart
sns.lineplot(data = spotify_data)#data = name of the data read above

#print the name of columns
list(name_of_data.columns)

#print the subset
sns.lineplot(data = name_of_data['name_of_columns'],label = "desired label")

#add label to axis
plt.xlabel("name_of_X-axis")


# In[ ]:


#Bar Charts and Heatmaps

#plot the barplot
sns.barplot(x = flight_data.index, y = flight_data['NK'])
#x = data on horizontal axis and y= data on vertical axis

#plot the heat maps
sns.heatmap(data = flight_data, annot = True)
#annot = True ensures all values appears on the chart


# In[ ]:


#Scatter plots

#plot the scatter plots
sns.scatterplot(x = name_of_data['name_of _column_on_x-axis'], 
                y = name_of_data['name_of _column_on_y-axis'])

#plot the graph with a regression line
sns.regplot(x = name_of_data['name_of _column_on_x-axis'], 
            y = name_of_data['name_of _column_on_y-axis'])

#To desiplay the relationship between 3 variables by colour coding the points
sns.scatterplot(x = name_of_data['name_of _column_on_x-axis'], 
                y = name_of_data['name_of _column_on_y-axis'], 
                hue = insurance_data['smoker'])

#2 separate regression lines can be added
sns.lmplot(x = "bmi", y = "charges", hue = "smoker", data = insurance_data)

#catagorical scatter plot--for discontinuous data
sns.swarmplot(x = name_of_data['name_of _column_on_x-axis'], 
              y = name_of_data['name_of _column_on_y-axis'])


# In[ ]:


#Histograms and density plots

#Plot a histogram
sns.distplot(a=iris_data['Petal Length (cm)'], kde = False)
# a = name of the column we want to plot, kde = False, just keep it here

#Plot a KDE(kernel density estimate)
sns.kdeplot(data = iris_data['Petal Length (cm)'], shade = True)

#Play a 2D KDE plot
sns.jointplot(x = iris_data['Petal length (cm)'], y = iris-data['Sepal Width (cm)'], kind = "kde")



# In[ ]:




