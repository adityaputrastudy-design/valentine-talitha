import streamlit as st
import random

st.set_page_config(page_title="Special for Tata", page_icon="💌", layout="wide")

# 1. State Management
if 'size_val' not in st.session_state:
    st.session_state.size_val = 20
if 'msg_val' not in st.session_state:
    st.session_state.msg_val = ""

# 2. CSS Master (Anti-Gagal)
# Gua tambahin selektor 'div[data-testid="stButton"]' biar gak bisa ngeles lagi
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; overflow-x: hidden; }}
    
    /* Tombol MAU: Melebar, Memanjang, dan Teks Membesar */
    div[data-testid="column"]:nth-child(1) div[data-testid="stButton"] button {{
        font-size: {st.session_state.size_val}px !important;
        height: {st.session_state.size_val * 2.5}px !important;
        width: 100% !important;
        background-color: #ff4d6d !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        transition: 0.2s;
    }}
    
    /* Tombol Gamau: Stay small */
    div[data-testid="column"]:nth-child(2) div[data-testid="stButton"] button {{
        background-color: #3d3d3d !important;
        color: white !important;
        font-size: 14px !important;
        height: 50px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Hai dek tata sayang ku, cinta ku, dunia ku, istri ku, pacar ku, semua-semua nya! ❤️")
st.markdown("### Kamu mau gak rayain valentine sama aku :D ? 🌹🍫")

# 3. Layout dengan rasio kolom yang dinamis
# Col1 (MAU) akan makan ruang Col2 (Gamau) secara horizontal
c1, c2 = st.columns([st.session_state.size_val, 20])

with c1:
    if st.button("MAU DONG! 😍"):
        st.balloons()
        st.success("Yeay! Happy Valentine's Day Tata sayang! 🍫🌹")
        st.image("https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd", use_container_width=True)
        st.snow()

with c2:
    if st.button("Gamau malas ahh 🥹"):
        st.session_state.size_val += 45  # Gua naikin biar pertumbuhannya gila
        
        # Message Natural ala lo
        messages = [
            "Loh kok gamau? Nolak = Tombol MAU nya makin gede loh!",
            "Iyain aja yaa sayangg, jangan males-malesan hehe ❤️",
            "Udah lah dek klik MAU aja, capek loh ngetik pesannya 😋",
            "Tega banget sih sama mas... klik MAU aja pleasee! 🙏",
            "Gak ada pilihan lain lah sayang, klik mau aja yaa!",
            "Ayo dong dek tata sayang, sekali klik aja tombol MAU nya ✨"
        ]
        st.session_state.msg_val = random.choice(messages)
        st.rerun()

if st.session_state.msg_val:
    st.error(st.session_state.msg_val)

st.markdown("<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat oleh Aditya <3 </p>", unsafe_allow_html=True)
