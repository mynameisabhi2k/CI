import streamlit as st

#UI

st.title('Power Calculator')
st.write('Enter the number to calculate its square, cube, fifth powers.')

#Input
n=st.number_input('Enter Integer Numnber',value=1,step=1)

#Calculate
square = n**2
cube = n**3
fifth = n**5

#Display
st.write(f'The square of {n} is {square}')
st.write(f'The cube of {n} is {cube}')
st.write(f'The fifth power of {n} is {fifth}')