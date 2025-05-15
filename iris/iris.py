import streamlit as st
import pickle

st.title("Iris Plant Prediction")
sl=st.number_input("Enter sepal lenght")
sw=st.number_input("Enter sepal width")
pl=st.number_input("Enter petal length")
pw=st.number_input("Enter petal width")
button=st.button("Predict")

if button:
    model=pickle.load(open("iris.pkl","rb"))
    res=model.predict([[sl,sw,pl,pw]])[0]
    st.markdown(f"predict Iris Class:{res}")
