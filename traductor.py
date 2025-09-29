
import requests  # Importa requests para hacer peticiones HTTP

def traductor(txt, lan_origen="es", lan_destino="en", entrada=1):
    """
    Traduce un texto de un idioma a otro usando la API gratuita de MyMemory.
    
    Parámetros:
        txt (str): Mensaje para solicitar al usuario el texto a traducir.
        lan_origen (str): Idioma de origen. Ejemplo: "es", "en", "fr", "it".
        lan_destino (str): Idioma de destino. Ejemplo: "en", "es", "fr", "de".
        entrada (int): 1 -> Solicita texto al usuario | 0 -> Usa txt directamente.
    
    Retorna:
        str: Texto traducido o el original si ocurre un error.
    """
    try:
        # Si entrada es 1, se pide texto por teclado
        if entrada == 1:
            entrada = input(f"{txt}: ")
        else:
            entrada = txt

        # URL de la API
        url = "https://api.mymemory.translated.net/get"
        
        # Parámetros de la petición
        params = {"q": entrada, "langpair": f"{lan_origen}|{lan_destino}"}
        
        # Se hace la petición GET
        response = requests.get(url, params=params)
        response.raise_for_status()  # Lanza error si la API falla

        # Extrae el texto traducido del JSON de respuesta
        texto_traducido = response.json()["responseData"]["translatedText"]

        # Retorna el texto traducido
        return texto_traducido

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error en la traducción: {e}")
        # Devuelve el texto original si falla la traducción
        return entrada


# Ejemplos de uso
print(traductor("Escribe algo para traducir", "es", "en", entrada=1))  # Usuario escribe en español → inglés
print(traductor("Hola mundo", "es", "fr", entrada=0))  # Traduce directamente de español → francés
print(traductor("Good morning", "en", "es", entrada=0))  # Traduce directamente de inglés → español
