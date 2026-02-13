import streamlit as st
import random

st.set_page_config(page_title="Special for Tata", page_icon="💌", layout="centered")

# Session state
if 'size_val' not in st.session_state: st.session_state.size_val = 24
if 'msg_val' not in st.session_state: st.session_state.msg_val = ""
if 'show_pic' not in st.session_state: st.session_state.show_pic = False
if 'reject_count' not in st.session_state: st.session_state.reject_count = 0

# CSS PERFECT - Dynamic size + Reset button
st.markdown(f"""
<style>
.stApp {{ 
    background: linear-gradient(135deg, #0e1117 0%, #1a1f2e 50%, #16213e 100%);
    min-height: 100vh;
}}
.mau-btn {{
    font-size: {st.session_state.size_val}px !important;
    height: {max(80, st.session_state.size_val * 3.2)}px !important;
    width: {min(98, 40 + st.session_state.reject_count * 12)}vw !important;
    background: linear-gradient(45deg, #ff4d6d, #ff6b9d) !important;
    color: white !important;
    font-weight: bold !important;
    border: none !important;
    border-radius: 25px !important;
    box-shadow: 0 15px 35px rgba(255,77,109,0.5) !important;
    cursor: pointer !important;
    transition: all 0.5s ease !important;
    display: block !important;
    margin: 20px auto !important;
    padding: {max(15, st.session_state.size_val * 0.6)}px {max(25, st.session_state.size_val)}px !important;
    box-sizing: border-box !important;
    line-height: 1.1 !important;
    overflow: hidden !important;
    text-align: center !important;
    position: relative !important;
    z-index: 999 !important;
}}
.mau-btn:hover {{
    transform: scale(1.05) !important;
    box-shadow: 0 25px 50px rgba(255,77,109,0.7) !important;
}}
.mau-btn span {{
    font-size: {st.session_state.size_val}px !important;
    font-weight: bold !important;
    line-height: 1.1 !important;
    white-space: nowrap !important;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3) !important;
}}
.gamau-btn {{
    background: linear-gradient(45deg, #3d3d3d, #555) !important;
    color: white !important;
    font-size: 16px !important;
    width: 240px !important;
    height: 55px !important;
    border-radius: 20px !important;
    border: none !important;
    margin: 20px auto !important;
    font-weight: 600 !important;
    display: block !important;
}}
.reset-btn {{
    background: linear-gradient(45deg, #4f46e5, #7c3aed) !important;
    color: white !important;
    font-size: 14px !important;
    width: 180px !important;
    height: 45px !important;
    border-radius: 25px !important;
    border: none !important;
    margin: 30px auto !important;
    font-weight: 600 !important;
    box-shadow: 0 10px 30px rgba(79, 70, 229, 0.4) !important;
    position: fixed !important;
    bottom: 30px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    z-index: 1000 !important;
}}
.reset-btn:hover {{
    transform: translateX(-50%) translateY(-2px) !important;
    box-shadow: 0 15px 40px rgba(79, 70, 229, 0.6) !important;
}}
.gif-container {{
    max-width: 600px; margin: 20px auto; border-radius: 25px; overflow: hidden;
    box-shadow: 0 25px 60px rgba(0,0,0,0.6);
}}
</style>
""", unsafe_allow_html=True)

st.title("💕 Hai dek Tata sayang ku! 💕")

# Handle MAU click via query param
if st.query_params.get("show_pic") == ["true"]:
    st.session_state.show_pic = True
    st.query_params.clear()
    st.rerun()

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
    
else:
    st.markdown("### Kamu mau gak rayain Valentine sama aku? 😍🌹🍫")
    
    # ✅ TOMBOL MAU - SELALU CLICKABLE & MEMBESAR
    st.markdown(f"""
    <button class="mau-btn" onclick="window.location.href='?show_pic=true'">
        <span>MAU DONG! 😍💖 ({st.session_state.size_val}px)</span>
    </button>
    """, unsafe_allow_html=True)
    
    # ✅ TOMBOL GAMAU - SELALU TERSEDIA
    if st.button("**Gamau malas ahh** 😤", key="gak_btn"):
        st.session_state.reject_count += 1
        st.session_state.size_val += 20  # Membesar agresif setiap klik
        messages = [
            f"😱 ({st.session_state.reject_count}x reject!) Tombol MAU makin RAKSASA!",
            "💔 Iyain dong sayangg ❤️",
            f"📏 Size {st.session_state.size_val}px - hampir nutup layar!",
            f"✨ Tombol MAU udah {st.session_state.reject_count}x lebih besar!",
            f"🚨 Reject #{st.session_state.reject_count} - GEDE BANGET!"
        ]
        st.session_state.msg_val = random.choice(messages)
        st.rerun()

# Error message
if st.session_state.msg_val:
    st.error("💥 " + st.session_state.msg_val)

# ✅ TOMBOL RESET - SELALU DI BAWAH (Fixed position)
st.markdown("""
<button class="reset-btn" onclick="window.location.href=window.location.pathname">
    🔄 Reset
</button>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align: center; padding: 80px 40px 40px 40px; color: #aaa;'>
    <p style='font-size: 1.2em; margin: 0; color: #ff6b9d;'>Made with ❤️ by Aditya</p>
    <p style='font-size: 0.95em;'>Happy Valentine's Day 2026! 💕</p>
</div>
""", unsafe_allow_html=True)
