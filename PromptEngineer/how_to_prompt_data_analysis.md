# Como Criar um Prompt para Analisar Dados de Equipamentos (CSV)

Este guia explica como formular um prompt para analisar o arquivo `equipment_list.csv`, que contém detalhes de equipamentos como nome, marca, categoria, preço, moeda e país.

---

## 📁 Etapa 1: Entenda a Estrutura do CSV

O arquivo CSV contém as seguintes colunas:

- `Equipment Name` (Nome do Equipamento)
- `Brand` (Marca)
- `Category` (Categoria)
- `Price` (Preço)
- `Currency` (Moeda)
- `Country` (País)

Exemplo de linha:

Laptop, Dell, Electronics, 1200.00, USD, USA

---

## 🧠 Etapa 2: Defina Seus Objetivos de Análise

Antes de criar um prompt, decida o que você quer descobrir. Exemplos de objetivos:

- Preço médio por categoria ou marca.
- Equipamento mais caro por país.
- Disponibilidade de equipamentos por país.
- Comparação de preços entre moedas diferentes.

---

## 📝 Etapa 3: Exemplos de Prompts

Aqui estão alguns exemplos de prompts para analisar os dados:

### 🔍 Estatísticas Descritivas Básicas

Analise o preço médio dos equipamentos por categoria a partir do arquivo CSV enviado.
Liste todos os equipamentos que custam mais de 1000 em USD.
Mostre o número de tipos diferentes de equipamentos disponíveis por país.
Compare o preço médio dos equipamentos entre os EUA e a Alemanha com base no arquivo CSV.


## Insights
📈 Resumo da Análise:
1. Preço Médio por Categoria:

Electronics: $587,50 USD (maior preço médio)
Accessories: $46,67 USD
Furniture: $175,00 USD
Networking: $90,00 USD

2. Equipamentos Acima de $1000:
Apenas 1 equipamento atende a este critério:

Laptop Dell - $1.200 USD (categoria Electronics, fabricado nos EUA)

3. Distribuição por País:

EUA: 4 equipamentos (40% do total)
Coreia do Sul, Suíça, China, Japão, Suécia: 1 equipamento cada (10% cada)

4. Comparação EUA vs Alemanha:

EUA: Preço médio de $416,25 USD (4 equipamentos)
Alemanha: Não há equipamentos da Alemanha nos dados fornecidos

🔍 Insights Principais:

A categoria Electronics tem o maior preço médio, puxado principalmente pelo laptop
Os EUA lideram em quantidade de equipamentos representados
Apenas um produto ultrapassa a marca de $1000
A distribuição geográfica é bem diversificada, representando 6 países diferentes.
A visualização interativa em html [analysis.html] mostra todos esses dados com gráficos e métricas detalhadas para uma análise mais visual e completa.
(Página publicada de visualização)[https://claude.ai/public/artifacts/cae49e0f-063a-45e1-9091-f09937c4611b]