# Codigo Genear Qr
```bash
import qrcode
import streamlit as st
from streamlit_option_menu import option_menu

filename = "qr_codes/qr_code.png"

st.set_page_config(page_title="QR Code Generator", page_icon="pegar_icono", layout="centered")

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


st.sidebar.image("ideabien_transparente.PNG",caption="")

with st.sidebar:  
    selected = option_menu('Aplicativos Web con Sus respectivas explicacion y Codigo',
                           ['Codigo QR en Paython',
                            'Nueva Opcion', 
                            ],
                           icons = ['activity','bar-chart'],
                           default_index = 0)


```
## **Explicacion del Codigo como Generar QR?**
```bash
- Instalar la Libreria: qrcode
- Crear Carpeta: qr_codes - En la carpeta raiz del codigo
```

