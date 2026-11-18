# Citizen Assist AI
### Assistente Digital de Orientação ao Cidadão

## 1. Sobre o projeto

O Citizen Assist AI é um assistente digital desenvolvido em Python com o objetivo de facilitar o acesso dos jovens a informações sobre documentos, serviços públicos e direitos relacionados à entrada na vida adulta e no mercado de trabalho.

O sistema funciona pelo terminal e utiliza uma base de conhecimento em formato JSON para responder dúvidas com informações organizadas, fontes oficiais e linguagem simples.

O assistente utiliza um mecanismo de busca baseado em palavras-chave e pontuação para identificar a orientação mais adequada à pergunta realizada pelo usuário.

## 2. Público-alvo e problema identificado

**Público-alvo:** Jovens que estão iniciando a vida adulta e ingressando no mercado de trabalho.

**Problema:** Muitos jovens encontram dificuldades para localizar informações confiáveis sobre documentação, direitos trabalhistas, benefícios e serviços públicos. As informações estão distribuídas em diferentes plataformas e nem sempre são apresentadas de maneira simples.

**Solução:** Desenvolver um assistente digital que centralize orientações e facilite a localização de informações verificadas, apresentando documentos necessários, locais de atendimento e fontes de consulta.

## 3. Objetivos de Desenvolvimento Sustentável (ODS)

O projeto está relacionado aos seguintes Objetivos de Desenvolvimento Sustentável da ONU:

- **ODS 8 – Trabalho Decente e Crescimento Econômico:** facilitar o acesso a informações sobre direitos trabalhistas e oportunidades profissionais.
- **ODS 10 – Redução das Desigualdades:** democratizar o acesso à informação e aos serviços públicos.
- **ODS 16 – Paz, Justiça e Instituições Eficazes:** promover transparência e acesso a informações de fontes governamentais.

## 4. Tecnologias utilizadas

- Python 3
- Visual Studio Code
- JSON para armazenamento da base de conhecimento e histórico.
- CSV para exportação dos atendimentos.
- GitHub para versionamento e disponibilização do projeto.

Foram utilizados módulos nativos do Python, sem necessidade de bibliotecas externas.

## 5. Estrutura do projeto

```text
citizen-assist-ai/
│
├── README.md
├── main.py
├── orientacao.py
├── base_conhecimento.py
├── assistente.py
│
└── data/
    ├── base_conhecimento.json
    ├── historico.json
    └── atendimentos.csv
```

## 6. Funcionalidades implementadas

- Carregamento de uma base de conhecimento em JSON.
- Organização das informações em três categorias.
- Busca de orientações por palavras-chave.
- Cálculo de pontuação e nível de confiança.
- Navegação por categorias.
- Exibição de documentos necessários e locais de atendimento.
- Apresentação das fontes e datas de verificação.
- Bloqueio de perguntas contendo possíveis dados pessoais.
- Tratamento de entradas inválidas.
- Registro dos atendimentos em JSON.
- Cálculo de indicadores de utilização.
- Exportação dos atendimentos para CSV.
- Avaliação da facilidade de uso.

## 7. Base de conhecimento

A base contém 10 orientações distribuídas em três categorias:

**Trabalho e Renda**
1. Carteira de Trabalho Digital.
2. Seguro-Desemprego.
3. Consulta do FGTS.
4. Programa Jovem Aprendiz.
5. Extrato de Contribuição do INSS (CNIS).

**Documentação**
6. Consulta da situação do CPF.
7. Comprovante de inscrição no CPF.
8. Primeiro título de eleitor.

**Serviços Digitais**
9. Criação de conta Gov.br.
10. Aumento do nível da conta Gov.br.

Cada orientação possui identificador, categoria, título, palavras-chave, resposta, documentos, local de atendimento, fonte e data de verificação.

## 8. Programação orientada a objetos

O sistema utiliza três classes principais:

**Orientacao**

Armazena os dados de cada orientação e possui o método `exibir()`, responsável por apresentar as informações ao usuário.

**BaseConhecimento**

Responsável por carregar o arquivo JSON, criar os objetos Orientacao, listar categorias, filtrar orientações e realizar a busca inteligente.

**Assistente**

Responsável pela interação com o usuário, navegação, registro dos atendimentos, cálculo dos indicadores e exportação CSV.

As classes trabalham por composição: o Assistente possui um objeto BaseConhecimento, que contém uma lista de objetos Orientacao.

## 9. Regra de pontuação da busca

A busca utiliza regras de pontuação:

- Cada