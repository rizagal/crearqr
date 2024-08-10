import qrcode
import streamlit as st
from streamlit_option_menu import option_menu
from st_paywall import add_auth

filename = "qr_codes/qr_code.png"

st.set_page_config(page_title="QR Code Generator", page_icon="🌐", layout="centered")

def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


st.sidebar.image("SIGES17.png",caption="")

with st.sidebar:

    st.warning("debes estar subscrito")
    add_auth(required=True)
    st.success("Bienvenido")
    selected = option_menu('Aplicativos Web con Sus respectivas explicacion y Codigo',
                           ['Codigo QR en Paython',
                            'Consulta Resultado Indicadores Atencion al Usuario', 
                            ],
                           icons = ['activity','bar-chart'],
                           default_index = 0)


if(selected == 'Codigo QR en Paython'):
#create a streamlit app     
    st.image("images/supports.JPG", use_column_width=True)
    st.title("QR Code Generator")
    url = st.text_input("Enter the URL")

    if st.button("Generate QR Code"):
        generate_qr_code(url, filename)
        st.image(filename, use_column_width=True)
        with open(filename, "rb") as f:
                        image_data = f.read()  
        download = st.download_button(label="Download QR", data=image_data, file_name="qr_generated.png")
