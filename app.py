import os
Restaurantes = [{nome,categoria,ativo}] 
def nome_app():
    print("Disk Larica\n")
def voltar():
    input("\n tecle entre para voltar ao menu principal")
    os.system("cls")
    main()
def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair\n")
def finalizar_app():
    os.system("cls")
    print("Encerrando programa")
def invalida():
    print("opção invalida!")
    voltar()
def cadastrar():
    os.system("cls")
    print("Cadastro de novos restaurantes\n")
    nome_cadastrado = input("Digite o nome do restaurante a ser cadastrado: \n")
    categoria_cadastrada = input("digite a categoria do restaurante: \n")
    dados_do_restaurante = {nome: nome_cadastrado, categoria: categoria_cadastrada, ativo: False}
    Restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_cadastrado} foi cadastrado!\n")
    voltar()
def listar():
    os.system('cls')
    print("Lista de restaurantes cadastrados")
    for restaurante in Restaurantes:
        print(f'- {restaurante}\n')
    voltar()

def estado_restaurante():
    print("Trocar estado do restaurante")
    nome_restaurante = input("Ensira o nome do restaurante: ")
    restaurante_encontrado = False
    for restaurante in Restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
    if not restaurante_encontrado:
        print("o restaurante não foi encontrado")
    voltar()

def mostrar_escolha():
    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            estado_restaurante()
        elif opcao == 4:
            finalizar_app()
        else:
            invalida()
    except:
        invalida()


def main():
    os.system("cls")
    nome_app()
    exibir_opcoes()
    mostrar_escolha()

main()