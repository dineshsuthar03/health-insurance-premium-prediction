#!/usr/bin/env python
# coding: utf-8

# In[4]:





# In[11]:


import pickle
import numpy as np
# load the model from disk
loaded_model = pickle.load(open('streamlit_insurance_predictcharges.pkl', 'rb'))
import streamlit as st
# Creating the Titles and Image
st.title("Predict insurance charges")
st.header("Calculating the insurance charges that could be charged by an insurer based on a person's attributes")
# Output:<streamlit.DeltaGenerator.DeltaGenerator at 0x2a8a8bed088>
import pandas as pd
def load_data():
    df = pd.DataFrame({'sex': ['male','female'],
                       'smoker': ['yes', 'no']}) 
    return df
df = load_data()
import pandas as pd
def load_data():
    df1 = pd.DataFrame({'region' : ['southeast' ,'northwest' ,'southwest' ,'northeast']}) 
    return df1
df1 = load_data()
# Take the users input

sex = st.selectbox("Select Sex", df['sex'].unique())
smoker = st.selectbox("Are you a smoker", df['smoker'].unique())
region = st.selectbox("Which region do you belong to?", df1['region'].unique())
age = st.slider("What is your age?", 18, 100)
bmi = st.slider("What is your bmi?", 10, 60)
children = st.slider("Number of children", 0, 10)

# converting text input to numeric to get back predictions from backend model.
if sex == 'male':
    sex = 1
else:
    sex = 0
    
if smoker == 'yes':
    smoker = 1
else:
    smoker = 0
    
if region == 'southeast':
    region = 3
elif region == 'northwest':
    region = 2
elif region == 'southwest':
    region = 4
else:
    region = 1
    

# store the inputs
features = [ age, sex, bmi, children ,smoker ,region]
# convert user inputs into an array fr the model

int_features = [int(x) for x in features]
final_features = [np.array(int_features)]
if st.button('Predict'):           # when the submit button is pressed
    prediction =  loaded_model.predict(final_features)
    st.balloons()
    st.success(f'Your insurance charges would be: Rs.{round(prediction[0],2)}')
    


# In[ ]:


# import os
# ROOT_DIR = os.path.abspath(os.curdir)
# ROOT_DIR


# In[ ]:





# In[ ]:




