import streamlit
import pandas

streamlit.title('Título: Haciendo cositas')

streamlit.header('Header 1')

streamlit.text('My new code has no sense')
streamlit.text('----------------')
streamlit.text('--Example code--')
streamlit.text('----------------')

streamlit.header('Header 2')

streamlit.text('Y ahora unas moñerías varias')
streamlit.text('🥣 🥗 🐔 🥑🍞')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

