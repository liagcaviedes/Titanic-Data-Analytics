import streamlit as st

# URLs de las páginas a incrustar
url1 = "https://verdaderahistoriadeltitanic.blogspot.com/2015/04/los-perros-del-titanic.html"
url2 = "https://es.wikipedia.org/wiki/RMS_Titanic"
url3 = "https://www.encyclopedia-titanica.org/"

col1, spacer, col2, spacer2, col3 = st.columns([1, 0.4, 1, 0.4, 1])

with col1:
    st.markdown('Historia del Titanic')
    st.components.v1.iframe(url1, width=200, height=100)  
    if st.button("Ir a Historia del Titanic"):
        st.write(f'<meta http-equiv="refresh" content="0; url={url1}">', unsafe_allow_html=True)
    


with col2:
    st.markdown("Wikipedia")
    st.components.v1.iframe(url2, width=200, height=100)
    if st.button("Ir Wikipedia"):
        st.write(f'<meta http-equiv="refresh" content="0; url={url2}">', unsafe_allow_html=True)



with col3:
    st.markdown("Enciclopedia Titánica")
    st.components.v1.iframe(url3, width=200, height=100)
    if st.button("Ir a Enciclopedia Titánica"):
        st.write(f'<meta http-equiv="refresh" content="0; url={url3}">', unsafe_allow_html=True)
