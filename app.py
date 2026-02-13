import streamlit as st
import random
import time

st.set_page_config(page_title="Special for Tata", page_icon="💌", layout="centered")

if 'size_val' not in st.session_state:
    st.session_state.size_val = 24
if 'msg_val' not in st.session_state:
    st.session_state.msg_val = ""
if 'show_pic' not in st.session_state:
    st.session_state.show_pic = False
if 'reject_count' not in st.session_state:
    st.session_state.reject_count = 0

# CSS yang lebih robust untuk tombol MAU
st.markdown(f"""
    <style>
    .stApp {{ 
        background: linear-gradient(135deg, #0e1117 0%, #1a1f2e 50%, #16213e 100%);
        overflow-x: hidden; 
        min-height: 100vh;
    }}
    
    /* Tombol MAU - pakai class spesifik + key */
    div[data-testid="stButton"] button[kind="primary"][key="mau_btn"] {{
        font-size: {st.session_state.size_val}px !important;
        height: {max(60, st.session_state.size_val * 2.5)}px !important;
        width: {min(95, 40 + st.session_state.reject_count * 8)}vw !important;
        background: linear-gradient(45deg, #ff4d6d, #ff6b9d) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 25px !important;
        border: none !important;
        box-shadow: 0 10px 30px rgba(255,77,109,0.4) !important;
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
        display: block !important;
        margin: 20px auto !important;
        position: relative !important;
        z-index: 999 !important;
    }}
    
    /* Hover effect */
    div[data-testid="stButton"] button[kind="primary"][key="mau_btn"]:hover {{
        transform: scale(1.05) !important;
        box-shadow: 0 20px 40px rgba(255,77,109,0.6) !important;
    }}
    
    /* Tombol Gamau - kecil dan terjepit */
    div[data-testid="stButton"] button[kind="secondary"] {{
        background-color: #3d3d3d !important;
        color: white !important;
        font-size: 16px !important;
        width: 200px !important;
        height: 50px !important;
        margin: 15px auto !important;
        border-radius: 15px !important;
        display: block !important;
    }}
    
    /* GIF container */
    .gif-container {{
        width: 100% !important;
        max-width: 600px !important;
        margin: 0 auto !important;
        border-radius: 20px !important;
        overflow: hidden !important;
        box-shadow: 0 20px 60px rgba(0,0,0,0.5) !important;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("💕 Hai dek Tata sayang ku! 💕")

if st.session_state.show_pic:
    st.balloons()
    st.markdown("## Yeay! Happy Valentine's Day Tata sayang! 🍫🌹✨")
    st.snow()
    
    # GIF dari Google Drive - pastikan linknya benar
    st.markdown("""
    <div class="gif-container">
        <img src="https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd" 
             alt="Valentine GIF" 
             style="width: 100%; height: auto; display: block;">
    </div>
    """, unsafe_allow_html=True)
    
    st.success("Aku sayang banget sama kamu Tata ❤️")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🎈 Ulangi? 🎈", use_container_width=True):
            # Reset semua state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
            
else:
    st.markdown("### Kamu mau gak rayain Valentine sama aku? :D 🌹🍫")
    
    # Tombol MAU (selalu di atas)
    col1, col2 = st.columns([1,1])
    with col1:
        st.empty()  # Spacer
    with col2:
        if st.button("**MAU DONG!** 😍💖", key="mau_btn", use_container_width=True):
            st.session_state.show_pic = True
            st.rerun()

    # Tombol Gamau (di bawah)
    if st.button("**Gamau malas ahh** 🤬😠", key="gak_btn"):
        st.session_state.reject_count += 1
        st.session_state.size_val = 24 + (st.session_state.reject_count * 8)
        messages = [
            f"Loh kok gamau? ({st.session_state.reject_count}x nolak) Tombol MAU nya makin RAKSASA! 😱",
            "Iyain aja yaa sayangg ❤️ Jangan buat mas sedih",
            "Tega banget sih sama mas... Tombolnya udah mau nutup layar nih! 🙏",
            "Ayo dong dek Tata sayang ✨ Coba klik MAU yuk!",
            f"Udah jangan nolak! Liat tuh tombolnya udah gede banget ({st.session_state.size_val}px)!"
        ]
        st.session_state.msg_val = random.choice(messages)
        st.rerun()

# Pesan reject
if st.session_state.msg_val:
    st.error("💥 " + st.session_state.msg_val)

# Footer
st.markdown("""
<div style='text-align: center; padding: 40px; color: #888;'>
    <p style='font-size: 1.1em; margin: 0;'>Made with ❤️ by Aditya</p>
    <p style='font-size: 0.9em;'>Happy Valentine's Day 2026! 💕</p>
</div>
""", unsafe_allow_html=True)
