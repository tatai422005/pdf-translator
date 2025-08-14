Translation-Capabilities
🧠 Overview
This project delivers an intelligent and accessible web application that extracts text from PDF files and converts it into high-quality audio, supporting multiple languages and real-time translation. It is designed to promote inclusivity and accessibility, helping users with visual impairments, reading difficulties, or language barriers consume document content through natural-sounding speech.

Whether you're a student, researcher, or someone who prefers auditory learning, this tool makes it easy to listen to content from PDFs in your native or preferred language, all through an intuitive web interface built with Flask.

🚀 Features
🌍 Multilingual Translation
Seamlessly translates extracted text using the Google Translate API, supporting a wide range of global languages.

📄 PDF Text Extraction
Efficiently extracts clean, readable text from PDFs—including multi-page and complex formats—using PyMuPDF (fitz).

🔊 Text-to-Speech (TTS) Conversion
Converts both original and translated text into clear, natural audio using Google Text-to-Speech (gTTS).

🖥️ Web-Based Interface
A user-friendly Flask web application that allows users to upload PDFs, choose languages, and play or download the resulting audio.

📱 Cross-Platform Compatibility
Works smoothly on desktops, tablets, and mobile devices, ensuring consistent user experience across platforms.

⚙️ Installation
🧩 Prerequisites
Ensure you have the following installed:

Python 3.8+
pip (Python package installer)
📦 Required Libraries
Flask
PyMuPDF (fitz)
gTTS
googletrans (or compatible Google Translate wrapper)
🛠️ Setup Instructions
Clone the repository:

git clone https://github.com/arpan12345seth/Multilingual-PDF-Text-to-Speech-Converter-with-Translation-Capabilities.git
cd Multilingual-PDF-Text-to-Speech-Converter-with-Translation-Capabilities
Install the dependencies:

pip install -r requirements.txt
Run the application:

python app.py
Access the web platform:
Open your browser and go to:
http://127.0.0.1:5000

🎯 Use Cases
Visually impaired users who rely on audio formats.
Language learners looking to practice listening and pronunciation.
Multitaskers who prefer to listen while working.
Researchers or students consuming academic papers on the go.
🧩 Future Enhancements
Add support for OCR-based text extraction for scanned PDFs.
Enable offline translation and speech synthesis.
Implement voice customization (pitch, speed, accents).
Add cloud storage options for uploaded files.
