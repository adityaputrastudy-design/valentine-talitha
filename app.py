import streamlit as st
import random

st.set_page_config(page_title="Special for Tata", page_icon="💌", layout="centered", initial_sidebar_state="collapsed")

# 🌟 State Management
if 'size_val' not in st.session_state: st.session_state.size_val = 28
if 'msg_val' not in st.session_state: st.session_state.msg_val = ""
if 'show_pic' not in st.session_state: st.session_state.show_pic = False
if 'reject_count' not in st.session_state: st.session_state.reject_count = 0

# ✨ AESTHETIC CSS MASTER - Glassmorphism + Neon Glow
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
/* Global Aesthetic */
.stApp {{
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    min-height: 100vh;
    font-family: 'Poppins', sans-serif;
    overflow-x: hidden;
}}

/* Glassmorphism Container */
.main .block-container {{
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(20px);
    border-radius: 30px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 3rem;
    box-shadow: 0 25px 45px rgba(0,0,0,0.1);
    max-width: 800px;
    margin: 2rem auto;
}}

/* Title Glow Effect */
h1 {{
    background: linear-gradient(45deg, #ff6b9d, #ff8e8e, #ffd93d);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 700;
    text-align: center;
    text-shadow: 0 0 30px rgba(255, 107, 157, 0.5);
    animation: glow 2s ease-in-out infinite alternate;
}}
@keyframes glow {{
    from {{ text-shadow: 0 0 20px #ff6b9d, 0 0 30px #ff6b9d, 0 0 40px #ff6b9d; }}
    to {{ text-shadow: 0 0 20px #ffd93d, 0 0 30px #ffd93d, 0 0 40px #ffd93d; }}
}}

/* MARKER + MAU BUTTON RAKSASA - NEON PULSE */
.mau-marker + div [data-testid="stButton"][key="mau_btn_1"] button,
div[data-testid="stButton"][key="mau_btn_1"] button {{
    font-size: {st.session_state.size_val}px !important;
    height: {max(90, st.session_state.size_val * 3.5)}px !important;
    width: {min(98, 45 + st.session_state.reject_count * 15)}vw !important;
    background: linear-gradient(45deg, #ff6b9d, #ff8e8e, #ffb6c1) !important;
    color: white !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 40px !important;
    box-shadow: 
        0 20px 40px rgba(255, 107, 157, 0.4),
        0 0 30px rgba(255, 107, 157, 0.3),
        inset 0 1px 0 rgba(255,255,255,0.3) !important;
    padding: {max(25, st.session_state.size_val * 0.9)}px 40px !important;
    line-height: 1.1 !important;
    transition: all 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
    margin: 20px auto !important;
    position: relative !important;
    z-index: 999 !important;
    overflow: hidden !important;
    text-shadow: 0 2px 10px rgba(0,0,0,0.3) !important;
    animation: pulse-glow {1 + st.session_state.reject_count * 0.2}s infinite !important;
}}

@keyframes pulse-glow {{
    0% {{ box-shadow: 0 20px 40px rgba(255,107,157,0.4), 0 0 30px rgba(255,107,157,0.3); }}
    50% {{ box-shadow: 0 30px 60px rgba(255,107,157,0.6), 0 0 50px rgba(255,107,157,0.5); }}
    100% {{ box-shadow: 0 20px 40px rgba(255,107,157,0.4), 0 0 30px rgba(255,107,157,0.3); }}
}}

/* MAU BUTTON HOVER */
div[data-testid="stButton"][key="mau_btn_1"] button:hover {{
    transform: scale(1.05) translateY(-5px) !important;
    box-shadow: 
        0 35px 70px rgba(255,107,157,0.7),
        0 0 60px rgba(255,107,157,0.6) !important;
}}

/* MAU BUTTON TEXT */
.mau-marker + div [data-testid="stButton"][key="mau_btn_1"] button > div > div,
.mau-marker + div [data-testid="stButton"][key="mau_btn_1"] button > div > p {{
    font-size: {st.session_state.size_val}px !important;
    font-weight: 700 !important;
    text-shadow: 0 2px 10px rgba(0,0,0,0.4) !important;
}}

/* GAMAU BUTTON - Elegant Dark */
div[data-testid="stButton"][key="gak_btn_1"] button {{
    background: linear-gradient(45deg, rgba(61,61,61,0.9), rgba(85,85,85,0.9)) !important;
    backdrop-filter: blur(10px) !important;
    color: white !important;
    font-size: 20px !important;
    font-weight: 600 !important;
    width: 320px !important;
    height: 70px !important;
    border-radius: 25px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    margin: 25px auto !important;
    box-shadow: 0 15px 35px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.2) !important;
    transition: all 0.3s ease !important;
}}
div[data-testid="stButton"][key="gak_btn_1"] button:hover {{
    transform: translateY(-3px) !important;
    box-shadow: 0 20px 45px rgba(0,0,0,0.5) !important;
}}

/* Success Message */
div[data-testid="stSuccessBlock"] {{
    background: linear-gradient(45deg, rgba(34,197,94,0.2), rgba(74,222,128,0.2)) !important;
    backdrop-filter: blur(10px) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(34,197,94,0.3) !important;
    padding: 1.5rem !important;
}}

/* Error Message */
div[data-testid="stErrorBlock"] {{
    background: linear-gradient(45deg, rgba(239,68,68,0.2), rgba(248,113,113,0.2)) !important;
    backdrop-filter: blur(10px) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(239,68,68,0.4) !important;
}}

/* GIF Container - Glass Effect */
.gif-container {{
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(20px);
    border-radius: 30px;
    padding: 20px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 25px 60px rgba(0,0,0,0.3);
    max-width: 650px;
    margin: 20px auto;
}}

/* Reset Button */
div[data-testid="stButton"]:has([key="reset_btn"]) button {{
    background: linear-gradient(45deg, #6b7280, #9ca3af) !important;
    color: white !important;
    border-radius: 20px !important;
    font-weight: 600 !important;
    height: 55px !important;
    box-shadow: 0 10px 30px rgba(107,114,128,0.4) !important;
}}
</style>
""", unsafe_allow_html=True)

st.title("✨ Hai Tata Sayangku ✨")

if st.session_state.show_pic:
    st.balloons()
    st.markdown("## 🎉 Yeay! Happy Valentine's Day Tata Sayang! 🍫🌹💖")
    
    st.markdown("""
    <div class="gif-container">
        <img src="https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd" 
             style="width:100%; height:auto; display:block; border-radius: 20px;">
    </div>
    """, unsafe_allow_html=True)
    
    st.snow()
    st.success("💖 Aku sayang banget sama kamu Tataaa ❤️")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎈 Main Lagi? 🎈", key="reset_btn", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
            
else:
    st.markdown("### 💕 Kamu mau rayain Valentine sama aku gak? 😍🌹🍫")
    
    # ✨ MARKER + TOMBOL MAU RAKSASA
    st.markdown('<div class="mau-marker" style="display:none;"></div>', unsafe_allow_html=True)
    
    if st.button("💖 **MAU DONG!** 💖", key="mau_btn_1", use_container_width=True):
        st.session_state.show_pic = True
        st.rerun()
    
    # Tombol Gamau - Elegant
    if st.button("**Gamau malas ahh** 😤", key="gak_btn_1", use_container_width=True):
        st.session_state.reject_count += 1
        st.session_state.size_val += 25  # SUPER AGRESIF!
        messages = [
            f"😱💥 ({st.session_state.reject_count}x reject!) Tombol MAU udah RAKSASA!",
            "💔 Iyain dong Tata sayangg ❤️ Jangan buat Aditya sedih",
            f"📏 Size {st.session_state.size_val}px! Tombolnya mau NUTUPIN LAYAR! 😱",
            "✨ Ayo klik MAU yuk Tata cantikku!",
            f"🚨 Reject #{st.session_state.reject_count} - GEDE BANGET SIH! 😤"
        ]
        st.session_state.msg_val = random.choice(messages)
        st.rerun()

if st.session_state.msg_val:
    st.error("💥 " + st.session_state.msg_val)

# Footer Aesthetic
st.markdown("""
<div style='
    text-align: center; 
    padding: 3rem 2rem; 
    color: rgba(255,255,255,0.9);
    background: rgba(0,0,0,0.1);
    backdrop-filter: blur(15px);
    border-radius: 25px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-top: 2rem;
'>
    <p style='font-size: 1.4em; margin: 0; font-weight: 700; color: #ff6b9d;'>
        Made with ❤️ by Aditya
    </p>
    <p style='font-size: 1em; margin: 0.5rem 0 0 0;'>
        Happy Valentine's Day 2026! 💕✨
    </p>
</div>
""", unsafe_allow_html=True)
