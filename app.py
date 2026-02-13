import streamlit as st
import random

st.set_page_config(page_title="Special for Tata", page_icon="💌", layout="centered")

if 'size_val' not in st.session_state:
    st.session_state.size_val = 18
if 'msg_val' not in st.session_state:
    st.session_state.msg_val = ""
if 'show_pic' not in st.session_state:
    st.session_state.show_pic = False

# CSS MASTER: Tombol MAU bakal nutupin apa pun di bawahnya
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; overflow-x: hidden; }}
    
    /* Tombol MAU: Melebar dan Menutup */
    .mau-btn-container {{
        position: relative;
        z-index: 999;
    }}
    .mau-btn-container button {{
        font-size: {st.session_state.size_val}px !important;
        height: {st.session_state.size_val * 2.5}px !important;
        width: {min(100, 40 + st.session_state.size_val/2)}% !important;
        background-color: #ff4d6d !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 20px;
        transition: 0.3s;
    }}
    
    /* Tombol Gamau: Stay di tempat */
    .gak-btn-container button {{
        background-color: #3d3d3d !important;
        color: white !important;
        font-size: 14px !important;
        width: 100% !important;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Hai dek tata sayang ku! ❤️")

if st.session_state.show_pic:
    st.balloons()
    st.success("Yeay! Happy Valentine's Day Tata sayang! 🍫🌹")
    # Pake link placeholder stabil dulu buat ngetes
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueW92Ynk1bmZ4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTfuxV6m6z2A0M/giphy.gif", use_container_width=True)
    st.snow()
    if st.button("Ulangi?"):
        st.session_state.show_pic = False
        st.session_state.size_val = 18
        st.rerun()
else:
    st.markdown("### Kamu mau gak rayain valentine sama aku :D ? 🌹🍫")
    
    # Pake container biasa, jangan columns biar gak penyet
    st.markdown('<div class="mau-btn-container">', unsafe_allow_html=True)
    if st.button("MAU DONG! 😍", key="mau_btn"):
        st.session_state.show_pic = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="gak-btn-container">', unsafe_allow_html=True)
    if st.button("Gamau malas ahh 🤬😠", key="gak_btn"):
        st.session_state.size_val += 40
        messages = [
            "Loh kok gamau? Nolak = Tombol MAU nya makin gede loh!",
            "Iyain aja yaa sayangg ❤️",
            "Tega banget sih sama mas... 🙏",
            "Ayo dong dek tata sayang ✨"
        ]
        st.session_state.msg_val = random.choice(messages)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.msg_val:
    st.error(st.session_state.msg_val)
