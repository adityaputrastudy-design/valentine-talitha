import streamlit as st
import random

st.set_page_config(page_title="Special for Talitha", page_icon="💌", layout="centered")

# 1. State Management untuk ekspansi brutal
if 'size' not in st.session_state:
    st.session_state.size = 100 # Ukuran lebar dasar dalam persen

# 2. CSS untuk memaksa tombol MAU menelan layar
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; overflow: hidden; }}
    h1, h3, p {{ color: #ffffff !important; text-align: center; }}
    
    /* Tombol Gak Mau: Stay in place */
    .gak-container {{
        position: relative;
        z-index: 1;
    }}
    .gak-btn > button {{
        background-color: #3d3d3d !important;
        color: white !important;
        width: 100%;
        border-radius: 20px;
    }}

    /* Tombol MAU: Melebar, Memanjang, dan Menutup */
    .mau-container {{
        position: relative;
        z-index: {st.session_state.size}; /* Semakin gede, semakin di depan */
    }}
    .mau-btn > button {{
        width: {st.session_state.size}% !important; /* Melebar ke samping */
        height: {st.session_state.size * 0.8}px !important; /* Memanjang ke bawah */
        font-size: {st.session_state.size / 4}px !important; /* Tulisan ikut membesar */
        background-color: #ff4d6d !important;
        color: white !important;
        border-radius: 20px;
        font-weight: bold;
        transition: all 0.3s ease;
        white-space: nowrap;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Hai Talitha! ❤️")
st.markdown("### Kamu mau jadi Valentine aku gak? 🌹🍫")

gif_url = "https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd"

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="mau-container mau-btn">', unsafe_allow_html=True)
    if st.button("MAU! 😍"):
        st.balloons()
        st.success("Yeay! Happy Valentine's Day, Talitha! 🍫🌹")
        st.image(gif_url, use_container_width=True)
        st.snow()
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="gak-container gak-btn">', unsafe_allow_html=True)
    if st.button("Gak Mau 😜"):
        # Penambahan ukuran yang jauh lebih brutal
        st.session_state.size += 60 
        
        messages = [
            "Gak bisa nolak! 😜", "Ayo klik yang kiri!", "Makin gede loh!",
            "Tega banget sih...", "Error: Tombol nolak hilang sebentar lagi!"
        ]
        st.error(random.choice(messages))
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat oleh Aditya <3 </p>", unsafe_allow_html=True)
