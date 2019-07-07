#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#Basic data exploration


# save file path for easier access
mel_file_path = 'file path'

#read the data in title mel_data
mel_data = pd.read_csv(mel_file_path)
                       
#summary of the data
mel_data.describe()


# In[ ]:


#First machine learning model


#to see the name of colums
mel_data = pd.read_csv(mel_file_path)
mel_data.columns

#drop the missing value
mel_data = mel_data.dropna(axis=0)

#2 approach to be focused on 1.dot notation(select prediction target) 2.select a column first(features)
#prediction target
y = mel_data.Price #y is the prediction target

#choosing features--columns that are inputted into our models and later used to make predictions
mel_features = ['Rooms','Bathroom','Landsize','Lattitude','Longtitude'] #selecting features
X = mel_data[mel_features]  #the data of selected feature is called x by convention

#take a look of the feature
X.describe()
X.head()       #show the top few rows

#scikity-learn library is used to create the model, its wirtten as sklearn
#Type steps: 1.Define 2.Fit(capture pattern from provided data) 3.Pedict 4.Evaluate
#emaple
from sklearn.tree import DecisionTreeRegressor

mel_model = decisionTreeregressor(random_state = 1)#Define the model, specify a random_state to ensure the same result

mel_model.fit(X.y)   #fit model

print("Making prediction for the following 5 houses")
print(X.head())
print("The predictions are")
print(mel_model.predict(X.head()))


# In[ ]:


#Model Validation


#Mean Absolute Error MAE is used to summarize the model
#Error = actual - predicted

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y, predicted_home_prices)    
#In-sample score, this is bad because some coincidence within the given data will be treated as pattern and will be examined to be accurate within the given data

#validation data---exclude some data when building the model and use these excluded date to test the accuracy
#train_test-split function can bak the data into 2 pieces
from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)
mel_model = DecisionTreeregressor()
mel_model.fit(train_X, train_y)
vav_predictons = mel_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))


# In[ ]:


#Underfitting and overfitting
    
    
#overfitting--a model matched the training data almost perfectly but does poorly in validation and other new data
#underfitting--a model that even performs poorly in training data
#max_leaf_nodes proides a sensible way to control overfitting and underfitting
from sklearn.metrics import mean_absolue_error
from sklearn.tree import DecisionTreeRegressor

#To get MAE easily
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisiontreeRegressor(max_leaf_nodes = max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae) 

#comparing MAE with different values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val;_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
#or alternatively
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
best_tree_size = min(scores, key=scores.get)
print(best_tree_size)

#After the best max_leaf_nodes is obtained
final_model = DecisionTreeRegressor(max_leaf_nodes = ??, random_state = ?)
    


# In[ ]:


#Random forests
    
    
from sklearn.ensemble import RandomForestregressor
from sklearn.mtrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state = 1)
forest_odel.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))


# In[ ]:





# In[ ]:




