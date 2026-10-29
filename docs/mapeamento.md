# Mapeamento: legado para destino

Este documento liga cada coluna do arquivo legado a um destino provável e a uma ideia inicial de regra. Os destinos são **hipóteses de estudo**. Cada linha começa como "A confirmar" e passa a "Confirmado" quando eu checo a definição do campo (por exemplo, no dicionário de dados do SAP) ou valido com alguém da área. Esta tabela evolui ao longo do plano, e o histórico fica nos commits.

## Clientes (`clientes_legado.csv`)

| Coluna de origem | Destino provável | Ideia inicial de regra | Status |
|---|---|---|---|
| codigo_legado | Chave do parceiro de negócios (cliente) | Guardar também como código antigo, para rastrear | A confirmar |
| nome | Nome do parceiro | Remover espaços extras e padronizar caixa | A confirmar |
| tipo_pessoa | Categoria (pessoa física ou jurídica) | Padronizar para F ou J | A confirmar |
| documento | Dados fiscais do parceiro | Manter só dígitos; validar 11 (física) ou 14 (jurídica) | A confirmar |
| email | Comunicação do parceiro | Rejeitar se inválido; vazio é aceitável, a decidir | A confirmar |
| telefone | Comunicação do parceiro | Padronizar o formato; tratar código do país | A confirmar |
| cep, cidade, uf | Endereço do parceiro | Validar UF contra a lista oficial; CEP com 8 dígitos | A confirmar |
| data_cadastro | Data de criação | Converter os três formatos; rejeitar data futura | A confirmar |
| situacao | Status ou bloqueio | A definir | A confirmar |

## Materiais (`materiais_legado.csv`)

| Coluna de origem | Destino provável | Ideia inicial de regra | Status |
|---|---|---|---|
| codigo_legado | Dados básicos do material (número) | Definir se vira número novo ou fica como código antigo | A confirmar |
| descricao | Texto breve do material (limite de 40 caracteres) | Remover U+2028; truncar ou rejeitar acima de 40, a decidir | A confirmar |
| unidade | Dados básicos (unidade de medida básica) | Padronizar para UN, CX, KG, PC | A confirmar |
| ncm | Dados de centro | 8 dígitos; rejeitar vazio ou incompleto | A confirmar |
| preco_custo | Dados de avaliação | Trocar vírgula por ponto; rejeitar negativo | A confirmar |
| grupo_mercadoria | Dados básicos (grupo de mercadorias) | Validar contra a lista de grupos | A confirmar |
| ativo | Status de bloqueio ou eliminação | Padronizar para S ou N | A confirmar |

## Perguntas em aberto

1. O código legado vira o número novo ou fica apenas como referência?
2. Linha rejeitada volta para o dono do dado ou é corrigida na carga?
3. Campo opcional vazio apaga o valor existente no destino ou o preserva? A regra adotada neste projeto é preservar.
