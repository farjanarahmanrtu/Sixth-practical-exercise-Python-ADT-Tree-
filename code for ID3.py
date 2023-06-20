#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


# In[50]:


data = pd.read_csv('SDN_traffic.csv')


# In[51]:


data =data.fillna(0)


# In[52]:


non_numeric_columns = data.select_dtypes(exclude=['float','int']).columns


# In[53]:


for column in non_numeric_columns:
    label_encoder = LabelEncoder()
    data[column] =label_encoder.fit_transform(data[column])


# In[54]:


X = data.drop('category', axis=1)  
y = data['category']


# In[55]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[56]:


clf = DecisionTreeClassifier(criterion='entropy')


# In[57]:


clf.fit(X_train, y_train)


# In[58]:


y_pred = clf.predict(X_test)


# In[59]:


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




