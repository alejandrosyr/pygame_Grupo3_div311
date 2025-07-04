import pygame
import random

pygame.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS_CLARO = (192, 192, 192)
GRIS_OSCURO = (128, 128, 128)
ROJO = (255, 0, 0)
NARANJA = (245, 153, 49)
AMARILLO = (243, 246, 144)
VERDE_CLARO = (102, 204, 0)
VERDE_OSCURO = (0, 102, 0)
CELESTE = (0, 176, 240)
AZUL = (0, 0, 255)
BORDEAU = (128, 0, 32)
VIOLETA = (120, 0, 180)

COLORES_CONTADOR = [CELESTE,         # 1
                    VERDE_CLARO,     # 2
                    NARANJA,         # 3
                    AMARILLO,        # 4
                    ROJO,            # 5
                    VERDE_OSCURO,    # 6
                    AZUL,            # 7
                    BORDEAU,         # 8
                    VIOLETA]         # 9

RESOLUCIONES = [{'ancho': 800, 'alto': 600},
                {'ancho': 1024, 'alto': 768},
                {'ancho': 1440, 'alto': 1080}]

DIFICULTADES = [{'nombre': 'Facil', 'filas': 8, 'columnas': 8, 'minas': 10,'multiplicador': 2},
                {'nombre': 'Medio', 'filas': 16, 'columnas': 16, 'minas': 50,'multiplicador': 4},
                {'nombre': 'Dificil', 'filas': 24, 'columnas': 24, 'minas': 120,'multiplicador': 6}]

resolucion = RESOLUCIONES[0]
dificultad = DIFICULTADES[0]
ANCHO_VENTANA = resolucion['ancho']
ALTO_VENTANA = resolucion['alto']

FILAS = dificultad['filas']
COLUMNAS = dificultad['columnas']
CANTIDAD_MINAS = dificultad['minas']

RUTA_FONDO = 'pygame_grupo3/assets/imagenes/fondo.png'
RUTA_FONDO_BLANCO = 'pygame_grupo3/assets/imagenes/fondo_blanco.png'
RUTA_BOTON = 'pygame_grupo3/assets/imagenes/boton.png'
RUTA_DERROTA = 'pygame_grupo3/assets/imagenes/derrota.png'
RUTA_VICTORIA = 'pygame_grupo3/assets/imagenes/victoria.png'
RUTA_TITULO = 'pygame_grupo3/assets/imagenes/titulo_juego.png'
RUTA_EQUIPO = 'pygame_grupo3/assets/imagenes/imagen_equipo.png'
RUTA_MINA = 'pygame_grupo3/assets/imagenes/mina.png'
RUTA_BANDERA = 'pygame_grupo3/assets/imagenes/bandera.png'
RUTA_TIMER = 'pygame_grupo3/assets/imagenes/timer.png'
RUTA_BANDERA_MINA = 'pygame_grupo3/assets/imagenes/banderas_minas.png'

RUTA_MUSICA_MENU = 'pygame_grupo3/assets/audio/intro.mp3'
RUTA_MUSICA_JUEGO = 'pygame_grupo3/assets/audio/juego.mp3'

RUTA_CLICK = 'pygame_grupo3/assets/audio/click.mp3'
RUTA_EXPLOSION = 'pygame_grupo3/assets/audio/explosion.mp3'
RUTA_RESET = 'pygame_grupo3/assets/audio/reset.mp3'
RUTA_SONIDO_DERROTA = 'pygame_grupo3/assets/audio/derrota.mp3'
RUTA_SONIDO_VICTORIA = 'pygame_grupo3/assets/audio/victoria.mp3'

RUTA_FUENTE_TITULO = 'pygame_grupo3/assets/font/PixelifySans-Bold.ttf'
RUTA_FUENTE_JUEGO = 'pygame_grupo3/assets/font/PixelifySans-VariableFont_wght.ttf'
RUTA_FUENTE_TIMER = 'pygame_grupo3/assets/font/fuente_contador.ttf'

RUTA_ARCHIVO = 'pygame_grupo3/puntaje.csv'

imagen_fondo = pygame.image.load(RUTA_FONDO)
imagen_fondo_blanco = pygame.image.load(RUTA_FONDO_BLANCO)
imagen_boton = pygame.image.load(RUTA_BOTON)
imagen_derrota = pygame.image.load(RUTA_DERROTA)
imagen_victoria = pygame.image.load(RUTA_VICTORIA)
imagen_titulo = pygame.image.load(RUTA_TITULO)
imagen_equipo = pygame.image.load(RUTA_EQUIPO)
imagen_mina = pygame.image.load(RUTA_MINA)
imagen_bandera = pygame.image.load(RUTA_BANDERA)
imagen_timer = pygame.image.load(RUTA_TIMER)
imagen_bandera_mina = pygame.image.load(RUTA_BANDERA_MINA)

imagen_fondo_escalada = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
imagen_fondo_blanco_escalada = pygame.transform.scale(imagen_fondo_blanco, (ANCHO_VENTANA, ALTO_VENTANA))
imagen_victoria_escalada = pygame.transform.scale(imagen_victoria, (ANCHO_VENTANA, ALTO_VENTANA))
imagen_derrota_escalada = pygame.transform.scale(imagen_derrota, (ANCHO_VENTANA, ALTO_VENTANA))
imagen_boton_escalada = pygame.transform.scale(imagen_boton, ((ANCHO_VENTANA * 0.16),(ALTO_VENTANA* 0.12)))
imagen_titulo_escalada = pygame.transform.scale(imagen_titulo, (ANCHO_VENTANA, ALTO_VENTANA))

volumen = 0.5
sonido_explosion = pygame.mixer.Sound(RUTA_EXPLOSION)
sonido_reset = pygame.mixer.Sound(RUTA_RESET)
sonido_click = pygame.mixer.Sound(RUTA_CLICK)
sonido_derrota = pygame.mixer.Sound(RUTA_SONIDO_DERROTA)
sonido_victoria = pygame.mixer.Sound(RUTA_SONIDO_VICTORIA)
pygame.mixer.music.set_volume(volumen)
sonido_explosion.set_volume(volumen)
sonido_reset.set_volume(volumen)
sonido_click.set_volume(volumen)
sonido_derrota.set_volume(volumen)
sonido_victoria.set_volume(volumen)

fuente_titulo = pygame.font.Font(RUTA_FUENTE_TITULO, ANCHO_VENTANA // 30)
fuente_juego = pygame.font.Font(RUTA_FUENTE_JUEGO, ANCHO_VENTANA // 30)
fuente_timer = pygame.font.Font(RUTA_FUENTE_TIMER, ANCHO_VENTANA // 30)

ventana_juego = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Py.Sweeper')


def reescalar_recursos(ancho, alto, dificultad_actual)->dict:
    '''
    Devuelve todos los recursos visuales, fuentes y el tablero ya escalados a la nueva resolución y dificultad.

    Args:
        ancho (int): El nuevo ancho de la ventana del juego en pixeles.
        alto (int): El nuevo alto de la ventana del juego en pixeles.
        dificultad_actual (dict): Diccionario con los parametros de la dificultad seleccionada

    Returns:
        dict: Un diccionario con todos los recursos reescalados y elementos necesarios para continuar el juego,
    '''
    valores_reescalados = {}
    ventana_nueva = pygame.display.set_mode((ancho, alto))
    fuente_titulo_nueva = pygame.font.Font(RUTA_FUENTE_TITULO, ancho // 30)
    fuente_juego_nueva = pygame.font.Font(RUTA_FUENTE_JUEGO, ancho // 30)
    fuente_timer_nueva = pygame.font.Font(RUTA_FUENTE_TIMER, ancho // 30)

    fondo_escalado = pygame.transform.scale(imagen_fondo, (ancho, alto))
    fondo_blanco_escalado = pygame.transform.scale(imagen_fondo_blanco, (ancho, alto))
    victoria_escalada = pygame.transform.scale(imagen_victoria, (ancho, alto))
    derrota_escalada = pygame.transform.scale(imagen_derrota, (ancho, alto))
    titulo_escalado = pygame.transform.scale(imagen_titulo, (ancho, alto))
    boton_escalado = pygame.transform.scale(imagen_boton, (int(ancho * 0.16), int(alto * 0.12)))

    timer_escalado = pygame.transform.scale(imagen_timer, (int(ancho * 0.18), int(alto * 0.13)))
    bandera_mina_escalada = pygame.transform.scale(imagen_bandera_mina, (int(ancho * 0.18), int(alto * 0.13)))


    filas = dificultad_actual['filas']
    columnas = dificultad_actual['columnas']
    minas = dificultad_actual['minas']
    valores_tablero = inicializar_tablero(ancho, alto, filas, columnas, minas)

    valores_reescalados = {'ventana': ventana_nueva,
                           'fuente_titulo': fuente_titulo_nueva,
                           'fuente_juego': fuente_juego_nueva,
                           'fuente_timer': fuente_timer_nueva,
                           'imagen_fondo_escalada': fondo_escalado,
                           'imagen_fondo_blanco_escalada': fondo_blanco_escalado,
                           'imagen_victoria_escalada': victoria_escalada,
                           'imagen_derrota_escalada': derrota_escalada,
                           'imagen_titulo_escalada': titulo_escalado,
                           'imagen_boton_escalada': boton_escalado,
                           'imagen_timer_escalada': timer_escalado,
                           'imagen_bandera_mina_escalada': bandera_mina_escalada,
                           'valores_tablero': valores_tablero}
    return valores_reescalados
        

def cambiar_volumen(volumen:float, operador:str) -> float:
    ''' Ajusta el volumen global de los sonidos y la musica.
        Args:
            volumen (float): Valor actual del volumen (0.0 a 1.0).
            operador (str): Operador para ajustar el volumen. '+' incrementa, '-' decrementa, cualquier otro valor lo mutea.
        Returns:
            float: Nuevo valor de volumen ajustado.
    '''
    if operador == '+':
        volumen += .1
    elif operador == '-':
        volumen -= .1
    else: 
        volumen = 0
    sonido_explosion.set_volume(volumen)
    sonido_click.set_volume(volumen)
    sonido_derrota.set_volume(volumen)
    sonido_victoria.set_volume(volumen)
    sonido_reset.set_volume(volumen)
    pygame.mixer.music.set_volume(volumen)

    return volumen


def mostrar_jugadores(lista_jugadores:list[dict], dificultad: dict)->None:
    ''' Muestra en pantalla los jugadores con la dificultad seleccionada y sus puntajes, ordenados de mayor a menor.\n
        Args:
            lista_jugadores (list[dict]): Lista de jugadores con nombre, puntaje y dificultad.
            dificultad (dict): Dificultad actual seleccionada (clave 'nombre').
        Returns:
            None
    '''
    texto_titulo = fuente_juego.render('Nombres       Puntos ', True, AMARILLO)
    rect_texto = texto_titulo.get_rect(center=(ANCHO_VENTANA * .58 , ALTO_VENTANA * .35))
    ventana_juego.blit(texto_titulo, rect_texto)
    alto_texto = ALTO_VENTANA * .4

    jugadores_filtrados = [] 
    contador_personas = 0

    for i in range(len(lista_jugadores)):
        if lista_jugadores[i]['dificultad'] == dificultad['nombre'] and contador_personas < 10:
            jugadores_filtrados.append(lista_jugadores[i])
            contador_personas += 1

    for jugador in jugadores_filtrados:
        ancho_texto = ANCHO_VENTANA * .5
        for valores in jugador.values():
            if valores == 'Facil' or valores == 'Dificil' or valores == 'Medio':
                continue
            texto_titulo = fuente_juego.render(f'{valores}', True, AMARILLO)
            rect_texto = texto_titulo.get_rect(center=(ancho_texto, alto_texto))
            ventana_juego.blit(texto_titulo, rect_texto)
            ancho_texto += 150
        alto_texto += 20


def guardar_resultados(ruta_archivo: str, lista_jugadores: list[dict], nombre: str, puntaje: int, dificultad: str) -> None:
    ''' Agrega/actualiza un jugador, ordena por puntaje y guarda todo en el archivo CSV.
        Args:
            ruta_archivo (str): Ruta del archivo CSV.
            lista_jugadores (list[dict]): Lista actual de jugadores.
            nombre (str): Nombre del jugador.
            puntaje (int): Puntaje final.
            dificultad (str): Dificultad jugada.
        Returns:
            None
    '''
    lista_jugadores = agregar_actualizar_y_ordenar(lista_jugadores, nombre, puntaje, dificultad)
    informacion_csv = crear_encabezado(['nombre', 'puntaje', 'dificultad'], ',')
    for jugador in lista_jugadores:
        informacion_csv += dar_formato_csv(jugador)

    escribir_archivo(ruta_archivo, 'w', informacion_csv)


def agregar_actualizar_y_ordenar(lista_jugadores: list[dict], nombre: str, puntaje: int, dificultad: str) -> list[dict]:
    ''' Agrega un nuevo jugador o actualiza su puntaje si ya existe, luego ordena la lista de mayor a menor puntaje.
        Args:
            lista_jugadores (list[dict]): Lista de jugadores.
            nombre (str): Nombre del jugador.
            puntaje (int): Puntaje obtenido.
            dificultad (str): Dificultad jugada.
        Returns: 
            list[dict]: Lista actualizada y ordenada.
    '''
    jugador_existente = False

    for jugador in lista_jugadores:
        if jugador['nombre'] == nombre:
            jugador['puntaje'] = puntaje
            jugador['dificultad'] = dificultad
            jugador_existente = True
            break

    if jugador_existente == False:
        nuevo_jugador = {
            'nombre': nombre,
            'puntaje': puntaje,
            'dificultad': dificultad
        }
        lista_jugadores.append(nuevo_jugador)

    lista_jugadores.sort(key=lambda x: x['puntaje'], reverse=True)
    return lista_jugadores


def crear_encabezado(lista_claves:list, separador:str)->str:
    ''' Crea un encabezado de texto para un archivo CSV.
        Args:
            lista_claves (list): Lista de claves que se usaran como encabezados.
            separador (str): Separador para unir las claves (ejemplo: ',').
        Returns:
            str: Encabezado formateado.
    '''
    return separador.join(lista_claves) + '\n'


def extraer_jugadores_csv(datos_archivo:str)->list:
    ''' Convierte el contenido de un archivo CSV en una lista de diccionarios de jugadores.
        Args:
            datos_archivo (str): Contenido completo del archivo CSV como cadena.
        Returns:
            list: Lista de jugadores como diccionarios.
    '''
    retorno_strip = datos_archivo.strip()
    retorno_split = retorno_strip.split('\n')
    lista = []
    if len(retorno_split) == 1:
        print('No se han cargado jugadores a la lista.')
    else:
        for i in range(len(retorno_split)):
            if i == 0:
                lista_claves = retorno_split[i].split(',') 
            else:
                lista_valores = retorno_split[i].split(',') 
                jugador = {}
                for j in range(len(lista_claves)):
                    if lista_valores[j].isdigit() == False:
                        jugador.update({lista_claves[j]:lista_valores[j]}) 
                    else:
                        jugador.update({lista_claves[j]:int(lista_valores[j])})
                lista.append(jugador)
    return lista


def validar_nombre(nombre_usuario: str) -> bool:
    ''' Valida que el nombre ingresado no sea vacio, tenga solo letras y tenga mínimo 4 caracteres.
        Args:
            nombre_usuario (str): = nombre ingresado.
        Return: 
            bool: retorna un valor booleano.
    '''
    nombre_valido = True
    if len(nombre_usuario) < 4 or nombre_usuario == '':
        nombre_valido = False
    else:
        for i in range(len(nombre_usuario)):
            letra = nombre_usuario[i]
            if letra.isalpha() == False:
                nombre_valido = False
    return nombre_valido

    
def dar_formato_csv(diccionario:dict)->str:
    ''' Convierte los valores de un diccionario en una línea de texto con formato CSV.
        Args:
            diccionario (dict): Diccionario cuyos valores se convertirán en una línea CSV.
        Returns:
            str: Cadena de texto con formato CSV.
    '''
    informacion = ''
    contador_valor = 0
    for valor in diccionario.values():
        contador_valor += 1
        if contador_valor != len(diccionario.keys()):
            informacion += str(valor) + ','
        else:
            informacion += str(valor) + '\n'
    return informacion


def escribir_archivo(ruta_archivo:str, modo_apertura:str, informacion:str)->None:
    ''' Escribe informacion en un archivo csv.
        Args:
            ruta_archivo (str): Ruta del archivo donde escribir.
            modo_apertura (str): Modo de apertura del archivo (ejemplo: 'w' para sobrescribir).
            informacion (str): Texto que se escribira en el archivo.
        Returns:
            None
    '''
    with open(ruta_archivo, modo_apertura) as archivo:
        archivo.write(informacion)


def leer_archivo(ruta_archivo:str)->str:
    ''' Lee el contenido de un archivo y lo devuelve como texto. Si el archivo no existe, lo crea vacio.
        Args:
            ruta_archivo (str): Ruta del archivo a leer.
        Returns:
            str: Contenido del archivo.
    '''
    datos_concatenados = ''
    try:
        with open(ruta_archivo, 'r') as archivo:
            datos_concatenados = archivo.read()        
    except:
        archivo = open(ruta_archivo, 'w')
        archivo.close()
    return datos_concatenados


def construir_matriz(superficie_tablero:pygame.Surface, filas: int, columnas: int) -> list[list[dict]]:
    ''' Construye una matriz de diccionarios que representan cada celda del tablero.
        Cada celda contiene:
        - 'mina': bool, indica si hay mina.
        - 'contador': int, minas vecinas.
        - 'estado': str, estado de la celda ('oculto', 'revelado', 'bandera').
        - 'posicion': tuple, coordenadas (fila, columna).
        - 'rect': pygame.Rect, posición y tamaño.
    Args:
        superficie_tablero (pygame.Surface): Superficie del tablero.
        filas (int): Cantidad de filas.
        columnas (int): Cantidad de columnas.
    Returns:
        list[list[dict]]: Matriz del tablero.
    '''
    matriz = []
    ancho_celda = superficie_tablero.get_width() // columnas
    alto_celda = superficie_tablero.get_height() // filas
    for i in range(filas):
        fila = []
        for j in range(columnas):
            posicion_x = j * ancho_celda
            posicion_y = i * alto_celda
            rect = pygame.Rect(posicion_x, posicion_y, ancho_celda, alto_celda)
            celda = {'mina': False,
                     'contador': 0,
                     'estado': 'oculto',
                     'posicion': (i, j),
                     'rect': rect}
            fila.append(celda)
        matriz.append(fila)
    return matriz


def generar_minas(matriz_recibida:list[list[dict]], cantidad_minas:int, fila_excluida:int, columna_excluida:int) -> None:
    ''' Coloca minas aleatorias evitando la celda seleccionada y sus vecinas.
        Args:
            matriz_recibida (list[list[dict]]): Matriz de celdas.
            cantidad_minas (int): Numero de minas.
            fila_excluida (int): Fila a excluir.
            columna_excluida (int): Columna a excluir.
        Returns:
            None
    '''
    limites = obtener_limites(matriz_recibida, fila_excluida, columna_excluida)
    fila_inicio = limites[0]
    fila_fin = limites[1]
    columna_inicio = limites[2]
    columna_fin = limites[3]

    while cantidad_minas > 0:
        fila = random.randint(0, len(matriz_recibida) - 1)
        columna = random.randint(0, len(matriz_recibida[0]) - 1)
        celda = matriz_recibida[fila][columna]
        if celda['mina'] == False and (fila < fila_inicio or fila > fila_fin or columna < columna_inicio or columna > columna_fin):
            celda['mina'] = True
            cantidad_minas -= 1


def obtener_limites(matriz_recibida:list[list[dict]], fila:int, columna:int)-> list:
    ''' Calcula los limites de filas y columnas vecinas.
        Args:
            matriz_recibida (list[list[dict]]): Matriz del tablero.
            fila (int): Fila de la celda.
            columna (int): Columna de la celda.
        Returns:
            list: [fila_inicio, fila_fin, columna_inicio, columna_fin].
    '''
    limites = []
    valor_filas = len(matriz_recibida)
    valor_columnas = len(matriz_recibida[0])
    if fila - 1 >= 0:
        fila_inicio = fila - 1
    else:
        fila_inicio = fila
    limites.append(fila_inicio)
    if fila + 1 < valor_filas:
        fila_fin = fila + 1
    else:
        fila_fin = fila
    limites.append(fila_fin)
    if columna - 1 >= 0:
        columna_inicio = columna - 1
    else:
        columna_inicio = columna
    limites.append(columna_inicio)
    if columna + 1 < valor_columnas:
        columna_fin = columna + 1
    else:
        columna_fin = columna
    limites.append(columna_fin)
    return limites


def actualizar_vecinos(matriz_recibida:list[list[dict]], fila:int, columna: int)-> None:
    ''' Incrementa contador de minas en cada celda vecina si no tiene mina.
        Args:
            matriz_recibida (list[list[dict]]): Matriz del tablero.
            fila (int): Fila de la celda.
            columna (int): Columna de la celda.
        Returns:
            None
    '''
    limites = obtener_limites(matriz_recibida, fila, columna)
    fila_inicio = limites[0]
    fila_fin = limites[1]
    columna_inicio = limites[2]
    columna_fin = limites[3]
    
    for i in range(fila_inicio, fila_fin + 1):
        for j in range(columna_inicio, columna_fin + 1):
            if (i != fila or j != columna) and matriz_recibida[i][j]['mina'] == False:
                matriz_recibida[i][j]['contador'] += 1


def comprobar_vecinos(matriz_recibida:list[list[dict]]) -> None:
    ''' Actualiza contadores de minas para todas las celdas de la matriz.
        Args:
            matriz_recibida (list[list[dict]]): Matriz del tablero.
        Returns:
            None
    '''
    for i in range(len(matriz_recibida)):
        for j in range(len(matriz_recibida[i])):
            if matriz_recibida[i][j]['mina'] == True:
                actualizar_vecinos(matriz_recibida, i, j)


def revelar_celdas(matriz_recibida:list[list[dict]], fila:int, columna:int)-> None:
    ''' Revela una celda y expande vecinas recursivamente si no hay minas. Si la celda es mina, revela todas.
        Args:
            matriz_recibida (list[list[dict]]): Matriz del tablero.
            fila (int): Fila de la celda.
            columna (int): Columna de la celda.
        Returns:
            None
    '''
    seguir = True
    celda = matriz_recibida[fila][columna]
    if celda['estado'] == 'revelado' or celda['estado'] == 'bandera':
        seguir = False
    if seguir == True:
        celda['estado'] = 'revelado'
        if celda['mina'] == True:
            for i in range(len(matriz_recibida)):
                for j in range(len(matriz_recibida[i])):
                    if matriz_recibida[i][j]['mina'] == True:
                        matriz_recibida[i][j]['estado'] = 'revelado'

        elif celda['contador'] == 0 and celda['mina'] == False:
            limites = obtener_limites(matriz_recibida, fila, columna)
            fila_inicio = limites[0]
            fila_fin = limites[1]
            columna_inicio = limites[2]
            columna_fin = limites[3]
            for i in range(fila_inicio, fila_fin + 1):
                for j in range(columna_inicio, columna_fin + 1):
                    if i != fila or j != columna:
                        revelar_celdas(matriz_recibida, i, j)


def verificar_victoria(matriz:list[list[dict]]) -> bool:
    ''' Verifica si todas las celdas sin minas estan reveladas.
        Args:
            matriz (list[list[dict]]): Matriz del tablero.
        Returns:
            bool: True si gano el juego, False si no.
    '''
    victoria = True
    for fila in matriz:
        for celda in fila:
            if celda['mina'] == False and celda['estado'] != 'revelado':
                victoria = False
    return victoria


def ajustar_lado_tablero(alto_ventana: int, filas: int, columnas: int) -> int:
    ''' Calcula el lado optimo del tablero ajustado a filas y columnas.
        Args:
            alto_ventana (int): Altura de la ventana.
            filas (int): Cantidad de filas.
            columnas (int): Cantidad de columnas.
        Returns:
            int: Tamaño ajustado del lado del tablero.
    '''
    lado_inicial = int(alto_ventana * 0.90)
    lado_min = int(alto_ventana * 0.85)
    lado_max = int(alto_ventana * 0.95)
    while lado_inicial % filas != 0 or lado_inicial % columnas != 0:
        if lado_inicial > lado_min and lado_inicial < lado_max:
            lado_inicial -= 1
        else:
            lado_inicial = lado_max
    return lado_inicial


def inicializar_tablero(ancho_ventana:int, alto_ventana:int, filas:int, columnas:int, cantidad_minas:int) -> list:
    ''' Inicializa tablero, superficie y elementos base.
        Args:
            ancho_ventana (int): Ancho de la ventana.
            alto_ventana (int): Alto de la ventana.
            filas (int): Numero de filas.
            columnas (int): Numero de columnas.
            cantidad_minas (int): Numero de minas.
        Returns:
            list: Datos iniciales del tablero y elementos necesarios.
    '''
    margen = int(ancho_ventana * 0.025)
    ancho_zona_tablero = int(ancho_ventana * 0.75)
    if ancho_zona_tablero < (alto_ventana - 2 * margen):
        lado_maximo = ancho_zona_tablero
    else:
        lado_maximo = alto_ventana - 2 * margen
    lado_tablero = ajustar_lado_tablero(lado_maximo, filas, columnas)
    superficie_tablero = pygame.Surface((lado_tablero, lado_tablero), pygame.SRCALPHA)
    ancho_celda = superficie_tablero.get_width() // columnas
    imagen_bandera_escalada = pygame.transform.scale(imagen_bandera, (ancho_celda - 8, ancho_celda - 8))
    imagen_mina_escalada = pygame.transform.scale(imagen_mina, (ancho_celda - 8, ancho_celda - 8))
    tablero_pos_x = ancho_ventana - lado_tablero - margen
    tablero_pos_y = (alto_ventana - lado_tablero) // 2
    matriz_celdas = construir_matriz(superficie_tablero, filas, columnas)
    banderas_restantes = cantidad_minas
    primer_click = True
    fin_juego = False
    retorno = [lado_tablero, superficie_tablero, tablero_pos_x, tablero_pos_y, matriz_celdas, banderas_restantes, primer_click, fin_juego, imagen_mina_escalada, imagen_bandera_escalada]
    return retorno


def dibujar_tablero(superficie_tablero:pygame.Surface, matriz_recibida:list[list[dict]], imagen_mina:pygame.Surface, imagen_bandera:pygame.Surface)-> None:
    ''' Dibuja el tablero segun el estado de cada celda.
        Args:
            superficie_tablero (pygame.Surface): Superficie del tablero.
            matriz_recibida (list[list[dict]]): Matriz de celdas.
            imagen_mina (pygame.Surface): Imagen de mina.
            imagen_bandera (pygame.Surface): Imagen de bandera.
        Returns:
            None
    '''
    for i in range(len(matriz_recibida)):
        for j in range(len(matriz_recibida[i])):
            celda = matriz_recibida[i][j]
            rectangulo = celda['rect']

            if celda['estado'] == 'revelado':
                if celda['mina'] == True:
                    color_fondo = ROJO
                else:    
                    color_fondo = GRIS_OSCURO
            else:
                color_fondo = GRIS_CLARO
            
            pygame.draw.rect(superficie_tablero, color_fondo, rectangulo)
            pygame.draw.rect(superficie_tablero, (0, 0, 0), rectangulo, 1)

            if celda['estado'] == 'revelado':
                if celda['mina'] == True:
                    centro_rectangulo = celda['rect'].center
                    rect_imagen = imagen_mina.get_rect(center=centro_rectangulo)
                    superficie_tablero.blit(imagen_mina, rect_imagen)
                elif celda['contador'] > 0:
                    fuente = fuente_titulo
                    color_numero = COLORES_CONTADOR[celda['contador']-1]
                    texto = fuente.render(str(celda['contador']), True, color_numero)
                    superficie_tablero.blit(texto, texto.get_rect(center=rectangulo.center))

            elif celda['estado'] == 'bandera':
                centro_rectangulo = celda['rect'].center
                rect_imagen = imagen_bandera.get_rect(center=centro_rectangulo)
                superficie_tablero.blit(imagen_bandera, rect_imagen)


def iniciar_transicion(ventana:pygame.Surface, fondo:pygame.Surface, imagen:pygame.Surface, duracion:int, ancho:int, alto:int, pantalla_victoria:bool = False) -> None:
    ''' Muestra transicion con imagen centrada sobre fondo.
        Args:
            ventana (pygame.Surface): Ventana principal.
            fondo (pygame.Surface): Fondo de la transicion.
            imagen (pygame.Surface): Imagen a mostrar.
            duracion (int): Duracion en cuadros.
            ancho (int): Ancho de ventana.
            alto (int): Alto de ventana.
            pantalla_victoria (bool, optativo): Si es pantalla de victoria. False por defecto.
        Returns:
            None
    '''
    reloj = pygame.time.Clock()
    contador = 0
    salir_antes = False
    while contador < duracion and salir_antes == False:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN and (evento.key == pygame.K_ESCAPE or evento.key == pygame.K_RETURN or evento.key == pygame.K_SPACE) and pantalla_victoria == False:
                salir_antes = True
            
        ventana.blit(fondo, (0, 0))
        rect_imagen = imagen.get_rect(center=(ancho // 2, alto // 2))
        ventana.blit(imagen, rect_imagen)
        pygame.display.flip()
        reloj.tick(30)
        contador += 1
    if pantalla_victoria == False:
        if salir_antes == True:
            pygame.mixer.music.set_pos(9.78)
    

def mostrar_transicion_inicial(ventana:pygame.Surface, ancho_ventana:int, alto_ventana:int, ruta_musica_intro:str) -> None:
    ''' Muestra animacion inicial con logo del equipo y titulo.
        Args:
            ventana (pygame.Surface): Ventana principal.
            ancho_ventana (int): Ancho de la ventana.
            alto_ventana (int): Alto de la ventana.
            ruta_musica_intro (str): Ruta de musica de introduccion.
        Returns:
            None
    '''
    
    pygame.mixer.music.load(ruta_musica_intro)
    pygame.mixer.music.set_volume(volumen)
    pygame.mixer.music.play(-1)
    imagen_equipo_transicion = pygame.transform.scale(imagen_equipo, (int(ancho_ventana * 0.7),int(alto_ventana * 0.7)))
    imagen_titulo_transicion = pygame.transform.scale(imagen_titulo, (int(ancho_ventana * 0.7),int(alto_ventana * 0.7)))

    iniciar_transicion(ventana, imagen_fondo_blanco_escalada, imagen_equipo_transicion, 300, ancho_ventana, alto_ventana)
    iniciar_transicion(ventana, imagen_fondo_blanco_escalada, imagen_titulo_transicion, 250, ancho_ventana, alto_ventana)


def cargar_botones(lista_nombres:list[str], fuente:pygame.font.Font, ventana:pygame.Surface, imagen_boton:pygame.Surface, x_inicial:float, y_inicial:float, margen:float, color_texto:tuple) -> list[dict]:
    ''' Carga y dibuja botones alineados con texto centrado.
        Args:
            lista_nombres (list[str]): Nombres de los botones.
            fuente (pygame.font.Font): Fuente de texto.
            ventana (pygame.Surface): Ventana principal.
            imagen_boton (pygame.Surface): Imagen base del botón.
            x_inicial (float): Posicion horizontal base.
            y_inicial (float): Posicion vertical base.
            margen (float): Separacion vertical.
            color_texto (tuple): Color del texto.
        Returns:
            list[dict]: Lista de diccionarios con informacion de botones.
    '''
    ancho_ventana = ventana.get_width()
    alto_ventana = ventana.get_height()
    ancho_boton = int(ancho_ventana * 0.25)
    alto_boton = int(alto_ventana * 0.12)
    imagen_escalada = pygame.transform.scale(imagen_boton, (ancho_boton, alto_boton))
    botones = []

    for i in range(len(lista_nombres)):
        posicion_x = int(ancho_ventana * x_inicial)
        posicion_y = int(alto_ventana * (y_inicial + i * margen))
        texto = lista_nombres[i]
        rect_boton = imagen_escalada.get_rect(center=(posicion_x, posicion_y))
        ventana.blit(imagen_escalada, rect_boton.topleft)
        texto_renderizado = fuente.render(texto, True, color_texto)
        rect_texto = texto_renderizado.get_rect(center=rect_boton.center)
        botones.append({'nombre': texto, 'rect': rect_boton})
        ventana.blit(texto_renderizado, rect_texto.topleft)     

    return botones


def cargar_fondo(ventana: pygame.Surface, ruta_fondo: str) -> None:
    ''' Carga y ajusta imagen de fondo de la ventana.
        Args:
            ventana (pygame.Surface): Ventana principal.
            ruta_fondo (str): Ruta de la imagen de fondo.
        Returns:
            None
    '''
    fondo = pygame.image.load(ruta_fondo).convert()
    fondo = pygame.transform.scale(fondo, (ventana.get_width(), ventana.get_height()))
    ventana.blit(fondo, (0, 0))


def dibujar_pantalla_general(pantalla_actual:str, matriz:list[list[dict]] = None, nombre_usuario:str = '',superficie_tablero: pygame.Surface = None, 
                             tablero_pos_x: int = 0, tablero_pos_y:int = 0, bandera_pausa:bool = False, imagen_mina:pygame.Surface = None, imagen_bandera:pygame.Surface = None,
                             segundos_transcurridos:int = 0, minutos_transcurridos:int = 0, banderas_restantes:int = 0, minas:int = 0) -> list[dict]:
    ''' Dibuja toda la interfaz segun pantalla actual y devuelve botones activos.
        Args:
            pantalla_actual (str): Pantalla a mostrar.
            matriz (list[list[dict]], optativo): Matriz del tablero. None por defecto.
            nombre_usuario (str, optativo): Nombre del jugador. '' por defecto.
            superficie_tablero (pygame.Surface, optativo): Superficie del tablero. None por defecto.
            tablero_pos_x (int, optativo): Posición X del tablero. 0 por defecto.
            tablero_pos_y (int, optativo): Posición Y del tablero. 0 por defecto.
            bandera_pausa (bool, optativo): Indica si está en pausa. False por defecto.
            imagen_mina (pygame.Surface, optativo): Imagen de mina. None por defecto.
            imagen_bandera (pygame.Surface, optativo): Imagen de bandera. None por defecto.
            segundos_transcurridos (int, optativo): Segundos del cronómetro. 0 por defecto.
            minutos_transcurridos (int, optativo): Minutos del cronómetro. 0 por defecto.
            banderas_restantes (int, optativo): Banderas restantes. 0 por defecto.
            minas (int, optativo): Total de minas. 0 por defecto.
        Returns:
            list[dict]: Lista de botones activos.
    '''
    lista_botones_pantalla = []
    cargar_fondo(ventana_juego, RUTA_FONDO)

    if pantalla_actual != 'victoria' and pantalla_actual != 'derrota':
        titulo_escalado = pygame.transform.scale(imagen_titulo, (int(ANCHO_VENTANA * 0.6), int(ALTO_VENTANA * 0.25)))
        rect_titulo = titulo_escalado.get_rect(center=(ANCHO_VENTANA // 2, int(ALTO_VENTANA * 0.1)))
        ventana_juego.blit(titulo_escalado, rect_titulo)

    match pantalla_actual:
        case 'menu_principal':
            if bandera_pausa == True:
                nombres = ['Continuar', 'Opciones', 'Puntajes', 'Salir']
            else:
                nombres = ['Jugar', 'Opciones', 'Puntajes', 'Salir'] 
        case 'seleccion_dificultad':
            texto = fuente_juego.render('Selecciona la dificultad', True, AMARILLO)
            rect_texto = texto.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 5))
            ventana_juego.blit(texto, rect_texto)
            nombres = ['Facil', 'Medio', 'Dificil', 'Atras']
        case 'opciones':
            texto = fuente_juego.render('Opciones', True, AMARILLO)
            rect_texto = texto.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 5))
            ventana_juego.blit(texto, rect_texto)
            nombres = ['Resolucion', 'Sonido', 'Atras']
        case 'resolucion':
            texto = fuente_juego.render('Resoluciones', True, AMARILLO)
            rect_texto = texto.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 5))
            ventana_juego.blit(texto, rect_texto)
            nombres = ['800x600', '1024x768', '1440x1080', 'Atras']    
        case 'sonido':
            texto = fuente_juego.render('Sonido', True, AMARILLO)
            rect_texto = texto.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 5))
            ventana_juego.blit(texto, rect_texto)
            nombres = ['Mutear', '+', '-', 'Atras']
        case 'puntajes':
            texto = fuente_juego.render('Puntajes', True, AMARILLO)
            rect_texto = texto.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 5))
            ventana_juego.blit(texto, rect_texto)
            nombres = ['Facil', 'Medio', 'Dificil', 'Atras']
            rect_puntos = pygame.Rect(ANCHO_VENTANA * .3 ,ALTO_VENTANA * .3,ANCHO_VENTANA * .60,ALTO_VENTANA * .60)
            pygame.draw.rect(ventana_juego, NEGRO, rect_puntos)
        case 'juego':
            superficie_tablero.fill(GRIS_CLARO)
            dibujar_tablero(superficie_tablero, matriz, imagen_mina, imagen_bandera)
            ventana_juego.blit(superficie_tablero, (tablero_pos_x, tablero_pos_y))
            nombres = ['Reiniciar', 'Atras']

            ancho_img_timer = int(ANCHO_VENTANA * 0.18)
            alto_img_timer = int(ALTO_VENTANA * 0.13)
            imagen_timer_escalada = pygame.transform.scale(imagen_timer, (ancho_img_timer, alto_img_timer))
            pos_x_timer = int(ANCHO_VENTANA * 0.04)
            pos_y_timer = int(ALTO_VENTANA * 0.07)
            ventana_juego.blit(imagen_timer_escalada, (pos_x_timer, pos_y_timer))

            texto_timer = fuente_timer.render(f'{minutos_transcurridos:02d}   {segundos_transcurridos:02d}', True, ROJO)
            rect_imagen = imagen_timer_escalada.get_rect(topleft=(pos_x_timer, pos_y_timer))
            rect_texto = texto_timer.get_rect(center=rect_imagen.center)
            rect_texto.y += 15
            ventana_juego.blit(texto_timer, rect_texto)

            ancho_img_bandera_mina = int(ANCHO_VENTANA * 0.18)
            alto_img_bandera_mina = int(ALTO_VENTANA * 0.13)
            imagen_bandera_mina_escalada = pygame.transform.scale(imagen_bandera_mina, (ancho_img_bandera_mina, alto_img_bandera_mina))
            pos_x_bandera_mina = int(ANCHO_VENTANA * 0.04)
            pos_y_bandera_mina = int(ALTO_VENTANA * 0.25)
            ventana_juego.blit(imagen_bandera_mina_escalada, (pos_x_bandera_mina, pos_y_bandera_mina))

            texto_banderas_minas = fuente_timer.render(f'{banderas_restantes:02d}   {minas:02d}', True, AZUL)
            rect_img_bandera_mina = imagen_bandera_mina_escalada.get_rect(topleft=(pos_x_bandera_mina, pos_y_bandera_mina))
            rect_texto_bandera_mina = texto_banderas_minas.get_rect(center=rect_img_bandera_mina.center)
            rect_texto_bandera_mina.y += 15
            ventana_juego.blit(texto_banderas_minas, rect_texto_bandera_mina)
        case 'victoria':
            ventana_juego.blit(imagen_victoria_escalada, (0,0))
            nombres = ['Ingresar']
            caja_texto = pygame.Rect(ANCHO_VENTANA * 0.25, ALTO_VENTANA * 0.5, 400, 50)
            pygame.draw.rect(ventana_juego, NEGRO, caja_texto)
            pygame.draw.rect(ventana_juego, ROJO, caja_texto, 2)

            texto_superficie = fuente_juego.render(nombre_usuario, True, ROJO)
            ventana_juego.blit(texto_superficie, (ANCHO_VENTANA * 0.28, ALTO_VENTANA * 0.51))

    if pantalla_actual == 'juego':
        lista_botones_pantalla = cargar_botones(nombres, fuente_juego, ventana_juego, imagen_boton, 0.16, 0.7, 0.14, AMARILLO)
    elif pantalla_actual == 'victoria':
        lista_botones_pantalla = cargar_botones(nombres, fuente_juego, ventana_juego, imagen_boton, 0.5, 0.7, 0.14, AMARILLO)
    elif pantalla_actual == 'puntajes':
        lista_botones_pantalla = cargar_botones(nombres, fuente_juego, ventana_juego, imagen_boton, 0.16, 0.4, 0.14, AMARILLO)
    else:
        lista_botones_pantalla = cargar_botones(nombres, fuente_juego, ventana_juego, imagen_boton, 0.5, 0.4, 0.14, AMARILLO)

    pygame.display.flip()
    return lista_botones_pantalla