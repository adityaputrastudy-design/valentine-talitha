import streamlit as st
import random

st.set_page_config(page_title="Special for Tata", page_icon="💌", layout="centered")

# 1. State Management
if 'size_val' not in st.session_state: st.session_state.size_val = 24
if 'msg_val' not in st.session_state: st.session_state.msg_val = ""
if 'show_pic' not in st.session_state: st.session_state.show_pic = False
if 'reject_count' not in st.session_state: st.session_state.reject_count = 0

# 2. CSS PERFECT - Menghilangkan "Kotak Kosong" dan Mengatur Ukuran Dinamis
st.markdown(f"""
<style>
/* Background & Dasar */
.stApp {{ 
    background: linear-gradient(135deg, #0e1117 0%, #1a1f2e 50%, #16213e 100%);
}}

/* Tombol MAU Raksasa: Melebar & Memanjang */
.mau-btn {{
    font-size: {st.session_state.size_val}px !important;
    height: {max(80, st.session_state.size_val * 3.2)}px !important;
    width: {min(95, 40 + st.session_state.reject_count * 10)}vw !important;
    background: linear-gradient(45deg, #ff4d6d, #ff6b9d) !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 25px !important;
    box-shadow: 0 15px 35px rgba(255,77,109,0.5) !important;
    cursor: pointer !important;
    border: none !important;
    display: block !important;
    margin: 20px auto !important;
    line-height: 1.1 !important;
    text-align: center !important;
    transition: all 0.3s ease-in-out !important;
}}

/* SEMBUNYIKAN TOMBOL ASLI STREAMLIT (Kotak Kosong) */
div[data-testid="stButton"]:has(button[key="mau_hidden"]) {{
    display: none !important;
}}
#mau-hidden-btn {{
    display: none !important;
}}

/* Gambar Container */
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
    
    # ✅ TOMBOL MAU RAKSASA (Satu-satunya yang terlihat)
    # Kita gunakan st.button dengan CSS khusus agar tidak ada kotak kosong
    if st.button("MAU DONG! 😍💖", key="mau_btn", use_container_width=True):
        st.session_state.show_pic = True
        st.rerun()
    
    # CSS Tambahan untuk memaksa tombol dengan key "mau_btn" jadi RAKSASA
    st.markdown(f"""
        <style>
        div[data-testid="stButton"]:has(button[key="mau_btn"]) button {{
            font-size: {st.session_state.size_val}px !important;
            height: {max(80, st.session_state.size_val * 3.2)}px !important;
            width: {min(100, 40 + st.session_state.reject_count * 12)}% !important;
            background: linear-gradient(45deg, #ff4d6d, #ff6b9d) !important;
            color: white !important;
            font-weight: bold !important;
            border-radius: 25px !important;
            box-shadow: 0 15px 35px rgba(255,77,109,0.5) !important;
        }}
        </style>
    """, unsafe_allow_html=True)
    
    # Tombol Gamau (Tetap kecil)
    if st.button("**Gamau malas ahh** 🤬😠", key="gak_btn", use_container_width=True):
        st.session_state.reject_count += 1
        st.session_state.size_val += 20  # Gua naikin biar pertumbuhannya lebih gila
        messages = [
            f"😱 Tombol MAU makin RAKSASA!",
            "💔 Iyain dong sayangg ❤️",
            f"Tega banget nolak {st.session_state.reject_count}x... 🙏",
            "✨ Ayo klik MAU Tata!",
            "Nanti tombolnya nutupin seluruh layar loh! 😱"
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
