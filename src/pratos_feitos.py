from banco_dados import conectar

def cadastrar():
    print("\n---- CADASTRAR Pratos Feitos----")
    nome = input("Nome do prato: ")
    custo = float(input("Custo: ").replace (",", "."))    
    
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO pratos_feitos (nome, custo) VALUES (%s, %s)",
    (nome, custo),
)
    
    conexao.commit()
    print(f"\n[OK] prato feito com id: {cursor.lastrowid}")

    cursor.close()
    conexao.close()


def listar_pratos_feitos():
    # Abrir a conexão com o banco de dados 
    conexao = conectar()
    # Criar o cursor para poder executar algum comando no banco de dados
    cursor = conexao.cursor()
    #Definir o comando de consulta dos funcionários
    cursor.execute("""
    SELECT
        id, nome, custo
    FROM pratos_feitos
    ORDER BY nome ASC
""")
    # fetchall() retorna todas as linhas encontradas naquela consulta
    # cada linha contém uma tupla com onde cada posição é a coluna do select
    pratos_feitos = cursor.fetchall()

    if len(pratos_feitos) == 0:
        print("Nenhum prato cadastrado")
        return

    print("-"*76, end="")
    print (f"\n {'ID':<4} {'NOME':>25} {'CUSTO':<20}")
    print("="*76)
    for prato in pratos_feitos:
        id = prato[0]
        nome = prato[1]
        custo = prato[2]

        print(
            f"{id:<4} {nome:<25} {custo:<20}"
        )
    print("-"*76)


def excluir_pratos_feitos():
    listar_pratos_feitos()

    id_pratos_feitos = int(input("Id do funcionario que você quer excluir: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE  FROM pratos_feitos WHERE id = %s", (id_pratos_feitos,))
    conexao.commit()

    cursor.close()
    conexao.close()
    # Rowcount é a quantidade de linhas que foram afetadas
    if cursor.rowcount == 0:
        print("Prato não encontrado com este id")
    else:
        print("Registro apagado com sucesso")


def alterar_pratos_feitos():
    listar_pratos_feitos()

    id_pratos_feitos = int(input("ID do funcionário que você quer alterar: "))
    nome = input("Nome: ")
    
    custo = float(input("Prato: ").replace (",", "."))
    

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE pratos_feitos SET nome = %s, custo = %s WHERE id = %s",
        (nome, custo, id_pratos_feitos)
    )
    conexao.commit()

    cursor.close()
    conexao.close()

    if cursor.rowcount == 0:
        print("Funcionário não encontrado com este id")
    else:
        print("Registro alterado com sucesso")



def menu_prato_feito():
    mensagem = """MENU:
    1 - Listar
    2 - Cadastrar
    3 - Editar
    4 - Apagar
    5 - Voltar
    Digite a opção desejada:"""

    opcao = int(input(mensagem))

    while opcao != 5:
        if opcao == 1:
            listar_pratos_feitos()
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            alterar_pratos_feitos()
        elif opcao == 4:
            excluir_pratos_feitos()
        elif opcao != 5:
            print("Opção inválida")
            print("\n")

        opcao = int(input(mensagem))