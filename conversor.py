space = '\33[1;34m_\033[m' * 60

print(space)
print('\n\033[1;31m{:^60}\033[m'.format('CONVERSOR'))
print(space)

while True:
    print('''\n\033[1;37mDigite \033[1;32m1\033[37m para converter de \033[1;32mDECIMAIS\033[37m para \033[1;32mBINÁRIOS\033[37m;
Digite \033[1;32m2\033[37m para converter de \033[1;32mDECIMAIS\033[37m para \033[1;32mHEXADECIMAIS\033[37m;
Digite \033[1;32m3\033[37m para converter de \033[1;32mBINÁRIOS\033[37m para \033[1;32mDECIMAIS\033[37m;
Digite \033[1;32m4\033[37m para converter de \033[1;32mBINÁRIOS\033[37m para \033[1;32mHEXADECIMAIS\033[37m;''')
    print(space)

    escolha = input('\n\033[1;37mDigite o número desejado ou "sair" para fechar o programa:\033[1;31m ')
    if escolha.upper() == 'SAIR':
        break
    print(space)


########################################################################################################################

    def decimal_bina():
        print('\n\033[1;31m{:^60}\033[m'.format('DECIMAL >>\033[1;32m>> BINÁRIO'))

        while True:
            decimal = input('\n\033[1;37mDigite o valor a ser convertido ou "sair" para voltar:\033[1;31m ')
            if decimal.upper() == 'SAIR':
                print(space)
                break
            decimal = int(decimal)
            valor = []
            binario = []

            while True:
                valor.append(decimal%2)
                decimal //= 2
                if decimal//2 < 1:
                    valor.append(decimal % 2)
                    break

            for a in range(len(valor) - 1, -1, -1):
                binario.append(str(valor[a]))
            binario = ''.join(binario)

            print('\n\033[1;32m{:^60}\033[m'.format(binario))
            print(space)


########################################################################################################################

    def decimal_hexa():
        print('\n\033[1;31m{:^60}\033[m'.format('DECIMAL >>\033[1;32m>> HEXADECIMAL'))

        hexadecimal = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b',
                   12: 'c', 13: 'd', 14: 'e', 15: 'f'}

        while True:
            valor = []
            hexa = []

            decimal = input('\n\033[1;37mDigite o valor a ser convertido ou "sair" para voltar:\033[1;31m ')
            if decimal.upper() == 'SAIR':
                print(space)
                break
            decimal = int(decimal)

            while True:
                resto = decimal % 16
                valor.append(resto)
                decimal //= 16

                if decimal % 16 == decimal:
                    resto = decimal % 16
                    valor.append(resto)
                    decimal //= 16
                    break

            for a in range(len(valor) - 1, -1, -1):
                hexa.append(hexadecimal[valor[a]])

            print('\n\033[1;32m{:^60}\033[m'.format(''.join(hexa)))
            print(space)


########################################################################################################################

    def binario_decimal():
        print('\n\033[1;31m{:^60}\033[m'.format('BINÁRIO >>\033[1;32m>> DECIMAL'))

        while True:
            binario = input('\n\033[1;37mDigite o valor a ser convertido ou "sair" para voltar:\033[1;31m ')
            if binario.upper() == 'SAIR':
                print(space)
                break
            soma = 0

            n = -1
            for a in range(len(binario)):
                if binario[n] == '1':
                    soma += 2 ** a
                n -= 1

            print('\n\033[1;32m{:^60}\033[m'.format(soma))


########################################################################################################################

    def binario_hexa():
        print('\n\033[1;31m{:^60}\033[m'.format('BINÁRIO >>\033[1;32m>> HEXADECIMAL'))

        binario = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6',
                   '0111': '7', '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd',
                   '1110': 'e', '1111': 'f'}

        while True:
            hexadecimal = []
            bina = input('\n\033[1;37mDigite o valor a ser convertido ou "sair" para voltar:\033[1;31m ')
            if bina.upper() == 'SAIR':
                print(space)
                break

            while (len(bina) % 4) != 0:
                bina = '0' + bina

            if ((len(bina)) % 4) == 0:
                b = (len(bina)) / 4
                n = 0
                n1 = 4
                for a in range(int(b)):
                    hexadecimal.append(binario[bina[n:n1]])
                    n += 4
                    n1 += 4

            print('\033[1;32m{:^60}\033[m'.format(''.join(hexadecimal)))
            print(space)


########################################################################################################################

    if escolha == '1':
        decimal_bina()
    elif escolha == '2':
        decimal_hexa()
    elif escolha == '3':
        binario_decimal()
    elif escolha == '4':
        binario_hexa()
