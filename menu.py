#Pantalla de carga
if __name__ == "__main__":
    print("Cargando...")

#librerias
import keyboard
import msvcrt
import chapters
import systems as s
from colorama import Fore

#Funciones
def tittle_of_the_game(argument):
    print("\n" * argument, end="")
    print("   ████████╗██╗  ██╗███████╗     ██████╗ ██████╗ ██╗   ██╗███████╗███████╗███████╗██╗   ██╗")
    print("   ╚══██╔══╝██║  ██║██╔════╝    ██╔═══██╗██╔══██╗╚██╗ ██╔╝██╔════╝██╔════╝██╔════╝╚██╗ ██╔╝")
    print("      ██║   ███████║█████╗      ██║   ██║██║  ██║ ╚████╔╝ ███████╗███████╗█████╗   ╚████╔╝ ")
    print("      ██║   ██╔══██║██╔══╝      ██║   ██║██║  ██║  ╚██╔╝  ╚════██║╚════██║██╔══╝    ╚██╔╝  ")
    print("      ██║   ██║  ██║███████╗    ╚██████╔╝██████╔╝   ██║   ███████║███████║███████╗   ██║   ")
    print("      ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝╚══════╝   ╚═╝   ")
    print(Fore.BLUE + "                                   ᴱˢᶜʳᶦᵇᵃ ¹ / ² / ³                              " + Fore.RESET)
    print("                                                                                                     _____")
    print("                                                                                                 /\\ /_____\\")
    print("                                                                                                /\\/ \\     /")
    print("                   "+Fore.BLUE+"[1]"+Fore.RESET+" JUGAR                                                                   / /   \\_-_/ ")
    print("                                                                                               \\ \\ \"\"\"\"V\"//\"\\")
    print("                                                                                                \\__    |//   \\")
    print("                   "+Fore.BLUE+"[2]"+Fore.RESET+" CREDITOS                                                                    |   //  |\\ \\")
    print("                                                                                                   |  //   | \\ \\")
    print("                                                                                                   | //|   | / /")
    print("                   "+Fore.BLUE+"[3]"+Fore.RESET+" SALIR                                                                       |// |   |/\\/")
    print("                                                                                                   |==[0]==|\\/")
    print("                                                                                                   |   |   |")
    print("                                                                                                   |   |   |")
    print("                                                                                                   |   |   |")
    print("                                                                                                   |   |   |")
    print("                                                                                                   |   |   |")
    print("                                                                                                   |___|___|")
    print("                                                                                                    |_ | _|")
    print("                                                                                                   (___|___) v0.98-β")
    print(Fore.RESET, end="")

def choice_of_chapter(argument):
    print("\n" * argument)
    while True:
        msvcrt.getch()
        key = keyboard.read_key()
        
        if key == "1":
            chapters.chapter_1()
        elif key == "2":
            s.credits()
        elif key == "3":
            s.exit_program()
        else:
            s.error_no_choice(1)

def screen_loading():
    print("\n"*1)
    print(" ██████╗ ██████╗ ███╗   ██╗████████╗██████╗  ██████╗ ██╗     ███████╗███████╗       ".center(115))
    print("██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██║     ██╔════╝██╔════╝    ██╗".center(115))
    print("██║     ██║   ██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║     █████╗  ███████╗    ╚═╝".center(115))
    print("██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║     ██╔══╝  ╚════██║    ██╗".center(115))
    print("╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗███████╗███████║    ╚═╝".center(115))
    print(" ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝       ".center(115))
    print("\n"*2)
    print(Fore.BLUE+"        TECLA:            TECLA:             TECLA:        ".center(115) + Fore.RESET)
    print("██████████████    ██████████████    ██████████████ ".center(115))
    print("██    ██╗   ██    ██ ██████╗  ██    ██  ██████╗ ██ ".center(115))   
    print("██   ███║   ██    ██ ╚════██╗ ██    ██  ╚═══██║ ██ ".center(115))   
    print("██   ╚██║   ██    ██  █████╔  ██    ██   █████╝ ██ ".center(115))   
    print("██    ██║   ██    ██ ██╔═══╝  ██    ██   ╚══██╗ ██ ".center(115))   
    print("██    ██║   ██    ██ ███████╗ ██    ██  ██████║ ██ ".center(115))   
    print("██    ╚═╝   ██    ██ ╚══════╝ ██    ██  ╚═════╝ ██ ".center(115))
    print("██████████████    ██████████████    ██████████████ ".center(115))
    print("\n"*1)
    print(Fore.BLUE + "Presione cualquier TECLA para continuar".center(115) + Fore.RESET)
    msvcrt.getch()
                                                
#Ejecutar musica y pantalla completa + pantalla de carga
if __name__ == "__main__":
    s.borderland()
    s.clean_screen()
    screen_loading()
    s.music_game()

#Menu principal
def main_menu():
        s.clean_screen()
        tittle_of_the_game(1)
        choice_of_chapter(0)

#Ejecutar menu principal
if __name__ == "__main__":
    main_menu()