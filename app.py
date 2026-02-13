import streamlit as st
import random

st.set_page_config(page_title="Special for Tata", page_icon="💌", layout="centered")

# Inisialisasi session state
if 'size_val' not in st.session_state:
    st.session_state.size_val = 24
if 'msg_val' not in st.session_state:
    st.session_state.msg_val = ""
if 'show_pic' not in st.session_state:
    st.session_state.show_pic = False
if 'reject_count' not in st.session_state:
    st.session_state.reject_count = 0

# CSS HACK POWERFUL - Dynamic size
st.markdown(f"""
<style>
.stApp {{ 
    background: linear-gradient(135deg, #0e1117 0%, #1a1f2e 50%, #16213e 100%);
    overflow-x: hidden; 
    min-height: 100vh;
}}

/* MARKER SPACER untuk target MAU button */
#mau-marker + div div button,
#mau-marker ~ div button:first-of-type {{
    font-size: {st.session_state.size_val}px !important;
    height: {max(60, st.session_state.size_val * 2.5)}px !important;
    width: {min(95, 40 + st.session_state.reject_count * 8)}vw !important;
    background: linear-gradient(45deg, #ff4d6d, #ff6b9d) !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 25px !important;
    box-shadow: 0 15px 35px rgba(255,77,109,0.5) !important;
    transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
    margin: 20px auto !important;
    display: block !important;
    position: relative !important;
    z-index: 999 !important;
}}

/* Hover effect */
#mau-marker + div div button:hover,
#mau-marker ~ div button:first-of-type:hover {{
    transform: scale(1.08) !important;
    box-shadow: 0 25px 50px rgba(255,77,109,0.7) !important;
}}

/* TEXT di button (Streamlit nest) */
#mau-marker + div div button > div > div,
#mau-marker + div div button > div > p,
#mau-marker ~ div button > div > div,
#mau-marker ~ div button > div > p {{
    font-size: {st.session_state.size_val}px !important;
    font-weight: bold !important;
    line-height: 1.2 !important;
}}

/* Gamau button - tetap kecil */
div[data-testid="stButton"] button:not(#mau-marker ~ div button:first-of-type) {{
    background-color: #3d3d3d !important;
    color: white !important;
    font-size: 16px !important;
    width: 220px !important;
    height: 50px !important;
    margin: 15px auto !important;
    border-radius: 15px !important;
    display: block !important;
}}

/* GIF Container */
.gif-container {{
    width: 100% !important;
    max-width: 600px !important;
    margin: 20px auto !important;
    border-radius: 25px !important;
    overflow: hidden !important;
    box-shadow: 0 25px 60px rgba(0,0,0,0.6) !important;
}}
</style>
""", unsafe_allow_html=True)

st.title("💕 Hai dek Tata sayang ku! 💕")

if st.session_state.show_pic:
    st.balloons()
    st.markdown("## 🎉 Yeay! Happy Valentine's Day Tata sayang! 🍫🌹✨")
    
    # GIF Google Drive - auto play
    st.markdown(f"""
    <div class="gif-container">
        <img src="https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd" 
             alt="Valentine Love GIF" 
             style="width: 100%; height: auto; display: block; animation: bounce 2s infinite;">
    </div>
    """, unsafe_allow_html=True)
    
    st.snow()
    st.success("💖 Aku sayang banget sama kamu Tata ❤️")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎈 Main Lagi? 🎈", use_container_width=True):
            # Reset semua
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
            
else:
    st.markdown("### Kamu mau gak rayain Valentine sama aku? 😍🌹🍫")
    
    # MARKER HACK untuk CSS target
    st.markdown('<span id="mau-marker" style="display:none;"></span>', unsafe_allow_html=True)
    
    # Tombol MAU - SEKARANG bakal Gede!
    if st.button("**MAU DONG!** 😍💖", key="mau_btn", use_container_width=True):
        st.session_state.show_pic = True
        st.rerun()

    # Tombol Gamau
    if st.button("**Gamau malas ahh** 🤬😠", key="gak_btn"):
        st.session_state.reject_count += 1
        st.session_state.size_val += 12  # Naik agresif
        messages = [
            f"😱 Loh kok gamau? ({st.session_state.reject_count}x nolak!) Tombol MAU makin RAKSASA!",
            "💔 Iyain aja yaa sayangg ❤️ Jangan buat mas sedih",
            f"Tombolnya udah {st.session_state.size_val}px! Mau nutup layar nih! 🙏",
            "✨ Ayo dong dek Tata sayang, klik MAU yuk!",
            f"Reject #{st.session_state.reject_count} - LIAT TUH GEDE BANGET! 😤"
        ]
        st.session_state.msg_val = random.choice(messages)
        st.rerun()

# Pesan reject
if st.session_state.msg_val:
    st.error("💥 " + st.session_state.msg_val)

# Footer cantik
st.markdown("""
<div style='text-align: center; padding: 40px; color: #aaa; font-family: "Segoe UI", sans-serif;'>
    <p style='font-size: 1.2em; margin: 0; color: #ff6b9d;'>Made with ❤️ by Aditya</p>
    <p style='font-size: 0.95em;'>Happy Valentine's Day 2026! 💕</p>
</div>
""", unsafe_allow_html=True)
