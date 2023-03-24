from random import randint
def menu():
    print('-' * 50)
    print('0- Sair\n1- Cadastrar funcionário\n2- Cadastrar cliente\n3- Armazenar camisas nacionais\n4- Armazenar camisas internacionais\n5- Comprar camisa\n6- Remover camisa do estoque\n7- Calcular a taxa de importação\n8- Ver estoque\n9- Listar clientes\n10- Imprimir histórico de compras')
    print('-' * 50)
    print()


def verificar_cpf(dicionario, chave):
    if chave in dicionario.keys():
        return True
    else:
        return False

def gerar_id():
    x = randint(1000, 9999)
    return x

def verificar_id(dicionario, id):
    if id in dicionario.keys():
        return True
    else:
        return False


