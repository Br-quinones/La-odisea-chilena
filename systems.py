import os
import sys
import menu
import time
import msvcrt
import keyboard
from PIL import Image
from pygame import mixer
from colorama import Fore, Style

#Para crear dialogos
def dialogue(character , message):
    if character == "Edgar":
        print(Fore.BLUE + f"{character}: " + Fore.RESET + message + "\n")
        msvcrt.getch()
    elif character == "Extraño":
        print(Fore.MAGENTA + f"{character}: " + Fore.RESET + message + "\n")
        msvcrt.getch()
    elif character == "Fernandez":
        print(Fore.RED + f"{character}: " + Fore.RESET + message + "\n")
        msvcrt.getch()
    elif character == "Gonzalez":
        print(Fore.GREEN + f"{character}: " + Fore.RESET + message + "\n")
        msvcrt.getch()
    elif character == "Rodriguez":
        print(Fore.YELLOW + f"{character}: " + Fore.RESET + message + "\n")
        msvcrt.getch()
    elif character == "Roleo":
        print(Fore.CYAN + f"~~~ {message} ~~~" + "\n" + Fore.RESET)
        msvcrt.getch()
    else:
        print("\n Error del desarrollador. \n")

#Para crear preguntas
def question(*alternatives):
    number_one = 1
    print("Ahora es tu turno Jugador, influye en el destino de la historia..." + "\n")
    for alternatives in alternatives:
        print(Fore.BLUE + f"[{number_one}]" + Fore.RESET + f" {alternatives}")
        number_one += 1
    print("")

#En caso de no elegir una altervativa
def error_no_choice(argument):
        if argument == 1:
            mixer.Channel(1).play(mixer.Sound("audio/error.mp3"))
            print(Fore.RED + "Caracter invalido." + Fore.RESET)
        elif argument == 0:
            mixer.Channel(1).play(mixer.Sound("audio/error.mp3"))
            print(Fore.RED + "Caracter invalido." + "\n" + Fore.RESET)

#Para crear finales
def ending(multimedia): #Suputamare esta huevada funciona a las justas
    variable = Image.open(f"imagen/{multimedia}.png")
    time.sleep(0.4)
    variable.show()
    time.sleep(2.2)
    keyboard.press_and_release("f11")
    mixer.music.load(f"audio/{multimedia}.mp3")
    mixer.music.play()
    time.sleep(10)
    keyboard.press_and_release("ctrl+w")

#Musica del juego musica_de_todo_el_juego
def music_game():
    mixer.init()
    mixer.music.load("audio/hoqtav_villas.mp3")
    mixer.music.play(-1)

#Para Limpiar la pantalla
def clean_screen():
    print(Style.BRIGHT, end="")
    os.system("cls")

#ajustar pantalla
def borderland():
    keyboard.press_and_release("f11")
    for _ in range(8):
        keyboard.press_and_release("ctrl+plus")

#Salir de programa
def exit_program():
    print("Saliendo...")
    sys.exit()

#Mostrar creditos
def credits():
    print("Cargando...")
    clean_screen()
    print("\n\n\n")
    print("                                       Director del juego: Brayan Quiñones.")
    print("                                       Productor Ejecutivo: Brayan Quiñones.")
    print("                                       Productor Asociado: Brayan Quiñones.")
    print("                                       Jefe de Producción: Brayan Quiñones.")
    print("                                       Diseñador del juego: Brayan Quiñones.")
    print("                                       Diseñador principal: Brayan Quiñones.")
    print("                                       Diseñador de sistemas: Brayan Quiñones.")
    print("                                       Diseñador narrativo: Brayan Quiñones.")
    print("                                       Diseñador de interfaz: Brayan Quiñones.")
    print("                                       Diseñador de experiencia: Brayan Quiñones.")
    print("                                       Programador principal: Brayan Quiñones.")
    print("                                       Programador de gameplay: Brayan Quiñones.")
    print("                                       Programador de sistemas: Brayan Quiñones.")
    print("                                       Programador de herramientas: Brayan Quiñones.")
    print("                                       Programador de interfaz : Brayan Quiñones.")
    print("                                       Artista principal: Brayan Quiñones.")
    print("                                       Artista conceptual: Brayan Quiñones.")
    print("                                       Artista 2D: Brayan Quiñones.")
    print("                                       Artista técnico: Brayan Quiñones.")
    print("                                       Director de arte: Brayan Quiñones.")
    print("                                       Director de audio: Brayan Quiñones.")
    print("                                       Diseñador gráfico: Brayan Quiñones.")
    print("                                       Diseñador de sonido: Brayan Quiñones.")
    print("                                       Tester de videojuegos: Brayan Quiñones.")
    print("                                       Corrector ortotipográfico: Gemeni & ChatGPT.")
    msvcrt.getch()

    menu.main_menu()

#Pasar linea
def pass_line():
    print("") #Esa huevada solo por que se ve feo en el codigo poner un "\n", ademas solo se usara unas veces

#Mostar final que te toco: A, B, C, S. 
def ascci_end(puntuation, text):
    os.system("cls")
    print("\n" * 8)

    if puntuation == "C":
        print(Fore.RED,end="")
        print("███████╗██╗███╗   ██╗ █████╗ ██╗          ██████╗".center(115))
        print("██╔════╝██║████╗  ██║██╔══██╗██║         ██╔════╝".center(115))
        print("█████╗  ██║██╔██╗ ██║███████║██║         ██║     ".center(115))
        print("██╔══╝  ██║██║╚██╗██║██╔══██║██║         ██║     ".center(115))
        print("██║     ██║██║ ╚████║██║  ██║███████╗    ╚██████╗".center(115))
        print("╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝     ╚═════╝".center(115))
        print(Fore.RESET,end="")
    
    elif puntuation == "B":
        print(Fore.YELLOW,end="")
        print("███████╗██╗███╗   ██╗ █████╗ ██╗          ██████╗".center(115))
        print("██╔════╝██║████╗  ██║██╔══██╗██║          ██╔══██╗".center(115))
        print("█████╗  ██║██╔██╗ ██║███████║██║          ██████╔╝".center(115))
        print("██╔══╝  ██║██║╚██╗██║██╔══██║██║          ██╔══██╗".center(115))
        print("██║     ██║██║ ╚████║██║  ██║███████╗     ██████╔╝".center(115))
        print("╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝     ╚═════╝ ".center(115))
        print(Fore.RESET,end="")

    elif puntuation == "A":
        print(Fore.GREEN,end="")
        print("███████╗██╗███╗   ██╗ █████╗ ██╗          █████╗ ".center(115))
        print("██╔════╝██║████╗  ██║██╔══██╗██║         ██╔══██╗".center(115))
        print("█████╗  ██║██╔██╗ ██║███████║██║         ███████║".center(115))
        print("██╔══╝  ██║██║╚██╗██║██╔══██║██║         ██╔══██║".center(115))
        print("██║     ██║██║ ╚████║██║  ██║███████╗    ██║  ██║".center(115))
        print("╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝".center(115))
        print(Fore.RESET,end="")

    elif puntuation == "S":
        print(Fore.CYAN,end="")
        print("███████╗██╗███╗   ██╗ █████╗ ██╗         ███████╗".center(115))
        print("██╔════╝██║████╗  ██║██╔══██╗██║         ██╔════╝".center(115))
        print("█████╗  ██║██╔██╗ ██║███████║██║         ███████╗".center(115))
        print("██╔══╝  ██║██║╚██╗██║██╔══██║██║         ╚════██║".center(115))
        print("██║     ██║██║ ╚████║██║  ██║███████╗    ███████║".center(115))
        print("╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚══════╝".center(115))

    else:
        print("Error del desarrollador a🐟t🐻.")
    
    print("")
    print(f"{text}".center(115))
    print("\n")
    print(Fore.BLUE + "Presione cualquier tecla para continuar.".center(115) + Fore.RESET)
    msvcrt.getche()
    music_game()
    menu.main_menu()
    


