import streamlit as st
import random

st.set_page_config(page_title="Special for Talitha", page_icon="💌")

# Inisialisasi ukuran tombol di session state
if 'font_size' not in st.session_state:
    st.session_state.font_size = 18
if 'button_padding' not in st.session_state:
    st.session_state.button_padding = 10

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

# Link Direct dari Google Drive lo (Pastikan ID ini benar)
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
        # Tambah ukuran tombol MAU setiap kali Gak Mau diklik
        st.session_state.font_size += 10
        st.session_state.button_padding += 5
        
        messages = [
            "Ayo dong, jangan gitu! 🥺", "Yakin banget nih? 💔", "Tega banget sih... 🙏",
            "Klik yang 'MAU!' aja ya! ✨", "Gak ada tombol 'Gak Mau' hari ini 😜",
            "Aku begadang loh buat ini... ☕", "Jari kamu kepeleset ya? ⬅️",
            "Tombol ini rusak, klik yang kiri! 🛠️", "Error: Jawaban tidak ditemukan 🚫",
            "Hatiku retak dikit nih... 🔨", "Masa cowok sekeren aku ditolak? 😎",
            "Nanti aku nangis di pojokan... 😭", "Pokoknya harus klik MAU! 😤",
            "Kalo klik ini lagi, tombol makin gede! 🎈", "Ciee yang ragu-ragu... ❤️"
        ]
        st.error(random.choice(messages))
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat dengan begadang oleh Aditya</p>", unsafe_allow_html=True)
