# FarmTech Python — Gestão do Agronegócio

Projeto acadêmico da FIAP para a atividade **Gestão do Agronegócio em Python — Capítulos 3 ao 6**.

> **Prazo da atividade:** 14/10/2026  
> **Formato:** trabalho em grupo  
> **Objetivo deste repositório:** concentrar a versão oficial da entrega e documentar claramente o problema, a solução, os requisitos atendidos e a forma de execução.

---

## 1. Problema escolhido

O projeto propõe um **sistema de gerenciamento de áreas agrícolas** para ajudar no registro e acompanhamento de informações importantes de uma plantação.

A solução permite cadastrar áreas/talhões e armazenar:

- nome da área;
- cultura;
- tamanho em hectares;
- pH do solo;
- nitrogênio (N);
- fósforo (P);
- potássio (K);
- observações do produtor.

O sistema também permite consultar, atualizar, excluir, salvar, carregar e exportar esses registros.

### Por que esse problema?

No agronegócio, informações de cultivo podem ficar espalhadas em anotações, planilhas e registros isolados. A proposta do projeto é centralizar esses dados em uma aplicação simples em Python, facilitando a organização das informações e demonstrando os conteúdos estudados nos capítulos 3 a 6.

---

## 2. Requisitos obrigatórios da atividade

| Requisito | Como aparece no projeto | Status |
|---|---|---|
| Funções/procedimentos com parâmetros | Funções distribuídas pelos módulos em `src/` | ✅ |
| Lista | Lista `registros` mantém as áreas em memória | ✅ |
| Tupla | `CULTURAS_PERMITIDAS`, `CAMPOS_RELATORIO` e `CAMPOS_AREA` | ✅ |
| Dicionário | Cada área agrícola é representada por um dicionário | ✅ |
| Tabela de memória | Lista de dicionários usada durante a execução | ✅ |
| Arquivo TXT | Relatório em `dados/relatorio.txt` | ✅ |
| Arquivo JSON | Persistência em `dados/registros.json` | ✅ |
| Conexão Oracle | Implementada em `src/banco_oracle.py` | 🟡 Aguardando validação com conta FIAP desbloqueada |
| Validação das entradas | `src/validacoes.py` | ✅ |
| Saídas legíveis | Menu, listagens e relatório formatados | ✅ |
| README com problema e solução | Este documento | ✅ |
| Código no GitHub | Repositório oficial do grupo | ✅ |

---

## 3. Funcionalidades atuais

O menu principal disponível em `main.py` é:

```text
==========================================
          FARMTECH SOLUTIONS
==========================================
1  - Cadastrar área agrícola
2  - Listar áreas
3  - Consultar área por ID
4  - Atualizar área
5  - Excluir área
6  - Salvar dados em JSON
7  - Carregar dados do JSON
8  - Exportar relatório TXT
9  - Enviar registros ao Oracle
10 - Consultar registros do Oracle
0  - Sair
```

As opções 1 a 8 e 0 foram validadas manualmente. As opções 9 e 10 estão implementadas, mas a validação real do banco Oracle depende da conta institucional da FIAP estar desbloqueada e com credenciais válidas.

---

## 4. Estrutura do projeto

```text
FarmTech-Python-Gestao-Agronegocio/
│
├── main.py
├── README.md
├── CONTRIBUTING.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── src/
│   ├── __init__.py
│   ├── cadastro.py
│   ├── consultas.py
│   ├── validacoes.py
│   ├── arquivos.py
│   └── banco_oracle.py
│
├── dados/
│   └── registros.json
│
├── database/
│   └── criar_tabelas.sql
│
├── docs/
│   └── PLANO_DE_TRABALHO.md
│
├── teste_arquivos.py
└── teste_oracle.py
```

---

## 5. Estruturas de dados utilizadas

Durante a execução, as áreas são armazenadas em uma **lista de dicionários**, funcionando como uma tabela temporária em memória.

Exemplo conceitual:

```python
{
    "id": 1,
    "nome_area": "Talhão A",
    "cultura": "Soja",
    "area_hectares": 15.5,
    "ph": 6.2,
    "nitrogenio": 30,
    "fosforo": 20,
    "potassio": 40,
    "observacoes": ""
}
```

### Uso de cada estrutura

- **Lista:** conjunto de áreas cadastradas durante a execução.
- **Dicionário:** representa cada área agrícola e seus campos.
- **Tupla:** utilizada para valores fixos, como culturas permitidas e nomes de campos.
- **Tabela de memória:** organização temporária formada pela lista de dicionários manipulada pelo sistema.

---

## 6. Integrantes e responsabilidades

| Integrante | Responsabilidade principal |
|---|---|
| Caio | Organização, integração, revisão e versão final |
| Paulo Vitor | Cadastro e estruturas de dados |
| Kauê Araujo | Consulta, atualização e exclusão |
| Juliana | Arquivos TXT e JSON |
| Cleidimar | Banco de dados Oracle |

A divisão indica a responsabilidade principal de cada integrante, mas todos devem compreender o funcionamento geral da solução.

---

## 7. Como executar o projeto

### 7.1 Clonar o repositório

```bash
git clone https://github.com/Caiobqz/FarmTech-Python-Gestao-Agronegocio.git
cd FarmTech-Python-Gestao-Agronegocio
```

### 7.2 Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 7.3 Executar a aplicação

```bash
python main.py
```

---

## 8. Configuração do Oracle

O projeto usa variáveis de ambiente para evitar que credenciais sejam publicadas no GitHub.

Copie o arquivo de exemplo:

### Windows PowerShell

```powershell
Copy-Item .env.example .env
```

Depois preencha localmente:

```env
ORACLE_USER=seu_usuario
ORACLE_PASSWORD=sua_senha
ORACLE_DSN=seu_dsn
```

**Nunca envie o arquivo `.env` para o GitHub.**

O script de criação da tabela está em:

```text
database/criar_tabelas.sql
```

O teste de conexão pode ser executado com:

```bash
python teste_oracle.py
```

### Situação atual do Oracle

O código de conexão, inserção, consulta e tratamento de erros está implementado. Durante os testes, o servidor Oracle respondeu, porém a conta institucional usada ficou bloqueada (`ORA-28000`). Por isso, a integração ainda precisa ser validada novamente após o desbloqueio da conta.

---

## 9. Arquivos JSON e TXT

### JSON

A opção **6** salva os registros atuais em:

```text
dados/registros.json
```

A opção **7** carrega os registros novamente para a memória.

### TXT

A opção **8** gera um relatório legível em:

```text
dados/relatorio.txt
```

Os arquivos são tratados pelo módulo `src/arquivos.py`.

---

## 10. Testes realizados

O fluxo principal foi testado manualmente com sucesso:

- cadastro de múltiplas áreas;
- validação de cultura por número;
- rejeição de pH acima de 14;
- listagem;
- consulta por ID;
- atualização parcial;
- exclusão;
- salvamento em JSON;
- carregamento do JSON;
- exportação do relatório TXT;
- tratamento de opção de menu inexistente;
- encerramento normal;
- falha de conexão Oracle tratada sem encerrar o programa.

Também existe `teste_arquivos.py`, com verificações de salvamento, carregamento, arquivo ausente, JSON inválido, lista vazia, acentuação e geração do TXT.

---

## 11. Checklist final

Antes da entrega:

- [x] programa inicia;
- [x] menu funciona;
- [x] cadastro funciona;
- [x] consulta funciona;
- [x] atualização funciona;
- [x] exclusão funciona;
- [x] lista é utilizada;
- [x] tupla é utilizada;
- [x] dicionário é utilizado;
- [x] tabela de memória está representada;
- [x] funções recebem parâmetros;
- [x] TXT funciona;
- [x] JSON funciona;
- [ ] Oracle validado com conexão real;
- [x] entradas inválidas são tratadas;
- [x] saídas são legíveis;
- [x] nenhuma credencial real está no repositório;
- [ ] teste final em instalação limpa/outra máquina;
- [ ] versão final identificada para entrega.

---

## 12. Status do projeto

| Etapa | Responsável | Status |
|---|---|---|
| Estrutura inicial | Caio | ✅ Concluída |
| Cadastro | Paulo Vitor | ✅ Concluído |
| Consulta/Atualização/Exclusão | Kauê Araujo | ✅ Concluído |
| TXT e JSON | Juliana | ✅ Concluído |
| Oracle | Cleidimar | 🟡 Implementado, aguardando validação real |
| Integração | Caio / Grupo | ✅ Concluída |
| Testes do fluxo principal | Grupo | ✅ Concluídos |
| README final | Grupo | 🟡 Em revisão |
| Revisão da entrega | Grupo | 🟡 Em andamento |

---

## 13. Segurança

- O arquivo `.env` não deve ser versionado.
- Usuários e senhas reais não devem ser colocados no código.
- O repositório mantém apenas `.env.example`.
- Antes da entrega, o grupo deve conferir `git status` e revisar os arquivos versionados.

---

## 14. Entrega

A versão existente na `main` no momento da entrega será tratada como a versão oficial.

Após a entrega, o grupo deve evitar alterações nessa versão para preservar exatamente o código avaliado.

---

## Integrantes

- Caio
- Paulo Vitor
- Kauê Araujo
- Juliana
- Cleidimar
