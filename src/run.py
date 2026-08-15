from funcionarios import menu_funcionario


def __main():
    mensagem = """MENU:
    1 - Funcionarios
    10 - Sair
    Digite a opção desejada:"""


    opcao = int(input(mensagem))

    while opcao != 10:
        if opcao == 1:
            menu_funcionario()
        elif opcao != 10:
            print("Opção inválida")
        print("\n")
        
        opcao = int(input(mensagem))



if __name__ == "__main__":
    __main()


