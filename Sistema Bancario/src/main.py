
from datetime import datetime
from classes.conta import Conta
from classes.correntista import Correntista
from classes.transacao import Transacao
from classes.ux import UX

menu = '''
    [c] Novo cliente
    [n] Nova conta
    [l] Listar contas
    [t] Trocar conta atual
    [d] Depositar
    [e] Extrato
    [s] Saque
    [q] Sair
'''
ux_format = UX()
transacoes = []
correntistas = []
_conta_corrente = Conta


def _calcular_saldo():

    return sum(transacao.valor if transacao.tipo == 'deposito' else -transacao.valor 
               for transacao in transacoes)


def _depositar():

    _imprimir_cabecalho('deposito')

    _valor_deposito = float(input('Informe o valor que deseja depositar: ').replace(',','.'))
    if _valor_deposito > 0:
        transacoes.append(Transacao(_conta_corrente.numero_conta, 
                                    'deposito', _valor_deposito, 
                                    datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
        print('Deposito efetuado...')
    else:
        print('Valor inválido...')        


def _extrato():

    print('\n')
    print(ux_format.preencher_linha('='))
    print(ux_format.centralizar_texto(
        f'Extrato Bancário -- Número da conta: {_conta_corrente.numero_conta}      Correntista: {correntistas[0].nome}'))
    print(ux_format.preencher_linha('='))
    
    for transacao in sorted(transacoes, key=lambda x: x.data, reverse=True):
        print(f'{transacao.data}            {transacao.tipo}         R$ {transacao.valor}')
    
    print(ux_format.preencher_linha('='))
    print(f'Saldo R$ {_calcular_saldo()}')
    print(ux_format.preencher_linha('='))


def _sacar():

    _imprimir_cabecalho('saque')

    _limite = 1000
    _saldo = _calcular_saldo()
    _valor_saque = float(input('Informe o valor que deseja sacar: ').replace(',','.'))

    if _valor_saque <= 0:
        print('Valor inválido!')   
    elif _valor_saque> _limite:
        print('Valor solicitado maior que o limite diário!')
    elif _saldo <= 0 or _saldo < _valor_saque:
        print('Saldo insuficiente!')
    else:
        transacoes.append(Transacao(_conta_corrente.numero_conta, 
                                    'saque', _valor_saque, 
                                    datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
        print('Saque efetuado. Aguarde a contagem das notas...')


def _novo_cliente(nome, cpf):
    
    try:
        correntistas.append(Correntista(nome, cpf))
    except ValueError:
        return False
    else:
        return True
    

def _nova_conta(correntista):

    _nova_conta = Conta(correntista.cpf)
    correntista.conta.append(_nova_conta)
    return True


def _pegar_correntista(cpf):
    return next(correntista for correntista in correntistas if correntista.cpf == cpf)


def _pegar_conta(numero_conta):
    global _conta_corrente
    _conta_corrente_selecionada = Conta

    for correntista in correntistas:
        for conta in correntista.conta:
            if int(conta.numero_conta) == int(numero_conta):
                _conta_corrente = conta
                break

    if _conta_corrente.numero_conta != numero_conta:
        print('Não foi possível carregar os dados da conta')


def _listar_contas():
     for cliente in correntistas:
        print(f'Cliente {cliente.nome}')
        for conta in cliente.conta:
            if _conta_corrente.numero_conta == conta.numero_conta: 
                _conta = f'{conta.numero_conta}  << selecionada'
            else:
                _conta = conta.numero_conta

            print(f'Conta {_conta}')


def _verificar_conta_corrente():
    if _conta_corrente is None:
        print('Escolha uma conta (numero) para as operações:')
        _listar_contas()
        return False
    else:
        return True
    

def _imprimir_cabecalho(titulo):
    print()    
    print(ux_format.preencher_linha('='))
    print(titulo.upper())
    print(ux_format.preencher_linha('='))
    print()


def _validarCPF(cpf):
    if len(cpf) < 8 or len(cpf) > 11:
        return False
    else:
        return True

while True:
    
    print(menu)

    if _conta_corrente.numero_conta is not None:
        print(f'Conta corrente selecionada : {_conta_corrente.numero_conta}' )
        print(' ')

    opcao = input('Digite a opcao desejada: ')

    if opcao == 'c':
        
        _imprimir_cabecalho('Novo cliente')

        _nome = input('Digite o nome do cliente: ')

        if(_nome!=''):
            _cpf = input('Digite o cpf do cliente (apenas numeros): ')

            if(_cpf!='' and _nome!=''):

                if not _validarCPF(_cpf):
                    print('CPF inválido!')
                else:
                    if len(correntistas) > 0:
                        _cliente_cadastrado = next(cliente for cliente in correntistas if cliente.cpf == _cpf 
                                      or cliente.nome == _nome)
                    else:
                        _cliente_cadastrado = False    

                if(_cliente_cadastrado):
                    if(_cliente_cadastrado.cpf == _cpf):
                        print('Cliente já existe! Informe um novo cpf!')
                else:
                    try:
                        if(_novo_cliente(nome=_nome, cpf=_cpf)):
                            
                            print(f'Novo Cliente {_nome} criado com sucesso!')
                            
                            _criar_conta=''

                            while(_criar_conta.lower() != 's' and _criar_conta.lower()!='n'):

                                _criar_conta = input('Deseja criar uma conta para esse cliente novo? (s/n)')

                                if(_criar_conta.lower()=='s'):
                                    try:
                                        _nova_conta(correntista=correntistas[-1])
                                    except ValueError:
                                        print('Ocorreu um problema ao criar a conta, contate o seu gerente.')
                                        break
                                    else:
                                        print('Conta criada com sucesso')    
                                        break    
                                elif(_criar_conta=='n'):
                                    break       
                    except ValueError:
                        print('Ocorreu um erro ao salvar o novo cliente')       
        else:
            print('Nome inválido!')

    elif opcao=='n':
        
        if len(correntistas) == 0:
            print('Para criar uma conta nova é necessário cadastrar um cliente primeiro')
        else:    
            _imprimir_cabecalho('nova conta')

            _cpf = input('Digite o cpf do cliente (apenas números):')

            if _validarCPF(_cpf) is False:
                print('Cpf inválido')
            else:
                correntista = _pegar_correntista(cpf=_cpf)
                if(correntista):
                    _nova_conta(correntista=correntista)
                    _conta_corrente = correntista.conta[-1]
                else:
                    print('Cliente não encontrado! Utilize a opção Novo Cliente para criar um novo com esse cpf')
    
    elif opcao == 'd':
        if _verificar_conta_corrente():
            _depositar()
    
    elif opcao == 'e':
        if _verificar_conta_corrente():
            _extrato()
    
    elif opcao == 's':
        if _verificar_conta_corrente():
            _sacar()
    
    elif opcao == 'q':
        break
    
    elif opcao=='l':

        _imprimir_cabecalho('correntistas / contas cadastradas')

        if len(correntistas) == 0:
            print('Nenhum correntista cadastrato. Utilize a opção [c] para cadastrar um novo cliente')
        else:
           _listar_contas()
    
    elif opcao=='t':

        _imprimir_cabecalho('Troca de conta de operacoes')
        _listar_contas()
        _conta_selecionada_troca = input('Digite o numero da conta:')
        if _conta_selecionada_troca!='':
            _pegar_conta(_conta_selecionada_troca)
        else:
            print('Numero de conta invalido.')

    else:
        print('Opção inválida')