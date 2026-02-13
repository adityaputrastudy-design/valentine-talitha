import streamlit as st
import random
import os

st.set_page_config(page_title="Special Message", page_icon="💌")

# CSS untuk Dark Mode
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2, h3, p, span, label { color: #ffffff !important; }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3.5em;
        background-color: #ff4d6d;
        color: white !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Hai Talitha! ❤️")
st.markdown("### Kamu mau jadi Valentine aku gak? 🌹🍫")

# PERBAIKAN: Gunakan nama file saja, jangan path C:\Users\...
gif_path = "valentine.gif"

col1, col2 = st.columns(2)

with col1:
    if st.button("MAU!"):
        st.balloons()
        st.success("Yeay! Sampai ketemu nanti! 🍫🌹")
        
        # Cek apakah file ada di folder GitHub
        if os.path.exists(gif_path):
            st.image(gif_path, caption="Happy Valentine's Day! ✨", use_container_width=True)
        else:
            st.error("File valentine.gif belum terdeteksi di GitHub!")

with col2:
    if st.button("Gak Mau"):
        messages = [
            "Ayo dong, jangan gitu! 🥺", 
            "Yakin banget nih?", 
            "Coba pikir lagi...", 
            "Tega banget sih...",
            "Klik yang 'MAU!' aja ya!"
        ]
        st.error(random.choice(messages))
