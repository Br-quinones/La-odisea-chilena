                                            #La odisea peruana (1883-1893)
    #El teniente Edgar despues de la guerra con chile devera de llevar a su tropa hacia Loreto puesto que ya estaba mas de 10 años lejos de su familia y patria, el viaje empieza desde Chile, pasando por varios departamentos, finalmente llegando Loreto. Toda la historia esta basada en La odisea de Homero.


#
#
#
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
#         ╔═══╗
#    ╔═════███╚════╗
#       ║███████║
#    ╚════╗███╔════╝
#         ╚═══╝║
#         
#

#                                                        
#███████╗██╗███╗   ██╗ █████╗ ██╗         ███████╗        
#██╔════╝██║████╗  ██║██╔══██╗██║         ██╔════╝    ██
#█████╗  ██║██╔██╗ ██║███████║██║         ███████╗  ██████
#██╔══╝  ██║██║╚██╗██║██╔══██║██║         ╚════██║    ██
#██║     ██║██║ ╚████║██║  ██║███████╗    ███████║             
#╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚══════╝    
# 
# print("Dineros infinitos")   
#
# #

#  _   _           
#| | | |          
#| |_| |__   ___  
#| __| '_ \ / _ \ 
#| |_| | | |  __/ 
# \__|_| |_|\___| 

#


#Dia 1: Refactorizar la historia por 3° vez y arreglar bugs con la parte de elecciones del jugador
#Dia 2: Una gampiiiiiiiiiiiiiiiiiiii, just i play rimworld
#Dia 3: La dieta del caballo xdxdxd
#Dia 4: jugar solo rimworld xddddddddddddddddd
#Dia 5: por el culo te la inco xdxdxd, bueno esta vez si chambie, estuve con el arte ascci de finales
#
from colorama import Fore
import msvcrt

def ascci_end(puntuation, argument_1,argument_2):
    print("\n" * argument_1)

    if puntuation == "C":
        print(Fore.RED,end="")
        print("█████████████████████████████████████████████████".center(argument_2))
        print("███████╗██╗███╗   ██╗ █████╗ ██╗          ██████╗".center(argument_2))
        print("██╔════╝██║████╗  ██║██╔══██╗██║         ██╔════╝".center(argument_2))
        print("█████╗  ██║██╔██╗ ██║███████║██║         ██║     ".center(argument_2))
        print("██╔══╝  ██║██║╚██╗██║██╔══██║██║         ██║     ".center(argument_2))
        print("██║     ██║██║ ╚████║██║  ██║███████╗    ╚██████╗".center(argument_2))
        print("╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝     ╚═════╝".center(argument_2))
        print("█████████████████████████████████████████████████".center(argument_2))
        print(Fore.RESET,end="")
    
    elif puntuation == "B":
        print(Fore.YELLOW,end="")
        print("█████████████████████████████████████████████████".center(argument_2))
        print("███████╗██╗███╗   ██╗ █████╗ ██╗          ██████╗".center(argument_2))
        print("██╔════╝██║████╗  ██║██╔══██╗██║          ██╔══██╗".center(argument_2))
        print("█████╗  ██║██╔██╗ ██║███████║██║          ██████╔╝".center(argument_2))
        print("██╔══╝  ██║██║╚██╗██║██╔══██║██║          ██╔══██╗".center(argument_2))
        print("██║     ██║██║ ╚████║██║  ██║███████╗     ██████╔╝".center(argument_2))
        print("╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝     ╚═════╝ ".center(argument_2))
        print("█████████████████████████████████████████████████".center(argument_2))
        print(Fore.RESET,end="")

    elif puntuation == "A":
        print(Fore.GREEN,end="")
        print("█████████████████████████████████████████████████".center(argument_2))
        print("███████╗██╗███╗   ██╗ █████╗ ██╗          █████╗ ".center(argument_2))
        print("██╔════╝██║████╗  ██║██╔══██╗██║         ██╔══██╗".center(argument_2))
        print("█████╗  ██║██╔██╗ ██║███████║██║         ███████║".center(argument_2))
        print("██╔══╝  ██║██║╚██╗██║██╔══██║██║         ██╔══██║".center(argument_2))
        print("██║     ██║██║ ╚████║██║  ██║███████╗    ██║  ██║".center(argument_2))
        print("╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝".center(argument_2))
        print("█████████████████████████████████████████████████".center(argument_2))
        print(Fore.RESET,end="")

    elif puntuation == "S":
        print(Fore.CYAN,end="")
        print("█████████████████████████████████████████████████".center(argument_2))
        print("███████╗██╗███╗   ██╗ █████╗ ██╗         ███████╗".center(argument_2))
        print("██╔════╝██║████╗  ██║██╔══██╗██║         ██╔════╝".center(argument_2))
        print("█████╗  ██║██╔██╗ ██║███████║██║         ███████╗".center(argument_2))
        print("██╔══╝  ██║██║╚██╗██║██╔══██║██║         ╚════██║".center(argument_2))
        print("██║     ██║██║ ╚████║██║  ██║███████╗    ███████║".center(argument_2))
        print("╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚══════╝".center(argument_2))
        print("█████████████████████████████████████████████████".center(argument_2))

    else:
        print("Error del desarrollador a🐟t🐻.")
    
    msvcrt.getche()


ascci_end("A",8,120)