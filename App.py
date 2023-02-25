import streamlit as st

st.title('BMI CALULATOR')
Weight = st.number_input('Enter Weight in KILOGRAMS',min_value=15,step=5)
Height = st.number_input('Enter Height in CENTIMETER',min_value=30,step=5)
st.write('1 Feet = 30.48 CM')

if st.button('BMI CALULATOR'):
    b=(Weight/(Height/100)**2) 
    if b <= 18.5:
        st.write("Oops! You are underweight.")  
    elif b <= 24.9:  
        st.write("Awesome! You are healthy.")  
    elif b <= 29.9:  
        st.write("Eee! You are over weight.")
    else:
        st.write("Seesh! You are obese.")
    st.write('Your BMI IS', b)
else:
    st.write('Enter the values for output')
