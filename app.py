import streamlit as st
import random

st.set_page_config(page_title="Special for Tata", page_icon="💌", layout="centered")

# Session state
if 'size_val' not in st.session_state: st.session_state.size_val = 24
if 'msg_val' not in st.session_state: st.session_state.msg_val = ""
if 'show_pic' not in st.session_state: st.session_state.show_pic = False
if 'reject_count' not in st.session_state: st.session_state.reject_count = 0
if 'game_active' not in st.session_state: st.session_state.game_active = True

# CSS PERFECT - Text fit + Reset button
st.markdown(f"""
<style>
.stApp {{ 
    background: linear-gradient(135deg, #0e1117 0%, #1a1f2e 50%, #16213e 100%);
    min-height: 100vh;
}}
.mau-btn {{
    font-size: {st.session_state.size_val}px !important;
    height: {max(80, st.session_state.size_val * 3.2)}px !important;
    width: {min(95, 40 + st.session_state.reject_count * 8)}vw !important;
    background: linear-gradient(45deg, #ff4d6d, #ff6b9d) !important;
    color: white !important;
    font-weight: bold !important;
    border: none !important;
    border-radius: 25px !important;
    box-shadow: 0 15px 35px rgba(255,77,109,0.5) !important;
    cursor: { 'pointer' if st.session_state.game_active else 'not-allowed' } !important;
    transition: all 0.5s ease !important;
    display: block !important;
    margin: 20px auto !important;
    padding: {max(15, st.session_state.size_val * 0.6)}px {max(25, st.session_state.size_val)}px !important;
    box-sizing: border-box !important;
    line-height: 1.1 !important;
    overflow: hidden !important;
    text-align: center !important;
    position: relative !important;
    opacity: {1.0 if st.session_state.game_active else 0.6} !important;
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
.mau-btn:disabled {{
    cursor: not-allowed !important;
    opacity: 0.5 !important;
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
}}
.reset-btn {{
    background: linear-gradient(45deg, #4f46e5, #7c3aed) !important;
    color: white !important;
    font-size: 16px !important;
    width: 200px !important;
    height: 50px !important;
    border-radius: 25px !important;
    border: none !important;
    margin: 20px auto !important;
    font-weight: 600 !important;
    box-shadow: 0 10px 30px rgba(79, 70, 229, 0.4) !important;
}}
.reset-btn:hover {{
    transform: translateY(-2px) !important;
    box-shadow: 0 15px 40px rgba(79, 70, 229, 0.6) !important;
}}
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
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🎈 Main Lagi?", key="reset_game"):
            # Full reset
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        
elif st.session_state.game_active:
    st.markdown("### Kamu mau gak rayain Valentine sama aku? 😍🌹🍫")
    
    # ✅ MAU BUTTON - Aktif di awal!
    st.markdown(f"""
    <button class="mau-btn" onclick="window.parent.location.href=window.parent.location.href.split('?')[0] + '?show_pic=true';">
        <span>MAU DONG! 😍💖</span>
    </button>
    """, unsafe_allow_html=True)
    
    # Gamau button
    col1, col2 = st.columns([1, 1])
    with col2:
        if st.button("**Gamau malas ahh** 😤", key="gak_btn", help="Buat tombol MAU membesar!"):
            st.session_state.reject_count += 1
            st.session_state.size_val += 18  # Membesar agresif
            st.session_state.game_active = False  # Disable MAU setelah reject pertama
            messages = [
                f"😱 ({st.session_state.reject_count}x) Tombol MAU RAKSASA!",
                "💔 Iyain dong sayangg ❤️",
                f"Size {st.session_state.size_val}px! Nutup layar nih! 😱",
                "✨ Sekarang klik tombol pink gede itu!",
                f"Reject #{st.session_state.reject_count} - GEDE BANGET!"
            ]
            st.session_state.msg_val = random.choice(messages)
            st.rerun()
else:
    # Game disabled - Tombol MAU membesar tapi disabled
    st.markdown("### Sekarang tombolnya udah gede! 😍 Klik aja!")
    
    st.markdown(f"""
    <button class="mau-btn" onclick="window.parent.location.href=window.parent.location.href.split('?')[0] + '?show_pic=true';" 
               {'disabled' if not st.session_state.game_active else ''}>
        <span>MAU DONG! 😍💖</span>
    </button>
    """, unsafe_allow_html=True)
    
    # RESET BUTTON - Kembalikan ke awal
    if st.button("🔄 Reset Game", key="reset_partial"):
        st.session_state.game_active = True
        st.session_state.reject_count = 0
        st.session_state.size_val = 24
        st.session_state.msg_val = ""
        st.rerun()

# Error message
if st.session_state.msg_val:
    st.error("💥 " + st.session_state.msg_val)

# Footer
st.markdown("""
<div style='text-align: center; padding: 40px; color: #aaa;'>
    <p style='font-size: 1.2em; margin: 0; color: #ff6b9d;'>Made with ❤️ by Aditya</p>
    <p style='font-size: 0.95em;'>Happy Valentine's Day 2026! 💕</p>
</div>
""", unsafe_allow_html=True)

# Handle query param for MAU click
if st.query_params.get("show_pic") == ["true"]:
    st.session_state.show_pic = True
    st.query_params.clear()
    st.rerun()
