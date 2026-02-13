import streamlit as st
import random

st.set_page_config(page_title="Special for Talitha", page_icon="💌")

# 1. Inisialisasi state
if 'font_size' not in st.session_state:
    st.session_state.font_size = 18
if 'button_padding' not in st.session_state:
    st.session_state.button_padding = 10
if 'last_msg' not in st.session_state:
    st.session_state.last_msg = ""

# 2. CSS diletakkan di bagian atas agar selalu render nilai terbaru
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; }}
    h1, h3, p {{ color: #ffffff !important; text-align: center; }}
    .mau-btn > button {{
        font-size: {st.session_state.font_size}px !important;
        padding: {st.session_state.button_padding}px !important;
        background-color: #ff4d6d !important;
        color: white !important;
        border-radius: 20px;
        width: 100%;
        font-weight: bold;
    }}
    .gak-btn > button {{
        background-color: #3d3d3d !important;
        color: #ffffff !important;
        border-radius: 20px;
        width: 100%;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Hai Talitha! ❤️")
st.markdown("### Kamu mau jadi Valentine aku gak? 🌹🍫")

gif_url = "https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd"

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="mau-btn">', unsafe_allow_html=True)
    if st.button("MAU! 😍"):
        st.balloons()
        st.success("Yeay! Happy Valentine's Day, Talitha! 🍫🌹")
        st.image(gif_url, use_container_width=True)
        st.snow()
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="gak-btn">', unsafe_allow_html=True)
    if st.button("Gak Mau 😜"):
        # Logika: Update state dulu, baru rerun
        st.session_state.font_size += 15
        st.session_state.button_padding += 8
        
        msgs = [
            "Ayo dong, jangan gitu! 🥺", "Yakin banget nih? 💔", "Tega banget sih... 🙏",
            "Klik yang 'MAU!' aja ya! ✨", "Aku udah begadang loh... ☕",
            "Jari kamu pasti kepeleset ya? ⬅️", "Duh, hatiku retak dikit nih... 🔨"
        ]
        st.session_state.last_msg = random.choice(msgs)
        st.rerun() # Refresh untuk membesarkan tombol
    st.markdown('</div>', unsafe_allow_html=True)

# Tampilkan pesan error di luar blok tombol agar tidak hilang saat rerun
if st.session_state.last_msg:
    st.error(st.session_state.last_msg)

st.markdown("<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat oleh Aditya <3 </p>", unsafe_allow_html=True)
