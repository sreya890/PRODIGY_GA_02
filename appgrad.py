import gradio as gr
import requests
import base64
from PIL import Image
from io import BytesIO


# Your Colab ngrok API
API_URL = "https://disarray-overeager-junction.ngrok-free.dev/generate"


def generate_image(prompt):

    if not prompt:
        return None

    response = requests.post(
        API_URL,
        json={"prompt": prompt},
        timeout=180
    )

    if response.status_code != 200:
        raise Exception(
            f"API Error: {response.status_code}"
        )

    data = response.json()

    image_bytes = base64.b64decode(
        data["image"]
    )

    image = Image.open(
        BytesIO(image_bytes)
    )

    return image


demo = gr.Interface(
    fn=generate_image,

    inputs=gr.Textbox(
        label="Enter your image prompt",
        placeholder="Example: A futuristic city at sunset",
        lines=2
    ),

    outputs=gr.Image(
        label="Generated Image"
    ),

    title="🎨 AI Image Generator",

    description=(
        "Generate images from text prompts "
        "using Stable Diffusion."
    ),

    examples=[
        ["A cute golden retriever sitting on a beach at sunset"],
        ["A futuristic city with flying cars"],
        ["A magical forest with glowing flowers"]
    ]
)


demo.launch()