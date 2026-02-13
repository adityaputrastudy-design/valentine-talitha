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
# GLOBAL STYLE
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


st.title("💌 Hai Tataaa 🤍")

# =========================
# AFTER CLICK MAU
# =========================
if st.session_state.show_pic:
    st.balloons()
    st.markdown("## Hehe… berarti kamu mau yaa 🤍✨")

    st.markdown("""
    <div style="max-width:600px;margin:20px auto;border-radius:25px;overflow:hidden;
                box-shadow:0 25px 60px rgba(0,0,0,0.6);">
        <img src="https://drive.google.com/uc?export=view&id=1yuyexrWlEGZP6edBVxIhFrq5GqAyjWVd" 
             style="width:100%; height:auto; display:block;">
    </div>
    """, unsafe_allow_html=True)

    st.snow()
    st.success("Aku seneng banget kamu bilang iya. Makasih yaa udah selalu ada 🤍")

# =========================
# MAIN QUESTION
# =========================
else:
    st.markdown("### Jadi… kamu mau nggak nemenin aku ngerayain Valentine bareng? 🥺🌹")

    # Styling tombol MAU dinamis (hanya tombol ini yang grow)
    st.markdown(f"""
    <style>
    div[data-testid="stButton"] > button[kind="secondary"] {{
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
        transition: all 0.3s ease-in-out !important;
    }}
    </style>
    """, unsafe_allow_html=True)

    # TOMBOL MAU
    if st.button("Iya, mau 🤍"):
        st.session_state.show_pic = True
        st.rerun()

    # TOMBOL GAMAU
    if st.button("Hmm… nggak dulu deh 😅"):
        st.session_state.reject_count += 1
        st.session_state.size_val += 20

        messages = [
            f"Hmm… udah nolak {st.session_state.reject_count} kali loh 😤",
            "Ih masa nggak sih… coba pikir lagi deh 🥺",
            f"Tombolnya makin gede nih… seriusan nggak mau? 😏",
            "Aku tunggu jawaban yang bener yaa 😌",
            "Yakin banget nih nggak mau? Aku sabar kok… tapi tombolnya nggak 😆"
        ]

        st.session_state.msg_val = random.choice(messages)
        st.rerun()


# =========================
# ERROR MESSAGE
# =========================
if st.session_state.msg_val:
    st.error("💬 " + st.session_state.msg_val)


# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
    <p style='font-size:1.1em;margin:0;color:#ff6b9d;'>Dibuat khusus buat kamu 🤍</p>
    <p style='font-size:0.9em;'>— Adit</p>
</div>
""", unsafe_allow_html=True)
