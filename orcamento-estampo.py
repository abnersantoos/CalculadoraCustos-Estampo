from dataclasses import dataclass

@dataclass
class ParametrosEstampo:
    # Dimensões gerais da ferramenta em mm
    comprimento: float  # mm
    largura: float      # mm
    altura: float       # mm
    
    # Insumos e Tratamentos
    custo_componentes_padrao: float  # Colunas, buchas, molas
    custo_tratamento_termico: float  # Têmpera/Revenimento do D2/VND
    preco_kg_aco_misto: float = 35.0  # Média ponderada 1045 + D2/VND
    
    # Horas Estimadas
    horas_cad_cam: float = 50.0
    horas_cnc: float = 90.0
    horas_convencional: float = 60.0
    horas_eletroerosao_fio: float = 50.0
    horas_montagem_ajuste: float = 80.0
    horas_tryout_prensa: float = 20.0
    
    # Taxas Horárias (R$/h)
    taxa_cad_cam: float = 120.0
    taxa_cnc: float = 160.0
    taxa_convencional: float = 90.0
    taxa_eletroerosao_fio: float = 140.0
    taxa_montagem_ajuste: float = 110.0
    taxa_tryout_prensa: float = 220.0
    
    margem_impostos: float = 30.0

class CalculadoraEstampo:
    DENSIDADE_ACO = 7.85

    def __init__(self, params: ParametrosEstampo):
        self.p = params

    def calcular_peso(self) -> float:
        vol_cm3 = (self.p.comprimento / 10) * (self.p.largura / 10) * (self.p.altura / 10)
        return (vol_cm3 * self.DENSIDADE_ACO) / 1000

    def calcular_orcamento(self):
        peso = self.calcular_peso()
        custo_aco = peso * self.p.preco_kg_aco_misto
        
        custo_mo = (
            (self.p.horas_cad_cam * self.p.taxa_cad_cam) +
            (self.p.horas_cnc * self.p.taxa_cnc) +
            (self.p.horas_convencional * self.p.taxa_convencional) +
            (self.p.horas_eletroerosao_fio * self.p.taxa_eletroerosao_fio) +
            (self.p.horas_montagem_ajuste * self.p.taxa_montagem_ajuste) +
            (self.p.horas_tryout_prensa * self.p.taxa_tryout_prensa)
        )
        
        custo_insumos = custo_aco + self.p.custo_tratamento_termico + self.p.custo_componentes_padrao
        custo_total_fabricacao = custo_mo + custo_insumos
        preco_final = custo_total_fabricacao * (1 + (self.p.margem_impostos / 100))
        
        print("=" * 60)
        print("         ORÇAMENTO DE FERRAMENTAL DE ESTAMPO")
        print("=" * 60)
        print(f"Dimensões: {self.p.comprimento}x{self.p.largura}x{self.p.altura} mm | Peso: {peso:.2f} kg")
        print(f"Custo Mão de Obra e Processos: R$ {custo_mo:,.2f}")
        print(f"Custo Aço + Tratamento Térmico + Padronizados: R$ {custo_insumos:,.2f}")
        print(f"Custo Direto: R$ {custo_total_fabricacao:,.2f}")
        print(f"VALOR FINAL ESTIMADO: R$ {preco_final:,.2f}")
        print("=" * 60)

if __name__ == "__main__":
    estampo_automotivo = ParametrosEstampo(
        comprimento=800,
        largura=500,
        altura=350,
        custo_componentes_padrao=8500.0,
        custo_tratamento_termico=6500.0
    )
    calc = CalculadoraEstampo(estampo_automotivo)
    calc.calcular_orcamento()
