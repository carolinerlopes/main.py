# main.py
# 💧 Sistema de Controle de Níveis de Água

Este projeto consiste em um sistema de monitoramento de reservatório desenvolvido em Python. Ele simula a leitura de sensores de um reservatório e exibe alertas coloridos no terminal para indicar o nível de criticidade da água, auxiliando na gestão de recursos hídricos.

Este projeto foi desenvolvido como atividade acadêmica para o curso de **Análise e Desenvolvimento de Sistemas (ADS) na FATEC**.

## 🎯 Objetivos do Projeto
- Aplicar o uso de **bibliotecas externas** (`colorama`).
- Estruturar o código de forma modular utilizando **funções**.
- Manipular coleções de dados através de **listas e dicionários**.
- Simular um ambiente de monitoramento real com dados pré-definidos.

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Biblioteca Colorama**: Utilizada para destacar as situações de risco com cores específicas (Vermelho, Amarelo, Verde, Ciano e Azul).

## 📊 Níveis de Monitoramento
O sistema processa cinco níveis de alerta:
1. **Nível 1 (Muito Baixo/Crítico):** Exibido em Vermelho.
2. **Nível 2 (Baixo):** Exibido em Amarelo.
3. **Nível 3 (Médio):** Exibido em Verde.
4. **Nível 4 (Alto):** Exibido em Ciano.
5. **Nível 5 (Muito Alto/Alerta):** Exibido em Azul.

## 📋 Como Executar

1. **Instale a dependência necessária:**
   ```bash
   pip install colorama
