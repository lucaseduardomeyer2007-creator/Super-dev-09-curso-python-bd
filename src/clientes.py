from datetime import date
from banco_dados import conectar
    

def cadastrar():
    print("\n---- CADASTRAR CLIENTE----")
    nome = input("Nome: ")
    documento = input("documento: ")
    telefone = int(input("Salário: ").replace (",", "."))
    
    
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO clientes (nome, documento, telefone) VALUES (%s, %s, %s)",
    (nome, documento, telefone),
)


    conexao.commit()
    print(f"\n[OK] Cliente cadastrado com id: {cursor.lastrowid}")

    cursor.close()
    conexao.close()




def listar_clientes():

    conexao = conectar()
  
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        id, nome, documento, telefone, 
    FROM clientes
    ORDER BY nome ASC
""")
    
    clientes = cursor.fetchall()

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado")
        return

    print("-"*76, end="")
    print (f"\n {'ID':<4} {'NOME':>25} {'DOCUMENTO':<20} {'TELEFONE':<12}")
    print("="*76)
    for cliente in clientes:
        id = cliente[0]
        nome = cliente[1]
        documento = cliente[2] if cliente[2] else "Sem documento"
        telefone = cliente[3] if cliente[3] else "Sem telefone"


        print(
            f"{id:<4} {nome:<25} {documento:<20} {telefone:<12}"
        )
    print("-"*76)


def excluir_clientes():
    listar_clientes()

    id_cliente = int(input("Id do cliente que você quer excluir: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE  FROM clientes WHERE id = %s", (id_cliente,))
    conexao.commit()

    cursor.close()
    conexao.close()
    # Rowcount é a quantidade de linhas que foram afetadas
    if cursor.rowcount == 0:
        print("Cliente não encontrado com este id")
    else:
        print("Registro apagado com sucesso")


def alterar_clientes():
    listar_clientes()

    id_cliente = int(input("ID do funcionário que você quer alterar: "))
    nome = input("Nome: ")
    documento = input("documento: ")
    telefone = int(input("Cliente: ").replace (",", "."))


    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE clientes SET nome = %s, documento = %s, telefone = %s WHERE id = %s",
        (nome, documento, telefone, id_cliente)
    )
    conexao.commit()

    cursor.close()
    conexao.close()

    if cursor.rowcount == 0:
        print("Cliente não encontrado com este id")
    else:
        print("Registro alterado com sucesso")



def menu_cliente():
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
            listar_clientes()
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            alterar_clientes()
        elif opcao == 4:
            excluir_clientes()
        elif opcao != 5:
            print("Opção inválida")
            print("\n")

        opcao = int(input(mensagem))