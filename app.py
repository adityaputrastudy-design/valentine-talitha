import streamlit as st
import random

st.set_page_config(page_title="Special for Tata", page_icon="💌", layout="centered")

# =========================
# SESSION STATE
# =========================
if 'size_val' not in st.session_state:
    st.session_state.size_val = 24

if 'msg_val' not in st.session_state:
    st.session_state.msg_val = ""

if 'show_pic' not in st.session_state:
    st.session_state.show_pic = False

if 'reject_count' not in st.session_state:
    st.session_state.reject_count = 0


# =========================
# GLOBAL BACKGROUND STYLE
# =========================
st.markdown("""
<style>
.stApp { 
    background: linear-gradient(135deg, #0e1117 0%, #1a1f2e 50%, #16213e 100%);
    min-height: 100vh;
    padding-bottom: 120px;
}
.footer {
    text-align: center;
    padding: 40px;
    color: #aaa;
}
</style>
""", unsafe_allow_html=True)


st.title("💕 Hai dek Tata sayang ku! 💕")

# =========================
# AFTER CLICK MAU
# =========================
if st.session_state.show_pic:
    st.balloons()
    st.markdown("## 🎉 Yeay! Happy Valentine's Day Tata sayang! 🍫🌹✨")

    st.markdown("""
    <div style="max-width:600px;margin:20px auto;border-radius:25px;overflow:hidden;
                box-shadow:0 25px 60px rgba(0,0,0,0.6);">
        <img src="https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd" 
             style="width:100%; height:auto; display:block;">
    </div>
    """, unsafe_allow_html=True)

    st.snow()
    st.success("💖 Aku sayang banget sama kamu Tata ❤️")

# =========================
# MAIN QUESTION
# =========================
else:
    st.markdown("### Kamu mau gak rayain Valentine sama aku? 😍🌹🍫")

    # Styling tombol MAU secara dinamis
    st.markdown(f"""
    <style>
    div[data-testid="stButton"] > button#maubtn {{
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
        display: block !important;
    }}
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # TOMBOL MAU (FIXED)
    # =========================
    if st.button("MAU DONG! 😍💖", key="maubtn"):
        st.session_state.show_pic = True
        st.rerun()

    # =========================
    # TOMBOL GAMAU
    # =========================
    if st.button("Gamau malas ahh 😤", key="gak_btn"):
        st.session_state.reject_count += 1
        st.session_state.size_val += 20

        messages = [
            f"😱 ({st.session_state.reject_count}x) Tombol MAU makin RAKSASA!",
            "💔 Iyain dong sayangg ❤️",
            f"Size sekarang {st.session_state.size_val}px 😳",
            f"✨ Udah ditolak {st.session_state.reject_count}x nih!",
            "🚨 Tombolnya hampir nutup layar!"
        ]

        st.session_state.msg_val = random.choice(messages)
        st.rerun()

    # =========================
    # RESET
    # =========================
    if st.button("🔄 Reset", key="reset_btn"):
        st.session_state.size_val = 24
        st.session_state.reject_count = 0
        st.session_state.msg_val = ""
        st.rerun()


# =========================
# ERROR MESSAGE
# =========================
if st.session_state.msg_val:
    st.error("💥 " + st.session_state.msg_val)


# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
    <p style='font-size:1.2em;margin:0;color:#ff6b9d;'>Made with ❤️ by Aditya</p>
    <p style='font-size:0.95em;'>Happy Valentine's Day 2026! 💕</p>
</div>
""", unsafe_allow_html=True)
