#voy a hacer una interfaz de un cajero automatico

#busca perfeccionar
import time as time

#valores
monto_a = 10000
monto_b = 20000
monto_c = 50000
monto_d = 100000
billetera = 0

#pantalla de inicio
print("""
#######################################
#                                     #
#   Bienvenido al cajero automatico   #
#         de Banco de Chile           #   
#                                     #                                  
#           ingrese su pin            #  
#######################################
""")

PIN = input("")
print("cargando...")
time.sleep(2)
#pantalla para elegir el monto-----------------
print("""
#####################################     
#   eliga su monto:                 #
#   a) = 10.000                     #
#   b) = 20.000                     #
#   c) = 50.000                     #
#   d) = 100.000                    #
#   e) = otro monto                 #
#####################################     
    """)
opcion = input("####> ").lower()

print("""
#####################################     
#                                   #
#       GENERANDO SU MONTO          #
#        espere porfavo...          #
#                                   #
#                                   #
#                                   #
#####################################    
         
      """)
time.sleep(5)
#logica
while opcion:
    if opcion == "a":
        print("...")
        billetera += monto_a
        
    elif opcion == "b":
        print("generando Monto...")
        billetera += monto_b
        
    elif opcion == "c":
        print("generando Monto...")
        billetera += monto_c
        
    elif opcion == "d":
        print("generando Monto...")
        billetera += monto_d
        

    elif opcion == "e":
        print("ingrese su monto deseado:")
        monto_personal = int(input("###$"))
        billetera += monto_personal
       
    
    else:
        print("ERROR")
        opcion = input("####> ").lower()

    print(f"Su billetera está en ${billetera}.")
    otra_operacion = input("Desea hacer otra operacion? [S/N]").upper()
    
    if otra_operacion == "N":
        break
    elif otra_operacion == "S":
        opcion = input("####> ").lower()
        
print("FIN")
print (f"billetera actual: ${billetera}")



