import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            conta = self.contas[self.index]
            return f"""\
                Agência:\t{conta.agencia}
                Número:\t{conta.numero}
                Titular:\t{conta.cliente.nome}
                Saldo:\t\tR$ {conta.saldo:.2f}
                """
        except IndexError:
                raise StopIteration
        finally:
            self.index += 1

class Cliente: 
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf                # Add CPF for unique identification
        self.nome = nome      
        self.data_nascimento = data_nascimento
        self.contas = []
        self.indice_conta = 0
        
    @property
    def contas(self):
        return self._contas

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
# class PessoaFisica(Cliente):
    
class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_transacao(Deposito(valor))

        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            self._historico.adicionar_transacao(Saque(valor))
        else:
            print("Saldo insuficiente ou valor inválido.")


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")


class Historico:
    def __init__(self): 
        self._transacoes = []

        @property
        def transacoes(self):
            return self._transacoes
        
        def adicionar_transacao(self, transacao):
            self._transacoes.append({
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            })
        
        def gerar_relatorio(self, tipo_transacao=None):
            for transacao in self._transacoes:
                if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                    yield transacao 

        def transacoes_do_dia(self):
            pass
class Transacao(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractclassmethod
    def registrar(self, conta):
        pass
    
class Saque(Transacao):
    def registrar(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(self)
        else:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")

class Deposito(Transacao):
    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(self)

def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado
    return envelope

def menu():
    menu = """\n
    ====================MENU================

        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nu]\tNovo Cliente
        [nc]\tNova Conta
        [lc]\tListar Contas
        [q]\tSair
        => """
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf,clientes):
    # for cliente in clientes:
    #     if cliente.cpf == cpf:
    #         return cliente
    # return None
    usuario_filtrados = [usuario for usuario in clientes if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None

def recuperar_conta_cliente(cliente):
    if len(cliente.contas) > 0:
        return cliente.contas[0]  # Assuming each client has one account
    return None

@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    valor = float(input("Informe o valor para depósito: "))
    conta.depositar(valor)
    print("\n@@@ Depósito realizado com sucesso! @@@")
    
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n===Depósito realizado com sucesso ===")
    else:
        print("\n@@@ Operação falhou! o valor informado é inválido. @@@")
        
    return saldo, extrato

@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    valor = float(input("Informe o valor para saque: "))
    conta.sacar(valor)

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): 
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    
    elif valor>0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente: 
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n==================EXTRATO================")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio():
        tem_transacao = True
        extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    if not tem_transacao:
        extrato = "Não foram realizadas movimentações"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("===============================================")

def exibir_extrato(saldo, /, *, extrato):
    print("======================= EXTRATO ========================")
    print("Não fora, realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("========================================================")

@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()

    # Create a new client and add to the list
    novo_cliente = Cliente(cpf, nome, data_nascimento)
    clientes.append(novo_cliente)  # Add the new client to the list

    print("\n@@@ Cliente cadastrado com sucesso! @@@")

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_cliente(cpf, clientes)

    if usuario:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf})
    print("=== Cliente criado com sucesso! ===")

@log_transacao
def criar_conta_de_um_cliente_para_o_banco(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ").strip()
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    # Create a new account for the client
    nova_conta = ContaCorrente(numero_conta, cliente)
    cliente["contas"].append(nova_conta)  # Add the account to the client
    contas.append(nova_conta)  # Also add the account to the global accounts list

    print("\n@@@ Conta criada com sucesso! @@@")

def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_cliente(cpf, clientes)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": usuario}

    print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")

@log_transacao
def listar_contas(contas):
    for conta in ContasIterador(contas):
        print("=" *100)
        print(textwrap.dedent(str(conta)))

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    clientes = []
    contas = []

    while True:
        opcao = menu()
        
        if opcao == 'd':
            valor = float (input("Informe o valor do deposito:"))
            saldo, extrato = depositar(saldo, valor, extrato)
            # depositar(clientes)
        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
            # sacar(clientes)
        elif opcao == 'e':
            exibir_extrato(saldo, extrato= extrato)
            # exibir_extrato(clientes)
        elif opcao == 'nu':
            criar_cliente(clientes)
        elif opcao == 'nc':
            numero_conta = len(contas) +1
            # criar_conta_de_um_cliente_para_o_banco(numero_conta, clientes, contas)
            conta = criar_conta(AGENCIA, numero_conta, clientes)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break

        else:
            print("Operação inválida!")
            
            
main()