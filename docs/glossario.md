# Glossário

Glossário em construção, com termos que uso no projeto. Cresce junto com o plano e é revisado quando eu confirmo um conceito na prática.

| Termo | Significado |
|---|---|
| ERP | Sistema de gestão que integra áreas da empresa (compras, vendas, finanças, estoque) numa base de dados única |
| SAP S/4HANA | Geração atual do ERP da SAP, que roda sobre o banco de dados HANA |
| ECC | Geração anterior do ERP da SAP, que muitas empresas ainda estão migrando |
| Módulo | Área funcional do ERP, como MM (materiais), FI (finanças) e SD (vendas) |
| Dados mestres | Cadastros que mudam pouco e são usados por muitos processos, como cliente, fornecedor e material |
| Dados transacionais | Registros do dia a dia, como pedidos, notas e movimentos de estoque |
| Objeto de migração | Conjunto de dados que se migra junto, como cliente ou material |
| Sistema legado | Sistema antigo de onde os dados saem |
| Mapeamento | Ligação entre cada campo de origem e o campo de destino, com a regra de conversão |
| Saneamento | Limpeza dos dados antes da carga: duplicados, formatos e caracteres inválidos |
| Staging table | Tabela intermediária onde os dados são carregados, validados e corrigidos antes de ir ao destino |
| Mock load | Carga de ensaio em ambiente de teste, repetida até sair limpa |
| Reconciliação | Conferência de que o que saiu da origem bate com o que chegou ao destino, com contagens e totais de controle |
| Cutover | Plano e execução da virada para o sistema novo, com cronograma e plano de retorno |
| Estrutura | Linha com vários campos, cada um com nome |
| SE11 | Transação do SAP que mostra a definição de tabelas e estruturas e a descrição de cada campo |
| SE16N | Transação do SAP que mostra os dados de uma tabela |
