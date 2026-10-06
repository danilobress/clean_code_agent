\# Diretrizes e Convenções do Projeto



Este documento define os padrões de codificação e arquitetura para o módulo de Service Desk. O não cumprimento destas regras resultará em reprovação no Code Review.



\## 1. Nomenclatura e Idioma

\* \*\*Idioma Base:\*\* Todo o código de domínio (variáveis, funções, métodos) deve ser escrito em \*\*Português\*\*. Termos técnicos consagrados (como `id`, `payload`, `request`) podem ser mantidos em inglês se fizerem parte da biblioteca padrão ou da interface da API.

\* \*\*Variáveis e Funções:\*\* Utilizar `snake\_case` com nomes expressivos e não abreviados (ex: `priorizar\_chamados`, `lista\_chamados`).

\* \*\*Classes:\*\* Utilizar `PascalCase` (ex: `ValidadorChamado`).

\* \*\*Testes:\*\* Funções de teste devem seguir o formato descritivo estruturado: `test\_dado\_\[cenario]\_quando\_\[acao]\_entao\_\[resultado]` (ex: `test\_dado\_prioridade\_invalida\_quando\_priorizar\_entao\_lanca\_value\_error`).



\## 2. Tipagem Estática

\* \*\*Type Hints:\*\* Obrigatório em todas as assinaturas de funções e métodos (Python 3.10+).

\* \*\*Coleções:\*\* Especificar o conteúdo interno das coleções sempre que possível (ex: `list\[dict]` ou `list\[str]`, nunca apenas `list`).



\## 3. Documentação

\* \*\*Docstrings:\*\* Obrigatórias em todas as funções públicas. Devem ser curtas, diretas e focar no "o quê" e não no "como".

\* \*\*Formato:\*\* Utilizar aspas triplas (`"""`) detalhando os parâmetros esperados e o tipo de retorno.



\## 4. Tratamento de Erros e Exceções

\* \*\*Falha Rápida (Fail-Fast):\*\* O código deve falhar imediatamente ao encontrar um estado inválido.

\* \*\*Exceções Descritivas:\*\* É estritamente proibido retornar `None`, `False` ou silenciar erros (`pass`) em caso de violação de regra de negócio. Utilize exceções nativas (como `ValueError` ou `TypeError`) com mensagens de erro claras explicando o motivo da falha.



\## 5. Padrões de Teste (QA/QE)

\* \*\*Framework:\*\* Utilizar exclusivamente o `pytest`.

\* \*\*Estrutura (AAA):\*\* Todos os testes devem ser divididos visualmente ou logicamente em Arrange (Preparação), Act (Ação) e Assert (Validação).

\* \*\*Independência:\*\* Cada teste deve ser completamente isolado. Não deve haver dependência de estado entre execuções. Utilizar `fixtures` para massa de dados repetitiva.



\## 6. Arquitetura e Clean Code

\* \*\*Responsabilidade Única (SRP):\*\* Funções e classes devem ter um único motivo para mudar. Separe a lógica de ordenação da lógica de validação de dados, caso o fluxo cresça.

\* \*\*Simplicidade:\*\* Evite otimizações prematuras. Privilegie a legibilidade e a manutenibilidade do código.

