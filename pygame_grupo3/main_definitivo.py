from funciones_definitivas import *

mostrar_transicion_inicial(ventana_juego, ANCHO_VENTANA, ALTO_VENTANA, RUTA_MUSICA_MENU)
pantalla_actual = 'menu_principal'
transicion_realizada = False
juego_activo = True
partida_activa = False
partida_pausada = False
input_activo = False

bandera_musica_menu = False
bandera_musica_juego = False

valores_tablero = inicializar_tablero(ANCHO_VENTANA, ALTO_VENTANA, FILAS, COLUMNAS, CANTIDAD_MINAS)
lado_tablero = valores_tablero[0]
superficie_tablero = valores_tablero[1]
tablero_pos_x = valores_tablero[2]
tablero_pos_y = valores_tablero[3]
matriz_celdas = valores_tablero[4]
banderas_restantes = valores_tablero[5]
primer_click = valores_tablero[6]
fin_juego = valores_tablero[7]
imagen_mina_escalada = valores_tablero[8]
imagen_bandera_escalada = valores_tablero[9]
evento_timer = pygame.USEREVENT + 1
segundos_transcurridos = 0
tiempo_total = 0
minutos_transcurridos = 0
puntaje_total = 0
nombre_usuario = ''


archivo_jugadores_str = leer_archivo(RUTA_ARCHIVO)

if archivo_jugadores_str == '':
    encabezado = crear_encabezado(['nombre', 'puntaje', 'dificultad'], ',')
    escribir_archivo(RUTA_ARCHIVO, 'a', encabezado)
    lista_jugadores = extraer_jugadores_csv(archivo_jugadores_str)
else:
    lista_jugadores = extraer_jugadores_csv(archivo_jugadores_str)

while juego_activo:

    for evento in pygame.event.get():
        if bandera_musica_menu == False and pantalla_actual == 'menu_principal':
            pygame.mixer.music.load(RUTA_MUSICA_MENU)
            pygame.mixer.music.set_volume(volumen)
            pygame.mixer.music.play(-1, 9.87)
            bandera_musica_menu = True
            bandera_musica_juego = False
        
        if bandera_musica_juego == False and pantalla_actual == 'juego':
            pygame.mixer.music.load(RUTA_MUSICA_JUEGO)
            pygame.mixer.music.set_volume(volumen)
            pygame.mixer.music.play(-1)
            bandera_musica_menu = False
            bandera_musica_juego = True

        if evento.type == pygame.QUIT:
            juego_activo = False

        if evento.type == evento_timer:
            if partida_activa == True and  fin_juego == False:
                segundos_transcurridos += 1
                tiempo_total += 1
                if segundos_transcurridos >= 60:
                    segundos_transcurridos = 0
                    minutos_transcurridos += 1

        if evento.type == pygame.KEYDOWN:
            if input_activo == True:
                if evento.key == pygame.K_RETURN and validar_nombre(nombre_usuario) == True:
                    guardar_resultados(RUTA_ARCHIVO, lista_jugadores, nombre_usuario, puntaje_total, dificultad['nombre'])
                    pantalla_actual = 'puntajes'
                    nombre_usuario = ''
                elif evento.key == pygame.K_BACKSPACE:
                    nombre_usuario = nombre_usuario[0:-1]
                else:
                    nombre_usuario += evento.unicode
                    
            if evento.key == pygame.K_ESCAPE:
                sonido_click.play()
                if pantalla_actual == 'opciones' or pantalla_actual == 'puntajes' or pantalla_actual == 'seleccion_dificultad':
                    pantalla_actual = 'menu_principal'
                elif pantalla_actual == 'resolucion' or pantalla_actual == 'sonido':
                    pantalla_actual = 'opciones'
                elif pantalla_actual == 'juego':
                    pantalla_actual = 'seleccion_dificultad'
                
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = evento.pos

            if pantalla_actual == 'menu_principal':
                for boton in lista_botones_pantalla:
                    if boton['rect'].collidepoint(posicion_mouse):
                        sonido_click.play()
                        match boton['nombre']:
                            case 'Jugar':
                                pantalla_actual = 'seleccion_dificultad' 
                            case 'Continuar':
                                pantalla_actual = 'juego'
                                if primer_click == True:
                                    pygame.time.set_timer(evento_timer, 0)
                                else:
                                    pygame.time.set_timer(evento_timer, 1000)
                                partida_pausada = False
                            case 'Opciones':
                                pantalla_actual = 'opciones'    
                            case 'Puntajes':
                                pantalla_actual = 'puntajes'
                            case 'Salir':
                                juego_activo = False

            elif pantalla_actual == 'opciones':
                pantalla_retorno = 'menu_principal'
                for boton in lista_botones_pantalla:
                    sonido_click.play()
                    if boton['rect'].collidepoint(posicion_mouse):
                        match boton['nombre']:
                            case 'Resolucion':
                                pantalla_actual = 'resolucion'
                                
                            case 'Sonido':
                                pantalla_actual = 'sonido'
                                
                            case 'Atras':
                                pantalla_actual = 'menu_principal'
                                
            elif pantalla_actual == 'resolucion':
                pantalla_retorno = 'opciones'
                for boton in lista_botones_pantalla:
                    if boton['rect'].collidepoint(posicion_mouse):
                        sonido_click.play()
                        match boton['nombre']:
                            case '800x600':
                                nueva_res = RESOLUCIONES[0]
                            case '1024x768':
                                nueva_res = RESOLUCIONES[1]
                            case '1440x1080':
                                nueva_res = RESOLUCIONES[2]
                            case 'Atras':
                                pantalla_actual = 'opciones'
                        if boton['nombre'] != 'Atras':
                            recursos = reescalar_recursos(nueva_res['ancho'], nueva_res['alto'], dificultad)
                            ventana_juego = recursos['ventana']
                            fuente_titulo = recursos['fuente_titulo']
                            fuente_juego = recursos['fuente_juego']
                            fuente_timer = recursos['fuente_timer']
                            imagen_fondo_escalada = recursos['imagen_fondo_escalada']
                            imagen_fondo_blanco_escalada = recursos['imagen_fondo_blanco_escalada']
                            imagen_victoria_escalada = recursos['imagen_victoria_escalada']
                            imagen_derrota_escalada = recursos['imagen_derrota_escalada']
                            imagen_titulo_escalada = recursos['imagen_titulo_escalada']
                            imagen_boton_escalada = recursos['imagen_boton_escalada']
                            imagen_timer_escalada = recursos['imagen_timer_escalada']
                            imagen_bandera_mina_escalada = recursos['imagen_bandera_mina_escalada']
                            valores_tablero = recursos['valores_tablero']

                            lado_tablero = valores_tablero[0]
                            superficie_tablero = valores_tablero[1]
                            tablero_pos_x = valores_tablero[2]
                            tablero_pos_y = valores_tablero[3]
                            matriz_celdas = valores_tablero[4]
                            banderas_restantes = valores_tablero[5]
                            primer_click = valores_tablero[6]
                            fin_juego = valores_tablero[7]
                            imagen_mina_escalada = valores_tablero[8]
                            imagen_bandera_escalada = valores_tablero[9]

                            ANCHO_VENTANA = nueva_res['ancho']
                            ALTO_VENTANA = nueva_res['alto']

                            pantalla_actual = 'opciones'
                                
            elif pantalla_actual == 'sonido':
                for boton in lista_botones_pantalla:
                    if boton['rect'].collidepoint(posicion_mouse):
                        sonido_click.play()
                        match boton['nombre']:
                            case '+':
                                volumen = cambiar_volumen(volumen, '+')
                            case '-':
                                volumen = cambiar_volumen(volumen, '-')
                            case 'Mutear':
                                volumen = cambiar_volumen(volumen, 'mutear')
                            case 'Atras':
                                pantalla_actual = 'opciones'
                                
            elif pantalla_actual == 'victoria':
                for boton in lista_botones_pantalla:
                    if boton['rect'].collidepoint(posicion_mouse):
                        match boton['nombre']:
                            case 'Ingresar':
                                if validar_nombre(nombre_usuario) == True:
                                    guardar_resultados(RUTA_ARCHIVO, lista_jugadores, nombre_usuario, puntaje_total, dificultad['nombre'])
                                    nombre_usuario = ''
                                    pantalla_actual = 'puntajes'

            elif pantalla_actual == 'puntajes':
                for boton in lista_botones_pantalla:
                    if boton['rect'].collidepoint(posicion_mouse):
                        sonido_click.play()
                        match boton['nombre']:
                            case 'Facil':
                                dificultad = DIFICULTADES[0]
                            case 'Medio':
                                dificultad = DIFICULTADES[1]
                            case 'Dificil':
                                dificultad = DIFICULTADES[2]
                            case 'Atras':
                                pantalla_actual = 'menu_principal'

            elif pantalla_actual == 'seleccion_dificultad':
                for boton in lista_botones_pantalla:
                    if boton['rect'].collidepoint(posicion_mouse):
                        sonido_click.play()
                        match boton['nombre']:
                            case 'Facil':
                                dificultad = DIFICULTADES[0]
                                pantalla_seleccionada = 'juego'
                            case 'Medio':
                                dificultad = DIFICULTADES[1]
                                pantalla_seleccionada = 'juego'
                            case 'Dificil':
                                dificultad = DIFICULTADES[2]
                                pantalla_seleccionada = 'juego'
                            case 'Atras':
                                pantalla_seleccionada = 'menu_principal'

                        FILAS = dificultad['filas']
                        COLUMNAS = dificultad['columnas']
                        CANTIDAD_MINAS = dificultad['minas']
                        pantalla_actual = pantalla_seleccionada
                        valores_tablero = inicializar_tablero(ANCHO_VENTANA, ALTO_VENTANA, FILAS, COLUMNAS, CANTIDAD_MINAS)
                        lado_tablero = valores_tablero[0]
                        superficie_tablero = valores_tablero[1]
                        tablero_pos_x = valores_tablero[2]
                        tablero_pos_y = valores_tablero[3]
                        matriz_celdas = valores_tablero[4]
                        banderas_restantes = valores_tablero[5]
                        primer_click = valores_tablero[6]
                        fin_juego = valores_tablero[7]
                        imagen_mina_escalada = valores_tablero[8]
                        imagen_bandera_escalada = valores_tablero[9]

            elif pantalla_actual == 'juego':

                if superficie_tablero.get_rect().collidepoint(posicion_mouse[0] - tablero_pos_x, posicion_mouse[1] - tablero_pos_y):
                    pos_relativa_x = posicion_mouse[0] - tablero_pos_x
                    pos_relativa_y = posicion_mouse[1] - tablero_pos_y

                    for i in range(FILAS):
                        for j in range(COLUMNAS):
                            celda = matriz_celdas[i][j]
                            if celda['rect'].collidepoint(pos_relativa_x, pos_relativa_y) and fin_juego == False:
                                sonido_click.play()
                                if evento.button == 1 and primer_click == True:
                                    generar_minas(matriz_celdas, CANTIDAD_MINAS, i, j)
                                    comprobar_vecinos(matriz_celdas)
                                    pygame.time.set_timer(evento_timer, 1000)
                                    tiempo_total = 0
                                    segundos_transcurridos = 0
                                    minutos_transcurridos = 0
                                    primer_click = False
                                    partida_activa = True

                                if evento.button == 1 and celda['estado'] == 'oculto':
                                    revelar_celdas(matriz_celdas, i, j)
                                    if celda['mina']:
                                        fin_juego = True
                                        pygame.time.set_timer(evento_timer, 0)
                                        sonido_explosion.play()
                                        pygame.time.delay(600)
                                        pygame.mixer.music.stop()
                                        sonido_derrota.play()
                                        iniciar_transicion(ventana_juego, imagen_fondo_blanco_escalada, imagen_derrota_escalada, 160, ANCHO_VENTANA, ALTO_VENTANA, True)
                                        pygame.mixer.music.play(-1)
                                    elif verificar_victoria(matriz_celdas) == True:
                                        fin_juego = True
                                        puntaje_total = int(10000 / (tiempo_total + 1)) * dificultad['multiplicador']
                                        pygame.time.set_timer(evento_timer, 0)
                                        input_activo = True
                                        pantalla_actual = 'victoria'
                                        pygame.mixer.music.stop()
                                        sonido_victoria.play()
                                        iniciar_transicion(ventana_juego, imagen_fondo_blanco_escalada, imagen_victoria_escalada, 160, ANCHO_VENTANA, ALTO_VENTANA, True)
                                        pygame.time.delay(4000)
                                        pygame.mixer.music.play(-1)
                                        
                                elif evento.button == 3 and primer_click == False:
                                    if celda['estado'] == 'oculto' and banderas_restantes > 0:
                                        celda['estado'] = 'bandera'
                                        banderas_restantes -= 1
                                    elif celda['estado'] == 'bandera':
                                        celda['estado'] = 'oculto'
                                        banderas_restantes += 1
                else:
                    for boton in lista_botones_pantalla:
                        if boton['rect'].collidepoint(posicion_mouse):
                            match boton['nombre']:
                                case 'Reiniciar':
                                    sonido_reset.play()
                                    valores_tablero = inicializar_tablero(ANCHO_VENTANA, ALTO_VENTANA, FILAS, COLUMNAS, CANTIDAD_MINAS)
                                    lado_tablero = valores_tablero[0]
                                    superficie_tablero = valores_tablero[1]
                                    tablero_pos_x = valores_tablero[2]
                                    tablero_pos_y = valores_tablero[3]
                                    matriz_celdas = valores_tablero[4]
                                    banderas_restantes = valores_tablero[5]
                                    primer_click = valores_tablero[6]
                                    fin_juego = valores_tablero[7]
                                    imagen_mina_escalada = valores_tablero[8]
                                    imagen_bandera_escalada = valores_tablero[9]
                                    segundos_transcurridos = 0
                                    tiempo_total = 0
                                    minutos_transcurridos = 0
                                    puntaje_total = 0
                                    pygame.time.set_timer(evento_timer, 0)
                                    primer_click = True
                                case 'Atras':
                                    sonido_click.play()
                                    if primer_click == True:
                                        partida_pausada = False
                                        pantalla_actual = 'menu_principal'
                                    else:
                                        partida_pausada = True
                                        pantalla_actual = 'menu_principal'
                                    pygame.time.set_timer(evento_timer, 0)
            

    if pantalla_actual != 'juego':
        lista_botones_pantalla = dibujar_pantalla_general(pantalla_actual, matriz_celdas, nombre_usuario,  superficie_tablero, tablero_pos_x, tablero_pos_y, partida_pausada)
        if pantalla_actual == 'puntajes':
            mostrar_jugadores(lista_jugadores, dificultad)
    else:
        lista_botones_pantalla = dibujar_pantalla_general(pantalla_actual, matriz_celdas, nombre_usuario, superficie_tablero , tablero_pos_x, tablero_pos_y, partida_pausada, 
                                                          imagen_mina_escalada, imagen_bandera_escalada, segundos_transcurridos, minutos_transcurridos, banderas_restantes, CANTIDAD_MINAS)
    pygame.display.flip()

pygame.quit()