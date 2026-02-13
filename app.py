import streamlit as st
import random

# Konfigurasi halaman
st.set_page_config(page_title="Special for Talitha", page_icon="💌")

# CSS untuk tampilan Dark Mode yang elegan
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    h1, h3, p {
        color: #ffffff !important;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3.5em;
        background-color: #ff4d6d;
        color: white !important;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Hai Talitha! ❤️")
st.markdown("### Kamu mau jadi Valentine aku gak? 🌹🍫")

# Link Direct dari Google Drive lo
gif_url = "https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd"

col1, col2 = st.columns(2)

with col1:
    if st.button("MAU! 😍"):
        st.balloons()
        st.success("Yeay! Happy Valentine's Day, Talitha! 🍫🌹")
        # Menampilkan GIF dari link Google Drive
        st.image(gif_url, caption="Happy Valentine's Day! ✨", use_container_width=True)
        st.snow()

with col2:
    if st.button("Gak Mau 😜"):
        messages = [
            "Coba pikir lagi... 🥺", 
            "Yakin banget nih? 💔", 
            "Tega banget sih... 🙏",
            "Klik yang MAU aja ya! ✨"
        ]
        st.error(random.choice(messages))

st.markdown("<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat sama Aditya</p>", unsafe_allow_html=True)
