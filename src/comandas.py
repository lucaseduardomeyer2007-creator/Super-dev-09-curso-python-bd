from banco_dados import conectar
from clientes import listar_clientes
# pip install rich
#py -m pip install rich
from rich.console import Console
from rich.table import Table

def cadastrar(): 
    listar_clientes()

    id_cliente = int(input("Digite o id do cliente: "))


    conexao = conectar()
    cursor = conexao.cursor
    cursor.execute("INSERT INTO comandas (id_cliente) VALUES (%s)",
    (id_cliente,),
    )

    conexao.commit()


    comanda_id = cursor.lastrowid
    print(f"Comanda gerada: {comanda_id}")
    cursor.close()
    conexao.close()





def listar_comandas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""SELECT
    cod.id,
    cli.nome
FROM comandas AS cod
INNER JOIN clientes AS cli ON (cod.id_cliente = cli.id)""")
    comandas = cursor.fetchall()

    if len(comandas) == 0:
        print("Nenhuma comanda cadastrada")
        return

    tabela = Table("Id", "Cliente", show_header=True)
    tabela.title = ("[not italic]: vampire[/] Comandas [not italic]:vampire[/]"
    )

    for comanda in comandas:
        # id = comanda[0]
        # nome = comanda[1]
        id, cliente = comanda
        tabela.add_row(str(id), cliente)


    console = Console()
    console.print(tabela)

    cursor.close()
    conexao.close()


def excluir_comanda():
    pass


def alterar_comanda():
    pass


def menu_comanda():
    pass

