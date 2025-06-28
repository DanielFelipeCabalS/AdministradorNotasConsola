print('*** Administrador de notas ***')

#Variables globales
id = 1
notas = []

def menu():
    print('''Escoge una opción:
    1. Agregar nota
    2. Mostrar todas las notas
    3. Buscar nota por id
    4. Buscar nota por palabra clave
    5. Editar nota
    6. Eliminar nota
    7. Salir''')

def imprimir_nota(nota):
    print(f"\nId: {nota['id']}"
          f"\nTítulo: {nota['titulo']}"
          f"\nContenido: {nota['contenido']}\n")

def obtener_indice_id(id_nota):
    for i, nota in enumerate(notas):
        if nota['id'] == id_nota:
            return i
    return None

def agregar_nota():
    global id
    titulo = input('Ingrese el título de la nota: ')
    contenido = input('Ingrese el contenido de la nota: ')
    notas.append({'id': id, 'titulo': titulo, 'contenido': contenido})
    id += 1
    print('Nueva nota creada con éxito')

def mostrar_notas():
    for nota in notas:
        imprimir_nota(nota)

def buscar_nota_id():
    buscar = int(input('Ingrese el id de la nota: '))
    for nota in notas:
        if nota.get('id') == buscar:
            imprimir_nota(nota)
            return nota
    print('Id no encontrado')

def buscar_nota_palabra():
    buscar = input('Ingrese la palabra que desea buscar: ')
    contador = 0
    for nota in notas:
        if buscar in nota.get('titulo') or buscar in nota.get('contenido'):
            imprimir_nota(nota)
            contador += 1
    if contador > 0:
        return
    else:
        print('No se encontró la palabra clave')

def editar_nota():
    nota = None
    nota = buscar_nota_id()
    if nota != None:
        indice = obtener_indice_id(nota['id'])
        print('1. Si deseas modificar el título'
              '\n2. Si deseas modificar el contenido'
              '\n3. Si deseas modificar todo')
        op = int(input('Ingrese la opción a modificar: '))
        if op == 1:
            titulo = input('Ingrese el nuevo título: ')
            notas [indice] = {'id': nota.get('id'), 'titulo': titulo, 'contenido': nota.get('contenido')}
            print('Título modificado')
            imprimir_nota(notas[indice])
        elif op == 2:
            contenido = input('Ingrese el nuevo contenido de la nota: ')
            notas[indice] = {'id': nota.get('id'), 'titulo': nota.get('titulo'), 'contenido': contenido}
            print('Contenido modificado')
            imprimir_nota(notas[indice])
        elif op == 3:
            titulo = input('Ingrese el nuevo título: ')
            contenido = input('Ingrese el nuevo contenido de la nota: ')
            notas[indice] = {'id': nota.get('id'), 'titulo': titulo, 'contenido': contenido}
            imprimir_nota(notas[indice])
        else:
            print('Ingresaste una opción inválida')
            editar_nota()

def eliminar_nota():
    mostrar_notas()
    eliminar = int(input('Ingrese el id de la nota a eliminar: '))
    for i, nota in enumerate(notas):
        if eliminar == nota['id']:
            del notas[i]
            print('Nota eliminada\n')
            return
    print('Ingrese un id válido.\n')
    eliminar_nota()

if __name__ == '__main__':
    while True:
        menu()
        op = int(input('Ingrese una opción: '))
        if op == 1:
            agregar_nota()
        elif op == 2:
            mostrar_notas()
        elif op == 3:
            buscar_nota_id()
        elif op == 4:
            buscar_nota_palabra()
        elif op == 5:
            editar_nota()
        elif op == 6:
            eliminar_nota()
        elif op == 7:
            print('Hasta luego!!!')
            break
        else:
            print('Ingrese una opción valida')