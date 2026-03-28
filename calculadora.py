# Calculadora con estructuras selectivas y repetivas
print("=== CALCULADORA ===")

opcion = 0
    

# estructura repetitiva WHILE
while opcion !=5:
    
    print("\nMENU DE OPCIONES")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion != 5:
        num1 = float(input("Digite el primer número: "))
        num2 = float(input("Digite el segundo número: "))
    
    # estrutura selectiva IF
    if opcion == 1:
        print("\nSUMA")
        
        resultado = num1 + num2
        print("Resultado: ", resultado)
        
        #estructura If-else
        
    elif opcion == 2:
        print("\nRESTA")
            
        resultado = num1 - num2
        print("Resultado: ", resultado)
            
    elif opcion == 3:
        print("\nMultiplicar")
                
        resultado = num1 * num2
        print("Resultado: ", resultado)
        
    elif opcion == 4: 
        print("\nDividir")
                    
        resultado = num1 / num2
        print("Resultado: ", resultado)
                    
    elif opcion == 5:
        print("Saliendo del programa.....")
                        
    else:
        print("Opción invalida")
                        
    print ("programa finalizado ")
                    
                
        
        
        
        
        
        
        
        
        
    