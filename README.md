# Exercícios Práticos de Lógica de Programação em Python

## Identificação
- **Estudante:** Davi Antonio Albano.
- **Turma:** DSM3-25.
- **Unidade Curricular:** Programação de Aplicativos.
- **Curso:** Técnico em Desenvolvimento de Sistemas — Integrado ao Ensino Médio.
- **Docente:** Ewerton de Oliveira Cercal.
- **Instituição:** SENAI.
- **Repositório:** Privado com colaborador adicionado (`ProfCercal`).
---

## Descrição
Neste repositório, você encontra 25 desafios práticos de lógica de programação resolvidos em Python, todos acompanhados de explicações detalhadas. O material foi desenvolvido para conectar a teoria acadêmica às exigências do mercado, cobrindo tópicos fundamentais como fluxo de entrada/saída, tomadas de decisão condicionais, laços (while e for) e estruturas de dados em listas. Além do código, o projeto se destaca pela organização limpa de pastas, histórico de commits via Git e padronização na documentação.

---

##  Tecnologia Utilizada
- **Linguagem de Programação:** Python.
- **Versão do Python:** `Python 3.9.6` (compatível com Python 3.9+).
- **Sistema de Controle de Versão:** Git 2.54.0.
- **Hospedagem e Colaboração:** GitHub.

Para verificar a versão do interpretador Python em seu terminal, execute:
```bash
python3 --version
```

---
 
##  Como Executar

### Pré-requisitos
Certifique-se de que o Python 3 esteja instalado no seu computador.

### 1. Clonar o repositório
Abra o terminal e execute o comando:
```bash
git clone https://github.com/DaviAntonioAlbano-hash/exercicios-python.git
```

### 2. Acessar a pasta do projeto
```bash
cd exercicios-python
```
---

## Índice dos Exercícios


## Parte 1 — Variáveis, Entrada e Saída

- **parte1-variaveis/ex01.py:** Declara variáveis com nome e idade e exibe cada informação em uma linha separada.
- **parte1-variaveis/ex02.py:** Solicita dois números ao usuário, converte as entradas e exibe a soma calculada.
- **parte1-variaveis/ex03.py:** Solicita o raio de um círculo e calcula sua área utilizando o valor de pi fixado em 3.14159.
- **parte1-variaveis/ex04.py:** Converte uma temperatura lida em graus Celsius para a escala Fahrenheit pela fórmula F = C * 9 / 5 + 32.
- **parte1-variaveis/ex05.py:** Lê o preço unitário e a quantidade comprada de um produto, calculando o valor total formatado com duas casas decimais.

## Parte 2 — Condicionais

- **parte2-condicionais/ex06.py:** Recebe um número inteiro e informa com precisão se ele é par ou ímpar.
- **parte2-condicionais/ex07.py:** Compara dois números e exibe qual é o maior ou informa se ambos são estritamente iguais.
- **parte2-condicionais/ex08.py:** Analisa um valor numérico informando se ele é positivo, negativo ou exatamente igual a zero.
- **parte2-condicionais/ex09.py:** Avalia a média escolar com tratamento de fronteiras (>= 6 Aprovado, 4 a 5.9 Recuperação, < 4 Reprovado).
- **parte2-condicionais/ex10.py:** Verifica a idade de uma pessoa informando se ela já possui idade suficiente para votar (mínimo 16 anos).

## Parte 3 — Repetição com while

- **parte3-while/ex11.py:** Exibe a sequência de números inteiros de 1 a 10, um por linha, utilizando laço while.
- **parte3-while/ex12.py:** Acumula valores inseridos pelo usuário em um laço while até a entrada da condição de parada 0, exibindo a soma final.
- **parte3-while/ex13.py:** Valida repetidamente a entrada de uma senha até que a palavra-chave "senai123" seja digitada, liberando o acesso.
- **parte3-while/ex14.py:** Exibe a tabuada completa de multiplicação de 1 a 10 para um determinado número informado pelo usuário.
- **parte3-while/ex15.py:** Lê sucessivos números até que o valor 0 seja inserido e contabiliza quantos números estritamente positivos foram digitados.

## Parte 4 — Repetição com for

- **parte4-for/ex16.py:** Percorre a faixa de 1 a 20 utilizando laço for com função geradora range, exibindo cada número em uma linha.
- **parte4-for/ex17.py:** Imprime apenas os números pares de 2 a 20 aplicando parâmetros de passo (step = 2) no range.
- **parte4-for/ex18.py:** Calcula e apresenta o somatório total de todos os números inteiros compreendidos no intervalo de 1 a 100.
- **parte4-for/ex19.py:** Calcula o fatorial de um número natural fornecido utilizando multiplicação iterativa controlada por for.
- **parte4-for/ex20.py:** Executa uma contagem regressiva de 10 até 1 utilizando passo negativo no range e finaliza exibindo a mensagem "Fim".

## Parte 5 — Listas

- **parte5-listas/ex21.py:** Cria uma lista contendo cinco números e itera sobre a coleção exibindo cada elemento individualmente.
- **parte5-listas/ex22.py:** Percorre iterativamente a lista de números do exercício anterior calculando o somatório total de seus elementos.
- **parte5-listas/ex23.py:** Determina o maior valor contido na lista inicializando a variável de comparação no primeiro índice da coleção.
- **parte5-listas/ex24.py:** Percorre a lista pré-definida [5, 12, 8, 20, 3, 15] e contabiliza quantos itens possuem valor estritamente superior a 10.
- **parte5-listas/ex25.py:** Exibe a lista [3, 7, 1, 9, 4] em ordem inversa utilizando controle explícito de índices decrementais, sem funções prontas.

---