# from tkinter import Image
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
from google import genai
import mimetypes

#setting up geimini model
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL_ID = "gemini-2.5-flash" 

#defing gemini response
def get_gemini_response(user_input, image_data, prompt):
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[user_input, image_data, prompt],
    )
    return response.text


#setting up image as input to pdf,jpg ,jpeg format
def input_image_setup(uploaded_file):
    if uploaded_file is None:
        return None

    mime_type, _ = mimetypes.guess_type(uploaded_file.name)
    img_bytes = uploaded_file.getvalue()

    return {
        "inline_data": {
            "mime_type": mime_type,
            "data": img_bytes
        }
    }

#initializing our streamlit app

st.set_page_config(page_title="MULTTILINGUAL INVOICE EXTRACTOR")
st.header("MULTILANGUAGE INVOICE EXTRACTOR")

input = st.text_input("INPUT PROMPT: ",key="input")
uploaded_file = st.file_uploader(
    "CHOOSE AN IMAGE OF INVOICE (JPG, JPEG, PNG, PDF)",
    type=["jpg", "jpeg", "png", "pdf"]
)
image = ""

if uploaded_file is not None:
    try: 
        image = Image.open(uploaded_file)
        st.image(image,caption="uploaded image. ", use_column_width=True)
    except Exception:
        st.warning("THIS FILE CAN'T BE PREVIEWED AS IMAGE")


submit = st.button("TELL ME ABOUT THE INVOICE")
#predefined prompt in order to get better output
input_prompt = """
You are an expert Understanding ivoices. We will upload a image as invoice and you will have to answer any questions based on the uploaded 
imvoices image """

# Handle submit
if submit and uploaded_file is not None:
    image_data = input_image_setup(uploaded_file)
    if image_data:
        try:
            response = get_gemini_response(input, image_data, input_prompt)
            st.subheader("The response is")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
