import streamlit as st
import random

st.set_page_config(page_title="Special for Talitha", page_icon="💌", layout="centered")

# 1. State Management yang presisi
if 'font_size' not in st.session_state:
    st.session_state.font_size = 18
if 'width_percent' not in st.session_state:
    st.session_state.width_percent = 45 # Lebar awal tombol MAU (dalam %)
if 'last_msg' not in st.session_state:
    st.session_state.last_msg = ""

# 2. CSS Master: Fokus pada ekspansi horizontal & vertikal
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; overflow-x: hidden; }}
    h1, h3, p {{ color: #ffffff !important; text-align: center; }}
    
    /* Container untuk menjaga kedua tombol tetap satu baris sejauh mungkin */
    div[data-testid="stHorizontalBlock"] {{
        align-items: center !important;
    }}

    /* Tombol MAU: Melebar ke samping & Manjang ke bawah secara brutal */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {{
        font-size: {st.session_state.font_size}px !important;
        width: 100% !important;
        height: {max(60, st.session_state.font_size * 2.2)}px !important;
        background-color: #ff4d6d !important;
        color: white !important;
        border-radius: 20px;
        font-weight: bold;
        transition: 0.2s;
    }}
    
    /* Tombol Gak Mau: Stay in place tapi makin terhimpit */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {{
        background-color: #3d3d3d !important;
        color: #ffffff !important;
        font-size: 14px !important;
        height: 50px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Hai Talitha! ❤️")
st.markdown("### Kamu mau jadi Valentine aku gak? 🌹🍫")

gif_url = "https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd"

# 3. Layout: Gunakan rasio yang berubah drastis
# Col1 akan membesar dari 1 bagian sampai 20 bagian dibanding Col2
col_ratio = st.session_state.width_percent / 10
col1, col2 = st.columns([col_ratio, 1])

with col1:
    if st.button("MAU! 😍"):
        st.balloons()
        st.success("Yeay! Happy Valentine's Day, Talitha! 🍫🌹")
        st.image(gif_url, use_container_width=True)
        st.snow()

with col2:
    # Tombol Gak Mau cuma bisa diklik kalo tombol MAU belum menutupi seluruh layar
    if st.session_state.width_percent < 200:
        if st.button("Gak Mau 😜"):
            st.session_state.font_size += 25   # Tulisan membesar
            st.session_state.width_percent += 40 # Melebar ke samping secara agresif
            
            msgs = [
                "Gak bisa nolak! 😜", "Yakin banget nih? 💔", "Tega banget sih... 🙏",
                "Klik yang 'MAU!' aja ya! ✨", "Aku begadang loh... ☕",
                "Tombol kirinya makin gede, awas ketutup! 🎈"
            ]
            st.session_state.last_msg = random.choice(msgs)
            st.rerun()

if st.session_state.last_msg:
    st.error(st.session_state.last_msg)

st.markdown("<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat oleh Aditya <3 </p>", unsafe_allow_html=True)
