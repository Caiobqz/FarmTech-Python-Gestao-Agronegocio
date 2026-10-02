# Guia de contribuição

Este arquivo define como o grupo deve trabalhar no repositório sem sobrescrever o trabalho dos outros.

## 1. Antes de começar

Sempre execute:

```bash
git checkout main
git pull
```

Não comece uma tarefa em uma cópia desatualizada do projeto.

## 2. Crie uma branch para sua tarefa

Exemplos:

```bash
git checkout -b feature/cadastro
git checkout -b feature/crud
git checkout -b feature/arquivos
git checkout -b feature/oracle
git checkout -b feature/integracao
```

Use uma branch por responsabilidade.

## 3. Trabalhe em pequenas etapas

Evite fazer dezenas de alterações antes do primeiro commit.

Exemplo de sequência:

```bash
git add .
git commit -m "Adiciona validacao de area"
```

Depois:

```bash
git push origin SUA-BRANCH
```

## 4. Abra um Pull Request

O Pull Request deve explicar:

- o que foi implementado;
- quais arquivos foram alterados;
- como foi testado;
- o que ainda falta.

## 5. Regra de revisão

Antes do merge:

- execute o programa;
- teste a funcionalidade nova;
- confirme que as funcionalidades antigas continuam funcionando;
- procure credenciais ou dados sensíveis;
- verifique se a documentação precisa ser atualizada.

## 6. Conflitos

Se houver conflito:

1. não apague o código do colega automaticamente;
2. leia os dois lados do conflito;
3. entenda qual parte é mais atual;
4. conversem antes de descartar uma alteração;
5. rode o programa novamente depois de resolver.

## 7. O que não deve ir para o GitHub

Nunca versionar:

- senha do Oracle;
- usuário real do banco, quando não for necessário;
- tokens;
- arquivos `.env` reais;
- dados pessoais desnecessários.

Use o arquivo `.env.example` apenas como modelo.

## 8. Padrão de commits

Prefira mensagens como:

```text
Implementa cadastro de areas agricolas
Adiciona validacao de valores numericos
Implementa persistencia em JSON
Adiciona consulta por ID
Adiciona conexao inicial com Oracle
Corrige exclusao de registro
Atualiza README com instrucoes do projeto
```

Evite:

```text
teste
coisa
ajuste
final
final2
agora vai
```
