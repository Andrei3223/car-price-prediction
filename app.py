import pickle
import numpy as np
import pandas as pd
import streamlit as st
import sklearn
from PIL import Image


# from sklearn import linear_model


def load_model(path='model.pickle'):
    with open(path, 'rb') as f:
        model = pickle.load(f)
    return model


def process_main_page():
    show_main_page()
    df = get_dataframe()
    get_result(df)


def show_main_page():
    image = Image.open('Drive.jpg')

    st.set_page_config(
        layout="wide",
        # initial_sidebar_state="auto",
        page_title="Car price predictor",
        # page_icon=image,

    )
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write(
            """
            # Predict the price of used vehicle 
            ### Enter data:
            """
        )
    with col2:
        st.image(image, width=600)


def get_dataframe():
    # reading data
    col1, col2 = st.columns([1, 1])
    with col1:
        year = st.number_input("The year of manufacture", 2019)
    with col2:
        driven = st.number_input("km driven", 35000)

    col3, col4 = st.columns([1, 1])
    with col3:
        fuel = st.selectbox("Fuel type",
                            ('Diesel', 'Petrol', 'CNG', 'LPG'))
    with col4:
        seller = st.selectbox("Seller type", ('Individual', 'Dealer', 'Trustmark Dealer'))

    col5, col6 = st.columns([1, 1])
    with col5:
        transmission = st.selectbox('Transmission type'
                                    , ('Manual', 'Automatic'))
    with col6:
        owner = st.selectbox('Owner type', ('First Owner', 'Second Owner',
                                            'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'))

    col7, col8, col9 = st.columns([1, 1, 1])
    with col7:
        mileage = st.number_input("Mileage (in kmpl (km/kg) )", 23)
    with col8:
        engine = st.number_input("Engine volume (in CC)", 1000)
    with col9:
        max_power = st.number_input('Max power (in bhp)', 50)
    seats = st.slider(
        "Seats number",
        min_value=1, max_value=30, value=5, step=1)

    # preparing data
    translatetion = {
        'Individual': 0, 'Dealer': 1, 'Trustmark Dealer': 2,
        'Manual': 0, 'Automatic': 1,
        'Test Drive Car': 0, 'Fourth & Above Owner': 1,
        'Third Owner': 2, 'Second Owner': 3, 'First Owner': 4,

    }

    data = {
        "year": year,
        "km_driven": driven,
        "seller_type": translatetion[seller],
        "transmission": translatetion[transmission],
        "owner": translatetion[owner],
        "mileage": mileage,
        "engine": engine,
        "max_power": max_power,
        "seats": seats,
        "Diesel": (lambda x: 1 if x == 'Diesel' else 0)(fuel),
        "Petrol": (lambda x: 1 if x == 'Petrol' else 0)(fuel),
        "CNG": (lambda x: 1 if x == 'CNG' else 0)(fuel),
        "LPG": (lambda x: 1 if x == 'LPG' else 0)(fuel)
    }

    df = pd.DataFrame(data, index=[0])

    return df


def get_result(df: pd.DataFrame):
    if st.button("Show result"):
        model = load_model()
        '''
            ## Your car characteristics:
        '''
        st.write(df)
        '''
            ## Approximate price of your car:
        '''
        res = model.predict(df)
        # st.markdown('<p class="big-font">%$res%</p>', unsafe_allow_html=True)
        st.write(f'{res[0]:0,.2f}', 'rubles',
                 unsafe_allow_html=True)
        # st.write(res[0])


if __name__ == "__main__":
    process_main_page()
