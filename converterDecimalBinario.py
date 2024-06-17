numeroBinario = input("Digite um numero binário pra converter pra decimal: ")


def binario_para_decimal(binario):

    decimal = 0
    potencia = len(binario) - 1
    for digito in binario:
        decimal += int(digito) * (2 ** potencia)
        potencia -= 1
    
    return decimal

decimal = binario_para_decimal(numeroBinario)

print(f"O número binário {numeroBinario} em decimal é {decimal}")