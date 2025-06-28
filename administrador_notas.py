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

def agregar_nota():
    global id
    titulo = input('Ingrese el título de la nota: ')
    contenido = input('Ingrese el contenido de la nota: ')
    notas.append({'id': id, 'titulo': titulo, 'contenido': contenido})
    id += 1
    print('Nueva nota creada con éxito')

def mostrar_notas():
    for nota in notas:
        print(f'''\t\tId: {nota.get('id')}
        Título: {nota.get('titulo')}
        Contenido: {nota.get('contenido')}''')

def buscar_nota_id():
    buscar = int(input('Ingrese el id de la nota: '))
    for nota in notas:
        if nota.get('id') == buscar:
            print(f'''\t\t\tId: {nota.get('id')}
            Título: {nota.get('titulo')}
            Contenido: {nota.get('contenido')}''')
            return nota
    print('Id no encontrado')

def buscar_nota_palabra():
    buscar = input('Ingrese la palabra que desea buscar: ')
    contador = 0
    for nota in notas:
        if buscar in nota.get('titulo') or buscar in nota.get('contenido'):
            print(f'''\t\t\tId: {nota.get('id')}
            Título: {nota.get('titulo')}
            Contenido: {nota.get('contenido')}''')
            contador += 1
    if contador > 0:
        return
    else:
        print('No se encontró la palabra clave')

def editar_nota():
    nota = None
    nota = buscar_nota_id()
    if nota != None:
        print('1. Si deseas modificar el título'
              '\n2. Si deseas modificar el contenido'
              '\n3. Si deseas modificar todo')
        op = int(input('Ingrese la opción a modificar: '))
        if op == 1:
            titulo = input('Ingrese el nuevo título: ')
            notas [nota.get('id')-1] = {'id': nota.get('id'), 'titulo': titulo, 'contenido': nota.get('contenido')}
            print('Título modificado')
            print(f'''\t\t\tId: {notas[nota.get('id')-1].get('id')}
            Título: {notas[nota.get('id')-1].get('titulo')}
            Contenido: {notas[nota.get('id')-1].get('contenido')}''')
        elif op == 2:
            contenido = input('Ingrese el nuevo contenido de la nota: ')
            notas[nota.get('id') - 1] = {'id': nota.get('id'), 'titulo': nota.get('titulo'), 'contenido': contenido}
            print('Contenido modificado')
            print(f'''\t\t\tId: {notas[nota.get('id') - 1].get('id')}
            Título: {notas[nota.get('id') - 1].get('titulo')}
            Contenido: {notas[nota.get('id') - 1].get('contenido')}''')
        elif op == 3:
            titulo = input('Ingrese el nuevo título: ')
            contenido = input('Ingrese el nuevo contenido de la nota: ')
            notas[nota.get('id') - 1] = {'id': nota.get('id'), 'titulo': titulo, 'contenido': contenido}
            print(f'''\t\t\tId: {notas[nota.get('id') - 1].get('id')}
            Título: {notas[nota.get('id') - 1].get('titulo')}
            Contenido: {notas[nota.get('id') - 1].get('contenido')}''')
        else:
            print('Ingresaste una opción inválida')
            editar_nota()

def eliminar_nota():
    mostrar_notas()
    eliminar = int(input('\nIngrese el id de la nota a eliminar: '))
    for nota in notas:
        if eliminar == nota.get('id'):
            notas.pop(eliminar - 1)
        else:
            print('Ingrese un id válido.')
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