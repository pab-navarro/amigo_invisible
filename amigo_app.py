import streamlit
import pandas
import folium
from streamlit_folium import st_folium

streamlit.markdown('<h1 align="center">BONO REGALO AMIGO INVISIBLE + CUMPLEAÑOS</h1>', unsafe_allow_html=True)
streamlit.markdown('Te queremos regalar este bono de parte de Pablo y Amaya. Este bono es canjeable en cualquier momento por un bautismo de vuelo en un avión ultraligero :airplane:.')
streamlit.markdown('**Lugar donde se realiza:** Casarrubios del Monte - Toledo')
streamlit.markdown('**Duración de la actividad:** Desde 30 minutos')
streamlit.markdown('**Incluye:**')
streamlit.markdown('Vuelo con piloto. En el ultraligero irán el piloto y participante.')
streamlit.markdown('**Recomendación:** No es necesaria ninguna indumentaria especial, vestimenta normal y cómoda, zapato bajo.')

streamlit.markdown('**No incluye:**')
streamlit.markdown('**Opcional:** Grabación del vuelo y se ofrece un video editado personalizado con la experiencia, por un coste de 20 € (pago directo el día del vuelo)')

streamlit.markdown("""
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr><td align="center"> <img src="https://www.rolactivo.com/admin/actividades/3195/casarubios-01_BIG.jpg"> </td> </tr>
<tr><td align="center"> <img src="https://www.rolactivo.com/admin/actividades/3195/casarubios-02_BIG.jpg"> </td> </tr>
<tr><td align="center"> <img src="https://www.rolactivo.com/admin/actividades/3195/avion_visto_xdcha_web_BIG.jpg"> </td></tr>
</tr> </table>""", unsafe_allow_html=True)


streamlit.markdown("""
<h1 align="center">LOCALIZACIÓN</h1>""", unsafe_allow_html=True)

# center on Liberty Bell, add marker
m = folium.Map(location=[40.189823, -4.024408], zoom_start=13)
folium.Marker(
    [40.189823, -4.024408], popup="Sitio del regalo", tooltip="Sitio del regalo"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)

streamlit.markdown("""
<h1 align="center">RICHI ATERRIZANDO</h1>""", unsafe_allow_html=True)

streamlit.markdown("""
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr><td align="center"> <img src="https://media3.giphy.com/media/HW14ptNE7lJw4/200.gif?cid=790b7611xq4pppva4mw60avv6h24ja5e2lx1v9t8oos6tdmd&rid=200.gif&ct=g"> </td></tr>
</tr> </table>""", unsafe_allow_html=True)
