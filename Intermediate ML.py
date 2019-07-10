#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Intermediate Machine Learning

#shape of data--(number of rows, number of columns)
print(name_of_data.shape)


# In[ ]:


#Missing values
    
#To know how many columns has missing data and how many entries is missing
miss_val_count_by_column = (X_train.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])

#get the name of the colums with missin data
cols_with_missing = [col for col in X_train.columns if X_train[col].isnull().any()]

#Method 1 Drop columns with missing values
reduced_X_train = X_train.drop(cols_with_missing, axis = 1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis = 1)

#Method 2 Imputation--fill the missing value with some number
from sklearn.impute import SimpleImputer
my_imputer = SimpleImputer()

imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid)) #Imputation

imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns#put back the column names

#Method 3 Imputation and note if some value is missing in that column
X_train_plus = X_train.copy()
X_valid_plus = X_valid.copy() #make a copy so that the original data will not be changed

for col in cols_with_missing:
    X_train_plus[col + '_was_missing'] = X_train_plus[col].isnull()
    X_balid_plus[col + '_was_missing'] = X_valid_plus[col].isnill()
    #making a new cloumn indicating what will be imputed
#then repeat the process of imputation in method 2


# In[ ]:


#Categorical Variables
    
#get list of categorical variables
s = (X_train.dtypes == 'object')#dtype = datatype
object_cols = list(s[s].index)
    
#Method 1 Drop Categorical Variables
drop_X_train = X_train.select_dtypes(exclude = ['object'])
drop_X_valid = X_valid.select_dtypes(exclude = ['object'])

#Method 2 Label encoding--assigns each value to a different integer
from sklearn.preprocessing import LabelEncoder

label_X_train = X_train.copy()
label_X_valid = X_valid.copy()#make copy to avoid chaging original data

encoder = LabelEncoder()
for col in object_cols:
    label_X_train[col] = encoder.fit_transform(X_train[col])
    label_X_valid[col] = encoder.transform(X_valid[col])]#apply label encder to each column with categprical data


#Method 3 One-hot encoding--create new columns indicating the presence of each possible value in the proginal data
#Method 3 works well when there is no clear order of categorical variable(no intrinic ranking--nominal vaiables)
from sklearn.preprocessing import OnehotEncoder

OH_encoder = OnehotEncoder(handle_unknown = 'ignore', sparse = False)
#handle_unknown = 'ignore' avoid errors when the validation data contains classes that arent represented in the training data
#sparse = False ensures that the encoded columns are returned as a numpy array
OH_cols_train = pd.Dataframe(OH-encoder.fit_transform(X_train[object_cols]))
OH_cols_valid = pd.Dataframe(OH-encoder.traisform(X_valid[object_cols]))# apply one-hot encoder to each column with catagorical data

OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index#put index back

num_X_train = X_train.drop(object_cols, axis = 1)
num_X_valid = X_valid.drop(object_cols, axis = 1)#remove categorical columns

OH_X_train = pd.concat([num_X_train, OH_cols_train], axis = 1)
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis = 1)#Add one-hot encoded columns to numerical features


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




