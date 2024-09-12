import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# App title
st.title("QR Code Generator")

# Get input from user
text = st.text_input("Enter the text to generate a QR code:")

# QR code generation button
if st.button("Generate QR Code"):
    if text:
        # Generate QR code
        qr_img = qrcode.make(text)
        
        # Convert PIL image to bytes
        buf = BytesIO()
        qr_img.save(buf, format="PNG")
        buf.seek(0)
        
        # Display QR code in Streamlit
        st.image(buf, caption="Generated QR Code", use_column_width=True)
        
        # Add QR code download button
        st.download_button("Download QR Code", buf, file_name="qrcode.png")
    else:
        st.warning("Please enter some text!")
