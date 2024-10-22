import streamlit as st 

def get_response(user_input):
    return f"Chat Bot: {user_input}"


st.title("Chatbot")
st.write("Enter any Message")

user_input = st.text_input("You")

if user_input:
    response = get_response(user_input)
    st.write(response)