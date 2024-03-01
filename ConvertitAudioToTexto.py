import speech_recognition as sr
import pyaudio
import wave

class Transcribrir : 

    def __init__(self, 
                 formato : pyaudio, 
                 cantidad_canales : int, 
                 tasa_muestreo: int, 
                 tamanio_buffer : int,
                 duracion_grabacion : int,
                 ruta_archivo : str) :
        self.formato = formato
        self.cantidad_canales = cantidad_canales
        self.tasa_muestreo = tasa_muestreo
        self.tamanio_buffer = tamanio_buffer
        self.duracion_grabacion = duracion_grabacion
        self.ruta_archivo = ruta_archivo
        self.duracion_grabacion = duracion_grabacion
        self.ruta_archivo = ruta_archivo


    def grabacion_audio(self):
        try :
            audio = pyaudio.PyAudio()
            stream = audio.open(
                format=self.formato,
                channels=self.cantidad_canales,
                rate=self.tasa_muestreo,
                input=True,
                frames_per_buffer=self.tamanio_buffer
            )
            frames = []
            final : int = self.tasa_muestreo/self.tamanio_buffer * self.duracion_grabacion
            for item in range(0, int(final)):
                data = stream.read(self.tamanio_buffer)
                frames.append(data)

            stream.stop_stream()
            stream.close()
            audio.terminate()

            wf = wave.open(self.ruta_archivo, "wb")
            wf.setnchannels(self.cantidad_canales)
            wf.setsampwidth(audio.get_sample_size(self.formato))
            wf.setframerate(self.tasa_muestreo)
            wf.writeframes(b"".join(frames))
            wf.close()

            resultado = self.transcribir_audio(self.ruta_archivo)
            if resultado["estado"] == "completado" :
                return { "mensaje" : resultado["texto"] }

            return { "mensaje" : "fallado" }

        except Exception as e:
            raise NameError(f"Ha ocurrido un error al momento de graabar el audio {e}")
        

    def transcribir_audio(self, ruta_archivo):
        try :
            r = sr.Recognizer()
            archivo_audio = sr.AudioFile(ruta_archivo)
            with archivo_audio as source:
                audio = r.record(source)
            texto = r.recognize_google(audio, language="es-ES")
            if texto :
                return {
                    "estado" : "completado",
                    "texto" : texto
                }
            return {
                "estado" : "Fallido",
                "mensaje" : "No se pudo transcribir"
            }
        except Exception as e:
            raise NameError(f"Ha ocurrido un error al momento de graabar el audio {e}")

formato = pyaudio.paInt16
canales = 2
tasa_muestreo = 16000  # Reducido de 44100 a 16000
tamanio_buffer = 2048  # Ajustado para equilibrar entre latencia y eficiencia
duracion = 3
ruta_archivo = "audio.wav"

transcribir = Transcribrir(formato,canales,tasa_muestreo,tamanio_buffer,duracion,ruta_archivo)
print(transcribir.grabacion_audio())
