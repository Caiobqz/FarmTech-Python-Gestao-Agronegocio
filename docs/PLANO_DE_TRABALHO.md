# Plano de trabalho do grupo

Este documento transforma a atividade em tarefas pequenas e verificáveis.

## Visão geral

O projeto será concluído em cinco blocos principais:

1. estruturas de dados e cadastro;
2. CRUD;
3. TXT e JSON;
4. Oracle;
5. integração, testes e documentação.

---

# 1. Caio — organização e integração

## Responsabilidades

- manter a estrutura geral do projeto;
- revisar Pull Requests;
- evitar que duas partes incompatíveis sejam integradas;
- manter README e documentação coerentes com o código real;
- executar o teste final antes da entrega.

## Passo a passo

1. Atualizar a `main`.
2. Conferir se cada módulo tem uma responsabilidade clara.
3. Revisar os Pull Requests dos demais integrantes.
4. Testar o projeto após cada merge importante.
5. Anotar erros encontrados.
6. Garantir que todos os requisitos da atividade estejam representados no código.
7. Fazer o teste final em uma instalação limpa ou em outra máquina do grupo.
8. Marcar o commit final usado na entrega.

## Critério de conclusão

- projeto integrado;
- nenhuma funcionalidade principal quebrada;
- README atualizado;
- requisitos conferidos um por um;
- versão final identificada.

---

# 2. Paulo Vitor — cadastro e estruturas de dados

## Objetivo

Criar o núcleo dos registros agrícolas em memória.

## Tarefas

1. Definir a estrutura de um registro.
2. Criar o cadastro de uma área/talhão.
3. Armazenar os registros em uma lista.
4. Representar cada registro por um dicionário.
5. Usar uma tupla em um ponto justificável, por exemplo para culturas permitidas.
6. Chamar as validações em vez de confiar diretamente no `input()`.

## Exemplo de campos

- id;
- nome da área;
- cultura;
- área em hectares;
- pH;
- N;
- P;
- K;
- observações.

## Casos para testar

- cadastro normal;
- nome vazio;
- área negativa;
- letras onde deveria haver número;
- pH inválido;
- cultura fora das opções definidas.

## Critério de conclusão

O cadastro precisa gerar um registro consistente e adicioná-lo à lista sem encerrar o programa em uma entrada inválida.

---

# 3. Kauê Araujo — consulta, atualização e exclusão

## Objetivo

Completar o CRUD da solução.

## Tarefas

1. Listar registros.
2. Consultar por ID.
3. Atualizar registro.
4. Excluir registro.
5. Tratar ID inexistente.
6. Evitar duplicação de lógica.

## Casos para testar

- lista vazia;
- um registro;
- vários registros;
- ID existente;
- ID inexistente;
- atualização parcial;
- exclusão e nova listagem.

## Critério de conclusão

O usuário deve conseguir encontrar, alterar e remover um registro sem corromper os demais dados.

---

# 4. Juliana — arquivos TXT e JSON

## Objetivo

Demonstrar manipulação de arquivos.

## Parte A — JSON

Implementar funções para:

1. salvar a lista de registros em JSON;
2. carregar a lista de registros do JSON;
3. tratar arquivo inexistente;
4. tratar arquivo vazio ou inválido quando possível.

## Parte B — TXT

Gerar um relatório legível para leitura humana.

O TXT deve apresentar os campos com rótulos claros, sem despejar diretamente a representação interna do dicionário.

## Casos para testar

- salvar lista vazia;
- salvar vários registros;
- carregar arquivo existente;
- arquivo inexistente;
- gerar relatório após alterações.

## Critério de conclusão

Os dados devem conseguir sair da memória para JSON e voltar, e o TXT deve ser fácil de ler.

---

# 5. Cleidimar — Oracle

## Objetivo

Demonstrar a conexão do Python com Oracle e persistir dados no banco.

## Tarefas

1. Criar o script SQL.
2. Criar a tabela principal.
3. Configurar a conexão Python.
4. Implementar inserção.
5. Implementar consulta.
6. Se possível, implementar atualização e exclusão.
7. Tratar falha de conexão.

## Segurança

As credenciais reais não podem ser enviadas ao GitHub.

Usar variáveis de ambiente:

```text
ORACLE_USER
ORACLE_PASSWORD
ORACLE_DSN
```

## Casos para testar

- conexão válida;
- credencial inválida;
- banco indisponível;
- inserir registro;
- consultar registro;
- fechar conexão corretamente.

## Critério de conclusão

O grupo precisa conseguir demonstrar uma conexão real com Oracle e operações documentadas.

---

# 6. Integração do menu

Quando os módulos estiverem prontos, o `main.py` deve conectar as funções em um fluxo único.

A lógica deve ser simples:

```text
mostrar menu
→ ler opção
→ validar
→ chamar função do módulo correspondente
→ voltar ao menu
```

Evitar colocar toda a lógica dentro do `main.py`.

---

# 7. Ordem recomendada de merge

1. validações;
2. cadastro;
3. CRUD;
4. JSON/TXT;
5. Oracle;
6. integração;
7. documentação final.

---

# 8. Revisão antes da entrega

Perguntas que o grupo deve conseguir responder com "sim":

- O problema do agronegócio está claro?
- Existe função com parâmetros?
- Existe lista?
- Existe tupla?
- Existe dicionário?
- Existe manipulação de TXT?
- Existe manipulação de JSON?
- Existe conexão Oracle?
- As entradas são validadas?
- A saída é legível?
- O programa não quebra em casos simples de erro?
- O README explica como executar?
- Nenhuma senha foi versionada?
- O commit entregue foi testado?
