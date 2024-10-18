
LIMITE_SAQUES = 3
LIMITE_SAQUE = 500

saldo = 0
numero_saques = 0

# Função pra montar as operações:
def realizar_operacao():
    global saldo, numero_saques  
    
    while True:  # Loop para continuar perguntando até o usuário decidir parar
        print('\nEscolha uma operação: ')
        print('1: Saque')
        print('2: Depósito')
        print('3: Saldo')
        print('0: Sair')

        operacao = input('Digite a operação desejada: ')

        if operacao == '1':  # Saque
            saque = int(input('Digite o valor que deseja sacar: '))
            excedeu_saldo = saque > saldo
            excedeu_limite = saque > LIMITE_SAQUE
            excedeu_saque = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print('\nSaldo insuficiente!')

            elif excedeu_limite:
                print(f'\nO valor de saque excede o limite de R${LIMITE_SAQUE:.2f}!')

            elif excedeu_saque:
                print(f'\nVocê já atingiu o número máximo de {LIMITE_SAQUES} saques diários!')

            elif saque > 0:  # Só realiza o saque se passar por todas as verificações
                saldo -= saque
                numero_saques += 1
                print(f'Saque de R${saque} realizado. Seu saldo atual é: R${saldo}.')
            else:
                print('O valor de saque deve ser maior que zero.')

        elif operacao == '2':  # Depósito
            deposito = int(input('Digite o valor que deseja depositar: '))
            if deposito > 0:
                saldo += deposito
                print(f'Depósito de R${deposito} realizado. Seu saldo atual é: R${saldo}.')
            else:
                print('O valor de depósito deve ser maior que zero.')

        elif operacao == '3':  # Saldo
            print(f'Seu saldo atual é: R${saldo}.')

        elif operacao == '0':  # Sair
            print('Obrigado por utilizar nosso serviço!')
            break

        else:
            print('Operação inválida. Tente novamente.')


realizar_operacao()
