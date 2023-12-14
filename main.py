import streamlit as st
import qrcode as qr

def generate_qr_code(url, image_name, qr_version):
    img = qr.make(url, version=qr_version)
    img.save(f"{image_name}.png")

def main():
    st.title("QR Code Generator")

    url = st.text_input("Enter the URL:")
    image_name = st.text_input("Enter the Image Name:")
    qr_version = st.slider("Select QR Code Size", min_value=1, max_value=40, value=10)

    if st.button("Generate QR Code"):
        if url and image_name:
            generate_qr_code(url, image_name, qr_version)
            st.image(f"{image_name}.png", caption="Generated QR Code", use_column_width=True)
        else:
            st.warning("Please enter both a valid URL and image name.")

if __name__ == "__main__":
    main()
