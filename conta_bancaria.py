import time
# Criar uma classe de Conta Bancária: Crie uma classe chamada ContaBancaria que represente uma conta bancária simples, com atributos saldo e titular. Adicione métodos para depositar dinheiro na conta, sacar dinheiro e imprimir o saldo atual.

class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo_atual = saldo
        self.saldo_anterior = saldo
        self.titular = titular
        
    def Depositar(self, valor):
        if valor <= 0:
            print('Não é possível depositar valores negativos ou zero.')
            return
        self.saldo_atual += valor
        print('\nRealizando depósito...')
        time.sleep(2)
        print('\nValor depositado com sucesso.')
        time.sleep(1)
        print(f'\nValor depositado: R${valor:.2f}')
        
    def Sacar(self, valor):
        if valor > self.saldo_atual:
            print('Valor solicitado maior que o saldo atual.')
            print('Finalizando Operação...')
            time.sleep(5)
            return
        self.saldo_atual -= valor
        print('Realizando saque...')
        time.sleep(2)
        print('\nSaque realizado com sucesso.')
        time.sleep(1)
        print(f'\nValor retirado: R${valor:.2f}')
            
    def Exibir_Mensagem(self):
        print(f'Bem-vindo, {self.titular}!')
        
    
    def Exibir_extrato(self):
        print('\nExibindo extrato...')
        time.sleep(2)
        print(f'\nTitular: {self.titular}')
        print(f'Saldo anterior: R${self.saldo_anterior:.2f}')
        print(f'Saldo Atual: R${self.saldo_atual:.2f}')


      
