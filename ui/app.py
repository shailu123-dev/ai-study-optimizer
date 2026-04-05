import streamlit as st
import sys
import os

# 🔧 Fix import path issue
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from environment.study_env import StudyEnvironment

# create environment
env = StudyEnvironment()

st.title("📚 AI Study Focus Simulator")

# store state in session
if "state" not in st.session_state:
    st.session_state.state = env.reset()

st.write("### Current State:")
st.write(st.session_state.state)

# action selection
action = st.selectbox(
    "Choose Action",
    ["alert_user", "motivate_user", "do_nothing"]
)

# button to take step
if st.button("Take Step"):
    new_state, reward = env.step(action)

    st.session_state.state = new_state

    st.write("### Updated State:")
    st.write(new_state)

    st.write("### Reward:")
    st.write(reward)