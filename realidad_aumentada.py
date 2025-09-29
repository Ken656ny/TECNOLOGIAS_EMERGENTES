import cv2  # Importa la librería OpenCV para procesamiento de imágenes
import numpy as np  # Importa NumPy para operaciones con matrices
import os

# ==========================
# Menú principal
# ==========================
def menu_ar():
    try:
        while True:
            opt = input(
                "Seleccione una operación:\n"
                "1 -> Generar marcadores ArUco\n"
                "2 -> Leer marcadores ArUco\n"
                "0 -> Salir\n"
                "Opción: "
            ).strip()

            if opt not in {'0', '1', '2'}:
                print("Seleccione una opción válida (0, 1, 2).")
                continue

            if opt == '1':
                generador_aruco()
            elif opt == '2':
                realidad_aumentada()
            elif opt == '0':
                print("Fin AR")
                break

    except KeyboardInterrupt:
        print("\nInterrupción detectada. Saliendo del menú.")
    except EOFError:
        print("\nEntrada no disponible. Saliendo del menú.")


# ==========================
# Generador de marcadores
# ==========================
def generador_aruco():
    """
    Genera y guarda imágenes de marcadores ArUco en el disco utilizando el diccionario 4x4_50.
    """

    output_dir = "marcadores"
    os.makedirs(output_dir, exist_ok=True)

    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

    for id_marker in range(6):  # Genera 6 marcadores
        img = cv2.aruco.generateImageMarker(aruco_dict, id_marker, 400)
        cv2.imwrite(f"{output_dir}/marker_{id_marker}.png", img)

    print("[OK] Marcadores generados exitosamente.")


# ==========================
# Realidad Aumentada
# ==========================
def realidad_aumentada():
    """
    Detecta marcadores ArUco en tiempo real desde una cámara y superpone imágenes específicas
    sobre cada marcador reconocido utilizando una transformación con homografía.
    """

    imagenes = {
        0: cv2.imread("/imagenes/java.jpg"),
        1: cv2.imread("/imagenes/javascript.jpg"),
        2: cv2.imread('/imagenes/sena.png'),
        3: cv2.imread('/imagenes/vscode.jpg'),
        4: cv2.imread('/imagenes/xamp.jpg'),
        5: cv2.imread('/imagenes/pyhon.png'),
    }

    for id_img, img in imagenes.items():
        if img is None:
            print(f"Error: No se pudo cargar la imagen asociada al ID {id_img}")
            return

    # Diccionario y parámetros de ArUco
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    parameters = cv2.aruco.DetectorParameters()

    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

    # Inicializa la cámara
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("No se pudo abrir la cámara.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detecta marcadores
        corners, ids, _ = detector.detectMarkers(frame)

        if ids is not None:
            for corner, marker_id in zip(corners, ids.flatten()):
                if marker_id in imagenes:
                    img_to_overlay = imagenes[marker_id]

                    pts_dst = np.array(corner[0], dtype="float32")

                    h, w = img_to_overlay.shape[:2]

                    pts_src = np.array([
                        [0, 0],
                        [w - 1, 0],
                        [w - 1, h - 1],
                        [0, h - 1]
                    ], dtype="float32")

                    matrix, _ = cv2.findHomography(pts_src, pts_dst)

                    warped_image = cv2.warpPerspective(img_to_overlay, matrix, (frame.shape[1], frame.shape[0]))

                    mask = np.zeros((frame.shape[0], frame.shape[1]), dtype="uint8")
                    cv2.fillConvexPoly(mask, pts_dst.astype(int), 255)

                    mask_inv = cv2.bitwise_not(mask)

                    frame_bg = cv2.bitwise_and(frame, frame, mask=mask_inv)

                    frame = cv2.add(frame_bg, warped_image)

        cv2.imshow("Realidad Aumentada", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


# ==========================
# Ejecución principal
# ==========================
if __name__ == "__main__":
    menu_ar()
