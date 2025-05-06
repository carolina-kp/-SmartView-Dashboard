import streamlit as st
from streamlit_chat import message

st.title("🤖 SmartBot Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Ask the bot a question about this dataset or dashboard:")

# Simulate reasoning responses
def respond(prompt):
    if "age" in prompt.lower():
        return "Age has moderate negative correlation with survival. Older passengers were less likely to survive, possibly due to priority given to children and women."
    elif "class" in prompt.lower():
        return "Passengers in 1st class had significantly higher survival rates. This shows how socioeconomic status influenced outcomes."
    elif "bias" in prompt.lower():
        return "We've reduced confirmation bias by using filters and presenting correlation rather than fixed narratives."
    else:
        return "That's a good question! This system currently simulates basic logic. Try asking about age, class, or bias."

if user_input:
    reply = respond(user_input)
    st.session_state.history.append((user_input, reply))

for i, (user, bot) in enumerate(reversed(st.session_state.history)):
    message(user, is_user=True, key=f"user_{i}")
    message(bot, key=f"bot_{i}")
