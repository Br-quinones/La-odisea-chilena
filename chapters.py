import msvcrt
import keyboard
import systems as s

def chapter_1():
    #Limpiar pantalla
    print("Cargando...")
    s.clean_screen()

    s.dialogue("Roleo", "La victoria del Pacífico es para ustedes ¡Chile ganó! Pero están atrapados en un desierto")
    s.dialogue("Fernandez", "¿Alguien sabe cuántos días llevamos tragando polvo?")
    s.dialogue("Edgar", "No pienses en eso. Solo sigue marchando.")
    s.dialogue("Rodriguez", "¡Es fácil decirlo, cuando te quedas con la mayor porción de agua!")
    s.dialogue("Gonzalez", "Rodriguez. Gritar no hace brotar agua.")
    s.dialogue("Edgar", "Soldados descansemos un momento. Tengo algo para ustedes.")
    s.dialogue("Edgar", "Los suministros no alcanzarán para todos.")
    s.dialogue("Roleo", "El teniente saca un revólver")
    s.dialogue("Fernandez", "¿Teniente...?")
    s.dialogue("Rodriguez", "¿Teniente...?")
    s.dialogue("Edgar", "Un juego rápido de la ruleta rusa.")
    s.dialogue("Gonzalez", "Teniente, usted acaba de enloquecer por insolación.")
    
    #Elección 1
    s.question( "Una partidita no caería mal ¡Empiezo yo!",
                "Tal vez sí esté algo loco por el calor desértico.",)
    
    while True:
        print("↓ Escriba su elección") ; msvcrt.getch()
        choice_player = keyboard.read_key()
        
        if choice_player == "1": #Primer final
            s.pass_line()
            s.dialogue("Edgar", "Bueno, el revólver ya está listo. Ahora solo toca jugar.")
            s.dialogue("Roleo", "El teniente se apunta a sí mismo y dispara...")
            s.ending("teniente_suicida")
            s.ascci_end("C", "La muerte del teniente fue un calvario lento y tortuoso. Resultado de su estupidez.")
        elif choice_player == "2":
            s.pass_line()
            s.dialogue("Edgar", "Bueno, Gonzalez, algo de razón tienes...")
            s.dialogue("Roleo", "El teniente cae en desmayo por insolación")
            chapter_2()
        else:
            s.error_no_choice(1)

def chapter_2():
    s.dialogue("Roleo", "Llegada la noche, el teniente despierta en un oasis")
    s.dialogue("Edgar", "Sí, sí, sí... un día más de vida.")
    s.dialogue("Gonzalez", "Teniente... estamos jodidos, unos bandidos marcaron este oasis.")
    s.dialogue("Gonzalez", "Llegarán en unas horas y matarán a cualquiera que esté aquí.")
    s.dialogue("Fernandez", "Tenemos que luchar. ¡Somos soldados entrenados para eso!")
    s.dialogue("Rodriguez", "Retirémonos, no vale la pena luchar siendo solo cuatro y con suministros limitados.")
    s.dialogue("Gonzalez", "Más aún, ¿qué pasaría si alguno de nosotros cae en batalla?")
    s.dialogue("Fernandez", "¡Maldición con ustedes!... estuvimos en plena guerra y no vamos a poder con unos bandidos.")
    s.dialogue("Fernandez", "Somos soldados con fusiles y entrenamiento, contra unos bandidos mal armados.")

    #Eleccion 2
    s.question("Luchar contra esos bandidos con valentía.",
                "Retirarse de este oasis con cobardía.")

    while True:
        print("↓ Escriba su elección") ; msvcrt.getch()
        choice_player = keyboard.read_key()
        
        if choice_player == "1": #Segundo final
            s.pass_line()
            s.dialogue("Edgar", "Soldados, alisten sus fusiles, vamos contra esos bandidos.")
            s.dialogue("Edgar", "No nos dejaremos intimidar por nada ni por nadie.")
            s.dialogue("Roleo", "Llegó la madrugada y a las lejanías se observó el enemigo...")
            s.ending("batallon_caido")
            s.ascci_end("B", "La muerte de todo el batallón fue en valentía ante un enemigo supremo en número.")
        elif choice_player == "2":
            s.pass_line()
            s.dialogue("Edgar", "Soldados, empiecen a marchar nos retiraremos.")
            s.dialogue("Edgar", "No vale la pena perder nuestras vidas por un charco de agua.")
            s.dialogue("Roleo", "Las horas pasaron hasta el amanecer...")
            chapter_3() 
        else:
            s.error_no_choice(1)

def chapter_3():
    s.dialogue("Gonzalez", "Teniente esos bandidos debieron de llegar de algún pueblo o asentamiento.")
    s.dialogue("Gonzalez", "No debemos estar muy lejos de la civilización.")
    s.dialogue("Edgar", "Busquemos aquel lugar entonces.")
    s.dialogue("Edgar", "Hmmm silencio... ¿escuchan eso? Es el sonido de la civilización.")
    s.dialogue("Roleo", "El batallón se acerca a aquel sonido, encontrando un campamento militar")
    s.dialogue("Edgar", "Acerquémonos a pedir suministros.")
    s.dialogue("Extraño", "¡Eh, alto ahí o disparo!")
    s.dialogue("Edgar", "Baja el arma, somos soldados que sirven a la patria.")
    s.dialogue("Extraño", "¿Cuál patria?")
    s.dialogue("Edgar", "La chilena, por supuesto.")
    s.dialogue("Extraño", "La chilena...")
    s.dialogue("Extraño", "Quédense entonces. Les daremos suministros y techo para que continúen con su viaje.")
    s.dialogue("Rodriguez", "Teniente, nosotros estamos buscando un pueblo. No un campamento militar.")
    s.dialogue("Gonzalez", "Deberíamos quedarnos esta noche y luego partir.")
    s.dialogue("Fernandez", "No. Este campamento y sus soldados son desconocidos, abastezcámonos y larguémonos.")

    #Eleccion 3
    s.question("Tomemos lo necesario y larguémonos lo antes posible.",
                "Quedémonos toda la noche y aprovisionémonos con más suministros.")

    while True:
        print("↓ Escriba su elección") ; msvcrt.getch()
        choice_player = keyboard.read_key()
        
        if choice_player == "1":
            s.pass_line()
            s.dialogue("Edgar", "¡Batallón! No hay tiempo que perder. Tomen lo ofrecido y marchemos.")
            s.dialogue("Roleo", "El batallón toma los suministros rápidamente y se marcha.")
            chapter_4()
        elif choice_player == "2": #Tercer final
            s.pass_line()
            s.dialogue("Edgar", "Soldados, descansaremos aquí. Mañana al amanecer continuaremos.")
            s.dialogue("Roleo", "Pasan las horas y cuando la medianoche llegó...")
            s.ending("la_traicion") 
            s.ascci_end("A", "En la noche oscura, el lobo disfrazado de oveja atacó al vulnerable batallón.")
        else:
            s.error_no_choice(1)

def chapter_4():
    s.dialogue("Edgar", "Tan solo sigamos buscando aquel pueblo.")
    s.dialogue("Rodriguez", "Esos suministros se acabaron tan rápido...")
    s.dialogue("Gonzalez", "Con el frío del desierto y la falta de suministros, esto será imposible.")
    s.dialogue("Fernandez", "Teniente tengo una idea, si nos dividimos, dos al oeste y dos al este.")
    s.dialogue("Rodriguez", "¿Qué pasará con los dos que no encuentren el pueblo?")
    s.dialogue("Fernandez", "El grupo que llegue a salvo deberá de emprender una búsqueda.")
    s.dialogue("Gonzalez", "Propongo algo mejor, cada uno a una dirección, este, oeste, sur y norte.")
    s.dialogue("Rodriguez", "¿Acaso propones que uno de nosotros regrese de donde escapamos?")
    s.dialogue("Rodriguez", "Sigamos avanzando juntos, como lo hemos hecho en todo el viaje.")
    
    #Eleccion 4
    s.question("Deberíamos separarnos en grupos de dos.",
                "Deberíamos ir cada uno por un camino (norte, sur, este, oeste).",
                "Deberíamos mantenernos todos juntos.")

    while True:
        print("↓ Escriba su elección") ; msvcrt.getch()
        choice_player = keyboard.read_key()
        
        if choice_player == "1":
            s.pass_line()
            s.dialogue("Edgar", "Fernandez y Gonzalez irán al norte, Rodriguez y yo iremos al sur.")
            s.dialogue("Rodriguez", "Pero, teniente...")
            s.ending("final_malo")
            s.ascci_end("B", "Ninguno de los grupos llegó, muriendo los dos en el desierto.")
        elif choice_player == "2": 
            s.pass_line()
            s.dialogue("Edgar", "Cada uno por su camino. Yo elijo el oeste. Ustedes elijan el suyo.")
            s.dialogue("Rodriguez", "Pero, teniente...")
            s.ending("final_malo")
            s.ascci_end("B", "Solo llegó un soldado que murió de depresión poco después.")
        elif choice_player == "3":
            s.pass_line()
            s.dialogue("Edgar", "Sigamos todos juntos hacia el este.")
            s.dialogue("Rodriguez", "Sí, teniente...")
            s.ending("final_bueno")
            s.ascci_end("S", "Todo el batallón volvió a Santiago, ahora están junto a su patria y familia.")

        else:
            s.error_no_choice(1)