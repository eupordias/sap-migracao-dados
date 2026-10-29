# Migração de dados SAP: projeto simulado

> Projeto de estudo com dados 100% fictícios. Ele mostra como eu aprendo e como eu trabalho. Não é, e não pretende ser, experiência em projeto SAP real.

## Em 30 segundos

| | |
|---|---|
| **Quem** | Éverson Dias, desenvolvedor full stack e encarregado de dados (DPO) na SETEQ/AL, em Maceió |
| **O quê** | Simulação de uma migração de dados mestres (clientes e materiais) de um sistema legado para um modelo de destino pensado para o S/4HANA |
| **Por quê** | Entrar no mercado SAP pela área de migração de dados, provando o aprendizado com entregas datadas e públicas |
| **Prazo** | 28/10/2026 a 22/12/2026: 8 semanas, 2 horas por noite |
| **Status** | Semana 1 de 8: fundamentos de SAP e preparação do projeto |
| **Ferramentas** | Python, SQL, PostgreSQL, Git |

**Summary (EN):** study project simulating a master data migration (customers and materials) from a legacy system to an S/4HANA-oriented target model, using fictional data only. I am a full stack developer and data protection officer (DPO) moving into SAP data migration. The plan runs from 2026-10-28 to 2026-12-22 and every step is committed with a date. This is not real SAP project experience.

## O que este repositório demonstra

- **Perfilamento de dados:** achar problemas de qualidade antes de carregar (duplicados, formatos, campos obrigatórios, caracteres que quebram a importação).
- **Mapeamento:** ligar cada campo do legado a um campo de destino, com a regra de transformação.
- **Limpeza e staging:** tratar o legado em tabelas intermediárias, com registro de tudo que for rejeitado e por quê.
- **Cargas de ensaio (mock loads):** repetir a carga até ela sair limpa.
- **Reconciliação:** provar, com contagens e totais de controle, que nada se perdeu.
- **Registro de defeitos e documentação:** cada erro com causa e correção.
- **Privacidade desde o início:** os dados são fictícios e o repositório não contém dado de pessoa, de aluno nem de cliente. Sou encarregado de dados (DPO) e trato isso como requisito do projeto.

## O cenário

A **Distribuidora Aurora** (empresa fictícia) troca o ERP legado pelo S/4HANA e precisa migrar dois objetos:

| Objeto | Arquivo de origem | Linhas | Problemas injetados de propósito |
|---|---|---|---|
| Clientes | `clientes_legado.csv` | 2.120 | duplicados, e-mails vazios ou inválidos, datas em formatos misturados, UF inválida, CEP incompleto, telefone sem padrão, tipo de pessoa fora do padrão |
| Materiais | `materiais_legado.csv` | 832 | duplicados, descrição acima de 40 caracteres, unidade de medida fora do padrão, NCM vazio ou incompleto, custo negativo ou com vírgula, status fora do padrão, caractere U+2028 que quebra o CSV |

Os arquivos não ficam no repositório. Eles são gerados por um script com semente fixa, então qualquer pessoa reproduz exatamente os mesmos dados.

## Como o trabalho é conduzido

1. Decidir a abordagem de carga (staging ou carga direta), com prós e contras.
2. Especificar e planejar, com tarefas pequenas e verificáveis.
3. Levantar a origem e o destino: estrutura, tipos e tamanhos.
4. Implementar com teste: cada regra de limpeza nasce com o seu caso de teste.
5. Carregar em ensaio e reconciliar relendo os dados e comparando com o arquivo de origem.
6. Tratar erros pela causa raiz, com evidência, antes de propor a correção.
7. Revisar antes de liberar.
8. Documentar o que foi feito e o resultado.

## Plano e status

O plano completo, com datas, está em [`docs/plano-de-estudo.md`](docs/plano-de-estudo.md). A cada noite eu registro o que estudei e o que construí em [`log-de-estudo.md`](log-de-estudo.md), e cada registro vira um commit com data.

| Semana | Datas | Foco | Status |
|---|---|---|---|
| 1 | 28/10 a 03/11 | Fundamentos de SAP, glossário e fluxo do projeto | Em andamento |
| 2 | 04/11 a 10/11 | Dados fictícios, perfilamento e mapeamento | Pendente |
| 3 | 11/11 a 17/11 | Staging, limpeza e primeira carga de ensaio | Pendente |
| 4 | 18/11 a 24/11 | Segunda carga, objeto material e reconciliação | Pendente |
| 5 | 25/11 a 01/12 | Ferramentas de migração, cutover e certificação | Pendente |
| 6 | 02/12 a 08/12 | Painel de reconciliação e demonstração no ar | Pendente |
| 7 | 09/12 a 15/12 | Currículo, entrevistas e candidaturas | Pendente |
| 8 | 16/12 a 22/12 | Reforço e balanço | Pendente |

## Estrutura do repositório

```
sap-migracao-dados/
├── README.md                  este arquivo
├── log-de-estudo.md           registro diário, com data
├── docs/
│   ├── plano-de-estudo.md     plano de 8 semanas
│   ├── escopo-e-abordagem.md  cenário, objetos e decisão de abordagem
│   ├── mapeamento.md          legado para destino, com status de confirmação
│   └── glossario.md           termos de migração de dados SAP
├── src/
│   └── gerar_dados_ficticios.py   gerador dos dados legados fictícios
├── sql/                       perfilamento, staging, limpeza e reconciliação
└── dados-ficticios/           saída do gerador (não versionada)
```

## Como reproduzir

Requisitos: Python 3.8 ou superior. O gerador usa só a biblioteca padrão.

```bash
git clone https://github.com/eupordias/sap-migracao-dados.git
cd sap-migracao-dados
python src/gerar_dados_ficticios.py
```

Saída na pasta `dados-ficticios/`: `clientes_legado.csv`, `materiais_legado.csv` e `gabarito_defeitos.csv` (a contagem dos defeitos injetados; só abro depois de terminar o perfilamento).

Para carregar no PostgreSQL, todas as colunas entram como texto, de propósito: se eu converter tipos na carga, o defeito desaparece e eu deixo de vê-lo.

## Certificados

Nenhum concluído ainda. Cada certificado entra aqui com a data de conclusão e o link da credencial.

| Curso | Emissor | Conclusão | Credencial |
|---|---|---|---|
| Executing Basic ERP Processes with SAP S/4HANA | SAP Learning | pendente | |
| Migrating Data to SAP S/4HANA Cloud, Public Edition | SAP Learning | pendente | |
| Migrating Data to SAP S/4HANA Using the Migration Cockpit | SAP Learning ou openSAP | pendente | |

Os certificados gratuitos são registros de conclusão de curso. Não são a certificação oficial "SAP Certified".

## O que este projeto não é

- Não tem acesso a um sistema SAP. O destino é um modelo em PostgreSQL que aproxima, de forma simplificada, o que um destino S/4HANA espera.
- Não usa o SAP Migration Cockpit de verdade. Eu estudo a ferramenta pelos cursos e reproduzo o raciocínio (staging, mapeamento, regras, carga de ensaio e reconciliação).
- Não substitui experiência em projeto. Substitui a promessa por evidência: o que eu aprendi, quando e como eu provei.

## Privacidade

Todos os dados são gerados aleatoriamente. Nomes, documentos, e-mails e telefones não pertencem a pessoas reais. O repositório não contém material de empregadores, de clientes nem de cursos de terceiros.

## Como este projeto foi feito

Uso ferramentas de IA (Claude) para apoiar o planejamento e como revisor, e a estrutura inicial do repositório e o gerador de dados nasceram com esse apoio. A leitura dos resultados, as decisões e o registro de estudo são meus.

## Contato

- LinkedIn: [linkedin.com/in/eversondias](https://www.linkedin.com/in/eversondias)
- Portfólio: [eversondias.dev.br](https://eversondias.dev.br)
- E-mail: eueversondias@gmail.com

Estou em busca de uma primeira oportunidade em migração de dados SAP, e também de vagas de desenvolvedor júnior ou analista de dados em regime CLT e remoto.
