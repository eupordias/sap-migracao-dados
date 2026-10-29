"""
Gerador de dados legados FICTICIOS para o projeto simulado de migracao SAP.

Cenario: Distribuidora Aurora (empresa ficticia) migra clientes e materiais
do ERP legado para o S/4HANA.

Todos os valores sao aleatorios. Nomes, documentos, e-mails e telefones nao
pertencem a pessoas reais. Nao use dados reais neste projeto.

Uso:
    python gerar_dados_ficticios.py
Saida (na pasta dados-ficticios):
    clientes_legado.csv, materiais_legado.csv
    gabarito_defeitos.csv  (contagem dos defeitos injetados; so abra depois
                            de terminar o seu perfilamento)
"""
import csv
import os
import random
from datetime import date, timedelta

random.seed(2026)
PASTA = "dados-ficticios"
os.makedirs(PASTA, exist_ok=True)

NOMES = ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Fabio", "Gabriela", "Hugo",
         "Isabela", "Joao", "Karina", "Lucas", "Marina", "Nelson", "Olivia",
         "Paulo", "Quiteria", "Rafael", "Sandra", "Tiago"]
SOBRENOMES = ["Silva", "Souza", "Oliveira", "Santos", "Lima", "Pereira",
              "Costa", "Almeida", "Ribeiro", "Carvalho", "Gomes", "Martins"]
EMPRESAS = ["Comercial", "Distribuidora", "Mercantil", "Industria", "Atacado"]
CIDADES = [("Maceio", "AL"), ("Recife", "PE"), ("Salvador", "BA"),
           ("Aracaju", "SE"), ("Natal", "RN"), ("Fortaleza", "CE")]
UNIDADES_OK = ["UN", "CX", "KG", "PC"]
GRUPOS = ["ALIMENTOS", "LIMPEZA", "BEBIDAS", "HIGIENE", "EMBALAGEM"]
PRODUTOS = ["Arroz", "Feijao", "Detergente", "Sabao em po", "Refrigerante",
            "Agua mineral", "Papel higienico", "Shampoo", "Sacola plastica",
            "Cafe torrado", "Acucar", "Oleo de soja"]

defeitos = {}
# Defeitos da linha em construcao. Cada linha guarda os seus, para que uma
# copia duplicada conte de novo os defeitos da linha original no gabarito.
linha_atual = []


def marca(nome):
    linha_atual.append(nome)


def conta(marcas):
    for nome in marcas:
        defeitos[nome] = defeitos.get(nome, 0) + 1


def digitos(n):
    return "".join(random.choice("0123456789") for _ in range(n))


def data_aleatoria():
    base = date(2012, 1, 1) + timedelta(days=random.randint(0, 5000))
    r = random.random()
    if r < 0.70:
        return base.strftime("%d/%m/%Y")
    if r < 0.90:
        marca("data_formato_iso")
        return base.strftime("%Y-%m-%d")
    if r < 0.97:
        marca("data_formato_curto")
        return base.strftime("%d-%m-%y")
    marca("data_futura")
    return (date(2026, 12, 31) + timedelta(days=random.randint(1, 400))).strftime("%d/%m/%Y")


def cliente(i):
    pj = random.random() < 0.3
    if pj:
        nome = f"{random.choice(EMPRESAS)} {random.choice(SOBRENOMES)} LTDA"
        doc = digits_fmt(14, pj=True)
    else:
        nome = f"{random.choice(NOMES)} {random.choice(SOBRENOMES)}"
        doc = digits_fmt(11)
    cidade, uf = random.choice(CIDADES)
    email = f"contato{i}@exemplo-ficticio.com.br"
    fone = f"({random.randint(11, 89)}) 9{digitos(4)}-{digitos(4)}"
    cep = f"{digitos(5)}-{digitos(3)}"
    r = random.random()
    if r < 0.03:
        marca("nome_com_espacos_extras")
        nome = f"  {nome.upper()}   "
    if random.random() < 0.08:
        marca("email_vazio")
        email = ""
    elif random.random() < 0.03:
        marca("email_invalido")
        email = email.replace("@", "")
    r = random.random()
    if r < 0.15:
        marca("telefone_sem_mascara")
        fone = fone.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
    elif r < 0.25:
        marca("telefone_com_codigo_pais")
        fone = "+55 " + fone
    if random.random() < 0.03:
        marca("uf_invalida")
        uf = random.choice(["XX", "al", "", "A"])
    if random.random() < 0.02:
        marca("cep_incompleto")
        cep = digitos(random.choice([4, 6, 7]))
    tipo = "J" if pj else "F"
    if random.random() < 0.1:
        marca("tipo_pessoa_fora_do_padrao")
        tipo = random.choice(["PF", "pf", "Fisica", "fisica"] if not pj else ["PJ", "pj", "Juridica", "juridica"])
    return [f"CLI-{i:06d}", nome, tipo, doc, email, fone, cep, cidade, uf,
            data_aleatoria(), random.choice(["A", "A", "A", "I", "B"])]


def digits_fmt(n, pj=False):
    d = digitos(n)
    if random.random() < 0.02:
        marca("documento_tamanho_errado")
        return d[:-1]
    if random.random() < 0.5:
        return d
    marca("documento_com_mascara")
    if pj:
        return f"{d[:2]}.{d[2:5]}.{d[5:8]}/{d[8:12]}-{d[12:]}"
    return f"{d[:3]}.{d[3:6]}.{d[6:9]}-{d[9:]}"


def gerar_clientes(total=2000):
    linhas, marcas = [], []
    for i in range(1, total + 1):
        linha_atual.clear()
        linhas.append(cliente(i))
        marcas.append(list(linha_atual))
    for m in marcas:
        conta(m)
    duplicados = random.sample(range(len(linhas)), int(total * 0.06))
    prox = total + 1
    for idx in duplicados:
        copia = list(linhas[idx])
        copia[0] = f"CLI-{prox:06d}"
        prox += 1
        conta(marcas[idx] + ["cliente_duplicado"])
        linhas.append(copia)
    random.shuffle(linhas)
    with open(os.path.join(PASTA, "clientes_legado.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["codigo_legado", "nome", "tipo_pessoa", "documento", "email",
                    "telefone", "cep", "cidade", "uf", "data_cadastro", "situacao"])
        w.writerows(linhas)


def gerar_materiais(total=800):
    linhas, marcas = [], []
    for i in range(1, total + 1):
        linha_atual.clear()
        desc = f"{random.choice(PRODUTOS)} {random.choice(['1kg', '500g', '2L', 'pacote', 'caixa 12un'])}"
        un = random.choice(UNIDADES_OK)
        ncm = digitos(8)
        custo = f"{random.uniform(1, 300):.2f}"
        ativo = random.choice(["S", "S", "S", "N"])
        if random.random() < 0.10:
            marca("descricao_acima_de_40_caracteres")
            desc = desc + " - embalagem promocional especial de fim de ano"
        if random.random() < 0.02:
            # U+2028 (separador de linha Unicode) quebra a importacao de CSV em
            # varias ferramentas; e um defeito real de legado.
            marca("descricao_com_separador_unicode_u2028")
            desc = desc.replace(" ", "\u2028", 1)
        if random.random() < 0.15:
            marca("unidade_fora_do_padrao")
            un = random.choice(["un", "UNID", "Pc", "cx", "kg", "Unidade"])
        if random.random() < 0.05:
            marca("ncm_vazio")
            ncm = ""
        elif random.random() < 0.03:
            marca("ncm_com_7_digitos")
            ncm = ncm[:7]
        if random.random() < 0.04:
            marca("custo_negativo")
            custo = "-" + custo
        elif random.random() < 0.10:
            marca("custo_com_virgula")
            custo = custo.replace(".", ",")
        if random.random() < 0.08:
            marca("ativo_fora_do_padrao")
            ativo = random.choice(["1", "0", "sim", "nao"])
        linhas.append([f"MAT-{i:05d}", desc, un, ncm, custo, random.choice(GRUPOS), ativo])
        marcas.append(list(linha_atual))
    for m in marcas:
        conta(m)
    duplicados = random.sample(range(len(linhas)), int(total * 0.04))
    prox = total + 1
    for idx in duplicados:
        copia = list(linhas[idx])
        copia[0] = f"MAT-{prox:05d}"
        prox += 1
        conta(marcas[idx] + ["material_duplicado"])
        linhas.append(copia)
    random.shuffle(linhas)
    with open(os.path.join(PASTA, "materiais_legado.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["codigo_legado", "descricao", "unidade", "ncm", "preco_custo",
                    "grupo_mercadoria", "ativo"])
        w.writerows(linhas)


gerar_clientes()
gerar_materiais()

with open(os.path.join(PASTA, "gabarito_defeitos.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["tipo_de_defeito", "quantidade_injetada"])
    for k in sorted(defeitos):
        w.writerow([k, defeitos[k]])

print("Arquivos gerados na pasta", PASTA)
print("Nao abra gabarito_defeitos.csv antes de terminar o perfilamento.")
