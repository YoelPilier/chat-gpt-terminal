import openai
from dotenv import load_dotenv
import os

load_dotenv()
key=os.getenv("OPENAI_API_KEY")

openai.api_key = key

     
mensajes = []
system_msg = input("¿Con qué tipo de bot te gustaría conversar?\n ")
mensajes.append({"role": "system", "content": system_msg})

print("Dile algo!")
while True: 
    mensaje = input()
    if mensaje == "salir":
        break
    mensajes.append({"role": "user", "content": mensaje})
    resultado = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mensajes)
    respuesta = resultado["choices"][0]["message"]["content"]
    mensajes.append({"role": "assistant", "content": respuesta})
    print("\n" + respuesta + "\n")
