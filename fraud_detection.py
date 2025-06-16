import streamlit as st
import pandas as pd
import joblib

model = joblib.load('fraud_detection_model.pkl')

st.title('Fraud Detection Prediction App')
st.markdown('Please enter the transaction details.')
st.divider()

transaction_type = st.selectbox('Transaction Type', ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEPOSIT'])
amount = st.number_input('Amount', min_value=0.0, value=1000.0)
oldbalance_org = st.number_input('Old Balance (Sender)', min_value=0.0, value=10000.0)
newbalance_org = st.number_input('New Balance (Sender)', min_value=0.0, value=9000.0)
oldbalance_dest = st.number_input('Old Balance (Receiver)', min_value=0.0, value=0.0)
newbalance_dest = st.number_input('New Balance (Receiver)', min_value=0.0, value=0.0)

if st.button('Predict'):
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalance_org],
        'newbalanceOrig': [newbalance_org],
        'oldbalanceDest': [oldbalance_dest],
        'newbalanceDest': [newbalance_dest]
    })
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error('This transaction is likely fraudulent.')
    else:
        st.success('This transaction is likely legitimate.')