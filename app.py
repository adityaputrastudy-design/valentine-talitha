import streamlit as st
import random

st.set_page_config(page_title="Special for Talitha", page_icon="💌")

# 1. State Management untuk ukuran yang terus bertambah
if 'font_size' not in st.session_state:
    st.session_state.font_size = 18
if 'padding' not in st.session_state:
    st.session_state.padding = 10
if 'last_msg' not in st.session_state:
    st.session_state.last_msg = ""

# 2. Base CSS untuk layout
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; overflow-x: hidden; }
    h1, h3, p { color: #ffffff !important; text-align: center; }
    .stButton>button { width: 100%; border-radius: 20px; font-weight: bold; border: none; transition: all 0.2s ease-in-out; }
    </style>
    """, unsafe_allow_html=True)

st.title("Hai Talitha! ❤️")
st.markdown("### Kamu mau jadi Valentine aku gak? 🌹🍫")

# Link Direct dari Google Drive lo
gif_url = "https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd"

# 3. Suntikan CSS Dinamis untuk memaksa ukuran tulisan & tombol
st.markdown(f"""
    <style>
    /* Menargetkan tombol MAU di kolom pertama */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {{
        font-size: {st.session_state.font_size}px !important;
        height: auto !important;
        min-height: {st.session_state.padding * 4}px !important;
        background-color: #ff4d6d !important;
        color: white !important;
        z-index: 999; /* Memastikan dia di atas elemen lain */
    }}
    /* Menargetkan tombol Gak Mau di kolom kedua */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {{
        background-color: #3d3d3d !important;
        color: white !important;
        font-size: 14px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("MAU! 😍"):
        st.balloons()
        st.success("Yeay! Happy Valentine's Day, Talitha! 🍫🌹")
        st.image(gif_url, use_container_width=True)
        st.snow()

with col2:
    # Jika ukuran sudah terlalu besar, kita hilangkan tombol Gak Mau secara visual
    if st.session_state.font_size < 200: 
        if st.button("Gak Mau 😜"):
            # Penambahan ukuran yang sangat agresif
            st.session_state.font_size += 25 
            st.session_state.padding += 15
            
            msgs = [
                "Ayo dong, jangan gitu! 🥺", 
                "Yakin banget nih? 💔", 
                "Tombol kirinya makin gede loh! ✨", 
                "Gak ada jalan keluar selain klik MAU! 😜"
            ]
            st.session_state.last_msg = random.choice(msgs)
            st.rerun()

if st.session_state.last_msg:
    st.error(st.session_state.last_msg)

st.markdown(f"<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat oleh Aditya <3 </p>", unsafe_allow_html=True)
