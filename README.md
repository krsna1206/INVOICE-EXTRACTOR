
## 📄 Multilingual Invoice Extractor using Gemini AI

A Streamlit-based web application that extracts and understands information from invoice images (JPG, JPEG, PNG, PDF) using Google Gemini (Generative AI). The app supports multilingual invoices and allows users to ask custom questions about the uploaded invoice.
## ⚠️ NOTE:

    Make sure not to commit .env to GitHub.
## 🚀 Features

📷 Upload invoice images (JPG / JPEG / PNG / PDF)

🌍 Multilingual invoice understanding

🤖 Powered by Google Gemini 2.5 Flash

🧠 Ask custom questions about the invoice

🖼️ Image preview before processing

⚡ Fast and interactive UI using Streamlit
## 🛠️ Tech Stack

➡️Python

➡️Streamlit

➡️Google Generative AI (Gemini)

➡️Pillow (PIL)

➡️dotenv
## 🔐 Environment Setup

1️⃣ Clone the repository

    git clone https://github.com/your-username/multilingual-invoice-extractor.git
    cd multilingual-invoice-extractor
2️⃣ Create and activate virtual environment

    python -m venv venv

    source venv/bin/activate   # For Linux/Mac

    venv\Scripts\activate      # For Windows
3️⃣ Install dependencies:

    pip install -r requirements.txt

🔑 Set Up Environment Variables

  Create a .env file in the root directory:

    GOGGLE_API_KEY=your_google_gemini_api_key
## ▶️ Run the Application:

    streamlit run app.py
## 🧠 How It Works

▫️User uploads an invoice image (or PDF).

▫️Image is converted into binary data.

▫️Gemini model processes the image + prompt.

▫️Extracted and interpreted invoice data is displayed.

▫️User can ask follow-up questions about the invoice.

📸 Supported File Types

    .jpg

    .jpeg

    .png

    .pdf
## 🧪 Example Use Cases

👉Extract invoice total amount

👉Identify vendor name

👉Extract invoice date

👉Understand multilingual invoices

🚀Ask contextual questions like:

 👉"What is the total tax?"

 👉"Who issued this invoice?"