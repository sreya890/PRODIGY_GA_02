# AI Image Generation Project

## Description

This project generates images from text prompts using a
pre-trained Stable Diffusion model.

## Technologies

- Python
- PyTorch
- Hugging Face Diffusers
- Stable Diffusion
- Streamlit
- Google Colab GPU

  ⚙️ System Architecture

The user enters a text prompt through the Streamlit interface.

The frontend sends the prompt to the FastAPI backend.

The backend passes the prompt to the pre-trained Stable Diffusion model.

The model generates an image based on the description.

The generated image is converted into Base64 format and returned through the API.

The frontend decodes and displays the image.

The user can download the generated image.



## Workflow

User enters a text prompt
        ↓
Streamlit interface
        ↓
Stable Diffusion model
        ↓
GPU inference
        ↓
Generated image
        ↓
Display / Save image
