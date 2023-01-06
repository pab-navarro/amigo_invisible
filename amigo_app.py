import streamlit
import pandas
import folium
from streamlit_folium import st_folium

streamlit.title('BONO REGALO AMIGO INVISIBLE')
streamlit.markdown('Este bono lo podrás canjear en el momento que mejor que venga.')
streamlit.markdown('**Lugar donde se realiza:** Casarrubios del Monte - Toledo')
streamlit.text('Duración de la actividad: Desde 30 minutos')
streamlit.text('Incluye:')
streamlit.text('Vuelo con piloto. En el ultraligero irán el piloto y participante.')
streamlit.text('Recomendación: No es necesaria ninguna indumentaria especial, vestimenta normal y cómoda, zapato bajo.')

streamlit.header('LOCALIZACIÓN')


# center on Liberty Bell, add marker
m = folium.Map(location=[40.189823, -4.024408], zoom_start=13)
folium.Marker(
    [40.189823, -4.024408], popup="Sitio del regalo", tooltip="Sitio del regalo"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)
