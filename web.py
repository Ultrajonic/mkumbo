#!/usr/bin/env python
# coding: utf-8

# In[12]:


import streamlit as st

st.header ('''My First Simple Web App''')
st.write ('''***By John Emmanuel***''')
st.write ('''**Temperature Calculations**''')
C = st.number_input('Insert a number in Celcius')
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




