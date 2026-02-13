import streamlit as st
import random

st.set_page_config(page_title="Special for Tata", page_icon="💌", layout="centered")

if 'size_val' not in st.session_state:
    st.session_state.size_val = 20
if 'msg_val' not in st.session_state:
    st.session_state.msg_val = ""
if 'show_pic' not in st.session_state:
    st.session_state.show_pic = False

# CSS MASTER: Memaksa tombol MAU menginvasi layar secara horizontal & vertikal
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; overflow-x: hidden; }}
    
    /* Target tombol MAU secara spesifik menggunakan key */
    div[data-testid="stButton"]:has(button:contains("MAU DONG!")) button {{
        font-size: {st.session_state.size_val}px !important;
        height: {st.session_state.size_val * 2}px !important;
        width: {min(100, 30 + st.session_state.size_val)}% !important; /* Paksa melebar ke samping */
        background-color: #ff4d6d !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 20px;
        transition: 0.2s ease-in-out;
        display: block !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }}
    
    /* Tombol Gamau tetap kecil agar terjepit */
    div[data-testid="stButton"]:has(button:contains("Gamau malas ahh")) button {{
        background-color: #3d3d3d !important;
        color: white !important;
        font-size: 14px !important;
        width: auto !important;
        margin: 10px auto !important;
        display: block !important;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Hai dek tata sayang ku! ❤️")

if st.session_state.show_pic:
    st.balloons()
    st.success("Yeay! Happy Valentine's Day Tata sayang! 🍫🌹")
    # Pake link Google Drive lo lagi, kita coba panggil di container bersih
    st.image("https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd", use_container_width=True)
    st.snow()
    if st.button("Ulangi?"):
        st.session_state.show_pic = False
        st.session_state.size_val = 20
        st.rerun()
else:
    st.markdown("### Kamu mau gak rayain valentine sama aku :D ? 🌹🍫")
    
    # Tombol MAU diletakkan paling atas
    if st.button("MAU DONG! 😍", key="mau_btn"):
        st.session_state.show_pic = True
        st.rerun()

    # Tombol Gamau diletakkan di bawahnya
    if st.button("Gamau malas ahh 🤬😠", key="gak_btn"):
        st.session_state.size_val += 60 # Pertumbuhan horizontal dan vertikal
        messages = [
            "Loh kok gamau? Nolak = Tombol MAU nya makin raksasa loh!",
            "Iyain aja yaa sayangg ❤️",
            "Tega banget sih sama mas... 🙏",
            "Ayo dong dek tata sayang ✨",
            "Udah jangan nolak, liat tuh tombolnya udah mau nutupin layar!"
        ]
        st.session_state.msg_val = random.choice(messages)
        st.rerun()

if st.session_state.msg_val:
    st.error(st.session_state.msg_val)

st.markdown("<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat oleh Aditya <3 </p>", unsafe_allow_html=True)
