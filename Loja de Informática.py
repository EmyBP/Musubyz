import os

produtos = []
NumProduto = []
vlrDoDia = 0
totalVendido = 0

def cadastrar():
    global produtos
    nome = input("Digite o nome do produto a ser cadastrado: ")
    preco = float(input("Digite o preço do produto: "))
    produto = {
        "Nome": nome,
        "Preço": preco
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso...")
    opcao = input("Deseja retornar ao menu (sim/não): ")    
    if opcao == "sim":
        os.system('cls')
        Menu()
    else:
        print("Finalizando sessão...")
    
def listar():
    print("====Lista de Produtos====")
    for i, produto  in enumerate(produtos, 1):
        print(f"{i} - Nome Produto:{produto["Nome"]}\n    Preço R$ {produto["Preço"]}")


def realizar_venda():
    global vlrDoDia
    global totalVendido
    print("====Lista de Produtos====")
    for Num, produto in enumerate(produtos, 1):
        print(f"{Num} - {produto["Nome"]}")
    escolha = int(input("Digite o número do produto que deseja comprar: "))
    produtos[escolha-1]
    vlrtotal = produto["Preço"]
    vlrDoDia += vlrtotal
    totalVendido += 1
    opcao = input("Deseja realizar outra compra? (sim/não)")
    if opcao == "sim":
        os.system('cls')
        realizar_venda()
    else:
        os.system('cls')
        Menu()



def relatorio():
    global vlrDoDia
    global totalVendido
    print("====Relatório do Dia====")
    print(f"Total em dinheiro arrecadado: R${vlrDoDia}")
    print(f"Produtos vendidos: {totalVendido}")
    if vlrDoDia > 1000:
        print("Ótimo trabalho hoje! Bateu a meta!")

        

def Menu():
    print("=== Loja de Informática ===")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Realizar Venda")
    print("4 - Relatório do Dia")
    print("5 - Sair")
    
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1 :
        cadastrar()
    elif opcao == 2 :
        listar()
    elif opcao == 3 :
        realizar_venda()
    elif opcao == 4 :
        relatorio()
    else:
        print("Finalizando sessão...")

Menu()