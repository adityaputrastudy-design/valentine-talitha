import streamlit as st
import random

st.set_page_config(page_title="Special for Talitha", page_icon="💌", layout="wide")

# 1. State Management untuk pertumbuhan raksasa
if 'font_size' not in st.session_state:
    st.session_state.font_size = 18
if 'btn_width' not in st.session_state:
    st.session_state.btn_width = 1  # Rasio lebar kolom

# 2. CSS untuk memaksa teks dan kotak membesar
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; overflow: hidden; }}
    h1, h3, p {{ color: #ffffff !important; text-align: center; }}
    
    /* Target tombol MAU: teks ikut membesar & tombol memenuhi container */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {{
        font-size: {st.session_state.font_size}px !important;
        height: {max(60, st.session_state.font_size * 2.5)}px !important;
        width: 100% !important;
        background-color: #ff4d6d !important;
        color: white !important;
        border-radius: 20px;
        font-weight: bold;
        border: none;
        box-shadow: 0px 0px 50px rgba(255, 77, 109, 0.6);
    }}
    
    /* Tombol Gak Mau */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {{
        background-color: #3d3d3d !important;
        color: #ffffff !important;
        font-size: 14px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Hai Talitha! ❤️")
st.markdown("### Kamu mau jadi Valentine aku gak? 🌹🍫")

gif_url = "https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd"

# 3. Kolom Dinamis: Semakin nolak, col1 (MAU) semakin lebar dibanding col2 (Gak Mau)
col1, col2 = st.columns([st.session_state.btn_width, 1])

with col1:
    if st.button("MAU! 😍"):
        st.balloons()
        st.success("Yeay! Happy Valentine's Day, Talitha! 🍫🌹")
        st.image(gif_url, use_container_width=True)
        st.snow()

with col2:
    # Jika sudah sangat lebar, tombol Gak Mau menghilang
    if st.session_state.btn_width < 15:
        if st.button("Gak Mau 😜"):
            st.session_state.font_size += 35   # Tulisan membesar drastis
            st.session_state.btn_width += 3    # Tombol melebar ke samping
            
            messages = [
                "Ayo dong, jangan gitu! 🥺", "Yakin banget nih? 💔", 
                "Tega banget sih... 🙏", "Klik yang 'MAU!' aja ya! ✨", 
                "Gak ada tombol 'Gak Mau' hari ini 😜", "Aku udah begadang loh... ☕",
                "Tombol kirinya makin gede, awas ketutup! 🎈", "Udah menyerah aja! 😍",
                "Ciee yang ragu-ragu... ❤️", "Error: Jawaban ditolak! 🚫",
                "Hatiku retak dikit nih... 🔨", "Pokoknya harus klik MAU! 😤"
            ]
            st.error(random.choice(messages))
            st.rerun()

st.markdown("<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat oleh Aditya <3 </p>", unsafe_allow_html=True)
