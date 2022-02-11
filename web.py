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
import streamlit as st
st.title("Press button to Vote")
if st.button('VOTE'):
     st.write('Voted!!')
else:
     st.write('Goodbye')




# In[ ]:
import streamlit as st
st.title("ULTRAJONIC STUDIO")
st.subtitle("Welcome in Media Production")
name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
     
     
option = st.selectbox(
     'What are you want to do in Ultrajonic Studio?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)



#Finally agree with above contents.............     
agree = st.checkbox('I agree')

if agree:
     st.write('Thank you, your done!!')


