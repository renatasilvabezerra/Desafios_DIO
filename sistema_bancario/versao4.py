
# Aprendendo novas opções!

# Constantes: permitindo fácil modificação caso os limites mudem no futuro
LIMITE_SAQUES = 3
LIMITE_SAQUE = 500

# Variáveis globais
saldo = 0
numero_saques = 0
extrato = ""

# Função para exibir o menu
def exibir_menu():
    menu = '''
    [s] Saque
    [d] Depósito
    [e] Extrato
    [q] Sair

    => '''
    return input(menu)


# Separando as funções:

def realizar_deposito(saldo, extrato):
    valor = float(input("\nInforme o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("\nOperação inválida. Valor deve ser maior que zero.")
    
    return saldo, extrato


def realizar_saque(saldo, extrato, numero_saques):
    if numero_saques >= LIMITE_SAQUES:
        print("\nVocê já realizou o número máximo de saques diários.")
        return saldo, extrato, numero_saques

    valor = float(input("\nInforme o valor do saque: "))

    if valor <= 0:
        print("\nOperação inválida. Valor deve ser maior que zero.")
    elif valor > saldo:
        print("\nSaldo insuficiente para realizar o saque.")
    elif valor > LIMITE_SAQUE:
        print(f"\nValor excede o limite de R$ {LIMITE_SAQUE:.2f} para saques.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n==========EXTRATO==========")
    print("Não há movimentação." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("===========================\n")


# Função principal
def main():
    saldo = 0
    extrato = ""
    numero_saques = 0

    while True:
        opcao = exibir_menu()

        if opcao == 'd':
            saldo, extrato = realizar_deposito(saldo, extrato)

        elif opcao == 's':
            saldo, extrato, numero_saques = realizar_saque(saldo, extrato, numero_saques)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato)

        elif opcao == 'q':
            print("\nSaindo do sistema. Até logo!")
            break

        else:
            print("\nOperação inválida! Tente novamente.")

# Iniciando o programa
if __name__ == "__main__":
    main()


"""
Em Python, toda vez que um arquivo é executado, 
uma variável especial chamada __name__ é definida automaticamente.
Se o arquivo é executado diretamente (por exemplo, via linha de
comando ou terminal), __name__ será igual a "__main__".
Se o arquivo é importado como um módulo em outro script, __name__
será o nome do arquivo (sem o .py).
if __name__ == "__main__":
Este if verifica se o arquivo está sendo executado diretamente. Se sim,
o bloco de código dentro dele é executado.
Se o arquivo foi importado como um módulo em outro arquivo, o bloco
não será executado, o que é útil para evitar a execução acidental de
código quando se está apenas importando funções ou classes de um módulo.
Nesse caso, main() é uma função definida no código anterior, que
contém a lógica principal do programa.
Quando o arquivo é executado diretamente, essa linha chama a função
main() e inicia o programa.

"""