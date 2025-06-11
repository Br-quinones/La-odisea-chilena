#Esto esta solo para probar algunas cositas antes de impentar en el juego base, ademas de algunos apuntes, recuerdos o ascci.

#                                            #La odisea chilena (1883-1893)

#            _____
#        /\ /_____\
#       /\/ \     /
#      / /   \_-_/ 
#      \ \ """"V"//""\
#       \__    |//   \
#          |   //  |\ \
#          |  //   | \ \
#          | //|   | / /
#          |// |   |/\/
#          |==[0]==|\/
#          |   |   |
#          |   |   |
#          |   |   |
#          |   |   |
#          |   |   |
#          |___|___|
#           |_ | _|
#          (___|___)
#         
#         ╔   ╗
#    ╔     ███╚    ╗
#       ║███████║
#    ╚    ╗███╔    ╝
#         ╚   ╝║
#        
#                                                        
#███████╗██╗███╗   ██╗ █████╗ ██╗         ███████╗        
#██╔    ╝██║████╗  ██║██╔  ██╗██║         ██╔    ╝    ██
#█████╗  ██║██╔██╗ ██║███████║██║         ███████╗  ██████
#██╔  ╝  ██║██║╚██╗██║██╔  ██║██║         ╚    ██║    ██
#██║     ██║██║ ╚████║██║  ██║███████╗    ███████║             
#╚ ╝     ╚ ╝╚ ╝  ╚   ╝╚ ╝  ╚ ╝╚      ╝    ╚      ╝    
# 
# print("Dineros infinitos")   
#
#  _   _           
#| | | |          
#| |_| |__   ___  
#| __| '_ \ / _ \ 
#| |_| | | |  __/ 
# \__|_| |_|\___| 
#

#Dia 1: Refactorizar la historia por tercera vez y arreglar bugs con la parte de elecciones del jugador.
#Dia 2: Una gampiiiiiiiiiiiiiiiiiiii, solo jugando el riwmolrdiossssss.
#Dia 3: La dieta del caballo xdxdxd osea paja y agua xdxdxd.
#Dia 4: jugar solo rimworld xddddddddddddddddd como un huevonaso crjmrd.
#Dia 5: por el culo te la inco xdxdxd, bueno esta vez si chambie, estuve con el arte ascci de finales, tambien probando el Git
#Dia 6: Hoy si po otra cosecha, termine el capitulo 2 y estoy apunto de irme por el 3, pero ya veremos. Depaso unos arreglos.
#Dia 7: Trabajando en el capitulo 3 y algunas minusias mas.
#Dia 8: Termine el cap 3 y tamos con el 4°, tmr por huevon no acabe el cap4, mañana nomas ps.
#Dia 9: Carajomierda profe tetraquinta hijoputa 160 ejercicios, no se pase ps si somos secuandaria. No hubo avanze pipipi.
#Dia 10: Puse la guia de controles. casi cuando acaba la noche agrege las imagenes para los finales.
#Dia 11: Trabajar en el cap 4 para ya intentar finalizarlo pero esos 160 ejercicios no me dejan trabajar agusto crjmrd.
#Dia 12: Probando el pyinstaller y haciendolo funcionar para pasar de .py a un rico .exe. tambien se agrego el icono.

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



#           
#
#            ███████
#            ██   ██
#            ██   ██
#      ████████   ██
#      ██  ENTER  ██
#      █████████████
#
#




