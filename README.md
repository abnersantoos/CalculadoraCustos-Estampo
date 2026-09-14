Markdown

# ✂️ Calculadora de Custo e Orçamento para Estampos Industriais

Projeto em Python focado no cálculo automatizado de custos de fabricação, usinagem por eletroerosão e tratamento térmico de estampos de corte, dobra e repuxo.

---

## 📌 Visão Geral do Projeto

Estampos progressivos e combinados exigem um levantamento rigoroso de custos focados em aços ferramenta de alta liga (como D2 e VND), processos de têmpera/revenimento e horas extensas de eletroerosão a fio (WEDM).

Este módulo calcula automaticamente:
* **Peso Bruto de Aço Misto:** Cubagem e pesagem considerando o Aço 1045 (placas/bases) e Aço D2/VND (punções e matrizes).
* **Carga Horária & Processos:** Custo por taxa/hora de Projeto CAD/CAM, Usinagem CNC, Eletroerosão a Fio (WEDM), Ajuste de Folgas de Corte e Try-out em Prensa.
* **Tratamento Térmico & Padronizados:** Custo de têmpera e revenimento, colunas de guia, buchas de esfera e molas prato.
* **Precificação Final:** Formatação do Custo Direto de Fabricação (CPV) e cálculo da margem de venda.

---

## 📐 Fórmulas Utilizadas

$$\text{Volume } (cm^3) = \frac{\text{Comprimento}}{10} \times \frac{\text{Largura}}{10} \times \frac{\text{Altura}}{10}$$

$$\text{Peso } (kg) = \frac{\text{Volume } (cm^3) \times 7,85}{1000}$$

$$\text{Valor Final} = (\text{Custo M.O.} + \text{Aço} + \text{Tratamento Térmico} + \text{Padronizados}) \times \left(1 + \frac{\text{Margem \%}}{100}\right)$$

---

## ⚙️ Como Executar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone o repositório e navegue até a pasta:
   ```bash
   git clone [https://github.com/SEU_USUARIO/orcameto-ferramentais.git](https://github.com/SEU_USUARIO/orcameto-ferramentais.git)
   cd orcameto-ferramentais
