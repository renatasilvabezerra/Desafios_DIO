
# Código do professor
menu = '''

[s] saque
[d] deposito
[e] extrato
[q] sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao =='d':
        valor = float(input('\nInforme o valor do depósito: '))

        if valor > 0:
            saldo+=valor
            extrato += f'Deposito: R$ {valor:.2f}\n'

        else:
            print('\nOperação inválida!')

    elif opcao =='s':
        valor= float(input('\nInforme o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= limite_saques

        if excedeu_saldo:
            print('\nSaldo insuficiente!')

        elif excedeu_limite:
            print('\nExcedeu o limite!')
        
        elif excedeu_saque:
            print('\nExcedeu número de saques!')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('\nO valor informado é inválido!')

    elif opcao =='e':
        print('\n==========EXTRATO==========\n')
        print('Não há movimentação!' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('\n===========================')

    elif opcao == 'q':
       break

    else:
        print('\nOperação inválida!')
        print('\nSelecione novamente a operação desejada: ')
