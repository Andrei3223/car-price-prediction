import pickle
import numpy as np
import pandas as pd
import streamlit as st
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
    # image = Image.open('data/titanic.jpg')

    st.set_page_config(
        layout="wide",
        # initial_sidebar_state="auto",
        page_title="Car price predictor",
        # page_icon=image,

    )

    st.write(
        """
        # Predict the price of used vehicle 
        ### Enter data:
        """
    )
    # st.image(image)


def get_dataframe():
    # reading data
    year = st.number_input("The year of manufacture")
    driven = st.number_input("km driven")
    fuel = st.selectbox("Fuel type",
                        ('Diesel', 'Petrol', 'CNG', 'LPG'))
    seller = st.selectbox("Seller type", ('Individual', 'Dealer', 'Trustmark Dealer'))
    transmission = st.selectbox('Transmission type'
                                , ('Manual', 'Automatic'))
    owner = st.selectbox('Owner type', ('First Owner', 'Second Owner',
                                        'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'))
    # mileage 	engine 	max_power 	seats
    mileage = st.number_input("Mileage (in kmpl (km/kg) )")
    engine = st.number_input("Engine volume (in CC)")
    max_power = st.number_input('Max power (in bhp)')
    seats = st.slider(
        "Seats number",
        min_value=1, max_value=30, value=2, step=1)

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
        st.write(df)
        res = model.predict(df)
        st.write(res)


if __name__ == "__main__":
    process_main_page()
