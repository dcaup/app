Este notebook implementa uma análise abrangente de intervenções para ansiedade utilizando técnicas avançadas para detecção de interações causais. O código adapta a estrutura de Mixture of Experts (MoE) para incorporar métodos de descoberta causal na presença de interações causais, com o objetivo de identificar potenciais interações entre diferentes fatores causais (grupo de intervenção, nível de ansiedade pré-intervenção e outras covariáveis) e sua influência nos níveis de ansiedade pós-intervenção.

## Funcionalidades Principais

O notebook segue um fluxo de trabalho estruturado:

1. **Carregamento e Validação de Dados**: Carrega dados sintéticos de intervenção para ansiedade, valida sua estrutura, conteúdo e tipos de dados. O conjunto de dados foi expandido para incluir covariáveis adicionais como idade, gênero, horas de terapia e uso de medicação.

2. **Pré-processamento de Dados**: Realiza codificação one-hot de colunas categóricas (grupo, gênero, medicação) e escalamento de características numéricas. Renomeia colunas para compatibilidade com statsmodels.

3. **Descoberta de Interações Causais**: Implementa a descoberta de interações causais utilizando regressão OLS (Ordinary Least Squares) do statsmodels com termos de interação. Analisa interações entre grupo, ansiedade pré-intervenção e outras covariáveis.

4. **Análise de Valores SHAP**: Quantifica a importância das características, considerando interações causais.

5. **Visualização de Dados**: Gera gráficos KDE, Violin, Coordenadas Paralelas e Hipergrafos, destacando efeitos de interação.

6. **Resumo Estatístico**: Realiza análise bootstrap e gera estatísticas resumidas, incluindo insights sobre interações causais.

7. **Relatório de Insights com LLMs**: Sintetiza resultados utilizando modelos Grok, Claude e Grok-Enhanced, enfatizando a análise de interações causais, validando as saídas dos LLMs e tratando possíveis erros de API.

## Requisitos

O notebook requer as seguintes bibliotecas Python:
- pandas
- matplotlib
- seaborn
- networkx
- shap
- scikit-learn
- numpy
- plotly
- scipy
- statsmodels

## Detalhes Técnicos

### Estrutura de Dados
O conjunto de dados inclui:
- `participant_id`: Identificador único para cada participante
- `group`: Grupo de intervenção (Grupo A, Grupo B, Controle)
- `anxiety_pre`: Nível de ansiedade pré-intervenção (escala 0-10)
- `anxiety_post`: Nível de ansiedade pós-intervenção (escala 0-10)
- `age`: Idade do participante
- `gender`: Gênero (Masculino, Feminino, Outro)
- `therapy_hours`: Horas de terapia
- `medication`: Uso de medicação (Sim, Não)

### Descoberta de Interações Causais
O notebook implementa um modelo de regressão OLS com termos de interação para identificar combinações de fatores que influenciam o resultado da intervenção. As interações são modeladas como:
- Interações entre grupo e ansiedade pré-intervenção
- Interações entre grupo e idade
- Interações entre grupo e horas de terapia
- Interações entre ansiedade pré-intervenção e idade
- Interações entre ansiedade pré-intervenção e horas de terapia
- Interações entre idade e horas de terapia

### Visualizações
O notebook gera várias visualizações para explorar os padrões de interação:
- **Gráficos KDE**: Visualizam a distribuição dos níveis de ansiedade pré e pós-intervenção
- **Gráficos Violin**: Mostram a distribuição da ansiedade pós-intervenção por grupo
- **Gráficos de Coordenadas Paralelas**: Ilustram as trajetórias dos participantes de ansiedade pré para pós-intervenção, estratificadas por grupo
- **Hipergrafos**: Representam as relações entre participantes baseadas em padrões de ansiedade

### Análise SHAP
A análise SHAP quantifica a contribuição de cada característica e interação para as previsões do modelo, fornecendo insights sobre como diferentes combinações de fatores afetam o resultado da intervenção.

### Análise Bootstrap
O notebook implementa análise bootstrap para calcular intervalos de confiança para estatísticas chave, oferecendo estimativas robustas da eficácia da intervenção.

### Integração com LLMs
Embora o notebook inclua funções para integração com modelos de linguagem (LLMs), as funções atuais são placeholders que retornam análises predefinidas. Em uma implementação completa, estas funções seriam substituídas por chamadas de API reais para Grok, Claude 3.7 Sonnet e Grok-Enhanced.

## Uso

O notebook está configurado para funcionar tanto no ambiente Google Colab quanto localmente. No Colab, os resultados são salvos em uma pasta na sua Google Drive. Localmente, são salvos em uma pasta no diretório atual.

## Recursos Adicionais

O código inclui tratamento robusto de erros e validação de dados para garantir a confiabilidade dos resultados. A validação verifica:
- Presença de colunas necessárias
- Tipos de dados corretos
- Ausência de IDs de participantes duplicados
- Rótulos de grupo válidos
- Valores de ansiedade dentro da faixa esperada (0-10)
- Faixas etárias válidas (18-100)
- Horas de terapia válidas (0-50)
- Rótulos de gênero válidos
- Rótulos de medicação válidos

## Conclusão

Este notebook representa uma abordagem avançada para analisar intervenções para ansiedade, com foco específico na detecção de interações causais. Ao identificar como diferentes fatores interagem para influenciar os resultados da intervenção, o código permite uma compreensão mais nuançada e personalizada da eficácia da intervenção em diferentes subgrupos.

## Autor

Hélio Craveiro Pessoa Júnior
