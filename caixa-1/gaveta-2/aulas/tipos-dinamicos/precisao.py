import time

# 1. Teste com número pequeno (cabe em 32-bit)
x = 12345678
inicio_pequeno = time.perf_counter()
for _ in range(10_000_000):
    _ = x + 1
fim_pequeno = time.perf_counter()
tempo_pequeno = fim_pequeno - inicio_pequeno

# 2. Teste com número gigante (precisão arbitrária - ~30.000 dígitos)
num_gigante = 2 ** 100000
inicio_gigante = time.perf_counter()
for _ in range(10_000):  # Menos repetições pois exige muito processamento
    _ = num_gigante + 1
fim_gigante = time.perf_counter()
# Multiplicamos por 1000 para projetar o tempo equivalente a 10 milhões de vezes
tempo_gigante_projetado = (fim_gigante - inicio_gigante) * 1000

print(f"Tempo com número pequeno: {tempo_pequeno:.4f} segundos")
print(f"Tempo com número gigante (projetado): {tempo_gigante_projetado:.4f} segundos")
