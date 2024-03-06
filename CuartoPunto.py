#Elabore un programa que permite registrar la información de los empleados
#De una compañía y le permita calcular el valor a pagar por concepto de nomina a
#Cada empleado. La información que se tiene por cada empleado es la siguiente (55ptos):
#id
#nombre
#cargo (Almacenista, Jefe IT, Administrador, Mensajero, Genrente)
#salario
#Para calcular el valor a pagar por cada empleado se debe tener en cuenta la
#Siguiente información:
#diasTrabajados
#horasExtras
#valorDia
#descuentoxCafeteria
#cuotaPrestamo
#El valor de la hora extra es de 5500 pesos. La información de la colilla de pago
#Se debe almacenar en caso de una solicitud de revisión por parte de algún
#Empleado que no este conforme con el pago la información que debe guardar
#La colilla de pago es la siguiente:
#mesPagado
#fechaPago(dd/mm/yyyy)
#sueldoBase
#valorTotalHrasExtras
#cuotaPrestamo
#descuentoxCafeteria
#totalAPagar
#La información se debe guardar en un archivo JSON.
#El gerente desea obtener la siguiente información:
#1. Total pagado por concepto de nomina
#2. Consultar la colilla de pago de un determinado empleado.

import json,os
from datetime import datetime

HORA_EXTRA = 5500

def calcular_valor_pagar(empleado):
    horas_extra = empleado['horasExtras']
    valor_dia = empleado['valorDia']
    descuento_cafeteria = empleado['descuentoxCafeteria']
    cuota_prestamo = empleado['cuotaPrestamo']

    valor_horas_extra = horas_extra * HORA_EXTRA
    sueldo_base = empleado['salario'] * empleado['diasTrabajados']
    total_horas_extra = empleado['horasExtras'] * HORA_EXTRA
    total_a_pagar = sueldo_base + total_horas_extra - descuento_cafeteria - cuota_prestamo

    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    colilla_pago = {
        'mesPagado': fecha_actual,
        'fechaPago': fecha_actual,
        'sueldoBase': sueldo_base,
        'valorTotalHrasExtras': total_horas_extra,
        'cuotaPrestamo': cuota_prestamo,
        'descuentoxCafeteria': descuento_cafeteria,
        'totalAPagar': total_a_pagar
    }

    return colilla_pago

def main():
    empleados = []

    try:
        with open('empleados.json', 'r') as file:
            empleados = json.load(file)
    except FileNotFoundError:
        pass

    while True:
        print("""
              ************
              *   Menú   *
              ************
              """)
        print("1. Agregar empleado")
        print("2. Calcular valor a pagar por empleado")
        print("3. Consultar colilla de pago de un empleado")
        print("4. Mostrar total pagado por concepto de nómina")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            os.system("cls")
            print("""
              *****************************
              *   Registro de Empleados   *
              *****************************
              """)
            empleado = {}
            empleado['id'] = input("Ingrese elID del empleado: ")
            empleado['nombre'] = input("Ingrese el Nombre del empleado: ")
            empleado['cargo'] = input("Ingrese el Cargo del empleado: ")
            empleado['salario'] = float(input("Ingrese el Salario del empleado: $"))
            empleado['diasTrabajados'] = int(input("Ingrese los Días trabajados: "))
            empleado['horasExtras'] = int(input("Ingrese las Horas extras: "))
            empleado['valorDia'] = float(input("Ingrese el Valor del día: $"))
            empleado['descuentoxCafeteria'] = float(input("Ingrese el Descuento por cafetería: &"))
            empleado['cuotaPrestamo'] = float(input("Ingrese la Cuota de préstamo: $"))
            empleados.append(empleado)
            print("EMPLEADO AGREGADO.")
            os.system ("pause")
            os.system ("cls")
        elif opcion == '2':
            print("""
              ********************
              *   Valor a pagar  *
              ********************
              """)
            for empleado in empleados:
                os.system("cls")
                colillapago = calcular_valor_pagar(empleado)
                print(f"Colilla de pago para {empleado['nombre']}:")
                print(colillapago)
                os.system("pause")
                os.system("cls")
        elif opcion == '3':
            os.system("cls")
            print("""
              *********************************
              *   Consultar Colilla de Pago   *
              *********************************
              """)
            id_empleado = input("Ingrese el ID del empleado: ")
            encontrado = False
            for empleado in empleados:
                if empleado['id'] == id_empleado:
                    encontrado = True
                    colilla_pago = calcular_valor_pagar(empleado)
                    print(f"Colilla de pago para {empleado['nombre']}:")
                    print(colilla_pago)
            if not encontrado:
                print("Empleado no encontrado.")
            os.system("pause")
            os.system("cls")
        elif opcion == '4':
            os.system("cls")
            print("""
              *******************************
              *   Total Pagado por Nomina   *
              *******************************
              """)
            total_nomina = sum(calcular_valor_pagar(empleado)['totalAPagar'] for empleado in empleados)
            print(f"Total pagado por concepto de nómina: {total_nomina} pesos.")
            os.system("pause")
            os.system("cls")
        elif opcion == '5':
            os.system("cls")
            print ("Guardando Datos...")
            with open('empleados.json', 'w') as file:
                json.dump(empleados, file, indent=4)
            print("Gracias por usar el sistema.")
            os.system("pause")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()