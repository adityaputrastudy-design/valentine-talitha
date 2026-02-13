import streamlit as st
import random

st.set_page_config(page_title="Special for Talitha", page_icon="💌", layout="centered")

# 1. Inisialisasi state untuk ukuran dan rasio kolom
if 'font_size' not in st.session_state:
    st.session_state.font_size = 18
if 'col_ratio' not in st.session_state:
    st.session_state.col_ratio = 1.0  # Rasio awal seimbang
if 'last_msg' not in st.session_state:
    st.session_state.last_msg = ""

# 2. CSS Dinamis: Mengatur tinggi tombol dan ukuran teks secara proporsional
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; overflow: hidden; }}
    h1, h3, p {{ color: #ffffff !important; text-align: center; }}
    
    /* Style Tombol MAU: Melebar & Memanjang otomatis mengikuti kolom */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {{
        font-size: {st.session_state.font_size}px !important;
        height: {max(60, st.session_state.font_size * 2)}px !important;
        background-color: #ff4d6d !important;
        color: white !important;
        border-radius: 20px;
        width: 100% !important;
        font-weight: bold;
        border: none;
        transition: 0.3s ease;
    }}
    
    /* Style Tombol Gak Mau: Tetap kecil di areanya */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {{
        background-color: #3d3d3d !important;
        color: #ffffff !important;
        border-radius: 20px;
        font-size: 14px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Hai Talitha! ❤️")
st.markdown("### Kamu mau jadi Valentine aku gak? 🌹🍫")

gif_url = "https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd"

# 3. Layout Kolom Dinamis: col1 akan semakin lebar menjepit col2
col1, col2 = st.columns([st.session_state.col_ratio, 1])

with col1:
    if st.button("MAU! 😍"):
        st.balloons()
        st.success("Yeay! Happy Valentine's Day, Talitha! 🍫🌹")
        st.image(gif_url, use_container_width=True)
        st.snow()

with col2:
    # Tombol Gak Mau akan hilang jika sudah terjepit habis
    if st.session_state.col_ratio < 10:
        if st.button("Gak Mau 😜"):
            # Pertumbuhan agresif ke samping dan teks
            st.session_state.font_size += 25
            st.session_state.col_ratio += 2.0  # Menambah lebar kolom ke samping
            
            messages = [
                "Ayo dong, jangan gitu! 🥺", "Yakin banget nih? 💔", 
                "Tega banget sih... 🙏", "Klik yang 'MAU!' aja ya! ✨", 
                "Gak ada tombol 'Gak Mau' hari ini 😜", "Aku begadang loh buat ini... ☕",
                "Tombol kirinya makin gede, awas ketutup! 🎈"
            ]
            st.session_state.last_msg = random.choice(messages)
            st.rerun()

if st.session_state.last_msg:
    st.error(st.session_state.last_msg)

st.markdown("<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat oleh Aditya <3 </p>", unsafe_allow_html=True)
