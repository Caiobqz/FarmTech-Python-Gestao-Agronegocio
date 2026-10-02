# FarmTech Python — Gestão do Agronegócio

Projeto acadêmico da FIAP para a atividade **Gestão do Agronegócio em Python — Capítulos 3 ao 6**.

> **Prazo da atividade:** 14/10/2026  
> **Formato:** trabalho em grupo  
> **Objetivo deste repositório:** concentrar a versão oficial da entrega e deixar explícito o que cada integrante precisa desenvolver, testar e revisar.

---

## 1. Problema escolhido

O projeto propõe um **sistema de gerenciamento de áreas agrícolas** para ajudar no registro e acompanhamento de dados importantes de uma plantação.

A solução permitirá cadastrar áreas/talhões e armazenar informações como:

- nome da área;
- cultura;
- tamanho em hectares;
- pH;
- nitrogênio (N);
- fósforo (P);
- potássio (K);
- observações do produtor.

O sistema também deverá permitir consultar, atualizar, excluir e exportar esses registros.

### Por que esse problema?

No agronegócio, informações de cultivo podem ficar espalhadas em anotações, planilhas e registros isolados. O projeto busca centralizar esses dados em uma aplicação simples em Python, aplicando diretamente os conteúdos estudados na disciplina.

---

## 2. Requisitos obrigatórios da atividade

O projeto deve demonstrar de forma clara:

- [ ] Funções e procedimentos com passagem de parâmetros
- [ ] Lista
- [ ] Tupla
- [ ] Dicionário
- [ ] Tabela de memória
- [ ] Manipulação de arquivo TXT
- [ ] Manipulação de arquivo JSON
- [ ] Conexão com banco de dados Oracle
- [ ] Validação dos dados digitados pelo usuário
- [ ] Saídas organizadas e fáceis de entender
- [ ] README explicando claramente o problema do agronegócio e a solução
- [ ] Código final disponível no GitHub

---

## 3. Funcionalidades planejadas

O menu principal deverá seguir aproximadamente este fluxo:

```text
====================================
       FARMTECH SOLUTIONS
====================================

1 - Cadastrar área agrícola
2 - Listar áreas
3 - Consultar área
4 - Atualizar área
5 - Excluir área
6 - Registrar dados agrícolas
7 - Exportar relatório TXT
8 - Salvar/carregar dados JSON
9 - Sincronizar/consultar Oracle
0 - Sair
```

O menu poderá ser ajustado durante o desenvolvimento, desde que os requisitos da atividade continuem claros.

---

## 4. Estrutura planejada

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
└── docs/
    └── PLANO_DE_TRABALHO.md
```

---

## 5. Como os dados serão representados

Durante a execução, os registros poderão ser armazenados em uma **lista de dicionários**.

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
    "potassio": 40
}
```

### Onde cada estrutura entra

- **Lista:** conjunto de áreas cadastradas.
- **Dicionário:** dados de cada área.
- **Tupla:** opções fixas ou valores que não devem ser alterados durante a execução.
- **Tabela de memória:** organização temporária dos registros durante a execução do programa.

---

## 6. Divisão inicial do grupo

| Integrante | Responsabilidade principal |
|---|---|
| Caio | Organização, integração, revisão e versão final |
| Paulo Vitor | Cadastro e estruturas de dados |
| Kauê Araujo | Consulta, atualização e exclusão |
| Juliana | Arquivos TXT e JSON |
| Cleidimar | Banco de dados Oracle |

> Todos devem entender o funcionamento geral. A divisão é de responsabilidade principal, não de isolamento.

---

## 7. Ordem correta de desenvolvimento

1. **Preparar o ambiente e clonar o projeto.**
2. **Criar uma branch para a tarefa.**
3. **Implementar cadastro e estruturas de dados.**
4. **Implementar consulta, atualização e exclusão.**
5. **Implementar validações.**
6. **Implementar persistência em JSON.**
7. **Implementar relatório TXT.**
8. **Implementar banco Oracle.**
9. **Integrar todos os módulos.**
10. **Testar entradas corretas e incorretas.**
11. **Revisar o README e a documentação.**
12. **Fazer a revisão final antes da entrega.**

O detalhamento de cada etapa está em [docs/PLANO_DE_TRABALHO.md](docs/PLANO_DE_TRABALHO.md).

---

## 8. Como começar

### Clonar

```bash
git clone https://github.com/Caiobqz/FarmTech-Python-Gestao-Agronegocio.git
cd FarmTech-Python-Gestao-Agronegocio
```

### Atualizar antes de trabalhar

```bash
git checkout main
git pull
```

### Criar uma branch

Exemplo:

```bash
git checkout -b feature/cadastro
```

### Enviar alterações

```bash
git add .
git commit -m "Implementa cadastro de areas agricolas"
git push origin feature/cadastro
```

Depois, abrir um **Pull Request** para a `main`.

Mais regras estão em [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 9. Regra principal do Git

**Não desenvolver diretamente na `main`.**

Fluxo esperado:

```text
main
 ↓
branch da tarefa
 ↓
desenvolvimento
 ↓
teste
 ↓
commit
 ↓
push
 ↓
Pull Request
 ↓
revisão
 ↓
merge na main
```

---

## 10. Testes obrigatórios

O grupo deve testar pelo menos:

### Entradas corretas

- área válida;
- cultura válida;
- números válidos;
- ID existente.

### Entradas incorretas

- letras onde deveria haver número;
- número negativo;
- opção de menu inexistente;
- ID inexistente;
- JSON ausente;
- Oracle indisponível.

O programa não deve encerrar inesperadamente por causa de uma entrada inválida.

---

## 11. Checklist final

Antes da entrega:

- [ ] programa inicia;
- [ ] menu funciona;
- [ ] cadastro funciona;
- [ ] consulta funciona;
- [ ] atualização funciona;
- [ ] exclusão funciona;
- [ ] lista é utilizada;
- [ ] tupla é utilizada;
- [ ] dicionário é utilizado;
- [ ] funções recebem parâmetros;
- [ ] TXT funciona;
- [ ] JSON funciona;
- [ ] Oracle funciona;
- [ ] entradas inválidas são tratadas;
- [ ] README está atualizado;
- [ ] nenhum login, senha ou segredo está no GitHub;
- [ ] todos os arquivos necessários estão versionados;
- [ ] versão final foi testada em uma máquina do grupo.

---

## 12. Status do projeto

| Etapa | Responsável | Status |
|---|---|---|
| Estrutura inicial | Caio | ✅ Preparada |
| Cadastro | Paulo Vitor | ⬜ Não iniciado |
| Consulta/Atualização/Exclusão | Kauê Araujo | ⬜ Não iniciado |
| TXT e JSON | Juliana | ⬜ Não iniciado |
| Oracle | Cleidimar | ⬜ Não iniciado |
| Integração | Grupo | ⬜ Não iniciado |
| Testes | Grupo | ⬜ Não iniciado |
| README final | Grupo | 🟡 Em evolução |
| Revisão da entrega | Grupo | ⬜ Não iniciado |

---

## 13. Entrega

A versão existente na `main` no momento da entrega será tratada como a **versão oficial**.

Após a entrega, o grupo deve evitar alterações na versão oficial para preservar exatamente o código avaliado.

---

## Integrantes

- Caio
- Paulo Vitor
- Kauê Araujo
- Juliana
- Cleidimar
