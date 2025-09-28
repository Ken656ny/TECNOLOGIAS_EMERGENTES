from transformes import pipeline
import pyttsx3
from traductor import traductor

def gen_text():
    texto = traductor("digite el texto base:","es|en")
    generador= pipeline("text-generation",model="gpt2")
    resultado= generador(texto,max_length=250,num_return_sequences=1,truncation=True)
    texto_generado= resultado[0]['generated_text']
    print("\n texto generado en español :",traductor(texto_generado[0:500],"en|es",0))
    
def traductor_nlp(texto):
    traductor = pipeline("translation",model="helsinki-NLP/opus-mt-es-en")
    texto_en = traductor(texto)[0]['translation_text']
    print("traduccion:",texto_en)
    
def text_to_audio(texto):
    engine= pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volumen", 1.0)
    engine.save_to_file("texto", "output.wav")
    engine.runAndwait()
    print("audio generado: output.wav")
    
def audio_to_text():
    stt= pipeline("automatic-speech-recognition",model="openai/whisper-small")
    audio_path= "audio.mp3"
    resultado = stt(audio_path)
    print("texto transcrito:",resultado["text"])
def traducir():
    texto= "introduzca el texto a traducir"
    while True:
        lang=input("selecione una operacion: \n 1-> español a ingles\n 2-> ingles a español\n 3-> español a portugues\n 4-> portugues a español\n 5-> español a italiano\n 6-> italiano a español\n 7-> español a frances \n 8-> frances a español\n 0-> salir\n opcion: ").strip()
        if lang == '1':
            l = "es|en"
            print(traductor(texto, l))
        elif lang == '2':
            l = "en|es"
            print(traductor(texto, l))
        elif lang == '3':
            l = "es|pt"
            print(traductor(texto, l))
        elif lang == '4':
            l = "pt|es"
            print(traductor(texto, l))
        elif lang == '5':
            l = "es|it"
            print(traductor(texto, l))
        elif lang == '6':
            l = "it|es"
            print(traductor(texto, l))
        elif lang == '7':
            l = "es|fr"
            print(traductor(texto, l))
        elif lang == '8':
            l = "fr|es"
            print(traductor(texto, l))
        elif lang == '0':
            print("Fin traductor")
            break
        else:
            print("Seleccione una opción válida")
