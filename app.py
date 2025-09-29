# app.py
from utilidades import clrscr, getch
from web_scraping import scraping
from operaciones_texto import traducir, audio_to_text, text_to_audio
from operaciones_texto import traductor_nlp, gen_text
from generar_imagen import generar_imagen
from blockchain import cadena_bloques
from codigos_qr import menu_qr
from realidad_aumentada import menu_ar

def main():
    while True:
        clrscr()
        option = input(
            "Seleccione una opción:\n"
            "---- Tecnologías emergentes y disruptivas ----\n"
            "1 -> Web scraping\n"
            "2 -> Traducir texto\n"
            "3 -> Generar imagen\n"
            "4 -> Audio a texto\n"
            "5 -> Texto a audio\n"
            "6 -> Procesamiento del lenguaje natural\n"
            "7 -> Generar texto\n"
            "8 -> Blockchain\n"
            "9 -> Códigos QR\n"
            "10 -> Realidad aumentada\n"
            "0 -> Salir\n"
            "Opción: "
        ).strip()

        match option:
            case '1':
                scraping()
                getch()
            case '2':
                traducir()
                getch()
            case '3':
                generar_imagen()
                getch()
            case '4':
                audio_to_text()
                getch()
            case '5':
                texto = input("Digite el texto a convertir: ")
                text_to_audio(texto)
                getch()
            case '6':
                texto = input("Digite el texto a convertir: ")
                traductor_nlp(texto)
                getch()
            case '7':
                gen_text()
                getch()
            case '8':
                cadena_bloques()
                getch()
            case '9':
                menu_qr()
                getch()
            case '10':
                menu_ar()
                getch()
            case '0':
                print("Bye")
                getch()
                break
            case _:
                print("Seleccione opción válida")
                getch()

if __name__ == "__main__":
    main()
