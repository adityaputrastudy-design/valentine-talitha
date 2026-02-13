import streamlit as st
import random

st.set_page_config(page_title="Special for Talitha", page_icon="💌")

# 1. Inisialisasi ukuran tombol di session state
if 'font_size' not in st.session_state:
    st.session_state.font_size = 18
if 'button_padding' not in st.session_state:
    st.session_state.button_padding = 10

# 2. CSS dinamis yang mengambil nilai dari session state
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; }}
    h1, h3, p {{ color: #ffffff !important; text-align: center; }}
    
    /* Tombol MAU yang ukurannya dinamis */
    .mau-btn > button {{
        font-size: {st.session_state.font_size}px !important;
        padding: {st.session_state.button_padding}px !important;
        background-color: #ff4d6d !important;
        color: white !important;
        border-radius: 20px;
        width: 100%;
        font-weight: bold;
        transition: 0.3s;
    }}
    
    /* Tombol Gak Mau tetap kecil */
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

# Link Direct dari Google Drive lo
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
        # 3. Logika penambahan ukuran secara drastis
        st.session_state.font_size += 15 
        st.session_state.button_padding += 8
        
        messages = [
            "Ayo dong, jangan gitu! 🥺",
            "Yakin banget nih? Gak nyesel? 💔",
            "Tega banget sih sama pejuang subuh... 🙏",
            "Klik yang 'MAU!' aja ya, jangan yang ini! ✨",
            "Gak ada tombol 'Gak Mau' di kamus kita hari ini 😜",
            "Aku udah begadang loh buat bikin ini... ☕",
            "Jari kamu pasti kepeleset ya? Coba klik yang kiri ⬅️",
            "Yah, tombol ini lagi rusak, coba klik yang 'MAU!' 🛠️",
            "Duh, hatiku retak dikit nih pas kamu klik ini... 🔨",
            "Pokoknya harus klik yang 'MAU!' 😤",
            "Plis... satu kali ini aja klik yang kiri 🙏",
            "Ciee yang ragu-ragu... klik 'MAU!' aja udah! 🌹"
        ]
        st.error(random.choice(messages))
        
        # 4. Paksa Streamlit untuk menggambar ulang halaman
        st.rerun() 
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat oleh Aditya <3 </p>", unsafe_allow_html=True)
