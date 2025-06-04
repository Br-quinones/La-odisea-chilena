import menu
import msvcrt
import keyboard
import systems as s

#Lo divide las funciones en capitulos para testear de manera mas facil ## recuerda we

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
            chapter_2() #Inicio del capitulo 2, aunque en verdad solo son escenas tmr
            break
        else:
            s.error_no_choice(1)

def chapter_2():
    #Escena 2
    s.dialogue("Roleo", "El teniente despierta con un oasis a su izquierda.")
    s.dialogue("Edgar", "Si si si... un dias mas de vida.")
    s.dialogue("Gonzalez", "Teniente... estamos jodidos, unos bandalos marcaron este oasis.")
    s.dialogue("Gonzalez", "Vendran en una hora y mataran a cualquiera que este aqui.")
    s.dialogue("Fernandez", "Tendremos que luchar, somos soldados entrenados para eso.")
    s.dialogue("Rodriguez", "Vayamonos no vale la pena luchar siendo solo 5 y con suministros limitados.")
    s.dialogue("Gonzalez", "Mas aun que pasaria si alguno de nosotros muere.")
    s.dialogue("Fernandez", "Maldia seas con ustedes, estuvimos en plena guerra y no vamos a poder con unos forasteros.")
    s.dialogue("Fernandez", "Somos soldados con fusiles y entrenamiento, contra unos bandalos con pistolas y sin entrenamiento.")

    #Eleccion 2
    s.question("Luchar contra esos bandalos con valentia.",
                "Retirase de este oasis con cobardia.")

    while True:
        print("↓ Escriba su eleccion") ; msvcrt.getch()
        choice_player = keyboard.read_key()
        
        if choice_player == "1": #Segundo final aca
            s.pass_line()
            s.dialogue("Edgar", "Soldados, alisten sus fusiles, vamos contra esos bandolos.")
            s.dialogue("Edgar", "Nos nos dejareos intimidar por nada y por nadie.")
            s.dialogue("Roleo", "Llego la madrugada y a las lejanias se observo el enemigo...")
            s.ending("batallon_caido", 10)
            s.ascci_end("B", "La muerte de todo el batallón fue en valentía ante un enemigo supremo en número.")
            break
        elif choice_player == "2":
            s.pass_line()
            s.dialogue("Edgar", "Soldados, empiezen a marchar nos retiraremos.")
            s.dialogue("Edgar", "No vale la pena perder nuestras vidas por un simple oasis.")
            s.dialogue("Roleo", "Pasan las horas hasta llegar a la madrugada.")
            break
        else:
            s.error_no_choice(1)


    


























    #Volver al Menu principal
    menu.main_menu()

