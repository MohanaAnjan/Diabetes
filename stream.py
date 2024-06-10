import streamlit as st
import plotly.graph_objects as go
from suger import *

# streamlit
st.set_page_config(page_title="Find your Diabetes status",layout='wide')
st.title(':blue[FIND YOUR DIABETES STATUS]')

name=st.text_input('**Enter Your Full Name**')
gen=st.selectbox('**Select Gender**', ('Male','Female','Others'), key='gender')
if gen=="Male":
    gen=1
elif gen=="Female":
    gen=0
else:
    gen=2

age = st.text_input('**Enter the Age**')
hypertension=st.selectbox('**Enter Hypertension status(BLOOD PRESSURE)**', ('Yes','No',), key='hypertension')
if hypertension=="Yes":
    hypertension=1
else:
    hypertension=0

smoke_hist=st.selectbox('**Select smoking_history**', ('never', 'No Info', 'current', 'former', 'ever', 'not current'),key='smoke_hist')
if smoke_hist=='never':
    smoke_hist=4
elif smoke_hist=='current':
    smoke_hist=0
elif smoke_hist=='ever':
    smoke_hist=1
elif smoke_hist=='former':
    smoke_hist=3
elif smoke_hist=='No Info':
    smoke_hist=2
elif smoke_hist=='not current':
    smoke_hist=5
heart_disease=st.selectbox('**Select heart_disease status**', ('Yes','No'), key='heart_disease')
if heart_disease=="Yes":
    heart_disease=0
else:
    heart_disease=1
bmi=st.text_input('**Enter your BMI**')
HbA1c_level=st.text_input('**Enter your HbA1c_level**')
blood_glucose_level=st.text_input('**Enter your blood_glucose_level**')

Get_data = st.button('**Retrieve and get results**')

# Define Session state to Get data button
if "Get_state" not in st.session_state:
    st.session_state.Get_state = False
if Get_data or st.session_state.Get_state:
    st.session_state.Get_state = True

    input=np.array([[gen,age,hypertension,smoke_hist,heart_disease,bmi,HbA1c_level,blood_glucose_level]])
    input_pred=model.predict(input)
    if input_pred==1:
        st.header(f'''OOPS! '{name} 'You have Diabetes''')
    else:
        st.header(f'''Congrats! '{name}' You have  NO Diabetes''')







