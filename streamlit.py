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
#Para que la lista sea tenga más sentido hacemos q la key sea fruta y no el id
my_fruit_list = my_fruit_list.set_index('Fruit')

#con esto ponemos listas de selección al dataframe
#primero sin 
#streamlit.multiselect ("Seleccione sus frutas:", list(my_fruit_list.index))
streamlit.multiselect ("Seleccione sus frutas:", list(my_fruit_list.index),['Avocado','Strawberries'])

streamlit.dataframe(my_fruit_list)

#New Section to display frutyvice api response
streamlit.header("Fruityvice Fruit Advice!")

import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json()) #just write the data to the screen

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
