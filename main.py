
from base_conhecimento import BaseConhecimento
from assistente import Assistente


def main():
    # Carrega a base de conhecimento
    base = BaseConhecimento("data/base_conhecimento.json")
    base.carregar()

    # Verifica se a base foi carregada corretamente
    if not base.orientacoes:
        print("Não foi possível iniciar o assistente.")
        return

    # Cria o assistente
    assistente = Assistente("Citizen Assist AI", base)

    # Inicia o atendimento
    assistente.iniciar()


if __name__ == "__main__":
    main()
