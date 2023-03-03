import openai
from dotenv import load_dotenv
import os
import datetime

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene la clave de API desde las variables de entorno
key = os.getenv("OPENAI_API_KEY")

# Asigna la clave de API a la variable api_key del módulo openai
openai.api_key = key

# Crea una lista vacía para almacenar los mensajes de la conversación
mensajes = []

# Pide al usuario el tipo de bot con el que quiere conversar y lo agrega a la lista de mensajes
system_msg = input("¿Con qué tipo de bot te gustaría conversar?\n ")
mensajes.append({"role": "system", "content": system_msg})

# Pide al usuario que comience la conversación y crea un bucle para continuarla hasta que el usuario escriba "salir"
print("Dile algo!")

while True: 
    mensaje = input()
    if mensaje == "salir":
        break
    
    # Agrega el mensaje del usuario a la lista de mensajes
    mensajes.append({"role": "user", "content": mensaje})
    
    # Utiliza la función ChatCompletion de la API de OpenAI para generar una respuesta del bot
    resultado = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mensajes)
    
    # Obtiene la respuesta generada por el bot y la agrega a la lista de mensajes
    respuesta = resultado["choices"][0]["message"]["content"]
    mensajes.append({"role": "assistant", "content": respuesta})
    
    # Imprime la respuesta del bot
    print("\n" + respuesta + "\n")

# Obtiene la fecha y hora actual y crea un archivo de texto con el historial de la conversación
now = datetime.datetime.now()
historial = open("Historial/{}.txt".format(now.strftime("%Y%m%d %H%M%S")), "w")