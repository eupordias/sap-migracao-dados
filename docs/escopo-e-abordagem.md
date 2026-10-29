# Escopo e abordagem

## Cenário

A Distribuidora Aurora, empresa fictícia, substitui o ERP legado pelo S/4HANA. Antes de ligar o sistema novo, os dados mestres de clientes e materiais precisam ser limpos, convertidos e carregados.

## Dentro do escopo

- Objeto **cliente**: cadastro com nome, tipo de pessoa, documento, contato, endereço e situação.
- Objeto **material**: cadastro com descrição, unidade de medida, NCM, custo, grupo de mercadorias e status.

## Fora do escopo

- Dados transacionais (pedidos, notas e saldos).
- Carga real em um sistema SAP.
- Qualquer dado de pessoa, de aluno ou de cliente real.

## Origem e destino

| | Descrição |
|---|---|
| **Origem** | Dois arquivos CSV do sistema legado, gerados por `src/gerar_dados_ficticios.py` |
| **Intermediário** | Tabelas de staging no PostgreSQL, com todas as colunas em texto |
| **Destino** | Modelo em PostgreSQL que aproxima, de forma simplificada, o que um destino S/4HANA espera |

## Decisão de abordagem

Duas opções, a decidir na semana 2:

| Critério | Staging (carregar, validar e depois mover) | Carga direta |
|---|---|---|
| Rastreabilidade do que foi rejeitado | Alta: tudo fica registrado | Baixa |
| Facilidade de repetir a carga de ensaio | Alta | Média |
| Velocidade | Menor | Maior |
| Risco de sujar o destino | Baixo | Alto |
| Como desfazer | Truncar a staging e recarregar | Depende do destino |

**Decisão:** pendente. Será registrada aqui, com a data e o motivo, junto com a primeira entrada do plano de carga.

## Critérios de pronto

- Todos os tipos de defeito dos arquivos foram encontrados, registrados e tratados ou rejeitados com motivo.
- A reconciliação fecha: linhas de origem, linhas rejeitadas e linhas carregadas somam o total.
- A carga de ensaio é repetível: rodar duas vezes dá o mesmo resultado.
- Cada decisão de regra está documentada.
