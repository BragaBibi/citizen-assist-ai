
import json
import unicodedata
from orientacao import Orientacao


class BaseConhecimento:
    def __init__(self, caminho):
        self.caminho = caminho
        self.orientacoes = []

    def normalizar(self, texto):
        texto = texto.lower().strip()

        texto = unicodedata.normalize("NFD", texto)
        texto = "".join(
            letra for letra in texto
            if unicodedata.category(letra) != "Mn"
        )

        for sinal in "?!.,;:()":
            texto = texto.replace(sinal, " ")

        return " " + " ".join(texto.split()) + " "

    def carregar(self):
        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            self.orientacoes = []

            for item in dados:
                orientacao = Orientacao(
                    item["id"],
                    item["categoria"],
                    item["titulo"],
                    item["palavras_chave"],
                    item["resposta"],
                    item["documentos"],
                    item["onde"],
                    item["fonte"],
                    item["verificado_em"]
                )

                self.orientacoes.append(orientacao)

            print(f"Base carregada: {len(self.orientacoes)} orientações.")

        except FileNotFoundError:
            print("Erro: arquivo da base de conhecimento não encontrado.")

        except json.JSONDecodeError:
            print("Erro: o arquivo JSON está corrompido ou possui formato inválido.")

        except (KeyError, TypeError):
            print("Erro: existem campos obrigatórios ausentes ou inválidos no JSON.")

    def categorias(self):
        return sorted(set(
            orientacao.categoria
            for orientacao in self.orientacoes
        ))

    def por_categoria(self, categoria):
        return [
            orientacao
            for orientacao in self.orientacoes
            if orientacao.categoria == categoria
        ]

    def pontuar(self, pergunta, orientacao):
        pergunta_normalizada = self.normalizar(pergunta)
        titulo_normalizado = self.normalizar(orientacao.titulo)

        pontos = 0

        # Cada palavra-chave encontrada vale 3 pontos
        for palavra in orientacao.palavras_chave:
            palavra_normalizada = self.normalizar(palavra)

            if palavra_normalizada in pergunta_normalizada:
                pontos += 3

        # Cada palavra da pergunta encontrada no título vale 1 ponto
        palavras_pergunta = set(pergunta_normalizada.split())

        for palavra in palavras_pergunta:
            if len(palavra) >= 4:
                if f" {palavra} " in titulo_normalizado:
                    pontos += 1

        return pontos

    def buscar(self, pergunta):
        resultados = []

        for orientacao in self.orientacoes:
            pontos = self.pontuar(pergunta, orientacao)

            resultados.append((pontos, orientacao))

        resultados.sort(key=lambda item: item[0], reverse=True)

        return resultados
