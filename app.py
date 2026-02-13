import streamlit as st
import random

st.set_page_config(page_title="Special for Tata", page_icon="💌", layout="centered")

# Session state
if 'size_val' not in st.session_state: st.session_state.size_val = 24
if 'msg_val' not in st.session_state: st.session_state.msg_val = ""
if 'show_pic' not in st.session_state: st.session_state.show_pic = False
if 'reject_count' not in st.session_state: st.session_state.reject_count = 0

# CSS PERFECT
st.markdown(f"""
<style>
.stApp {{ 
    background: linear-gradient(135deg, #0e1117 0%, #1a1f2e 50%, #16213e 100%);
    min-height: 100vh;
    padding-bottom: 120px;
}}
.mau-display {{
    font-size: {st.session_state.size_val}px !important;
    height: {max(80, st.session_state.size_val * 3.2)}px !important;
    width: {min(98, 40 + st.session_state.reject_count * 12)}vw !important;
    background: linear-gradient(45deg, #ff4d6d, #ff6b9d) !important;
    color: white !important;
    font-weight: bold !important;
    border: none !important;
    border-radius: 25px !important;
    box-shadow: 0 15px 35px rgba(255,77,109,0.5) !important;
    margin: 20px auto !important;
    padding: {max(15, st.session_state.size_val * 0.6)}px {max(25, st.session_state.size_val)}px !important;
    box-sizing: border-box !important;
    line-height: 1.1 !important;
    overflow: hidden !important;
    text-align: center !important;
    display: block !important;
    pointer-events: none !important;
}}
.mau-trigger {{
    height: {max(80, st.session_state.size_val * 3.2)}px !important;
    width: {min(98, 40 + st.session_state.reject_count * 12)}vw !important;
    opacity: 0 !important;
    position: absolute !important;
    z-index: 1000 !important;
    margin: 20px auto !important;
}}
.gamau-btn {{
    background: linear-gradient(45deg, #3d3d3d, #555) !important;
    color: white !important;
    font-size: 18px !important;
    width: 260px !important;
    height: 60px !important;
    border-radius: 20px !important;
    border: none !important;
    margin: 25px auto !important;
    font-weight: 600 !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3) !important;
}}
.reset-btn {{
    background: linear-gradient(45deg, #4f46e5, #7c3aed) !important;
    color: white !important;
    font-size: 16px !important;
    width: 220px !important;
    height: 55px !important;
    border-radius: 25px !important;
    border: none !important;
    margin: 30px auto !important;
    font-weight: 600 !important;
    box-shadow: 0 10px 30px rgba(79,70,229,0.4) !important;
}}
.gif-container {{
    max-width: 600px; margin: 20px auto; border-radius: 25px; overflow: hidden;
    box-shadow: 0 25px 60px rgba(0,0,0,0.6);
}}
.mau-container {{
    position: relative !important;
    margin: 20px auto !important;
    display: block !important;
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
    
else:
    st.markdown("### Kamu mau gak rayain Valentine sama aku? 😍🌹🍫")
    
    # ✅ CONTAINER MAU BUTTON (Visual + Functional)
    st.markdown(f"""
    <div class="mau-container">
        <button class="mau-display">
            <span>MAU DONG! 😍💖 ({st.session_state.size_val}px)</span>
        </button>
    </div>
    """, unsafe_allow_html=True)
    
    # MAU TRIGGER - Invisible tapi cover full area tombol
    if st.button(" ", key="mau_trigger", help="Klik tombol pink!"):
        st.session_state.show_pic = True
        st.rerun()
    
    # GAMAU - Membesarkan MAU
    if st.button("**Gamau malas ahh** 😤", key="gak_btn"):
        st.session_state.reject_count += 1
        st.session_state.size_val += 20
        messages = [
            f"😱 ({st.session_state.reject_count}x) Tombol MAU RAKSASA!",
            "💔 Iyain dong sayangg ❤️",
            f"Size {st.session_state.size_val}px - nutup layar nih!",
            f"✨ Tombol MAU udah {st.session_state.reject_count}x lebih besar!",
            f"🚨 Reject #{st.session_state.reject_count} - GEDE BANGET!"
        ]
        st.session_state.msg_val = random.choice(messages)
        st.rerun()
    
    # RESET
    if st.button("🔄 Reset", key="reset_btn"):
        st.session_state.size_val = 24
        st.session_state.reject_count = 0
        st.session_state.msg_val = ""
        st.rerun()

if st.session_state.msg_val:
    st.error("💥 " + st.session_state.msg_val)

# Footer
st.markdown("""
<div style='text-align: center; padding: 40px; color: #aaa;'>
    <p style='font-size: 1.2em; margin: 0; color: #ff6b9d;'>Made with ❤️ by Aditya</p>
    <p style='font-size: 0.95em;'>Happy Valentine's Day 2026! 💕</p>
</div>
""", unsafe_allow_html=True)
