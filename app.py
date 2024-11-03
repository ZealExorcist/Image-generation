import requests
import streamlit as st
from PIL import Image
from io import BytesIO

def generate_image(prompt, model, width, height, seed, no_logo, enhance, private):

    url = f"https://pollinations.ai/p/{prompt}?width={width}&height={height}&seed={seed}&nologo={no_logo}&enhance={enhance}&private={private}&model={model}"

    response = requests.get(url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    return image

st.title("AI Image Generator")

# Text inputs
prompt = st.text_input("Prompt", placeholder="Enter image description here")
model = st.text_input("Model", placeholder="Enter model type (flux, flux-realism, flux-cablyai, flux-anime, flux-3d, any-dark, flux-pro, turbo)")

# Number inputs for image dimensions and optional seed
width = st.number_input("Width", min_value=64, max_value=2048, value=512)
height = st.number_input("Height", min_value=64, max_value=2048, value=512)
seed = st.number_input("Seed (Optional)", value=42)

# Checkbox inputs
no_logo = st.checkbox("No Logo", value=False)
enhance = st.checkbox("Enhance", value=False)
private = st.checkbox("Private", value=False)

# Button to trigger image generation
if st.button("Generate"):
    # Generate image based on inputs
    generated_image = generate_image(prompt, model, width, height, seed, no_logo, enhance, private)
    
    # Display the generated image
    st.image(generated_image, caption="Generated Image", use_column_width=True)