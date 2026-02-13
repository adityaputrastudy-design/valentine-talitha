import streamlit as st
import random

st.set_page_config(page_title="Special for Tata", page_icon="💌", layout="centered")

# State Management
if 'size_val' not in st.session_state: st.session_state.size_val = 24
if 'msg_val' not in st.session_state: st.session_state.msg_val = ""
if 'show_pic' not in st.session_state: st.session_state.show_pic = False
if 'reject_count' not in st.session_state: st.session_state.reject_count = 0

# BLACK ELEGANT CSS - Minimal & Sophisticated
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Dark Elegant Background */
.stApp {{
    background: #0a0a0a;
    min-height: 100vh;
    font-family: 'Inter', -apple-system, sans-serif;
}}

/* Subtle gradient container */
.main .block-container {{
    background: linear-gradient(145deg, rgba(20,20,20,0.8), rgba(10,10,10,0.9));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 
        0 25px 50px rgba(0,0,0,0.5),
        0 0 0 1px rgba(255,255,255,0.05);
    padding: 3rem 2rem;
    max-width: 700px;
    margin: 2rem auto;
}}

/* Elegant Typography */
h1 {{
    color: #ffffff;
    font-weight: 600;
    font-size: 2.5rem;
    text-align: center;
    letter-spacing: -0.02em;
    margin-bottom: 1.5rem;
    text-shadow: 0 2px 10px rgba(255,255,255,0.1);
}}

h3 {{
    color: #e2e8f0;
    font-weight: 500;
    font-size: 1.3rem;
    text-align: center;
    margin-bottom: 2.5rem;
    letter-spacing: -0.01em;
}}

/* MAU BUTTON - Elegant Dark Pink Growth */
.mau-marker + div [data-testid="stButton"][key="mau_btn_1"] button,
div[data-testid="stButton"][key="mau_btn_1"] button {{
    font-size: {st.session_state.size_val}px !important;
    height: {max(85, st.session_state.size_val * 3.3)}px !important;
    width: {min(96, 42 + st.session_state.reject_count * 14)}vw !important;
    background: linear-gradient(135deg, #1e1e2e 0%, #2a1f3d 50%, #3a1c4d 100%) !important;
    border: 1px solid rgba(255,85,125,0.3) !important;
    color: #ffffff !important;
    font-weight: 600 !important;
    border-radius: 20px !important;
    box-shadow: 
        0 20px 40px rgba(0,0,0,0.4),
        0 0 0 1px rgba(255,85,125,0.2),
        inset 0 1px 0 rgba(255,255,255,0.1) !important;
    padding: {max(22, st.session_state.size_val * 0.85)}px 50px !important;
    line-height: 1.15 !important;
    transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
    margin: 20px auto !important;
    position: relative !important;
    z-index: 999 !important;
    overflow: hidden !important;
    letter-spacing: -0.01em;
}}

/* MAU BUTTON SUBTLE GLOW */
div[data-testid="stButton"][key="mau_btn_1"] button::before {{
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,85,125,0.2), transparent);
    transition: left 0.6s;
}}
div[data-testid="stButton"][key="mau_btn_1"] button:hover::before {{
    left: 100%;
}}
div[data-testid="stButton"][key="mau_btn_1"] button:hover {{
    transform: translateY(-3px) !important;
    box-shadow: 
        0 30px 60px rgba(0,0,0,0.6),
        0 0 0 1px rgba(255,85,125,0.4) !important;
}}

/* MAU BUTTON TEXT */
.mau-marker + div [data-testid="stButton"][key="mau_btn_1"] button > div > div,
.mau-marker + div [data-testid="stButton"][key="mau_btn_1"] button > div > p {{
    font-size: {st.session_state.size_val}px !important;
    font-weight: 600 !important;
    text-shadow: 0 1px 3px rgba(0,0,0,0.5) !important;
    letter-spacing: -0.015em;
}}

/* GAMAU BUTTON - Minimal Dark */
div[data-testid="stButton"][key="gak_btn_1"] button {{
    background: linear-gradient(135deg, #1a1a1a, #242424) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: #e2e8f0 !important;
    font-size: 18px !important;
    font-weight: 500 !important;
    width: 300px !important;
    height: 65px !important;
    border-radius: 18px !important;
    margin: 25px auto !important;
    box-shadow: 
        0 15px 35px rgba(0,0,0,0.4),
        inset 0 1px 0 rgba(255,255,255,0.08) !important;
    transition: all 0.3s ease !important;
    letter-spacing: -0.01em;
}}
div[data-testid="stButton"][key="gak_btn_1"] button:hover {{
    transform: translateY(-2px) !important;
    box-shadow: 
        0 20px 45px rgba(0,0,0,0.5),
        inset 0 1px 0 rgba(255,255,255,0.12) !important;
}}

/* Messages - Elegant */
div[data-testid="stSuccessBlock"], div[data-testid="stErrorBlock"] {{
    background: rgba(20,20,20,0.8) !important;
    backdrop-filter: blur(15px) !important;
    border-radius: 16px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    padding: 1.5rem !important;
    margin: 1rem 0 !important;
}}
.stErrorBlock > div > div {{
    color: #f87171 !important;
}}
.stSuccessBlock > div > div {{
    color: #10b981 !important;
}}

/* GIF Container */
.gif-container {{
    background: rgba(20,20,20,0.7);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 2rem;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 25px 60px rgba(0,0,0,0.6);
    max-width: 600px;
    margin: 2rem auto;
}}

/* Reset Button */
div[data-testid="stButton"]:has([key="reset_btn"]) button {{
    background: linear-gradient(135deg, #2d2d2d, #3a3a3a) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: #e2e8f0 !important;
    border-radius: 18px !important;
    font-weight: 500 !important;
    height: 60px !important;
    box-shadow: 0 15px 35px rgba(0,0,0,0.4) !important;
}}
</style>
""", unsafe_allow_html=True)

st.title("Hai Tata")

if st.session_state.show_pic:
    st.balloons()
    st.markdown("## Happy Valentine's Day")
    
    st.markdown("""
    <div class="gif-container">
        <img src="https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd" 
             style="width:100%; height:auto; display:block; border-radius: 20px;">
    </div>
    """, unsafe_allow_html=True)
    
    st.snow()
    st.success("Aku sayang banget sama kamu Tata")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Main Lagi?", key="reset_btn", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
            
else:
    st.markdown("### Mau rayain Valentine sama aku?")
    
    # MARKER + TOMBOL MAU RAKSASA
    st.markdown('<div class="mau-marker" style="display:none;"></div>', unsafe_allow_html=True)
    
    if st.button("MAU DONG", key="mau_btn_1", use_container_width=True):
        st.session_state.show_pic = True
        st.rerun()
    
    # Tombol Gamau
    if st.button("Gamau malas ahh", key="gak_btn_1", use_container_width=True):
        st.session_state.reject_count += 1
        st.session_state.size_val += 22  # Aggressive growth
        messages = [
            f"({st.session_state.reject_count}x) Tombol MAU makin besar",
            "Iyain dong sayang",
            f"Size {st.session_state.size_val}px - hampir nutup layar",
            "Ayo klik MAU",
            f"Reject #{st.session_state.reject_count} - gede banget"
        ]
        st.session_state.msg_val = random.choice(messages)
        st.rerun()

if st.session_state.msg_val:
    st.error(st.session_state.msg_val)

# Minimal footer
st.markdown("""
<div style='
    text-align: center; 
    padding: 2rem; 
    color: #a1a1aa;
    font-size: 0.95rem;
'>
    Made by Aditya | Happy Valentine's Day 2026
</div>
""", unsafe_allow_html=True)
