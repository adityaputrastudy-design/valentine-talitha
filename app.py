import streamlit as st
import random

st.set_page_config(page_title="Special for Talitha", page_icon="💌", layout="wide")

# Gunakan kunci (key) unik agar session state segar kembali
if 'size_val' not in st.session_state:
    st.session_state.size_val = 20
if 'msg_val' not in st.session_state:
    st.session_state.msg_val = ""

# CSS dengan selektor paling kuat (!important)
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; }}
    
    /* Memaksa tombol MAU membesar secara horizontal dan vertikal */
    div[data-testid="column"]:nth-child(1) button {{
        font-size: {st.session_state.size_val}px !important;
        height: {st.session_state.size_val * 2.5}px !important;
        width: 100% !important;
        background-color: #ff4d6d !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
    }}
    
    /* Tombol Gak Mau tetap kecil */
    div[data-testid="column"]:nth-child(2) button {{
        background-color: #3d3d3d !important;
        color: white !important;
        font-size: 14px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Hai dek tata sayang ku, cinta ku, dunia ku, istri ku, pacar ku, semua-semua nya! ❤️")
st.markdown("### Kamu mau gak rayain valentine sama aku :D ? 🌹🍫")

# Gunakan rasio kolom yang sangat kontras
c1, c2 = st.columns([st.session_state.size_val, 20])

with c1:
    if st.button("MAU DONG! "):
        st.balloons()
        st.success("Yeay! Happy Valentine's Day! 🍫🌹")
        st.image("https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd", use_container_width=True)
        st.snow()

with c2:
    if st.button("Gamau malas ahh 🥹 "):
        st.session_state.size_val += 40  # Penambahan sangat masif
        messages = ["Nolak = Tombol MAU nya makin gede", "Iyain aja yaa sayangg!", "Udah lah dek klik MAU aja"]
        st.session_state.msg_val = random.choice(messages)
        st.rerun()

if st.session_state.msg_val:
    st.error(st.session_state.msg_val)
