Este notebook implementa um sistema de simulação com múltiplos agentes descentralizados que processam dados multimodais (séries temporais financeiras, textos de notícias e sentimento de mídias sociais) para fazer recomendações financeiras (comprar/vender/manter). A implementação foca em demonstrar o fluxo de dados, análise e aspectos de explicabilidade de um sistema deste tipo.

## Fluxo de Trabalho

1. **Geração de Dados Sintéticos**: 
   - Séries temporais financeiras (preços de ações)
   - Manchetes de notícias (texto)
   - Pontuações de sentimento de mídias sociais

2. **Simulação de Agentes**: 
   - Implementação de múltiplos agentes com diferentes estratégias:
     - Agente Técnico: Baseado em médias móveis
     - Agente de Sentimento: Baseado em pontuações de sentimento
     - Agente Fundamental: Baseado em análise de notícias

3. **Processamento de Dados**: 
   - Cada agente processa os dados relevantes para sua estratégia específica

4. **Tomada de Decisão**: 
   - Cada agente toma uma decisão (comprar/vender/manter)

5. **Agregação (Simplificada)**: 
   - Combinação das decisões dos agentes (votação por maioria)

6. **Visualização**: 
   - Gráficos combinados mostrando preços, sentimento e decisões dos agentes
   - Gráficos de distribuição (histograma, KDE, violino) para preço e volume
   - Gráfico interativo de séries temporais utilizando Plotly
   - Mapa de calor de correlação entre preço, volume e sentimento

7. **Resumo Estatístico**: 
   - Estatísticas descritivas dos dados financeiros
   - Análise de bootstrap para intervalos de confiança

8. **Relatório de Insights com LLM**: 
   - Síntese das descobertas utilizando LLMs simulados:
     - Grok-base
     - Claude 3.7 Sonnet
     - Grok-Enhanced

## Dependências

```python
pip install pandas matplotlib seaborn plotly scipy
```

## Estrutura do Código

O notebook está organizado em várias seções principais:

### Funções Auxiliares
- Criação de diretórios
- Análise de texto com LLMs (simulada)

### Geração de Dados Sintéticos
- Dados financeiros (preços, volume)
- Dados de notícias (manchetes)
- Dados de sentimento

### Simulação de Agentes
- Implementação de diferentes estratégias de agentes
- Processamento de dados e tomada de decisão
- Agregação de decisões

### Visualização
- Gráficos combinados
- Gráficos de distribuição
- Gráficos interativos
- Mapas de calor de correlação

### Análise Estatística e Insights
- Estatísticas resumidas
- Análise de bootstrap
- Relatório de insights baseado em LLM

## Parâmetros Configuráveis

- `NUM_AGENTS`: Número de agentes simulados (padrão: 3)
- `NUM_DAYS`: Número de dias de dados simulados (padrão: 100) 
- `BOOTSTRAP_RESAMPLES`: Número de reamostragens para bootstrap (padrão: 500)
- `LINE_WIDTH`: Largura das linhas nos gráficos (padrão: 2.5)

## Resultados

O notebook gera os seguintes resultados no diretório `output_multimodal_agents/`:

- `combined_plot.png`: Gráfico combinado de preços, sentimentos e decisões dos agentes
- `price_distribution.png`: Gráficos de distribuição para preços
- `volume_distribution.png`: Gráficos de distribuição para volume
- `interactive_price_chart.html`: Gráfico interativo de preços
- `correlation_heatmap.png`: Mapa de calor de correlação
- `insights.txt`: Relatório de insights gerado pelos LLMs simulados

## Segurança e Notas de Implementação

- As chamadas de API para LLMs são simuladas. Em um ambiente de produção, você precisaria substituir as funções simuladas por chamadas reais para as APIs respectivas.
- Chaves de API são mostradas como placeholders; nunca armazene chaves de API diretamente no código em ambientes de produção.
- O notebook verifica se está sendo executado em um ambiente Google Colab para ajustar o caminho de saída adequadamente.

## Extensibilidade

Este notebook serve como um ponto de partida para implementações mais sofisticadas. Áreas para extensão incluem:

- Implementação de estratégias de agentes mais complexas
- Integração com fontes de dados reais (financeiras, notícias, mídias sociais)
- Utilização de chamadas reais para APIs de LLM
- Métodos de agregação mais avançados
- Validação de desempenho usando backtesting

## Palavras-chave

Dados Multimodais, Agentes Descentralizados, Tomada de Decisão Financeira, Simulação, Explicabilidade, LLMs, Visualização de Dados, Séries Temporais, Bootstrap

## Autor

Hélio Craveiro Pessoa Júnior
