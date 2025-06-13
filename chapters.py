import menu
import msvcrt
import keyboard
import systems as s

def chapter_1():
    #Limpiar la pantalla
    print("Cargando...")
    s.clean_screen()
    
    #Escena 1
    s.dialogue("Roleo", "La victoria del Pacífico es para ustedes ¡Chile ganó! Pero estan atrapados en un desierto")
    s.dialogue("Fernandez", "¿Alguien sabe cuántos días llevamos tragando polvo?")
    s.dialogue("Edgar", "No pienses en eso. Solo sigue marchando.")
    s.dialogue("Rodriguez", "¡Es fácil decirlo, cuando todavía te quedas la mayor porción de agua!")
    s.dialogue("Gonzalez", "Rodriguez. Gritar no hace brotar agua.")
    s.dialogue("Edgar", "Descansemos un momento. Tengo algo para ustedes.")
    s.dialogue("Edgar", "Los suministros no alcanzarán para todos.")
    s.dialogue("Roleo", "El teniente saca un revólver")
    s.dialogue("Fernandez", "¿Teniente...?")
    s.dialogue("Rodriguez", "¿Teniente...?")
    s.dialogue("Edgar", "Un juego rapido de rápido rusa.")
    s.dialogue("Gonzalez", "Teniente usted acaba de enloquecer por insolación.")
    
    #Elección 1
    s.question( "Una partidita no caería mal ¡Empiezo yo!",
                "Tal vez si este algo loco por el calor desértico.",)
    
    while True:
        print("↓ Escriba su elección") ; msvcrt.getch()
        choice_player = keyboard.read_key()
        
        if choice_player == "1": #Primer final
            s.pass_line()
            s.dialogue("Edgar", "Bueno, el revólver ya esta Listo. ahora solo toca jugar.")
            s.dialogue("Roleo", "El teniente se apunta a sí mismo y dispara...")
            s.ending("teniente_suicida")
            s.ascci_end("C", "La muerte del teniente fue un calvario lento y tortuoso. Resultado de su estupidez.")
        elif choice_player == "2":
            s.pass_line()
            s.dialogue("Edgar", "Bueno, Gonzalez, algo de razón tienes...")
            s.dialogue("Roleo", "El teniente cae desmayado por insolación")
            chapter_2()
        else:
            s.error_no_choice(1)

def chapter_2():
    #Escena 2
    s.dialogue("Roleo", "Llegada la noche despierta con un oasis a su izquierda.")
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
        print("↓ Escriba su elección") ; msvcrt.getch()
        choice_player = keyboard.read_key()
        
        if choice_player == "1": #Segundo final
            s.pass_line()
            s.dialogue("Edgar", "Soldados, alisten sus fusiles, vamos contra esos bandolos.")
            s.dialogue("Edgar", "Nos nos dejareos intimidar por nada y por nadie.")
            s.dialogue("Roleo", "Llego la madrugada y a las lejanias se observo el enemigo...")
            s.ending("batallon_caido")
            s.ascci_end("B", "La muerte de todo el batallón fue en valentía ante un enemigo supremo en número.")
        elif choice_player == "2":
            s.pass_line()
            s.dialogue("Edgar", "Soldados, empiezen a marchar nos retiraremos.")
            s.dialogue("Edgar", "No vale la pena perder nuestras vidas por un simple oasis.")
            s.dialogue("Roleo", "Pasan las horas hasta llegar a la madrugada...")
            chapter_3() 
        else:
            s.error_no_choice(1)

def chapter_3():
    s.dialogue("Gonzalez", "Teniente esos bandolos devieron de llegar de algun pueblo o asentamiento.")
    s.dialogue("Gonzalez", "Muy lejos de la civilización no deveremos de estar.")
    s.dialogue("Edgar", "Busquemos aquel pueblo entonces.")
    s.dialogue("Fernandez", "¿Se supone que estamos buscando el mismo pueblo de donde salieron los bandios?")
    s.dialogue("Gonzalez", "A callar pesimista, esa es nuestra ultima salvación")
    s.dialogue("Edgar", "Shhh silencio, ¿escuchan eso? es el sonido de la civilización.")
    s.dialogue("Roleo", "El batallón se acerca a aquel sonido, encontrando un campamento misterioso.")
    s.dialogue("Edgar", "tendremos que ir no hay mas opción, es preguntar o morir.")
    s.dialogue("Rodriguez", "Vamos entonces teniente.")
    s.dialogue("Extraño", "¡Hey alto ahi o disparo!")
    s.dialogue("Edgar", "Tranquilo somos soldados que sirven a la patria.")
    s.dialogue("Extraño", "¿Cual patria?")
    s.dialogue("Edgar", "La chilena desde luego.")
    s.dialogue("Extraño", "La chilena...")
    s.dialogue("Extraño", "Bueno entonces quedense, les daremos suministros  y techo para que sigan su viaje.")
    s.dialogue("Rodriguez", "Teniente nosotros estamos buscando un pueblo. No un campamento militar.")
    s.dialogue("Gonzalez", "Deveriamos de quedarmos esta noche y luego partir.")
    s.dialogue("Fernandez", "Este campamento y su gente son sospechosos, reabastezcamos y largemonos.")

    #Eleccion 3
    s.question("Agarremos lo necesario y larguemonos lo antes posible.",
                "Quedemonos toda la noche, y tomemos aun mas suministros. ")

    while True:
        print("↓ Escriba su elección") ; msvcrt.getch()
        choice_player = keyboard.read_key()
        
        if choice_player == "1":
            s.pass_line()
            s.dialogue("Edgar", "Batallon no tenemos tiempo que perder, toman lo ofrecido y marchemos.")
            s.dialogue("Roleo", "El batallon toma lo suministros ofrecidos lo mas rapido y se marcha.")
            chapter_4()
        elif choice_player == "2": #Tercer final
            s.pass_line()
            s.dialogue("Edgar", "Soldados, descazaremos aquí mañana en la madrugada continuaremos.")
            s.dialogue("Roleo", "Pasan las horas y cuando la medianoche llego..")
            s.ending("la_traicion") 
            s.ascci_end("A", "En la noche oscura el lobo disfrazado de oveja ataco al vulnerale batallón.")
        else:
            s.error_no_choice(1)

def chapter_4():
    s.dialogue("Edgar", "Tan solo sigamos buscando aquel pueblo...")
    s.dialogue("Rodriguez", "Esos suministros se acabaron tan rapido...")
    s.dialogue("Gonzalez", "Con el frio del desierto y la falta de sumistros esto sera imposible.")
    s.dialogue("Fernandez", "Teniente tengo una idea, si nos dividimos, 2 al oeste y 2 al este.")
    s.dialogue("Rodriguez", "¿Que pasara con los 2 que no encuentren el pueblo?")
    s.dialogue("Fernandez", "El grupo que llegue a salvo devera de emprender una busqueda.")
    s.dialogue("Gonzalez", "Propongo algo mejor, cada uno a una direccion, este, oeste, sur y norte.")
    s.dialogue("Rodriguez", "¿Acaso Propones que uno de nosotros regrese por donde venimos?")
    s.dialogue("Rodriguez", "Sigamos avanzando juntos, como lo hemos hecho en todo el viaje.")
    
    #Eleccion 4
    s.question("Deveriamos separarnos en grupos de 2.",
                "Deveriamos ir cada uno por un camino (norte, sur, este, oeste).",
                "Deveriamos manternos todos juntos.")

    while True:
        print("↓ Escriba su elección") ; msvcrt.getch()
        choice_player = keyboard.read_key()
        
        if choice_player == "1":
            s.pass_line()
            s.dialogue("Edgar", "Fernandez y Gonzalez iran al norte, Rodriguez y yo iremos al sur.")
            s.dialogue("Rodriguez", "Pero teniente...")
            s.ending("final_malo")
            s.ascci_end("B", "Nignuno de los grupos llego, muriendo los dos en el desierto.")
        elif choice_player == "2": 
            s.pass_line()
            s.dialogue("Edgar", "Cada uno a su camino. Yo eligo el oeste. Ustedes eligan el suyo.")
            s.dialogue("Rodriguez", "Pero teniente...")
            s.ending("final_malo")
            s.ascci_end("B", "Tan solo llego un soldado que muriendo de depresión poco despues.")
        elif choice_player == "3":
            s.pass_line()
            s.dialogue("Edgar", "Sigamos todos juntos para el este.")
            s.dialogue("Rodriguez", "Si teniente...")
            s.ending("final_bueno")
            s.ascci_end("S", "Todo el batallon volvio a Santiago ahora estan junto a su patria y familia.")

        else:
            s.error_no_choice(1)


