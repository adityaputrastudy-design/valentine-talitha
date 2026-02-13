import streamlit as st
import random

st.set_page_config(page_title="Special for Tata", page_icon="💌", layout="wide")

# 1. State Management
if 'size_val' not in st.session_state:
    st.session_state.size_val = 20
if 'msg_val' not in st.session_state:
    st.session_state.msg_val = ""
if 'show_celebration' not in st.session_state:
    st.session_state.show_celebration = False

# 2. CSS Master (Anti-Gagal)
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; overflow-x: hidden; }}
    
    /* Tombol MAU: Maksa melebar ke samping dan manjang ke bawah */
    div[data-testid="column"]:nth-child(1) div[data-testid="stButton"] button {{
        font-size: {st.session_state.size_val}px !important;
        height: {st.session_state.size_val * 2.8}px !important;
        width: 100% !important;
        background-color: #ff4d6d !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        transition: 0.1s;
    }}
    
    /* Tombol Gamau: Stay small */
    div[data-testid="column"]:nth-child(2) div[data-testid="stButton"] button {{
        background-color: #3d3d3d !important;
        color: white !important;
        font-size: 14px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Hai dek tata sayang ku, cinta ku, dunia ku, istri ku, pacar ku, semua-semua nya! ❤️")

if st.session_state.show_celebration:
    st.balloons()
    st.success("Yeay! Happy Valentine's Day Tata sayang! 🍫🌹")
    # MENGGUNAKAN LINK GAMBAR STABIL (Contoh: Direct Link Imgur/Discord)
    # Ganti link di bawah ini dengan direct link .gif lo yang sudah di-upload ke Imgur/Discord jika link Drive tetap mati
    st.image("https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd", caption="Happy Valentine's Day! ✨", use_container_width=True)
    st.snow()
    if st.button("Ulangi dari awal?"):
        st.session_state.show_celebration = False
        st.session_state.size_val = 20
        st.rerun()
else:
    st.markdown("### Kamu mau gak rayain valentine sama aku :D ? 🌹🍫")

    # 3. Layout: Col 1 akan semakin dominan
    c1, c2 = st.columns([st.session_state.size_val, 20])

    with c1:
        if st.button("MAU DONG! 😍"):
            st.session_state.show_celebration = True
            st.rerun()

    with c2:
        if st.button("Gamau malas ahh 🤬😠"):
            st.session_state.size_val += 70  # Pertumbuhan drastis
            messages = [
                "Loh kok gamau? Nolak = Tombol MAU nya makin gede loh!",
                "Iyain aja yaa sayangg, jangan males-malesan hehe ❤️",
                "Tega banget sih sama mas... klik MAU aja pleasee! 🙏",
                "Ayo dong dek tata sayang, sekali klik aja tombol MAU nya ✨"
            ]
            st.session_state.msg_val = random.choice(messages)
            st.rerun()

    if st.session_state.msg_val:
        st.error(st.session_state.msg_val)

st.markdown("<p style='text-align: center; font-size: 0.8em; color: #555;'>Dibuat oleh Aditya <3 </p>", unsafe_allow_html=True)
