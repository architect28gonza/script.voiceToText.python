# Transcribir Audio a Texto en Python

Este proyecto permite grabar audio desde un dispositivo de entrada (como un micrófono), guardar el audio en un archivo WAV y luego transcribir el audio a texto utilizando la API de Google Speech Recognition.
Requisitos Previos

Antes de comenzar, asegúrate de tener Python instalado en tu sistema. Este proyecto fue desarrollado usando Python 3.x. Además, necesitarás instalar las siguientes bibliotecas:

    PyAudio: Para acceder al micrófono y grabar audio.
    SpeechRecognition: Para transcribir el audio a texto.
    wave: Para leer y escribir archivos WAV.

Puedes instalar todas las dependencias necesarias ejecutando el siguiente comando:

```
pip install pyaudio SpeechRecognition wave
```

## Instalación
Para usar este proyecto, primero clona el repositorio o descarga el código fuente a tu sistema local. No hay pasos de instalación adicionales necesarios, siempre y cuando tengas instaladas las bibliotecas mencionadas anteriormente.

##  Uso
Para utilizar el script, necesitas crear una instancia de la clase Transcribrir con los parámetros apropiados para tu configuración de grabación. Aquí tienes un ejemplo de cómo configurarlo:

```python
from transcribir import Transcribrir
import pyaudio

formato = pyaudio.paInt16
canales = 2
tasa_muestreo = 16000  # Frecuencia de muestreo
tamanio_buffer = 2048  # Tamaño del buffer
duracion = 3  # Duración de la grabación en segundos
ruta_archivo = "audio.wav"  # Ruta donde se guardará el archivo de audio

transcribir = Transcribrir(formato, canales, tasa_muestreo, tamanio_buffer, duracion, ruta_archivo)
```

Después, puedes llamar al método grabacion_audio para iniciar la grabación y la transcripción:
```python
resultado = transcribir.grabacion_audio()
print(resultado)
```

Ejemplo de Ejecución
```
python tu_script.py
```

Reemplaza tu_script.py con el nombre de tu archivo Python que contiene el código principal.
## Notas Adicionales
Asegúrate de tener un micrófono conectado y configurado correctamente en tu sistema.
La API de Google Speech Recognition es gratuita, pero tiene límites en la cantidad de solicitudes que puedes hacer. Consulta la documentación oficial para más detalles.