#Elabore un programa en Python que permita registrar los productos de una
#Tienda de viveres. La información se debe almacenar en un archivo JSON. La
#Información de los productos es la siguiente (20ptos):
#id
#nombre
#valorUnitario
#stockmin
#stockmax
#valorUnitario
import json

def guardar_productos(product):
    with open('products.json', 'a') as file:
        json.dump(product, file, indent=4)
        file.write('\n')

def registrar_productos():
    
    id = input('Ingrese el Id del producto: ')
    nombre = input('Ingrese el nombre del producto: ')
    valor_unitario = float(input('Ingrese el valor unitario: '))
    stock_minimo = int(input('Ingrese el stock minimo: '))
    stock_maximo = int(input('Ingrese el stock maximo: '))

    producto = {
        'id': id,
        'nombre': nombre,
        'valorUnitario': valor_unitario,
        'stockminimo': stock_minimo,
        'stockmaximo': stock_maximo
    }

    guardar_productos(producto)

def main():
    while True:
        print("""
            *******************************************  
            * REGISTRO DE PRODUCTOS TIENDA DE VIVERES *
            *******************************************
          """)
        print('1. Registrar un nuevo Producto')
        print('2. Salir')

        option = int(input('Digite una Opcion: '))

        if option == 1:
            registrar_productos()
        elif option == 2:
            break
        else:
            print('Opcion Invalida.')

if __name__ == '__main__':
    main()