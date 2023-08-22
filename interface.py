import streamlit as st
import pandas as pd
import numpy as np
import pickle

loaded_model = pickle.load(open('Customer_churn_prediction.pkl', 'rb'))
sc = pickle.load(open('sc.pkl', 'rb'))

data=pd.read_csv("Telco-Customer-Churn.csv")
st.header("CUSTOMER CHURN PREDICTION")
st.write("In todays commercial world competition is high and every customer is valuable. Understanding the customer is of utmost importance, including being able to understand the behavior patterns of that customer. Customer Churn is the rate at which a commercial (very prevalent in SaaS platforms) customer leaves the commercial business and takes their money elsewhere. Understanding customer churn is vital to the success of a company and a churn analysis is the first step to understanding the customer.")
nav=st.sidebar.radio("navigation",["PREDICT","Dataset"])
if nav=="PREDICT":
    st.title("Predicting the customer churn")
    gender=st.selectbox("Gender",['Male','Female'],index=0)
    if gender=="Male":
        gender=1
    else:
        gender=0
    SeniorCitizen=st.selectbox("SeniorCitizen",[0,1],index=0)
    Partner=st.selectbox("Partner",['Yes','No'],index=1)
    if Partner=="No":
        Partner=0
    else:
        Partner=1
    Dependents=st.selectbox("Dependents",['Yes','No'],index=1)
    if Dependents=="No":
        Dependents=0
    else:
        Dependents=1
    tenure=st.number_input("tenure",min_value=0.0,max_value=72.0,value=0.0,step=1.0)
    PhoneService=st.selectbox("PhoneService",['Yes','No'],index=1)
    if PhoneService=="No":
        PhoneService=1
    else:
        PhoneService=0
    MultipleLines=st.selectbox("MultipleLines",['No','Yes','No phone Service'],index=1)
    if MultipleLines=="No":
        MultipleLines=0
    elif MultipleLines=="Yes":
        MultipleLines=2
    else:
        MultipleLines=1
    InternetService=st.selectbox("InternetService",['Fiber optic','DSL',"No"],index=0)
    if InternetService=='DSL':
        InternetService=0
    elif InternetService=='Fiber optic':
        InternetService=1
    else:
        InternetService=2
    OnlineSecurity=st.selectbox("OnlineSecurity",['No','Yes','No internet service'],index=1)
    if OnlineSecurity=='No':
        OnlineSecurity=0
    elif OnlineSecurity=='Yes':
        OnlineSecurity=2
    else:
        OnlineSecurity=1
    OnlineBackup=st.selectbox("OnlineBackup",['No','Yes','No internet service'],index=1)
    if OnlineBackup=='No':
        OnlineBackup=0
    elif OnlineBackup=='Yes':
        OnlineBackup=2
    else:
        OnlineBackup=1
    DeviceProtection=st.selectbox("DeviceProtection",['No','Yes','No internet service'],index=1)
    if DeviceProtection=='No':
        DeviceProtection=0
    elif DeviceProtection=='Yes':
        DeviceProtection=2
    else:
        DeviceProtection=1
    TechSupport=st.selectbox("TechSupport",['No','Yes','No internet service'],index=1)
    if TechSupport=='No':
        TechSupport=0
    elif TechSupport=='Yes':
        TechSupport=2
    else:
        TechSupport=1
    StreamingTV=st.selectbox("StreamingTV",['No','Yes','No internet service'],index=1)
    if StreamingTV=='No':
        StreamingTV=0
    elif StreamingTV=='Yes':
        StreamingTV=2
    else:
        StreamingTV=1
    StreamingMovies=st.selectbox("Streamingmovies",['No','Yes','No internet service'],index=1)
    if StreamingMovies=='No':
        StreamingMovies=0
    elif StreamingMovies=='Yes':
        StreamingMovies=2
    else:
        StreamingMovies=1
    Contract=st.selectbox("Contract",['Month-to-month','Two year','One year'],index=1)
    if Contract=='Month-to-month':
        Contract=0
    elif Contract=='Two year':
        Contract=2
    else:
        Contract=1
    PaperlessBilling=st.selectbox("PaperlessBilling",['Yes','No'],index=1)
    if PaperlessBilling=='Yes':
        PaperlessBilling=1
    else:
        PaperlessBilling=0
    PaymentMethod=st.selectbox("PaymentMethod",['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'],index=1)
    if PaymentMethod=="Electronic check":
        PaymentMethod=2
    elif PaymentMethod=="Mailed check":
        PaymentMethod=3
    elif PaymentMethod=="Bank transfer (automatic)":
        PaymentMethod=0
    else:
        PaymentMethod=1
    MonthlyCharges=st.number_input("MonthlyCharges",min_value=18.250000	,max_value=118.750000,value=18.250000,step=0.1000000)
    TotalCharges=st.number_input("TotalCharges",min_value=18.800000,max_value=8684.800000,value=18.800000,step=0.100000)

    if st.button("PREDICT"):
        classifier=loaded_model.predict(sc.transform([[gender, SeniorCitizen, Partner, Dependents,tenure, PhoneService, MultipleLines, InternetService,OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,StreamingTV, StreamingMovies, Contract, PaperlessBilling,PaymentMethod, MonthlyCharges, TotalCharges]]))
        if classifier == 0:
            st.error("Customer will not churn")
            st.write("<span style='font-size: 30px;'>Customer is not going to churn</span>", unsafe_allow_html=True)
        else:
            st.success("Customer will churn")
            st.write("<span style='font-size: 30px;'>Customer is going to churn</span>", unsafe_allow_html=True)
    st.write("")	
    st.write("A PROJECT BY")
    st.markdown("<h1 style='font-size: 20px;'>SYAM KRISHNA REDDY PULAGAM</h1>", unsafe_allow_html=True)
elif nav=="Dataset":
    st.success("Tick below to view the dataset")
    if st.checkbox("view dataset"):
        st.dataframe(data,width=500,height=500)