from hashlib import sha256  # Genera hashes seguros de los bloques
from datetime import datetime, timezone  # Para obtener marcas de tiempo con zona horaria UTC
import time  # Para medir el tiempo que tarda el proceso de minería

########################## Inicio cadena de bloques ##########################
# Clase que representa una transacción entre dos personas
class Transaccion:
    def __init__(self, emisor, receptor, cantidad):
        self.emisor = emisor      # Persona que envía
        self.receptor = receptor  # Persona que recibe
        self.cantidad = cantidad  # Cantidad enviada

    def __str__(self):
        # Representación en texto de la transacción
        return f"{self.emisor} le envía {self.cantidad} a {self.receptor}"


# Lista de transacciones para el primer bloque
transacciones_bloque1 = [
    Transaccion("Jose", "Jorge", 5),
    Transaccion("Jorge", "Jairo", 10),
    Transaccion("Jorge", "Daniela", 4)
]

# Lista de transacciones para el segundo bloque
transacciones_bloque2 = [
    Transaccion("Jose", "Jairo", 5),
    Transaccion("Juan", "Jairo", 10),
    Transaccion("Jorge", "Jose", 4)
]

# Clase que representa un bloque de la cadena
class Bloque:
    def __init__(self, bloque_anterior, transacciones):
        self.bloque_anterior = bloque_anterior  # Hash del bloque anterior
        self.transacciones = transacciones      # Lista de objetos Transaccion
        self.timestamp = datetime.now(timezone.utc).isoformat()  # Marca de tiempo en UTC
        self.intento_hash = 0  # Nonce: número de intentos para encontrar el hash válido

    def calcular_hash(self):
        """Calcula el hash del bloque combinando transacciones, bloque anterior, tiempo e intento"""
        transacciones_str = " ".join(str(t) for t in self.transacciones)  # Convierte las transacciones a texto
        info = transacciones_str + self.bloque_anterior + self.timestamp + str(self.intento_hash)
        return sha256(info.encode()).hexdigest()  # Devuelve el hash SHA-256
# Clase que representa la cadena completa de bloques
class Blockchain:
    dificultad = 5  # Nivel de dificultad: número de ceros que debe tener el hash válido al inicio

    def __init__(self):
        self.cadena = []  # Lista de bloques que forma la cadena

    def agregar_bloque(self, bloque):
        """Agrega un bloque minado a la cadena"""
        self.cadena.append(bloque)

    def minar_bloque(self, bloque):
        """Ejecuta el proceso de minería para encontrar un hash válido para el bloque"""
        inicio = time.time()  # Marca de tiempo inicial para medir el tiempo de minería
        while True:
            hash_actual = bloque.calcular_hash()
            if hash_actual.startswith("0" * self.dificultad):  # Verifica si el hash cumple con la dificultad
                self.agregar_bloque(bloque)  # Agrega el bloque si es válido
                print(f"\nBloque minado con éxito: {hash_actual}")
                print(f"Nonce encontrado: {bloque.intento_hash}")
                print(f"Tiempo de minado: {round(time.time() - inicio, 2)} segundos\n")
                break
            else:
                bloque.intento_hash += 1  # Aumenta el nonce hasta encontrar un hash válido

    def verificar_integridad(self):
        """Verifica que todos los bloques estén correctamente encadenados"""
        for i in range(1, len(self.cadena)):
            bloque_actual = self.cadena[i]
            bloque_anterior = self.cadena[i - 1]

            # Compara el hash almacenado con el recalculado del bloque anterior
            if bloque_actual.bloque_anterior != bloque_anterior.calcular_hash():
                return False  # Si no coinciden, la cadena ha sido manipulada
        return True  # Todo está en orden


def cadena_bloques():
    """
    Crea una cadena de bloques simple, mina dos bloques con un conjunto de transacciones
    y verifica la integridad de la cadena resultante.

    Proceso:
    1. Inicializa una instancia de Blockchain vacía.
    2. Crea el bloque génesis (primer bloque) con un hash anterior ficticio de 64 ceros.
    3. Mina el primer bloque (prueba de trabajo).
    4. Crea un segundo bloque que depende del hash del primero.
    5. Mina el segundo bloque.
    6. Verifica si la cadena de bloques es íntegra (sin alteraciones).

    Salida:
    Imprime en consola si la cadena es íntegra o ha sido alterada.
    """
    # Se crea la blockchain
    mi_blockchain = Blockchain()

    # Se crea y mina el primer bloque (bloque génesis)
    bloque1 = Bloque("0" * 64, transacciones_bloque1)  # Hash anterior ficticio de 64 ceros
    mi_blockchain.minar_bloque(bloque1)

    # Se crea y mina el segundo bloque, usando el hash del primero
    bloque2 = Bloque(mi_blockchain.cadena[-1].calcular_hash(), transacciones_bloque2)
    mi_blockchain.minar_bloque(bloque2)

    # Se verifica si la cadena es válida
    print("¿Cadena íntegra?:", mi_blockchain.verificar_integridad())


# Ejecutar la demo
cadena_bloques()
