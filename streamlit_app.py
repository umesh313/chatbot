import streamlit as st
import openai

# Initialize OpenAI client with API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set the app title
st.title("Your ChatBot Name")

# Initialize chat history in session state if not present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to get response from OpenAI GPT-3.5 Turbo
def get_response(user_input):
    messages = [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages]
    messages.append({"role": "user", "content": user_input})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response["choices"][0]["message"]["content"]

# User input box
user_input = st.chat_input("Type your message here...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get and display assistant response
    response = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
