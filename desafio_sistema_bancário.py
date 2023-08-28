saldo = 0
limite_saque = 500
limite_saques = 3
extrato = ''

while True:
    menu = f'''
******** MENU ********

    [1] DEPOSITAR
    [2] SACAR
    [3] EXTRATO
    [4] SAIR

SALDO: R$ {saldo:.2f}
======================
'''
    print(menu)
    opção = input()
    if opção == '1':
        depósito = float(input('VALOR DO DEPÓSITO: R$ '))
        if depósito < 0:
            print('VALOR INVÁLIDO!')
        else:
            saldo += depósito
            extrato += f'DEPÓSITO: R$ {depósito:.2f}\n'
    elif opção == '2':
        saque = float(input('VALOR DO SAQUE: R$ '))
        if saque > saldo:
            print('NÃO É POSSÍVEL REALIZAR O SAQUE, SALDO INSUFICIENTE.')
        elif saque < 0:
            print('VALOR INVÁLIDO!')
        elif saque > limite_saque:
            print('VALOR DO SAQUE SUPERIOR AO LIMITE DE R$ 500.00, ENTRE COM UM NOVO VALOR.')
        elif limite_saques == 0:
            print('VOCÊ ATINGIU O LIMITE DE SAQUES DIÁRIO!')
        else:
            saldo -= saque
            extrato += f'SAQUE:    R$ {saque:.2f}\n'
            limite_saques -= 1
    elif opção == '3':
        print('******** EXTRATO ********')
        print(extrato)
        print(f'SALDO:    R$ {saldo:.2f}')
        print('*************************')
    elif opção == '4':
        break
    else:
        print('OPÇÃO INVÁLIDA, POR FAVOR SELECIONE NOVAMENTE A OPERAÇÃO DESEJADA.')
