from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def getGemini_response(input, image=None):  # Set default value for image
    if image:
        response = model.generate_content([input, image])
    else:
        response = model.generate_content([input])  # Only text input

    return response.text


# Streamlit UI
st.set_page_config(page_title="Google Gemini Chatbot", page_icon="🐾")
st.title("SEVA BOT: Your AI Assistant for Pet Care & Support")
st.subheader("Upload an image or describe what's happening with the animal")
st.sidebar.success("How can I help you?")

# User Input
input = st.text_input("Input prompt:", key="input")

# File Upload
image = None  # Initialize image to avoid NameError
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)  # Updated

# Submit Button
if st.button("Give me the response"):
    response = getGemini_response(input, image)
    st.subheader("Hey!, here is your response:")
    st.write(response)
