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

streamlit.text('Leer y mostrar el contenido de un csv del bucket de Amazon mediante "pandas"')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#con esto ponemos listas de selección al dataframe
streamlit.multiselect ("Seleccione sus frutas:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
