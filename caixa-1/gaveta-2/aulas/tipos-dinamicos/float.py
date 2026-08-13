from decimal import Decimal

# 1. Teste com o Float padrão (que nasce como dízima)
soma_float = 0.1 + 0.2
print("Resultado com Float:  ", soma_float)

# 2. Teste com o Decimal (que guarda o número exato)
soma_decimal = Decimal('0.1') + Decimal('0.2')
print("Resultado com Decimal:", soma_decimal)


"""def precisao():
    if (0.1 + 0.2 == 0.3):
        return True
    else: 
        return False

print(precisao())"""

