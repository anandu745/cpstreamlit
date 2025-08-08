import streamlit as st
import random
import time

# Config
st.set_page_config(page_title="Chest Piece", page_icon="🐔", layout="centered")

# Session state
if 'players' not in st.session_state:
    st.session_state.players = []
if 'winner' not in st.session_state:
    st.session_state.winner = None
if 'clear_input' not in st.session_state:
    st.session_state.clear_input = False

if st.session_state.clear_input:
    st.session_state.name_input = ""
    st.session_state.clear_input = False

# CSS: Mobile optimized
st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .block-container {
            padding: 1rem 1rem 2rem;
            max-width: 100% !important;
        }
        input, button {
            font-size: 18px !important;
        }
        .winner {
            font-size: 2.2rem;
            font-weight: bold;
            text-align: center;
            margin: 2rem 0;
            color: #f97316;
            animation: bounce 0.6s ease-in-out;
        }
        .player-tag {
            background-color: #f97316;
            color: white;
            display: inline-block;
            padding: 0.6rem 1.2rem;
            margin: 0.4rem 0.4rem 0 0;
            border-radius: 30px;
            font-weight: 500;
            font-size: 1.1rem;
        }
        .stButton > button {
            background-color: #f97316;
            color: white;
            border: none;
            padding: 0.8rem 1.5rem;
            border-radius: 10px;
            font-weight: bold;
            font-size: 1.1rem;
            width: 100%;
        }
        .stTextInput input {
            padding: 0.6rem;
            font-size: 1rem;
            border-radius: 10px;
            border: 2px solid #f97316;
        }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🐔 Fod Kazhicho san</h1>", unsafe_allow_html=True)

# Input
st.text_input("Enter Name", key="name_input", placeholder="Tap and type a name")

if st.button("➕ Add Player"):
    name = st.session_state.name_input.strip()
    if name and name not in st.session_state.players:
        st.session_state.players.append(name)
        st.session_state.clear_input = True
        st.rerun()

# Show Players
if st.session_state.players:
    st.markdown("#### Players:")
    st.markdown("".join([f"<span class='player-tag'>{name}</span>" for name in st.session_state.players]), unsafe_allow_html=True)

    if st.button("🎯 Spin Wheel"):
        with st.spinner("Spinning..."):
            spin_area = st.empty()
            for i in range(20):
                selected = random.choice(st.session_state.players)
                spin_area.markdown(f"<h3 style='text-align:center;'>🎡 {selected}</h3>", unsafe_allow_html=True)
                time.sleep(0.1 + i * 0.01)
            st.session_state.winner = selected
            spin_area.empty()
        st.success("Winner selected!")

# Show Winner
if st.session_state.winner:
    st.markdown(f"<div class='winner'>{st.session_state.winner} wins the chest piece! 🍗</div>", unsafe_allow_html=True)

    if st.button("🗑️ Remove Winner"):
        st.session_state.players.remove(st.session_state.winner)
        st.session_state.winner = None
        st.rerun()

    if st.button("🔄 Reset All"):
        st.session_state.players = []
        st.session_state.winner = None
        st.rerun()

