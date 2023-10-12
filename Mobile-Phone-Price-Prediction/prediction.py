import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle

model = pickle.load(open('model.pkl','rb'))

st.title("Phone Price Range Prediction")

st.markdown(" This is a simple web application that predicts the price range of your mobile phone based on the phone's specifications.")
st.markdown("The price ranges are given as follows: ")
st.markdown(
"""
* Low Cost
* Medium Cost
* High Cost
* Very High Cost
""")

st.markdown("The data used for this project was collected from [Kaggle](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification) and machine learning was employed to predict the price ranges based on the data obtained. You can find the full project (with codes) on [GitHub](https://github.com/awojidetola/Mobile-Phone-Price-Prediction)")

battery_power = st.number_input("Enter Battery Power in mAh")
bluetooth = st.selectbox("Does your phone have bluetooth?", ("Yes","No"))
if bluetooth == "Yes":
    blue = 1
else:
    blue = 0

clock_speed = st.number_input("What is the microprocessor speed", value=2.0)
sim = st.selectbox("Does your phone have Dual Sim?",("Yes","No"))
if sim == "Yes":
    dual_sim = 1
else:
    dual_sim = 0

fc = st.number_input("What is your front camera mega pixels?")
speed= st.selectbox("Is your phone 4G?",("Yes","No"))
if speed == "Yes":
    four_g = 1
else:
    four_g = 0

int_memory = st.number_input("What is your internal memory in GB?")
m_dep = st.number_input("What is your phone's mobile depth in cm?")

mobile_wt = st.number_input("What is the weight of your phone?")
n_cores = st.number_input("What is the number of cores of processor?")
pc = st.number_input("What is the main camera quality in mega pixels?")
px_height = st.number_input("What is the pixels resolution height?")
px_width = st.number_input("What is the pixels resolution width?")
ram = st.number_input ("What is the ram in MB?")
sch = st.number_input("What is the screen height in cm?")
scw = st.number_input("What is the screen width in cm?")
talk_time = st.number_input("What is your phone talk time, How long can your phone last when you are constantly talking on phone?")
speed_2 = st.selectbox("Does your phone have 3G?",("Yes","No"))
if speed_2 == "Yes":
    three_g = 1
else:
    three_g = 0
ts= st.selectbox("Is your phone touch screen?",("Yes","No"))
if ts == "Yes":
    touch_screen = 1
else:
    touch_screen = 0

w = st.selectbox("Does your phone have WIFI?",("Yes","No"))
if w == "Yes":
    wifi = 1
else:
    wifi = 0

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

data = [[battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width,ram, sch, scw, talk_time, three_g, touch_screen, wifi]]

result = model.predict(data)

if result[0] == 0:
    result_2 = "Low Cost"

elif result[0] == 1:
    result_2 = "Medium Cost"

elif result [0] == 2:
    result_2 = "High Cost"

else:
    result_2 = "Very High Cost"

if st.button('Submit'):
     st.write("Your Phone has a {} Price Range".format(result_2))
else:
     st.write('')
