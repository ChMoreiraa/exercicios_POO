import math
from scipy.optimize import minimize # type: ignore

# Função para calcular o custo total
def calcular_custo_total(r, volume, custo_base_unitario, custo_lateral_unitario, tampa):
    pi = math.pi
    h = volume / (pi * r**2)  # Calcula a altura a partir do volume e do raio
    area_base = pi * r**2
    area_lateral = 2 * pi * r * h
    
    custo_base = area_base * custo_base_unitario
    custo_lateral = area_lateral * custo_lateral_unitario
    
    custo_total = custo_base + custo_lateral
    
    if tampa == 's':
        area_tampa = pi * r**2  # Área da tampa (mesma área da base)
        custo_tampa = area_tampa * custo_base_unitario
        custo_total += custo_tampa
    
    return custo_total

# Função para calcular as dimensões ótimas
def calcular_dimensoes_ótimas(volume, tampa, custo_base_unitario, custo_lateral_unitario):
    # Usando otimização para encontrar o raio que minimiza o custo total
    res = minimize(calcular_custo_total, x0=[1], args=(volume, custo_base_unitario, custo_lateral_unitario, tampa), bounds=[(0.1, None)])
    
    raio_otimo = res.x[0]
    altura_otima = volume / (math.pi * raio_otimo**2)  # Calcula a altura a partir do volume e raio
    
    return round(raio_otimo, 2), round(altura_otima, 2)

# Função para exibir os resultados
def exibir_resultados(volume, tampa, custo_base_unitario, custo_lateral_unitario):
    raio_otimo, altura_otima = calcular_dimensoes_ótimas(volume, tampa, custo_base_unitario, custo_lateral_unitario)

    print("\nDimensões ótimas (cm):")
    print(f"Raio: {raio_otimo} cm")
    print(f"Altura: {altura_otima} cm")

    # Cálculo de custos
    if tampa == 's':
        area_base = math.pi * raio_otimo**2
        area_lateral = 2 * math.pi * raio_otimo * altura_otima
        area_tampa = math.pi * raio_otimo**2
        custo_base = area_base * custo_base_unitario
        custo_lateral = area_lateral * custo_lateral_unitario
        custo_tampa = area_tampa * custo_base_unitario  # Mesmo custo da base para a tampa
        custo_total = custo_base + custo_lateral + custo_tampa
        print("\nCustos:")
        print(f"Custo Base: R$ {round(custo_base, 2)}")
        print(f"Custo Lateral: R$ {round(custo_lateral, 2)}")
        print(f"Custo Tampa: R$ {round(custo_tampa, 2)}")
        print(f"Custo Total: R$ {round(custo_total, 2)}")
    else:
        area_base = math.pi * raio_otimo**2
        area_lateral = 2 * math.pi * raio_otimo * altura_otima
        custo_base = area_base * custo_base_unitario
        custo_lateral = area_lateral * custo_lateral_unitario
        custo_total = custo_base + custo_lateral
        print("\nCustos:")
        print(f"Custo Base: R$ {round(custo_base, 2)}")
        print(f"Custo Lateral: R$ {round(custo_lateral, 2)}")
        print(f"Custo Total: R$ {round(custo_total, 2)}")

# Função principal para coletar os dados do usuário
def main():
    volume = float(input("Digite o volume do recipiente (em cm³ ou ml): "))
    tampa = input("O recipiente terá tampa? (s/n): ").strip().lower()
    custo_base_unitario = float(input("Digite o custo do material da base (R$ por cm²): "))
    custo_lateral_unitario = float(input("Digite o custo do material da lateral (R$ por cm²): "))

    # Exibir os resultados com base nas entradas
    exibir_resultados(volume, tampa, custo_base_unitario, custo_lateral_unitario)

# Chama a função principal para executar o programa
if __name__ == "__main__":
    main()
