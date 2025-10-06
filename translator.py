import streamlit as st
import google.generativeai as genai
import os

# Set up the Google API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBJxLNNzqBR6Wjuha4t6V7dbzfOn06JTk8"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Initialize the Gemini model
model = genai.GenerativeModel("models/gemini-2.5-flash")


def language_translate(text, source_lang, target_lang):
    prompt = f"""
    Translate the following text from {source_lang} to {target_lang}:

    {text}
    
    
    please don't add extra text, only tranlated text
    """
    response = model.generate_content(prompt)
    return response.text if response else "Translation failed."


# Streamlit App UI
st.title("Language Translator using Gemini AI")

# User input for text
user_text = st.text_area("Enter text to translate:")

# Language options
languages = ["English", "Spanish", "French", "German","Urdu", "Hindi", "Chinese", "Japanese", "Russian", "Arabic",
             "Portuguese"]
source_lang = st.selectbox("Select source language:", languages)
target_lang = st.selectbox("Select target language:", languages)

if st.button("Translate"):
    if user_text.strip():
        translation = language_translate(user_text, source_lang, target_lang)
        st.subheader("Translated Text:")
        st.write(translation)
    else:
        st.warning("Please enter text to translate.")
