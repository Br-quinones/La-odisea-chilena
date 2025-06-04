import menu
import msvcrt
import keyboard
import systems as s

def chapter_1():
    #Limpiar la pantalla
    print("Cargando...")
    s.clean_screen()

    #Escena 1
    s.dialogue("Roleo", "La victoria del pacifico es para ustedes ¡Chile gano! Pero estan atrapados en un desierto. ")
    s.dialogue("Fernandez", "¿Alguien sabe cuántos días llevamos tragando polvo?")
    s.dialogue("Edgar", "No pienses en eso. Solo sigue marchando.")
    s.dialogue("Rodriguez", "¡Es fácil decirlo, cuando todavía te quedas la mayor porción de agua!")
    s.dialogue("Gonzalez", "Rodriguez. Gritar no hace brotar agua.")
    s.dialogue("Edgar", "Descansemos un momento, tengo algo para ustedes.")
    s.dialogue("Edgar", "Los suministros no alcanzaran para todos.")
    s.dialogue("Roleo", "El teniente saca un revolver")
    s.dialogue("Fernandez", "¿Teniente...?")
    s.dialogue("Rodriguez", "¿Teniente...?")
    s.dialogue("Gonzalez", "¿Teniente...?")
    s.dialogue("Edgar", "Un juego rapido de la ruleta rusa.")
    s.dialogue("Gonzalez", "Teniente acaba de caer en la locura por insolacion.")
    
    #Elección 1
    s.question( "Una partidita no caeria mal ¡Empiezo yo!",
                "Tal vez si este algo loco por el calor desertico.",)
    
    while True:
        print("↓ Escriba su eleccion") ; msvcrt.getch()
        choice_player = keyboard.read_key()
        
        if choice_player == "1": #Primer final
            s.pass_line()
            s.dialogue("Edgar", "Bueno el revolver ya esta aleatorizado, ahora solo toca jugar.")
            s.dialogue("Roleo", "El teniente se apunta a si mismo y dispara...")
            s.ending("teniente_suicida", 10)
            s.ascci_end("C", "La muerte del teniente fue un calvario lento y tortuoso, provocada por su estupidez.")
            break
        elif choice_player == "2":
            s.pass_line()
            s.dialogue("Edgar", "Bueno Gonzalez, algo de razón tiene...")
            s.dialogue("Roleo", "El teniente cae en desmayo por la insolacion.")
            break
        else:
            s.error_no_choice(1)
        
    #Escena 2
    s.dialogue("Roleo", "El teniente despierta en un oasis a su izquierda una fuente de agua y a su izquierda una fogata.")
    s.dialogue("Edgar", "Si si si... Es tan delicioso este manjar llamado agua.")
    s.dialogue("Gonzalez", "Teniente despierte despierte")

    





























    #Volver al Menu principal
    menu.main_menu()

