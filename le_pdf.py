import pdfplumber as pp 
from gtts import gTTS

texto_pdf = ''

with pp.open("cms.pdf") as pdf:
    for page in pdf.pages:
        texto_pdf += page.extract_text()


print(texto_pdf)
tts = gTTS(text = texto_pdf, lang='pt')
tts.save('audio.mp3')