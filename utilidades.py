import os 
import msvcrt

def clrscr():
    os.system("cls" if os.name== "nt" else 'clear')
def getch():
    print("presione cualquier tecla para continuar ... ")
    msvcrt.getch()