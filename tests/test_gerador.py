"""
Testes do gerador de dados ficticios.

O gabarito precisa bater com o que esta nos arquivos gerados. As linhas
duplicadas copiam os defeitos da linha original, entao esses defeitos
tambem contam no gabarito.

Uso (na raiz do repositorio):
    python -m unittest
"""
import csv
import os
import subprocess
import sys
import tempfile
import unittest

GERADOR = os.path.join(os.path.dirname(__file__), "..", "src", "gerar_dados_ficticios.py")


def ler(pasta, arquivo):
    with open(os.path.join(pasta, arquivo), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


class GabaritoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        subprocess.run([sys.executable, os.path.abspath(GERADOR)], cwd=cls.tmp.name,
                       check=True, capture_output=True)
        pasta = os.path.join(cls.tmp.name, "dados-ficticios")
        cls.clientes = ler(pasta, "clientes_legado.csv")
        cls.materiais = ler(pasta, "materiais_legado.csv")
        cls.gabarito = {l["tipo_de_defeito"]: int(l["quantidade_injetada"])
                        for l in ler(pasta, "gabarito_defeitos.csv")}

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_totais_de_linhas(self):
        self.assertEqual(len(self.clientes), 2120)
        self.assertEqual(len(self.materiais), 832)
        self.assertEqual(self.gabarito["cliente_duplicado"], 120)
        self.assertEqual(self.gabarito["material_duplicado"], 32)

    def test_gabarito_conta_defeitos_das_linhas_duplicadas(self):
        no_arquivo = {
            "email_vazio": sum(c["email"] == "" for c in self.clientes),
            "tipo_pessoa_fora_do_padrao": sum(c["tipo_pessoa"] not in ("F", "J") for c in self.clientes),
            "ncm_vazio": sum(m["ncm"] == "" for m in self.materiais),
            "ncm_com_7_digitos": sum(len(m["ncm"]) == 7 for m in self.materiais),
            "custo_negativo": sum(m["preco_custo"].startswith("-") for m in self.materiais),
        }
        for defeito, quantidade in no_arquivo.items():
            with self.subTest(defeito=defeito):
                self.assertEqual(self.gabarito[defeito], quantidade)


if __name__ == "__main__":
    unittest.main()
