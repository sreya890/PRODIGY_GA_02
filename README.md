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


 Prerequisites

Python 3.10 or a compatible Python version

pip package manager

A Hugging Face account if model access requires authentication

A Google account to run the backend on Google Colab

An ngrok account or authentication token for exposing the API endpoint


 Installation and Setup

1. Clone the Repository

git clone https://github.com/YOUR-USERNAME/AI-Image-Generator.git
cd AI-Image-Generator

Replace YOUR-USERNAME with your GitHub username and use your actual repository name.

2. Create a Virtual Environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Start the Image Generation Backend

Open colab_backend.ipynb in Google Colab.

Select a GPU runtime if available.

Install the required backend dependencies.

Configure your ngrok authentication token securely.

Run the notebook cells to load Stable Diffusion and start the FastAPI server.

Copy the active ngrok URL provided by the notebook.

The backend must remain running while generating images.

5. Configure the API URL

Set the active backend URL in your environment before starting Streamlit.

In PowerShell:

$env:API_URL="https://YOUR-ACTIVE-NGROK-URL"

Use the URL provided by your current Colab session. Do not include /generate if your application already appends that endpoint.

6. Run the Streamlit Application

streamlit run app.py

Open the local URL displayed in your terminal, usually http://localhost:8501.

Enter an image description and click the generate button to create an image.

💡 Example Prompts

A futuristic city with flying cars at sunset.

A realistic tiger walking through a dense forest.

A robot assisting humans in a modern laboratory.

A peaceful mountain landscape with a lake and sunrise.

A fantasy castle floating above the clouds.
