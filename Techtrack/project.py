import streamlit as st
import time
st.title("Hello Streamlit!")
if st.button("Click me for snow!"):
    for _ in range(20):
        st.snow()
        time.sleep(4.5)
if st.button("Click me for !"):
    st.balloons()
