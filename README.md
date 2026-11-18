# Citizen Assist AI
## Assistente Digital de Orientação ao Cidadão

## 1. Sobre o projeto

O Citizen Assist AI é um assistente digital desenvolvido em Python com o objetivo de facilitar o acesso a informações e orientações sobre serviços públicos.

O sistema permite que o cidadão faça perguntas sobre diferentes serviços e receba orientações organizadas, com informações sobre documentos necessários, locais de atendimento e fontes oficiais.

O projeto foi desenvolvido como parte da Global Solution 2026.2, na disciplina de Pensamento Computacional e Automação com Python.

## 2. Público-alvo

O público-alvo são jovens que estão ingressando no mercado de trabalho e precisam de orientação sobre documentação, serviços digitais e oportunidades profissionais.

O assistente busca simplificar o acesso a informações importantes, contribuindo para a autonomia e inclusão digital desse público.

## 3. Objetivos

- Facilitar o acesso a informações sobre serviços públicos.
- Orientar jovens sobre documentação e oportunidades de trabalho.
- Incentivar a autonomia digital.
- Organizar informações em uma base de conhecimento JSON.
- Utilizar Python para automatizar consultas e registrar atendimentos.
- Disponibilizar fontes oficiais para consulta.

## 4. Objetivos de Desenvolvimento Sustentável (ODS)

O projeto está relacionado aos seguintes Objetivos de Desenvolvimento Sustentável da ONU:

- **ODS 8 – Trabalho Decente e Crescimento Econômico:** apoio aos jovens que estão ingressando no mercado de trabalho.
- **ODS 10 – Redução das Desigualdades:** facilitação do acesso à informação e aos serviços públicos.
- **ODS 16 – Paz, Justiça e Instituições Eficazes:** incentivo ao acesso à informação e à cidadania.

## 5. Tecnologias utilizadas

- Python
- JSON
- CSV
- Visual Studio Code
- GitHub

## 6. Estrutura do projeto

```text
citizen-assist-ai/
├── README.md
├── main.py
├── orientacao.py
├── base_conhecimento.py
├── assistente.py
└── data/
    ├── base_conhecimento.json
    ├── historico.json
    └── atendimentos.csv
```

## 7. Funcionalidades

- Consulta de informações por perguntas digitadas pelo usuário.
- Busca de orientações por palavras-chave.
- Navegação por categorias.
- Exibição de documentos necessários e locais de atendimento.
- Apresentação de fontes e datas de verificação.
- Identificação de perguntas sem resultados.
- Validação de entradas inválidas.
- Bloqueio de entradas que aparentam conter dados pessoais.
- Registro do histórico de atendimentos em JSON.
- Exportação dos atendimentos para CSV.
- Cálculo de indicadores de utilização.

## 8. Base de conhecimento

A base de conhecimento é armazenada no arquivo `data/base_conhecimento.json`.

O projeto possui 10 orientações distribuídas em três categorias:

### Trabalho e Renda

- Carteira de Trabalho Digital.
- Seguro-Desemprego.
- FGTS.
- Jovem Aprendiz.
- CNIS.

### Documentação

- Consulta da situação do CPF.
- Comprovante de CPF.
- Primeiro título eleitoral.

### Serviços Digitais

- Criação de conta Gov.br.
- Aumento do nível da conta Gov.br.

Cada orientação possui identificador, categoria, título, palavras-chave, resposta, documentos necessários, local de atendimento, fonte e data de verificação.

## 9. Programação orientada a objetos

O projeto foi desenvolvido utilizando três classes principais:

### Classe Orientacao

Representa cada orientação disponível na base de conhecimento e possui o método `exibir()`, responsável por apresentar as informações ao usuário.

### Classe BaseConhecimento

Responsável por carregar os dados do arquivo JSON, normalizar textos, identificar categorias e realizar as buscas.

### Classe Assistente

Controla a interação com o usuário, apresenta o menu, registra os atendimentos, calcula indicadores e exporta os dados para CSV.

## 10. Sistema de busca

O sistema utiliza uma busca baseada em palavras-chave e pontuação.

A pontuação funciona da seguinte maneira:

- Palavra-chave encontrada na pergunta: **+3 pontos**.
- Palavra da pergunta com quatro ou mais letras encontrada no título: **+1 ponto**.

A classificação dos resultados é:

- **Alta confiança (HIGH):** 6 pontos ou mais.
- **Média confiança (MEDIUM):** de 3 a 5 pontos.
- **Sem resultado:** menos de 3 pontos.

Os textos são normalizados para facilitar a identificação das palavras, desconsiderando diferenças entre letras maiúsculas, minúsculas e acentos.

## 11. Segurança e transparência

O assistente possui uma validação para bloquear entradas que aparentem conter dados pessoais, como sequências de oito ou mais dígitos ou endereços de e-mail.

Além disso, o sistema informa que não é um canal oficial de atendimento e apresenta fontes para que o usuário possa consultar as informações diretamente.

## 12. Histórico e indicadores

Os atendimentos são armazenados no arquivo `data/historico.json`.

O sistema registra informações como:

- Data do atendimento.
- Origem do atendimento.
- Pergunta realizada.
- Identificador da orientação encontrada.
- Indicação de resposta encontrada.
- Indicação de que a orientação ajudou.
- Quantidade de tentativas.
- Tempo de atendimento.
- Nota de facilidade, quando registrada.

Os dados também podem ser exportados para `data/atendimentos.csv`.

O sistema calcula indicadores como percentual de perguntas respondidas, percentual de orientações úteis, tempo médio de atendimento, média de tentativas e facilidade de utilização quando há avaliações registradas.

## 13. Como executar o projeto

É necessário ter Python instalado no computador.

1. Faça o download ou clone este repositório.
2. Abra a pasta do projeto no Visual Studio Code.
3. Abra o terminal integrado.
4. Execute o comando:

```bash
python main.py
```

O menu principal será apresentado no terminal.

## 14. Testes realizados

Foram realizados testes funcionais e testes com usuários para avaliar o funcionamento e a qualidade das orientações fornecidas pelo Citizen Assist AI.

### 14.1 Testes funcionais

Foram testadas as seguintes funcionalidades:

- Busca de orientações com resultado.
- Busca utilizando diferentes palavras e expressões.
- Navegação por categorias.
- Perguntas sem correspondência na base.
- Entradas inválidas.
- Bloqueio de possíveis dados pessoais.
- Registro do histórico de atendimentos.
- Exportação de arquivos CSV.
- Cálculo dos indicadores.

### 14.2 Testes com usuários

Os testes foram realizados com três participantes, totalizando 12 interações, sendo quatro perguntas para cada participante.

Foram avaliados os seguintes aspectos:

- Se o assistente encontrou a orientação solicitada.
- Tempo necessário para obter a resposta.
- Se a orientação foi útil.
- Quantidade de tentativas necessárias.

### 14.3 Resultados obtidos

| Indicador | Resultado |
|---|---:|
| Participantes | 3 |
| Total de interações | 12 |
| Perguntas respondidas | 12 (100%) |
| Orientações consideradas úteis | 12 (100%) |
| Tempo total | 223 segundos |
| Tempo médio por pergunta | 18,6 segundos |
| Total de tentativas | 23 |
| Média de tentativas por pergunta | 1,92 |

### 14.4 Análise dos resultados

Os resultados demonstraram que o Citizen Assist AI conseguiu localizar orientações para todas as 12 perguntas realizadas pelos participantes.

Todos os participantes consideraram as orientações úteis, indicando que as informações apresentadas atenderam às necessidades identificadas durante os testes.

O tempo médio de resposta foi de aproximadamente 18,6 segundos por pergunta. A média de tentativas foi de 1,92, considerando todas as interações.

O segundo participante apresentou um número maior de tentativas, especialmente na consulta sobre CPF, indicando uma oportunidade de melhoria no mecanismo de busca e na identificação de palavras-chave.

De maneira geral, os testes demonstraram resultados positivos quanto à capacidade de localizar informações e auxiliar os usuários.

**Observação:** não foi registrada uma nota de facilidade de utilização de 1 a 5 para cada participante nesta rodada de testes.

## 15. Limitações do projeto

O Citizen Assist AI utiliza uma base de conhecimento previamente cadastrada. Portanto, não responde a assuntos que não estejam contemplados nessa base.

O mecanismo de busca é baseado em palavras-chave e pontuação, não sendo um sistema de inteligência artificial generativa conectado a serviços externos.

As informações precisam ser verificadas e atualizadas periodicamente. O assistente também não realiza solicitações ou procedimentos oficiais em nome do cidadão.

## 16. Fontes de informação

As orientações foram estruturadas com base em fontes institucionais e serviços oficiais, incluindo:

- Portal Gov.br: https://www.gov.br/
- Ministério do Trabalho e Emprego: https://www.gov.br/trabalho-e-emprego/
- Caixa Econômica Federal: https://www.caixa.gov.br/
- Tribunal Superior Eleitoral: https://www.tse.jus.br/

As fontes específicas de cada orientação estão disponíveis no arquivo `data/base_conhecimento.json`.

## 17. Integrantes

**Integrante:** Maria Beatriz Braga de Lima  
**RM:** 570501

## 18. Repositório e apresentação

**GitHub:** https://github.com/BragaBibi/citizen-assist-ai

**Vídeo de apresentação:** [Inserir link do YouTube após a gravação]

---

**Citizen Assist AI — Informação acessível, cidadania e autonomia digital.**
