import streamlit as st
import socket

st.title('Află IP-ul unui Site')

# Introducerea URL-ului site-ului
url = st.text_input('Introduceți URL-ul site-ului:')


# Funcția pentru a rezolva IP-ul
def get_ip_address(url_local):
    try:
        ip_address_local = socket.gethostbyname(url_local)
        return ip_address_local
    except socket.gaierror:
        return 'Nu s-a putut rezolva IP-ul pentru URL-ul introdus.'


# Afișează IP-ul dacă URL-ul a fost introdus
if url:
    ip_address = get_ip_address(url)
    st.write(f'Adresa IP a site-ului {url} este: {ip_address}')
