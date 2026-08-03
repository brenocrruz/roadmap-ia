temp_geral = 0

for i in range (3):
    temp = float(input(f"Digite a {i+1}ª temperatura: "))
    temp_geral = temp_geral + temp

print(f"\nTemperatura média: {temp_geral/3}°C")