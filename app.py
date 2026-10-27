import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO


API_URL = "https://disarray-overeager-junction.ngrok-free.dev/generate"
st.write("API URL:", API_URL)


st.title("🎨 AI Image Generator")

prompt = st.text_input(
    "Enter your image prompt",
    placeholder="Example: A futuristic city at sunset"
)


if st.button("Generate Image"):

    if prompt:

        with st.spinner("Generating image..."):

            response = requests.post(
                API_URL,
                json={"prompt": prompt},
                timeout=180
            )

        if response.status_code == 200:

            data = response.json()

            image_bytes = base64.b64decode(
                data["image"]
            )

            image = Image.open(
                BytesIO(image_bytes)
            )

            st.image(
                image,
                caption=prompt,
                    
            )

        else:

            st.error(
                f"API Error: {response.status_code}"
            )

    else:

        st.warning("Please enter a prompt.")