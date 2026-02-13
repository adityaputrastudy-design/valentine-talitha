import streamlit as st
import random

st.set_page_config(page_title="Special for Talitha", page_icon="💌")

# 1. State Management untuk pertumbuhan agresif
if 'font_size' not in st.session_state:
    st.session_state.font_size = 18
if 'padding' not in st.session_state:
    st.session_state.padding = 10
if 'last_msg' not in st.session_state:
    st.session_state.last_msg = ""

# 2. Base CSS dan Animasi
st.markdown(f"""
    <style>
    .stApp {{ 
        background-color: #0e1117; 
        overflow: hidden; 
    }}
    h1, h3, p {{ 
        color: #ffffff !important; 
        text-align: center; 
        transition: 0.3s;
    }}
    
    /* Target tombol MAU agar membesar secara absolut */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {{
        font-size: {st.session_state.font_size}px !important;
        height: {max(60, st.session_state.font_size * 2)}px !important;
        background-color: #ff4d6d !important;
        color: white !important;
        border-radius: 20px;
        width: 100% !important;
        font-weight: bold;
        border: none;
        box-shadow: 0px 0px 50px rgba(255, 77, 109, 0.5);
        transition: all 0.2s ease-in-out;
    }}
    
    /* Tombol Gak Mau tetap kecil */
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

# Direct link Google Drive Anda
gif_url = "https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd"

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("MAU! 😍"):
        st.balloons()
        st.success("Yeay! Happy Valentine's Day, Talitha! 🍫🌹")
        st.image(gif_url, use_container_width=True)
        st.snow()

with col2:
    # Jika tulisan sudah terlalu besar (raksasa), tombol Gak Mau dihilangkan secara otomatis
    if st.session_state.font_size < 350:
        if st.button("Gak Mau 😜"):
            # Pertumbuhan tulisan dan tombol yang sangat masif
            st.session_state.font_size += 30 
            st.session_state.padding += 15
            
            # Daftar pesan yang sangat banyak dan bervariasi
            messages = [
                "Ayo dong, jangan gitu! 🥺", "Yakin banget nih? 💔", 
                "Tega banget sih sama pejuang subuh... 🙏", "Klik yang 'MAU!' aja ya! ✨", 
                "Gak ada tombol 'Gak Mau' di kamus kita hari ini 😜", "Aku udah begadang loh... ☕",
                "Jari kamu kepeleset ya? Coba klik yang kiri ⬅️", "Yah, tombol ini rusak! 🛠️",
                "Error 404: Jawaban 'Gak Mau' tidak ditemukan 🚫", "Duh, hatiku retak dikit... 🔨",
                "Masa cowok sekeren aku ditolak? 😎", "Nanti aku nangis di pojokan... 😭",
                "Tombol kirinya makin gede loh, awas ketutup! 🎈", "Ciee yang ragu-ragu... ❤️",
                "Plis... satu kali ini aja klik yang kiri 🙏", "Ayo deh, kasih kesempatan! 🌹",
                "Gak mau tau, pokoknya harus klik yang 'MAU!' 😤", "Nolak sekali lagi, tombolnya jadi raksasa! 🦖",
                "Tuh kan, makin gede tulisannya... 😱", "Udah deh, menyerah aja dan klik 'MAU!' 😍"
            ]
            st.session_state.last_msg = random.choice(messages)
            st.rerun()

if st.session_state.last_msg:
    st.error(st.session_state.last_msg)

st.markdown("<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat oleh Aditya <3 </p>", unsafe_allow_html=True)
