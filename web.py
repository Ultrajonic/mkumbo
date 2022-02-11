#!/usr/bin/env python
# coding: utf-8

# In[12]:


import streamlit as st

st.header ('''My Simple Web App''')
st.write ('''***By Ultrajonic_96***''')
st.write ('''**Temperature Calculations**''')
C = st.slider('Slide to Change Input Value of Temperature in Celcius',0.00,500.00,1000.00)
F = (((C)*(9/5))+32)
st.write(F, "Fahrenheit")
K = (((F - 32)*(5/9))+(273.15))
st.write(K, "Kelvin")


# In[2]:


import streamlit as st
from math import pi
st.write ('''***Volume of a Sphere***''')
r = st.sidebar.number_input('Slide to Change Input Value of radius in cm')
V = ((4/3)*(pi)*(r**3))
st.write ("The value of volume of a Sphere is ",V)


# In[ ]:





# In[ ]:




