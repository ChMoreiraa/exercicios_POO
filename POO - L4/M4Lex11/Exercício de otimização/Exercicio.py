import math

class RecipienteCilindrico:
    def __init__(self, volume, custo_base, custo_lateral, possui_tampa):
        if volume <= 0:
            raise ValueError("O volume deve ser maior que zero.")
        if custo_base < 0 or custo_lateral < 0:
            raise ValueError("Os custos da base e da lateral não podem ser negativos.")
        if possui_tampa not in [0, 1]:
            raise ValueError("Escolha inválida para tampa. Use 0 (não) ou 1 (sim).")

        self.volume = volume
        self.custo_base = custo_base
        self.custo_lateral = custo_lateral
        self.possui_tampa = bool(possui_tampa)
        self.raio = None
        self.altura = None
        self.area_base = None
        self.area_lateral = None
        self.custo_total = None

    def definir_dimensoes(self):
        """Calcula as dimensões do cilindro: raio e altura."""
        fator_divisao = 2 if self.possui_tampa else 1
        self.raio = (self.volume / (fator_divisao * math.pi)) ** (1 / 3)
        self.altura = self.volume / (math.pi * self.raio ** 2)

    def calcular_custos(self):
        """Determina os custos com base na área da base e lateral."""
        self.area_base = math.pi * self.raio ** 2
        self.area_lateral = 2 * math.pi * self.raio * self.altura
        custo_das_bases = self.area_base * self.custo_base * (2 if self.possui_tampa else 1)
        custo_lateral_total = self.area_lateral * self.custo_lateral
        self.custo_total = custo_das_bases + custo_lateral_total

    def exibir_resultados(self):
        """Mostra as dimensões e custos do recipiente."""
        print("\nDimensões do Recipiente:")
        print(f"Raio: {self.raio:.2f} cm")
        print(f"Altura: {self.altura:.2f} cm")
        print("\nCustos:")
        print(f"Custo da Base: R$ {(self.area_base * self.custo_base):.2f}")
        print(f"Custo da Lateral: R$ {(self.area_lateral * self.custo_lateral):.2f}")
        print(f"Custo Total: R$ {self.custo_total:.2f}")

def iniciar_programa():
    try:
        print("Bem-vindo ao otimizador de recipientes!")
        volume = float(input("Informe o volume do recipiente (em cm³): "))
        custo_base = float(input("Informe o custo do material da base (R$/cm²): "))
        custo_lateral = float(input("Informe o custo do material da lateral (R$/cm²): "))
        possui_tampa = int(input("O recipiente terá tampa? [0] Não | [1] Sim: "))

        recipiente = RecipienteCilindrico(volume, custo_base, custo_lateral, possui_tampa)
        recipiente.definir_dimensoes()
        recipiente.calcular_custos()
        recipiente.exibir_resultados()

    except ValueError as erro:
        print(f"Erro de entrada: {erro}")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")

if __name__ == "__main__":
    iniciar_programa()
