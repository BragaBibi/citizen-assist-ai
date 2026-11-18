
import json
import csv
import re
import time
from datetime import datetime


class Assistente:
    def __init__(self, nome, base):
        self.nome = nome
        self.base = base
        self.historico = []
        self.facilidade = []

        self.arquivo_historico = "data/historico.json"
        self.arquivo_csv = "data/atendimentos.csv"

        self.carregar_historico()

    def carregar_historico(self):
        try:
            with open(self.arquivo_historico, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            if isinstance(dados, list):
                self.historico = dados
                self.facilidade = [
                    item["facilidade"]
                    for item in dados
                    if item.get("facilidade") is not None
                ]
            else:
                self.historico = []

        except (FileNotFoundError, json.JSONDecodeError):
            self.historico = []

    def salvar_historico(self):
        with open(self.arquivo_historico, "w", encoding="utf-8") as arquivo:
            json.dump(self.historico, arquivo, ensure_ascii=False, indent=4)

    def validar_dados_pessoais(self, texto):
        quantidade_digitos = len(re.findall(r"\d", texto))
        return quantidade_digitos < 8 and "@" not in texto

    def registrar(self, origem, pergunta, id_orientacao,
                  encontrou, ajudou, tentativas, tempo_segundos):

        atendimento = {
            "data": datetime.now().isoformat(timespec="seconds"),
            "origem": origem,
            "pergunta": pergunta,
            "id_orientacao": id_orientacao,
            "encontrou": encontrou,
            "ajudou": ajudou,
            "tentativas": tentativas,
            "tempo_segundos": tempo_segundos,
            "facilidade": None
        }

        self.historico.append(atendimento)
        self.salvar_historico()

    def perguntar(self):
        tentativas = 0
        inicio = time.time()

        while True:
            pergunta = input(
                "\nDigite sua dúvida (0 para voltar): "
            ).strip()

            if pergunta == "0":
                return

            if not pergunta:
                print("Digite uma pergunta válida.")
                continue

            if not self.validar_dados_pessoais(pergunta):
                print(
                    "Atenção: não digite CPF, telefone ou e-mail. "
                    "Reescreva sua pergunta."
                )
                continue

            tentativas += 1
            resultados = self.base.buscar(pergunta)

            if not resultados or resultados[0][0] < 3:
                print("\nNão encontrei uma orientação para essa dúvida.")
                print("Tente utilizar outras palavras ou navegar pelas categorias.")

                tempo = round(time.time() - inicio, 1)

                self.registrar(
                    "pergunta",
                    pergunta,
                    None,
                    False,
                    False,
                    tentativas,
                    tempo
                )

                inicio = time.time()
                tentativas = 0
                continue

            pontos, orientacao = resultados[0]

            confianca = "ALTA" if pontos >= 6 else "MÉDIA"

            print(f"\nConfiança da resposta: {confianca} ({pontos} pontos)")

            orientacao.exibir()

            alternativas = [
                (p, o) for p, o in resultados[1:3] if p >= 3
            ]

            if alternativas:
                print("\nOutras orientações relacionadas:")
                for pontos_alt, alternativa in alternativas:
                    print(f"- {alternativa.titulo}")

            while True:
                resposta = input(
                    "\nEssa orientação respondeu sua dúvida? (s/n): "
                ).strip().lower()

                if resposta in ("s", "n"):
                    break

                print("Resposta inválida. Digite s ou n.")

            tempo = round(time.time() - inicio, 1)

            self.registrar(
                "pergunta",
                pergunta,
                orientacao.id,
                True,
                resposta == "s",
                tentativas,
                tempo
            )

            print("\nAtendimento registrado!")
            return

    def navegar(self):
        categorias = self.base.categorias()

        if not categorias:
            print("\nNenhuma categoria disponível.")
            return

        while True:
            print("\n===== CATEGORIAS =====")

            for indice, categoria in enumerate(categorias, start=1):
                print(f"{indice} - {categoria}")

            print("0 - Voltar")

            opcao = input("\nEscolha uma categoria: ").strip()

            if opcao == "0":
                return

            if not opcao.isdigit() or not (1 <= int(opcao) <= len(categorias)):
                print("Opção inválida. Tente novamente.")
                continue

            categoria = categorias[int(opcao) - 1]
            orientacoes = self.base.por_categoria(categoria)

            while True:
                print(f"\n===== {categoria.upper()} =====")

                for indice, orientacao in enumerate(orientacoes, start=1):
                    print(f"{indice} - {orientacao.titulo}")

                print("0 - Voltar")

                escolha = input("\nEscolha uma orientação: ").strip()

                if escolha == "0":
                    break

                if not escolha.isdigit() or not (
                    1 <= int(escolha) <= len(orientacoes)
                ):
                    print("Opção inválida. Tente novamente.")
                    continue

                orientacao = orientacoes[int(escolha) - 1]

                inicio = time.time()
                orientacao.exibir()

                while True:
                    resposta = input(
                        "\nEssa orientação ajudou? (s/n): "
                    ).strip().lower()

                    if resposta in ("s", "n"):
                        break

                    print("Resposta inválida. Digite s ou n.")

                tempo = round(time.time() - inicio, 1)

                self.registrar(
                    "categoria",
                    orientacao.titulo,
                    orientacao.id,
                    True,
                    resposta == "s",
                    1,
                    tempo
                )

                print("\nAtendimento registrado!")

    def indicadores(self):
        total = len(self.historico)

        print("\n========== INDICADORES ==========")

        if total == 0:
            print("Ainda não existem atendimentos registrados.")
            return

        encontrados = sum(
            1 for item in self.historico if item["encontrou"]
        )

        ajudaram = sum(
            1 for item in self.historico if item["ajudou"]
        )

        tempo_medio = sum(
            item["tempo_segundos"] for item in self.historico
        ) / total

        tentativas_media = sum(
            item["tentativas"] for item in self.historico
        ) / total

        taxa_encontrada = encontrados / total * 100
        taxa_acerto = ajudaram / total * 100

        print(f"Total de atendimentos: {total}")
        print(f"Respostas encontradas: {taxa_encontrada:.1f}%")
        print(f"Taxa de acerto (ajudou): {taxa_acerto:.1f}%")
        print(f"Tempo médio: {tempo_medio:.1f} segundos")
        print(f"Tentativas por atendimento: {tentativas_media:.1f}")

        notas = [
            item["facilidade"]
            for item in self.historico
            if item.get("facilidade") is not None
        ]

        if notas:
            media = sum(notas) / len(notas)
            print(f"Facilidade de uso: {media:.1f}/5")
        else:
            print("Facilidade de uso: ainda não avaliada.")

        print("\nDúvidas sem solução:")

        sem_solucao = [
            item["pergunta"]
            for item in self.historico
            if not item["encontrou"]
        ]

        if sem_solucao:
            for pergunta in sem_solucao:
                print(f"- {pergunta}")
        else:
            print("Nenhuma dúvida sem solução.")

        print("=================================")

    def exportar_csv(self):
        campos = [
            "data",
            "origem",
            "pergunta",
            "id_orientacao",
            "encontrou",
            "ajudou",
            "tentativas",
            "tempo_segundos",
            "facilidade"
        ]

        with open(
            self.arquivo_csv,
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as arquivo:

            escritor = csv.DictWriter(
                arquivo,
                fieldnames=campos
            )

            escritor.writeheader()
            escritor.writerows(self.historico)

        print("\nAtendimentos exportados para data/atendimentos.csv!")

    def iniciar(self):
        print("\n" + "=" * 55)
        print(f"BEM-VINDO AO {self.nome.upper()}")
        print("Orientação digital para jovens cidadãos")
        print("=" * 55)

        while True:
            print("\n========== MENU PRINCIPAL ==========")
            print("1 - Fazer uma pergunta")
            print("2 - Navegar por categorias")
            print("3 - Consultar indicadores")
            print("4 - Exportar atendimentos CSV")
            print("0 - Sair")

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "0":
                break
            elif opcao == "1":
                self.perguntar()
            elif opcao == "2":
                self.navegar()
            elif opcao == "3":
                self.indicadores()
            elif opcao == "4":
                self.exportar_csv()
            else:
                print("Opção inválida. Escolha uma opção do menu.")

        while True:
            nota = input(
                "\nAvalie a facilidade de uso (1 a 5): "
            ).strip()

            if nota in ("1", "2", "3", "4", "5"):
                nota = int(nota)
                self.facilidade.append(nota)

                if self.historico:
                    self.historico[-1]["facilidade"] = nota

                break

            print("Nota inválida. Digite um número de 1 a 5.")

        self.salvar_historico()
        self.exportar_csv()
        self.indicadores()

        print(f"\nObrigado por utilizar o {self.nome}!")
