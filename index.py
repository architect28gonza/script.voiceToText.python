
import speech_recognition as sr
recognizer = sr.Recognizer()

def ejecutar_proceso(comando_voz) : 
    print(f"Usted dijo : {comando_voz}")

def escuchar_comandos_voz():
    with sr.Microphone() as source: 
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try :
        texto = recognizer.recognize_google(audio, language="es-ES")
        ejecutar_proceso(texto)
    except Exception as e:
        print("")


while True : 
    escuchar_comandos_voz() 