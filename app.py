import streamlit as st
import random

st.set_page_config(page_title="Special for Talitha", page_icon="💌")

# 1. State Management
if 'font_size' not in st.session_state:
    st.session_state.font_size = 18
if 'padding' not in st.session_state:
    st.session_state.padding = 10
if 'last_msg' not in st.session_state:
    st.session_state.last_msg = ""

# 2. Base CSS
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h3, p { color: #ffffff !important; text-align: center; }
    .stButton>button { width: 100%; border-radius: 20px; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("Hai Talitha! ❤️")
st.markdown("### Kamu mau jadi Valentine aku gak? 🌹🍫")

gif_url = "https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd"

# 3. Suntikan CSS Dinamis untuk Tombol MAU
st.markdown(f"""
    <style>
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {{
        font-size: {st.session_state.font_size}px !important;
        padding: {st.session_state.padding}px !important;
        background-color: #ff4d6d !important;
        color: white !important;
    }}
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {{
        background-color: #3d3d3d !important;
        color: white !important;
    }}
    </style>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("MAU! 😍"):
        st.balloons()
        st.success("Yeay! Happy Valentine's Day, Talitha! 🍫🌹")
        st.image(gif_url, use_container_width=True)
        st.snow()

with col2:
    if st.button("Gak Mau 😜"):
        # Penambahan ukuran yang sangat drastis agar langsung terasa
        st.session_state.font_size += 20 
        st.session_state.padding += 10
        
        msgs = [
            "Ayo dong, jangan gitu! 🥺", "Yakin banget nih? 💔", 
            "Klik yang 'MAU!' aja ya! ✨", "Aku udah begadang loh... ☕",
            "Tombol kirinya bakal terus membesar loh! 🎈"
        ]
        st.session_state.last_msg = random.choice(msgs)
        st.rerun()

if st.session_state.last_msg:
    st.error(st.session_state.last_msg)

st.markdown(f"<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat oleh Aditya <3 </p>", unsafe_allow_html=True)
