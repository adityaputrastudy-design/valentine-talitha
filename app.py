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
           "Ayo dong, jangan gitu! 🥺",
            "Yakin banget nih? Gak nyesel? 💔",
            "Tega banget sih sama pejuang subuh... 🙏",
            "Klik yang 'MAU!' aja ya, jangan yang ini! ✨",
            "Gak ada tombol 'Gak Mau' di kamus kita hari ini 😜",
            "Aku udah begadang loh buat bikin ini... ☕",
            "Jari kamu pasti kepeleset ya? Coba klik yang kiri ⬅️",
            "Yah, tombol ini lagi rusak, coba klik yang 'MAU!' 🛠️",
            "Error 404: Jawaban 'Gak Mau' tidak ditemukan 🚫",
            "Duh, hatiku retak dikit nih pas kamu klik ini... 🔨",
            "Pikirkan lagi, masa cowok sekeren aku ditolak? 😎",
            "Nanti aku nangis di pojokan loh... 😭",
            "Kamu cuma ngetes kesabaran aku kan? 😇",
            "Gak mau tau, pokoknya harus klik yang 'MAU!' 😤",
            "Plis... satu kali ini aja klik yang kiri 🙏",
            "Kalo kamu klik ini lagi, nanti aku kirim spam balon! 🎈",
            "Ciee yang ragu-ragu... klik 'MAU!' aja udah! 🌹"
        ]
        st.error(random.choice(messages))

st.markdown("<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat sama Adit <3</p>", unsafe_allow_html=True)
