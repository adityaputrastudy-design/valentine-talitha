import streamlit as st
import random

st.set_page_config(page_title="Special for Tata", page_icon="💌", layout="centered")

# 1. State Management
if 'size_val' not in st.session_state: st.session_state.size_val = 24
if 'msg_val' not in st.session_state: st.session_state.msg_val = ""
if 'show_pic' not in st.session_state: st.session_state.show_pic = False
if 'reject_count' not in st.session_state: st.session_state.reject_count = 0

# 2. CSS MASTER - SATU CSS UNTUK SEMUA (Spesifik banget!)
st.markdown(f"""
<style>
/* Background */
.stApp {{ 
    background: linear-gradient(135deg, #0e1117 0%, #1a1f2e 50%, #16213e 100%);
    min-height: 100vh;
}}

/* MARKER untuk target tombol MAU */
.mau-marker + div [data-testid="stButton"][key="mau_btn_1"] button,
div[data-testid="stButton"][key="mau_btn_1"] button {{
    font-size: {st.session_state.size_val}px !important;
    height: {max(80, st.session_state.size_val * 3.2)}px !important;
    width: {min(98, 40 + st.session_state.reject_count * 12)}vw !important;
    background: linear-gradient(45deg, #ff4d6d, #ff6b9d) !important;
    color: white !important;
    font-weight: bold !important;
    border: none !important;
    border-radius: 25px !important;
    box-shadow: 0 20px 40px rgba(255,77,109,0.6) !important;
    padding: {max(20, st.session_state.size_val * 0.8)}px !important;
    line-height: 1.1 !important;
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
    margin: 15px auto !important;
    display: block !important;
    position: relative !important;
    z-index: 999 !important;
    overflow: hidden !important;
}}

/* TEXT di dalam tombol MAU */
.mau-marker + div [data-testid="stButton"][key="mau_btn_1"] button > div > div,
.mau-marker + div [data-testid="stButton"][key="mau_btn_1"] button > div > p {{
    font-size: {st.session_state.size_val}px !important;
    font-weight: bold !important;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3) !important;
}}

/* Hover effect */
.mau-marker + div [data-testid="stButton"][key="mau_btn_1"] button:hover {{
    transform: scale(1.05) !important;
    box-shadow: 0 30px 60px rgba(255,77,109,0.8) !important;
}}

/* Gamau button - tetap kecil */
div[data-testid="stButton"][key="gak_btn_1"] button {{
    background: linear-gradient(45deg, #3d3d3d, #555) !important;
    color: white !important;
    font-size: 18px !important;
    width: 280px !important;
    height: 60px !important;
    border-radius: 20px !important;
    margin: 20px auto !important;
    font-weight: bold !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4) !important;
}}

/* GIF Container */
.gif-container {{
    max-width: 600px; margin: 20px auto; border-radius: 25px; overflow: hidden;
    box-shadow: 0 25px 60px rgba(0,0,0,0.6);
}}
</style>
""", unsafe_allow_html=True)

st.title("💕 Hai dek Tata sayang ku! 💕")

if st.session_state.show_pic:
    st.balloons()
    st.markdown("## 🎉 Yeay! Happy Valentine's Day Tata sayang! 🍫🌹✨")
    
    st.markdown("""
    <div class="gif-container">
        <img src="https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd" 
             style="width:100%; height:auto; display:block;">
    </div>
    """, unsafe_allow_html=True)
    
    st.snow()
    st.success("💖 Aku sayang banget sama kamu Tata ❤️")
    
    if st.button("🎈 Main Lagi? 🎈", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
            
else:
    st.markdown("### Kamu mau gak rayain Valentine sama aku? 😍🌹🍫")
    
    # ✅ MARKER + TOMBOL MAU RAKSASA (UNIQUE KEY!)
    st.markdown('<div class="mau-marker" style="display:none;"></div>', unsafe_allow_html=True)
    
    if st.button("**MAU DONG!** 😍💖", key="mau_btn_1", use_container_width=True):
        st.session_state.show_pic = True
        st.rerun()
    
    # Tombol Gamau (UNIQUE KEY!)
    if st.button("**Gamau malas ahh** 🤬😠", key="gak_btn_1", use_container_width=True):
        st.session_state.reject_count += 1
        st.session_state.size_val += 20  # Naik gila-gilaan!
        messages = [
            f"😱 ({st.session_state.reject_count}x) Tombol MAU RAKSASA!",
            "💔 Iyain dong sayangg ❤️",
            f"Size {st.session_state.size_val}px! Nutup layar nih! 😱",
            "✨ Ayo klik MAU Tata!",
            f"Reject #{st.session_state.reject_count} - GEDE BANGET!"
        ]
        st.session_state.msg_val = random.choice(messages)
        st.rerun()

if st.session_state.msg_val:
    st.error("💥 " + st.session_state.msg_val)

st.markdown("""
<div style='text-align: center; padding: 40px; color: #aaa;'>
    <p style='font-size: 1.2em; margin: 0; color: #ff6b9d;'>Made with ❤️ by Aditya</p>
    <p style='font-size: 0.95em;'>Happy Valentine's Day 2026! 💕</p>
</div>
""", unsafe_allow_html=True)
