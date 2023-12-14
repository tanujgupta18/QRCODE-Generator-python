import streamlit as st
import qrcode as qr

def generate_qr_code(url):
    img = qr.make(url, version=10)  # You can adjust the version/size as needed
    img.save("Generated_QR_Code.png")

def main():
    st.title("QR Code Generator")

    url = st.text_input("Enter the URL:")

    if st.button("Generate QR Code"):
        if url:
            generate_qr_code(url)
            st.image("Generated_QR_Code.png", caption="Generated QR Code", use_column_width=True)
        else:
            st.warning("Please enter a valid URL.")

if __name__ == "__main__":
    main()
