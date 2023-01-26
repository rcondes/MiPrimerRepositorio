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

fruit_choice = streamlit.text_input ('Sobre que fruta quieres info?', 'kiwi')
stream.write('El usuario eligió', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json()) # Tan solo manda los datos en crudo a la pantalla

# Descargamos el contenido normalizado del JSON con Panda
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Lo mostramos en una tabla
streamlit.dataframe(fruityvice_normalized)

