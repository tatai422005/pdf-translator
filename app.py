from flask import Flask, render_template, request, url_for
import fitz  # PyMuPDF
from googletrans import Translator
from gtts import gTTS
import gtts.lang
import os
import time
from httpcore._exceptions import ReadTimeout

app = Flask(__name__, template_folder="templates")

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def translate_text_with_retry(text, dest_language, retries=3):
    translator = Translator()
    attempts = 0
    while attempts < retries:
        try:
            translated = translator.translate(text, dest=dest_language)
            return translated.text
        except ReadTimeout:
            attempts += 1
            time.sleep(1)  # Wait for 1 second before retrying
            if attempts == retries:
                return None  # Return None if translation fails

def text_to_speech_with_retry(text, lang_code, output_file, retries=3):
    attempts = 0
    while attempts < retries:
        try:
            tts = gTTS(text=text, lang=lang_code)
            tts.save(output_file)
            return output_file
        except ReadTimeout:
            attempts += 1
            time.sleep(1)
            if attempts == retries:
                return None  # Return None if TTS fails

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Save the uploaded PDF file
        pdf_file = request.files["pdf"]
        pdf_path = os.path.join("uploads", pdf_file.filename)
        pdf_file.save(pdf_path)

        # Get the destination language from user input
        dest_language = request.form["language"]

        # Extract text from the PDF
        extracted_text = extract_text_from_pdf(pdf_path)

        # Translate the extracted text to the selected language
        translated_text = translate_text_with_retry(extracted_text, dest_language)

        if translated_text is None:
            # Translation failed after retries
            return render_template("error.html", message="Translation failed due to timeout. Please try again later.")

        # Convert the original text to speech (default in English)
        original_voice_file = text_to_speech_with_retry(extracted_text, lang_code='en', output_file="static/original_output.mp3")

        # Convert the translated text to speech
        translated_voice_file = text_to_speech_with_retry(translated_text, lang_code=dest_language, output_file="static/translated_output.mp3")

        if original_voice_file is None or translated_voice_file is None:
            # TTS conversion failed after retries
            return render_template("error.html", message="Text-to-Speech conversion failed. Please try again later.")

        # Return the original text, translated text, and audio file URLs
        return render_template("result.html",
                               original_text=extracted_text,
                               translated_text=translated_text,
                               original_voice_url=url_for('static', filename='original_output.mp3'),
                               translated_voice_url=url_for('static', filename='translated_output.mp3'))

    # Get the list of supported languages for text-to-speech
    supported_languages = gtts.lang.tts_langs()
    return render_template("index.html", languages=supported_languages)

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)