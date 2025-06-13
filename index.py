#Esto esta solo para probar algunas cositas antes de impentar en el juego base, ademas de algunos apuntes, recuerdos o ascci.

#                                            La odisea chilena (1883-1893)

#Dia 1: Refactorizar la historia por tercera vez y arreglar bugs con la parte de elecciones del jugador.
#Dia 2: No avances, estuve jugando RimWorld.
#Dia 3: Jaja otro dia sin avances.
#Dia 4: jugar solo RimWorld otro día mas.
#Dia 5: Bueno esta vez si trabaje, estuve con el arte ascci de finales, tambien probando GitHub.
#Dia 6: Termine el capitulo 2 y arreglos de algunos bugs.
#Dia 7: Trabajando en el capitulo 3 y limpiando el codigo un poquito.
#Dia 8: Termine el capitulo 3 y estoy con el 4 capitulo.
#Dia 9: No hubo avanze por tareas con la secundaria. Solo un poco con el 4 capitulo.
#Dia 10: Agrege la guia de controles y agrege las imagenes para los finales.
#Dia 11: Trabaje en el capitulo 4, retrasos tambien por la secundaría.
#Dia 12: Probando el pyinstaller y haciendolo funcionar para pasar de .py a .exe. tambien se agrego el icono.
#Dia 13: Se investiga y programa para ver si es posible crear el siguiente proyecto. No cambios es este proyecto hoy.
#Dia 14: Se termina la historia, Correcion de ortografia y de sentido en el capitulo 1 y cambios en el index. 













#Librerias
import time ; import sys ; import msvcrt ; import keyboard
from colorama import Fore, Style

#Graficos
def men_normal():
    print(Fore.BLUE + Style.BRIGHT,end="")
    print("            ▒▒▒▓███████████▓▒           ")
    print("        ▒██████████▓▓▓▓██▓████▓         ")
    print("      ▒███████▓█▓▓▓█▓█▓███▓▓▓███        ")
    print("     ▓███▓██▓▓████▓██▓█▓▓▓███▓██▒       ")
    print("     ▓██▓███▓█▓████████▓▓█████▓██       ")
    print("     ▒█████████▓▓▓███████████████▒      ")
    print("     ▒██████▓█████▒▒▒▒▒██████████▒      ")
    print("     ▒███████▓█▓█▒     ░▒▓█▓▓▒▒██▒      ")
    print("     ▒█████████▓█▓░░▒▒░░░░░▒▒▒▒██▒      ")
    print("     ▒████████████▒░▒▒▒▒▒▒▒▒▒▒▒▓█▒      ")
    print("     ▒██████████▓▓▓▒▒▒▒▒▒▒▒▒▒▒░▓█▒      ")
    print("     ▒███████▓███▓▒▒▒▒▒▒▒▒▒▒▒▒░▒▓▒      ")
    print("     ▓█▒░░▓██▓█▓▒▒▒▒░░░░░░░░░░░▒█▒      ")
    print("     ▓█▒▒▒░▒███▒░░▒░░░▒▒▒▒▒█▓█████      ")
    print("     ██░▒██▒▒████▒░▓██████████████      ")
    print("     ▒█▒▒▒▓▒░▓█▓███████████▒▒█████      ")
    print("      ▒█ ░░▒▒▒█▒▒▒▒█▓██████░ ████       ")
    print(" ▒▓███▓██░░▒▒▒▒▒▒▒▒██████▓▒░░▒██▒       ")
    print("██████████▓█▒▒▒▒▒▒▒▒█▓▒▒▒▒░░░ ░█        ")
    print("█████████▓▓█▓▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▓▓▒░▒█      ")
    print("██████████▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒░▒▓██▓▒█      ")
    print("▓▓█▓████▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▓▓▓██     ")
    print("██▓▒██▒░░▒▓▒▒▒▓█▓▒▒▒▒▒▒█████▒▒▓███      ")
    print("█▓▒█▓░░▒▒▒▒▒▒▒▒▒▓▓▒▒▓▒▒░░░▒▒▒▒█████     ")
    print("▓▓██░░▒▒▒▒▒▒▒▒▓▒▒▓▓▓▒▒▒▒▒▓██▓▓██████    ")
    print("▓██▒░▒▒▒▒▒▒▒▒▒▓▓▓▓▓██▓▒▒▒░▒░▒█████▓██   ")
    print("▓▓█▒░▒▒▒▒▒▒▓▒▒▒▓▓██████▓▒▒▒▒█████▓▓██░  ")
    print("█▓█▒░▒▒▒▒▒▒▒▒▒▓▓▓▓████████▓▒████▓██▓██  ")
    print("▓██▒░▒░▒░░░▒▒▒▒▒▒▒▓▓████▓▒▒▒███▓▓█▓▓▓█  ")
    print(Fore.BLACK + Style.DIM,end="")
    print(Style.RESET_ALL,end="")
    time.sleep(0.2)

#Sistema de dialogos
def dialogue(mensaje):
    for letra in mensaje:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.02)
    msvcrt.getch()

#Pantalla completa y zoom
def borderland():
    keyboard.press_and_release("f11")
    for _ in range(5):
        keyboard.press_and_release("ctrl+plus")
        time.sleep(0.01)

borderland()
men_normal()
dialogue("""¡Oye tú! ¿Crees que eres bueno en algo? ¿Piensas que tienes la mente más rápida que la mía? ¡Ja! Me da la risa.He estado practicando mis estrategias secretas y mis movimientos maestros... Y déjame decirte, ¡estoy lista! Así que, te reto, sí, a ti, a una partida de tres en raya.No te asustes, eh. Solo quiero ver si tienes lo necesario para ganarle a la campeona. Pero te advierto, no me ando con chiquitas. ¡Vas a tener que esforzarte mucho si quieres ver cómo le pongo una "X" a tu "O"!¿Aceptas el reto o te vas a acobardar? ¡Dime cuándo y dónde!""")


