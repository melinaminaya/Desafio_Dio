menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 10000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Informe o valor do depósito: "))

        if valor >0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        print("Saque")
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite: 
            print("Operação falhou! O valor de saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "e":
        print("\n************ EXTRATO **************")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("************************************")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

# def main():
#     def analise_vendas(vendas):
#         total_vendas = sum(vendas)
#         media_vendas = total_vendas / len(vendas)
    
    
#         return f"{total_vendas}, {media_vendas:.2f}"

#     def obter_entrada_vendas():
#         # Solicita a entrada do usuário em uma única linha
#         entrada = input()
#         numeros_como_strings = entrada.split(',')
#         vendas = list(map(int, numeros_como_strings))
    
#         return vendas

#     vendas = obter_entrada_vendas()
#     print(analise_vendas(vendas))

# main()

# def produto_mais_vendido(produtos):
#     contagem = {}
    
#     for produto in produtos:
#         if produto in contagem:
#             contagem[produto] += 1
#         else:
#             contagem[produto] = 1
    
#     max_produto = None
#     max_count = 0
    
#     for produto, count in contagem.items():
#         # TODO: Encontre o produto com a maior contagem:
#         if(count > max_count):
#           max_count = count
#           max_produto = produto
    
#     return max_produto

# def obter_entrada_produtos():
#     # Solicita a entrada do usuário em uma única linha
#     entrada = input()
#     # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
#     lista_produtos = [produto.strip() for produto in entrada.split(",")]
#     produtos = lista_produtos
    
#     return produtos

# produtos = obter_entrada_produtos()
# print(produto_mais_vendido(produtos))