import streamlit as st
import joblib
import pandas as pd
import numpy as np

model = joblib.load('model.pkl')



st.title('Nepal House Price Prediction using Data Science and Machine Learning')

st.divider()

bedrooms = st.number_input('Enter Number of Bedrooms', min_value=0, value=0)
bathrooms = st.number_input('Enter Number of Bathrooms', min_value=0, value=0)
parking = st.number_input('Enter Number of Parking', min_value=0, value=0)

X = [[bedrooms,bathrooms,parking]]

# data = [
#     {
#         'Bedroom': bedrooms,
#         'Bathroom': bathrooms,
#         'Parking': parking
#     }
# ]

# df = pd.DataFrame(data=data)

# df['Bedroom'] = np.array(bedrooms)
# df['Bathroom'] = np.array(bathrooms)
# df['Parking'] = np.array(parking)



st.divider()

predict_button = st.button('PREDICT')

if predict_button:
    # print(bathrooms)
    # print(df)
    st.balloons()
    X_array = np.array(X)
    prediction = model.predict(X)
    prediction = abs(prediction)
    prediction = prediction/10000

    st.write(f'House Price is Rs.  {prediction[0][0]:,.2f}')
    print(prediction)

    # print(df)

st.divider()

st.write('Developed by SUSHAN BANIYA')


