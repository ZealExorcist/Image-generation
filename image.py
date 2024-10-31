import requests
import gradio as gr
from PIL import Image
from io import BytesIO

def generate_image(prompt, model, width, height, seed, no_logo, enhance, private):

    url = f"https://pollinations.ai/p/{prompt}?width={width}&height={height}&seed={seed}&nologo={no_logo}&enhance={enhance}&private={private}&model={model}"

    response = requests.get(url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    return image

with gr.Blocks() as demo:
    gr.Markdown("## AI Image Generator")

    prompt = gr.Textbox(label="Prompt", placeholder="Enter image description here")
    model = gr.Textbox(label="Model", placeholder="Enter model type (flux, flux-realism, flux-cablyai, flux-anime, flux-3d, any-dark, flux-pro, turbo)")
    width = gr.Number(label="Width", value=512)
    height = gr.Number(label="Height", value=512)
    seed = gr.Number(label="Seed (Optional)", value=42)
    
    no_logo = gr.Checkbox(label="No Logo", value=False)
    enhance = gr.Checkbox(label="Enhance", value=False)
    private = gr.Checkbox(label="Private", value=False)
    
    output_image = gr.Image(label="Generated Image")
    
    generate_button = gr.Button("Generate")
    
    # Define button click action with inputs and outputs
    generate_button.click(generate_image, 
                          inputs=[prompt, model, width, height, seed, no_logo, enhance, private], 
                          outputs=output_image)

demo.launch()
