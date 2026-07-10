def validar_codigo(codigo): return len(codigo.strip()) > 0
def validar_titulo(titulo): return len(titulo.strip()) > 0
def validar_plataforma(plataforma): return len(plataforma.strip()) > 0
def validar_genero(genero): return len(genero.strip()) > 0
def validar_editor(editor): return len(editor.strip()) > 0
def validar_precio(precio): return precio > 0
def validar_stock(stock): return stock >= 0
def validar_multiplayer(multiplayer):
def validar_clasificacion(clasificacion):

def buscar_codigo(codigo, juegos):
    return codigo.upper() in juegos


def busqueda_precio(p_min, p_max, juegos, inventario):
    resultados = []
    for cod, datos in inventario.items():
        if p_min <= datos[0] <= p_max and datos[1] > 0:
            resultados.append(f"{juegos[cod][0]}--{cod}")
    resultados.sort()
    return resultados


def agregar_juego(titulo, plataforma, genero, editor, clasificacion, precio, stock, juegos, inventario)
    if buscar_codigo(codigo, juegos):
        return False
    juegos[codigo.upper()] = [titulo, plataforma, genero, clasificacion, multiplayer, editor]
    inventario[codigo.upper()] = [precio, stock]
    return True

        

def actualizar_precio(codigo, nuevo_juego, inventario):
    if buscar_codigo(codigo, inventario):
        inventario[codigo.upper()][0] = nuevo_precio
        return True
    return False


def eliminar_juego(codigo, juegos, inventario):
    if buscar_codigo(codigo, juegos:
        del juegos [codigo.upper()]
        del inventario [codigo.upper()]
        return True
    return False

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6: 
                return opcion
            print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")
            

def gestion_agregar(juegos, inventario):
    if buscar_codigo(codigo, juegos)
    return False



def mostrar_menu():
    print("=====MENÚ PRINCIPAL=====")
    print("1. Stock por plataforma")
    print("2. Busqueda de juego por rango de precio")
    print("3. Actualizar preico juego")
    print("4. Agregar juego")
    print("5. Eliminar Juego")
    print("6. Salir")


def main ():


    juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
    ...
}


    inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
    ...
}

    
    while True:
        mostrar_menu():
        op = leer_opcion():

        if op == 1:

        elif op == 2:
            try:
                p_min = int(input("Precio mínimo: "))
                p_max = int(input("Precio máximo: "))
                
                if p_min > p_max:
                    print("El precio mínimo no puede ser mayor que el máximo.")
                else:
                    res = busqueda_precio(p_min, p_max, juegos, inventario):

                    if len(res) == 0:
                        print("No existen juegos en ese rango de precio.")

                    else:
                        for r in res:
                            print(r)
            except ValueError:
                print("Debe ingresar valores enteros."

        elif op == 3:
            while True:
                cod = input("Código: ")
                try:
                    val = input("Nuevo Precio: "))

                    if not validar_precio(val):
                        print("Precio inválido.")
                    elif actualizar_precio(cod, val, juegos):
                        print("Precio actualizado")
                    else: print("El código no existe")
                
                except ValueError:
                    print("Debe ingresar valores numéricos.")
                
                if input("¿Desea actualizar otro precio (s/n)? ").lower() == 'n':
                    break


        elif op == 4:
            gestion_agregar(juegos, inventario)

        elif op == 5:
            gestion_eliminar(juegos, inventario)
        elif op == 6:
            print("Programa finalizado.")
            break
        
if__name__ == "__main__" : main()