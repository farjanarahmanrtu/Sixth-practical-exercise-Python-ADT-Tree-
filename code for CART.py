#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


# In[61]:


data = pd.read_csv('SDN_traffic.csv')


# In[62]:


data =data.fillna(0)


# In[63]:


non_numeric_columns = data.select_dtypes(exclude=['float','int']).columns


# In[64]:


for column in non_numeric_columns:
    label_encoder = LabelEncoder()
    data[column] =label_encoder.fit_transform(data[column])


# In[65]:


X = data.drop('category', axis=1)  
y = data['category']


# In[66]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[73]:


clf = DecisionTreeClassifier(criterion='gini')


# In[74]:


clf.fit(X_train, y_train)


# In[75]:


y_pred = clf.predict(X_test)


# In[76]:


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




