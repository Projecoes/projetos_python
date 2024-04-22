""" Calculadora com while """
while True:
    num1 = input('Digite um número: ')
    operador = input('Digite o operador (+-/*): ')
    num2 = input('Digite outro número: ')
    

    numeros_validos = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True

    except ValueError :
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ###

    print('realizando os calculos...')
    if operador == '+' :
        resultado = num1_float + num2_float
        print(resultado)
    
    elif operador == '-' :
        resultado = num1_float - num2_float
        print(resultado)

    elif operador == '*':
        resultado = num1_float * num2_float
        print(resultado)

    elif operador == '/' :
        if  num2_float == 0 :
         print('tudo que é dividido por zero é zero')
         continue
        resultado = num1_float / num2_float
        print(resultado)
    
    
    ####

    sair = input("quer sair? [S]im: ") \
        .lower().startswith('s') 
    if sair :
        break 