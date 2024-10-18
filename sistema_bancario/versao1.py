# Operações: sacar, depositar e vizualizar saldo - versão 1

print('Digite 1 para saque, digite 2 para depósito, digite 3 para extrato')
operacao = int(input('Digite a operacao desejada: '))
saldo = 0

if operacao == 1:
    saque = int(input('Digite o valor que deseja sacar: '))
    saldo = saldo - saque
    print(f'Saldo após saque: {saldo}')

elif operacao == 2:
    deposito = int(input('Digite o valor que deseja depositar: '))
    saldo = saldo + deposito
    print(f'Saldo após depósito: {saldo}')

elif operacao == 3:
    print(f'Saldo atual: {saldo}')

else:
    print('Operação inválida.')


