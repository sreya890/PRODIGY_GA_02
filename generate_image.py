# generate_image.py

import torch
from diffusers import StableDiffusionPipeline


MODEL_ID = "stable-diffusion-v1-5/stable-diffusion-v1-5"


# Load the Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16,
    use_safetensors=True
)

# Use GPU
pipe = pipe.to("cuda")


def generate_image(prompt):
    """
    Generate an image from a text prompt.
    """

image = pipe(
    prompt,
    negative_prompt="blurry, low quality, distorted, deformed, artifacts",
    num_inference_steps=40,
    guidance_scale=7.5
).images[0]

    return image


