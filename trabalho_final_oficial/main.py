from datetime import datetime
from funcoes import *
from loja import Loja
from funcionario import Funcionario
from cliente import Cliente
from nacionais import Nacionais
from internacionais import Internacionais
from camisas import Camisas
from taxa import Taxacao

Taxacao.register(Internacionais)

loja = Loja()

#Alguns dados já estão cadastrados na loja para facilitar a interação e tornar o uso do sistema mais rápido e simples.
data_nascimento1 = datetime.strptime(('19 09 2002'), ('%d %m %Y')).date()
data_nascimento2 = datetime.strptime(('14 01 2003'), ('%d %m %Y')).date()
loja.funcionarios['48376995960'] = Funcionario('Eduardo', '48376995960', data_nascimento1, 2500)
loja.clientes['10491464509'] = Cliente('Carlos', '10491464509', data_nascimento2, 'dev')
loja.camisas_inter[2222] = Internacionais(2222, 'PSG', 250, 100, 'M', 'França')
loja.camisas_nacionais[1111] = Nacionais(1111, 'Santos', 289, 200, 'G', 'Brasil')

while True:
    menu()
    try:
        op = int(input('Escolha umas das opções: '))
        assert 0 <= op <= 10
        if op == 0:
            print('<<<')
            break
        elif op == 1:
            print(f'{10 * "-"} CADASTRAR FUNCIONÁRIO {10 * "-"}')
            nome = str(input('Nome: '))
            while True:
                cpf = str(input('CPF do funcionário (11 digitos): '))
                if len(cpf) == 11:
                    break
                else:
                    print('CPF inválido, tente novamente! ')
            data_nascimento = datetime.strptime(input('Data de nascimento - dia, mes, ano (separados por espaço): '), ('%d %m %Y')).date()
            salario = float(input('Salário: '))
            if verificar_cpf(loja.funcionarios, cpf):
                print('O funcionário já está cadastrado! ')
            else:
                loja.funcionarios[cpf] = Funcionario(nome, cpf, data_nascimento, salario)
                print(f'Funcionário {nome} cadastrado com sucesso! ')
        elif op == 2:
            print(f'{10 * "-"} CADASTRAR CLIENTE {10 * "-"}')
            nome = str(input('Nome: '))
            while True:
                cpf = str(input('CPF do cliente (11 digitos): '))
                if len(cpf) == 11:
                    break
                else:
                    print('CPF inválido, tente novamente! ')
            data_nascimento = datetime.strptime(input('Data de nascimento - dia, mes, ano (separados por espaço): '), ('%d %m %Y')).date()
            profissao = str(input('Profissão: '))
            if verificar_cpf(loja.clientes, cpf):
                print(f'O cliente {nome} já está cadastrado! ')
            else:
                loja.clientes[cpf] = Cliente(nome, cpf, data_nascimento, profissao)
                print(f'Cliente {nome} cadastrado com sucesso! ')
        elif op == 3:
            print(f'{5 * "-"} ARMAZENAR CAMISAS NACIONAIS {5 * "-"}')
            cpf = str(input('CPF do funcionário: '))
            if verificar_cpf(loja.funcionarios, cpf):
                id = gerar_id()
                time = str(input('Time: '))
                pais = 'Brasil'
                preco = float(input('Preço: '))
                quantidade = int(input('Quantidade: '))
                tamanho = str(input('Tamanho: '))
                if verificar_id(loja.camisas_nacionais, id):
                    print('Esse id já existe, tente novamente! ')
                else:
                    loja.camisas_nacionais[id] = Nacionais(id, time, preco, quantidade, tamanho, pais)
                    print(f'Camisa nacional do {time} armazenada com sucesso! ')
            else:
                print('Ops, opção restrita aos funcionários da loja! ')
        elif op == 4:
            print(f'{2 * "-"} ARMAZENAR CAMISAS INTERNACIONAIS {2 * "-"}')
            cpf = str(input('CPF do funcionário: '))
            if verificar_cpf(loja.funcionarios, cpf):
                id = gerar_id()
                time = str(input('Time: '))
                pais = str(input('País: '))
                preco = float(input('Preço: '))
                quantidade = int(input('Quantidade: '))
                tamanho = str(input('Tamanho: '))
                if verificar_id(loja.camisas_inter, id):
                    print('Esse id já existe, tente novamente! ')
                else:
                    loja.camisas_inter[id] = Internacionais(id, time, preco, quantidade, tamanho, pais)
                    print(f'Camisa internacional do {time} armazenada com sucesso! ')
            else:
                print('Ops, opção restrita aos funcionários da loja! ')
        elif op == 5:
            print(f'{10 * "-"} COMPRAR CAMISA {10 * "-"}')
            for chave in loja.clientes.keys():
                loja.clientes[chave].listar_clientes2()
            cpf = str(input('CPF do cliente: '))
            if verificar_cpf(loja.clientes, cpf):
                print('1- Comprar camisa de time nacional\n2- Comprar camisa de time internacional')
                try:
                    op = int(input('Qual a sua escolha de compra: '))
                    assert 1 <= op <= 2
                    if op == 1:
                        for chave in loja.camisas_nacionais.keys():
                            loja.camisas_nacionais[chave].listar_camisas()
                        id = int(input('Id da camisa que você deseja comprar: '))
                        if verificar_id(loja.camisas_nacionais, id):
                            quant = int(input('Quantas camisas vai comprar: '))
                            x, mensagem = loja.camisas_nacionais[id].comprar(quant, cpf)
                            if x == True:
                                print(mensagem)
                            elif x == False:
                                print(mensagem)
                        else:
                            print('Camisa de time não existe na loja! ')
                    elif op == 2:
                        for chave in loja.camisas_inter.keys():
                            loja.camisas_inter[chave].listar_camisas()
                        id = int(input('Id da camisa que você deseja comprar: '))
                        if verificar_id(loja.camisas_inter, id):
                            quant = int(input('Quantas camisas vai comprar: '))
                            x, mensagem = loja.camisas_inter[id].comprar(quant, cpf)
                            if x == True:
                                print(mensagem)
                            elif x == False:
                                print(mensagem)
                except ValueError:
                    print('Valor inválido, tente novamente! ')
                except AssertionError:
                    print('Opcão inválida, tente novamente! ')
            else:
                print('Ops, percebemos que você não está cadastrado na loja,\ncadastre-se para efetuar suas compras :( ')
        elif op == 6:
            print(f'{8 * "-"} REMOVER CAMISA DO ESTOQUE {8 * "-"}')
            cpf = str(input('CPF do funcionário: '))
            if verificar_cpf(loja.funcionarios, cpf):
                print('1- Remover camisa de time nacional\n2- Remover camisa de time internacional')
                try:
                    op = int(input('Escolha uma das opções acima: '))
                    assert 1 <= op <= 2
                    if op == 1:
                        for chave in loja.camisas_nacionais.keys():
                            loja.camisas_nacionais[chave].listar_camisas()
                        id = int(input('Digite o id da camisa você deseja remover do estoque: '))
                        if verificar_id(loja.camisas_nacionais, id):
                            loja.camisas_nacionais.pop(id)
                            print('A camisa que você escolheu, foi removida do estoque com sucesso! ')
                        else:
                            print('O id que você digitou não existe, tente novamente :( ')
                    elif op == 2:
                        for chave in loja.camisas_inter.keys():
                            loja.camisas_inter[chave].listar_camisas()
                        id = int(input('Digite o id da camisa você deseja remover do estoque: '))
                        if verificar_id(loja.camisas_inter, id):
                            loja.camisas_inter.pop(id)
                            print('A camisa que você escolheu, foi removida do estoque com sucesso! ')
                        else:
                            print('O id que você digitou não existe, tente novamente :( ')
                except ValueError:
                    print('Valor inválido, tente novamente! ')
                except AssertionError:
                    print('Opcão inválida, tente novamente! ')
            else:
                print('Ops, opção restrita aos funcionários da loja! ')
        elif op == 7:
            print(f'{6 * "-"} CALCULAR TAXA DE IMPORTAÇÃO {6 * "-"}')
            #Essa taxa de importação é referente as camisas internacionais armazenadas na loja e somente funcionários podem ter acesso a essa área.
            cpf = str(input('CPF do funcionário: '))
            if verificar_cpf(loja.funcionarios, cpf):
                loja.calcular_taxacao()
                loja.imprimir_taxacao()
            else:
                print('Ops, opção restrita aos funcionários da loja! ')
        elif op == 8:
            #Opção vai listar todos os produtos armazenados na loja, nacionais e internacionais.
            cpf = str(input('CPF do funcionário: '))
            if verificar_cpf(loja.funcionarios, cpf):
                for chave in loja.camisas_nacionais.keys():
                    loja.camisas_nacionais[chave].listar_camisas()
                for chave in loja.camisas_inter.keys():
                    loja.camisas_inter[chave].listar_camisas()
            else:
                print('Ops, opção restrita aos funcionários da loja! ')
        elif op == 9:
            #Opção vai listar todos os clientes cadastrados na loja, com a devida autenticação do funcionário
            cpf = str(input('CPF do funcionário: '))
            if verificar_cpf(loja.funcionarios, cpf):
                for chave in loja.clientes.keys():
                    loja.clientes[chave].listar_clientes()
            else:
                print('Ops, opção restrita aos funcionários da loja! ')
        elif op == 10:
            cpf = str(input('CPF do funcionário: '))
            if verificar_cpf(loja.funcionarios, cpf):
                print('1- Ver histórico de compras de camisas nacionais\n2- Ver histórico de compras de camisas internacionais\n')
                try:
                    op = int(input('Opção: '))
                    assert 1 <= op <= 2
                    if op == 1:
                        for chave in loja.camisas_nacionais.keys():
                            loja.camisas_nacionais[chave].listar_camisas()
                        id = int(input('ID da camisa para ver histórico de suas compras: '))
                        loja.camisas_nacionais[id].historico_compras.imprime()
                    elif op == 2:
                        for chave in loja.camisas_inter.keys():
                            loja.camisas_inter[chave].listar_camisas()
                        id = int(input('ID da camisa para ver histórico de suas compras: '))
                        loja.camisas_inter[id].historico_compras.imprime()
                except ValueError:
                    print('Valor inválido, tente novamente! ')
                except AssertionError:
                    print('Opcão inválida, tente novamente! ')
            else:
                print('Ops, opção restrita aos funcionários da loja! ')
    except ValueError:
        print('Valor inválido, tente novamente! ')
    except AssertionError:
            print('Opcão inválida, tente novamente! ')