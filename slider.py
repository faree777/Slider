import streamlit as st
st.title("Streamline Sliders")
st.subheader("Slide 1:")
x = st.slider(" A number between 0-100")
st.write("Slider Number:" , x)