from conta_bancaria import ContaBancaria
import time

print('Sistema Bancário.')
titular_da_conta = input('Digite o nome do titular da conta: ')
saldo_inicial = float(input('Digite o saldo inicial da conta: '))

conta = ContaBancaria(saldo_inicial, titular_da_conta)
conta.Exibir_Mensagem()

while True:
    print('Selecione a operação que deseja realizar:')
    print('1 - Realizar Depósito')
    print('2 - Realizar Saque')
    print('3 - Exibir Extrato')
    print('0 - Sair')

    opcao = int(input('Digite uma opção: '))
    
    if opcao == 1:
        valor_deposito = float(input('Digite o valor que deseja depositar: '))
        conta.Depositar(valor_deposito)
    elif opcao == 2:
        valor_saque = float(input('Digite o valor que deseja sacar: '))
        conta.Sacar(valor_saque)
    elif opcao == 3:
        conta.Exibir_extrato()
    elif opcao == 0:
        print('Até mais...')
        break
    else:
        print('Opção inválida. Tente novamente.')
    
    time.sleep(3)

