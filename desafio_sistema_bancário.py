menu = '''
******** MENU ********
    [1] DEPOSITAR
    [2] SACAR
    [3] EXTRATO
    [4] SAIR
'''
saldo = 0
limite_saque = 500
limite_saque_diário = 1500
limite_saques = 3
extrato = ''
extrato_depósitos = 0
extrato_saques = 0

while True:
    print(menu)
    opção = input()
    if opção == '1':
        depósito = float(input('VALOR DO DEPÓSITO: R$ '))
        if depósito < 0:
            print('VALOR INVÁLIDO!')
        else:
            saldo += depósito
            extrato_depósitos += depósito
    elif opção == '2':
        saque = float(input('VALOR DO SAQUE: R$ '))
        if saque > saldo:
            print('NÃO É POSSÍVEL REALIZAR O SAQUE, SALDO INSUFICIENTE.')
        elif saque > limite_saque_diário:
            print('VALOR DO SAQUE SUPERIOR AO LIMITE DIÁRIO!')
        elif saque > limite_saque:
            print('VALOR DO SAQUE SUPERIOR AO LIMITE DE R$ 500.00, ENTRE COM UM NOVO VALOR.')
        elif limite_saques == 0:
            print('VOCÊ ATINGIU O LIMITE DE SAQUES DIÁRIO!')
        else:
            saldo -= saque
            extrato_saques += saque
            limite_saque_diário -= saque
            limite_saques -= 1
    elif opção == '3':
        print('******** EXTRATO ********')
        print(f'DEPÓSITOS: R$ {extrato_depósitos:,.2f}')
        print(f'SAQUES: R$ {extrato_saques:,.2f}')
        print(f'SALDO: R$ {saldo:,.2f}')
    elif opção == '4':
        break
    else:
        print('OPÇÃO INVÁLIDA, POR FAVOR SELECIONE NOVAMENTE A OPERAÇÃO DESEJADA.')