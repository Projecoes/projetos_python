''' Calculadora com while'''


'''Primeira parte conferindo se o primeiro numero o segundo e o operador estáo corretos'''
while True :
    num_1 = input('Digite o primeiro numero: ')
    operador = input('Informe o operador(+-/*): ')
    num_2 = input('Digite o segundo numero: ')


    numeros_validos = None
    
    try :
        num1_float = float(num_1)
        num2_float = float(num_2)
        
        numeros_validos = True

    except ValueError:
        print('Um dos numeros foi digitado errado')
        continue

    if numeros_validos is None :
        print('Um ou ambos os numeros são invalidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos :
        print("operador invalido.")
        continue
    if len(operador) > 1 :
        print("somente um operador é permitido.")

    #####
        '''Segunda parte os Calculos'''
    print('realizando os calculos')
    if operador == '+' :
        print(f'{num1_float} + {num2_float} = {num1_float + num2_float}')
    
    elif operador == '-' :
        print(f'{num1_float} - {num2_float} = ', num1_float - num2_float)

    elif operador == '*':
        print(f'{num1_float} * {num2_float} = ', num1_float * num2_float)

    elif operador == '/' :
        print(f'{num1_float} / {num2_float} = ', num1_float / num2_float)

    else :
        print('Nem deveria chegar aqui.')


    #####


    sair = input("quer sair? [S]im: ") \
        .lower().startswith('s') 
    if sair :
        break 