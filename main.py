import streamlit as st
import qrcode as qr

def generate_qr_code(url, image_name):
    img = qr.make(url)
    img.save(f"{image_name}.png")

def main():
    st.title("QR Code Generator")

    url = st.text_input("Enter the URL: ")
    image_name = st.text_input("Enter the Image Name: ")

    if st.button("Generate QR Code"):
        if url and image_name:
            generate_qr_code(url, image_name)
            st.image(f"{image_name}.png", caption="Generated QR Code", use_column_width=True)
        else:
            st.warning("Please enter both a valid URL and image name.")

if __name__ == "__main__":
    main()
