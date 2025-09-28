import qrcode  # Para generar códigos QR
import cv2     # Para leer QR desde imágenes o cámara


def gen_qr():
    """Genera un código QR a partir de una entrada digitada"""
    data = input("Digite la entrada para el código QR: ")

    # Crear código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Crear imagen
    img = qr.make_image(fill="black", back_color="white")
    img.save("codigo_gr.png")
    print("✅ Código QR generado y guardado como 'codigo_gr.png'")



def leer_qr_img():
    """Lee un código QR desde una imagen"""
    imagen = cv2.imread("codigo_gr.png")

    detector = cv2.QRCodeDetector()
    data, vertices, rectified_qr = detector.detectAndDecode(imagen)

    if data:
        print(f" Contenido del QR: {data}")
        print(f" Primer elemento del QR: {data.split()[0]}")
    else:
        print(" No se detectó ningún código QR en la imagen.")



def leer_qr_cam():
    """Lee un código QR en tiempo real usando la cámara"""
    cap = cv2.VideoCapture(0)  # 0 = cámara por defecto
    detector = cv2.QRCodeDetector()

    print("Escaneando... presiona 'q' para salir.")

    while True:
        _, frame = cap.read()
        data, bbox, _ = detector.detectAndDecode(frame)

        if bbox is not None:
            # Dibujar polígono verde alrededor del QR
            cv2.polylines(frame, [bbox.astype(int)], True, (0, 255, 0), 2)

            if data:
                print(f" QR detectado: {data}")
                print(f" Primer elemento del QR: {data.split()[0]}")

        cv2.imshow("Escáner QR", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def menu_qr():
    try:
        while True:
            opt = input(
                "\nSeleccione una operación:\n"
                "1 -> Generar QR\n"
                "2 -> Leer QR desde imagen\n"
                "3 -> Leer QR desde cámara\n"
                "0 -> Salir\n"
                "Opción: "
            ).strip()

            if opt not in {"0", "1", "2", "3"}:
                print(" Seleccione una opción válida (0, 1, 2 o 3).")
                continue

            if opt == "1":
                gen_qr()
            elif opt == "2":
                leer_qr_img()
            elif opt == "3":
                leer_qr_cam()
            elif opt == "0":
                print(" Fin del programa QR.")
                break

    except KeyboardInterrupt:
        print("\n Interrupción detectada. Saliendo del menú.")
    except EOFError:
        print("\n Entrada no disponible. Saliendo del menú.")