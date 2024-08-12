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


st.sidebar.image("ideabien_transparente.png",caption="")

with st.sidebar: 
    st.warning("debes estar subscrito")
    add_auth(
    required=True,
    login_button_text="Iniciar con Google",
    login_button_color="#FD504D",
    login_sidebar=True,
    )  
    st.success("Bienvenido: " + st.session_state.email)   
    # st.write(st.session_state.user_subscribed)
    selected = option_menu('Aplicativos Web con Sus respectivas explicacion y Codigo',
                           ['Codigo QR en Paython',
                            'Nueva Opcion', 
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

    st.markdown("""---""")
    with open(f'contenido_qr.md', 'r') as f:
        st.markdown(f.read())
