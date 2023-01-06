import streamlit
import pandas
import folium
from streamlit_folium import st_folium

streamlit.title('My Parent New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


# center on Liberty Bell, add marker
m = folium.Map(location=[40.189823, -4.024408], zoom_start=14)
folium.Marker(
    [40.189823, -4.024408], popup="Sitio del regalo", tooltip="Sitio del regalo"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)
