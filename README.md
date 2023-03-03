# chat-gpt-terminal

Pues eso, un ejemplo utilizando la api de OpenAi, en python plano.  

## Requisitos

* Python 3.10.2 o superior
* una cuenta en OpenAi y una api key [OpenAI](https://platform.openai.com/overview)

## Instalación

Primero ejecuta los siguientes comandos para crear un entorno virtual y activarlo:

    python -m venv env
    env/scripts/activate

Instala las dependencias:
  
    pip install -r requirements.txt

crea un archivo `.env`  en chat-gpt-terminal/ con el siguiente contenido:

    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

donde `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` es tu api key que creaste en la pagina de openai.

## Uso

Ejecuta el script `chat.py`:

    python chat.py

Listo, ya puedes hablar con el bot.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
