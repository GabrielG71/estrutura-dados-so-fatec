# CLAUDE.md — Guia de Contexto para IAs

> Este arquivo existe para que qualquer IA (Claude, Copilot, GPT, etc.) entenda
> imediatamente o propósito, estrutura e convenções deste repositório, e saiba
> como ajudar o dono de forma efetiva.

---

## 1. Quem é o dono deste repositório

**Gabriel Gonçalves** — estudante de Análise e Desenvolvimento de Sistemas (ADS)
na **FATEC Ourinhos**, atualmente no **3.º semestre**.

Fora da faculdade, Gabriel trabalha como engenheiro de software com foco em
sistemas backend, sendo fluente em TypeScript, PHP e Python. Ou seja: ele sabe
programar muito bem — o que está aprendendo aqui é a *teoria e prática acadêmica*
de ED e SO, não a lógica básica de programação. Não trate ele como iniciante.

---

## 2. O que é este repositório

Coleção de atividades avaliativas (AAs) e materiais de estudo de duas disciplinas
do 3.º semestre:

| Disciplina            | Natureza   | Linguagem / Formato          |
|-----------------------|------------|------------------------------|
| Estrutura de Dados    | Prática    | C (padrão C99), GCC          |
| Sistemas Operacionais | Teórica    | Dissertativa, PDFs, texto    |

O repositório **não é um projeto de produção**. É um acervo pessoal de estudos e
entregas acadêmicas. O critério de qualidade é: código correto, bem comentado e
que demonstra compreensão do conceito — não necessariamente código production-grade.

---

## 3. Estrutura de diretórios

```
.
├── estrutura-de-dados/
│   ├── aa01/          # Sistema de menu interativo
│   ├── aa02/          # Calculadora de média e variância
│   ├── aa03/          # Simulação de sorteio (loteria)
│   ├── aa04/          # Gerenciamento de estoque (structs)
│   ├── aa05/          # Potência recursiva
│   ├── aa06/          # Lista encadeada simples
│   ├── aa07/          # Fila (FIFO)
│   ├── aa08/          # Pilha (LIFO)
│   ├── aa09/          # Lista duplamente encadeada circular
│   ├── ae/            # Avaliações escritas (PDFs de prova)
│   └── output/        # Executáveis compilados (ignorar para análise de código)
│
└── sistemas-operacionais/
    ├── aa01/          # Fundamentos de SO e instalação de sistemas
    ├── aa02/          # Mainframes e supercomputadores
    ├── aa03/          # Chamadas de sistema (system calls)
    ├── aa04/          # Virtualização e emulação
    ├── aa05/          # Interfaces de linha de comando (CLI)
    ├── aa06/          # Processos, componentes e escalonamento
    ├── aa07/          # Threads, sincronização e modelos de thread
    ├── aa08/          # Condições de corrida e exclusão mútua
    ├── aa09/          # Problemas clássicos: Jantar dos Filósofos, Leitores-Escritores
    └── aa10/          # Deadlocks — condições necessárias e estratégias de tratamento
```

---

## 4. Convenções do repositório

### Estrutura de Dados (C)
- Cada `aa0X/` contém tipicamente um `main.c` e eventualmente arquivos `.h`
- Toda alocação dinâmica usa `malloc`/`calloc`/`realloc` + `free` explícito
- Ponteiros são usados extensivamente — comentar quando a lógica não é trivial
- Novos exercícios devem seguir o padrão: um arquivo por TAD quando aplicável
- Compilar com: `gcc -Wall -Wextra -std=c99 -o output/nome nome.c`
- **Não usar** bibliotecas externas — apenas `<stdio.h>`, `<stdlib.h>`, `<string.h>`, `<time.h>` e similares da libc

### Sistemas Operacionais (Teórico)
- Atividades são dissertativas — respostas em texto corrido, não bullet points rasos
- Cada `aa0X/` contém um arquivo de resposta (`.txt`, `.pdf` ou `.md`)
- Quando for ajudar a redigir: linguagem técnica, objetiva, em português
- Citar conceitos do livro "Sistemas Operacionais Modernos" (Tanenbaum) é bem-vindo

---

## 5. Mapa de conceitos cobertos

### Estrutura de Dados — progressão lógica

```
Fundamentos C (AA01–AA05)
  ├── Funções, fluxo, I/O              → AA01
  ├── Vetores, ponteiros, estatística  → AA02
  ├── Aleatoriedade, arrays            → AA03
  ├── Structs aninhadas                → AA04
  └── Recursão                         → AA05

Estruturas Lineares Dinâmicas (AA06–AA09)
  ├── Lista encadeada simples          → AA06
  ├── Fila (FIFO)                      → AA07
  ├── Pilha (LIFO)                     → AA08
  └── Lista duplamente enc. circular   → AA09

[Próximos tópicos prováveis]
  ├── Árvore Binária de Busca (BST)
  ├── Árvore AVL
  ├── Hash tables
  └── Grafos (BFS/DFS)
```

### Sistemas Operacionais — progressão lógica

```
Conceitos Base (AA01–AA05)
  ├── O que é um SO, tipos, história   → AA01
  ├── Arquiteturas de hardware         → AA02
  ├── Interface kernel ↔ userspace     → AA03
  ├── Virtualização                    → AA04
  └── Shell e CLI                      → AA05

Gerenciamento de Processos (AA06–AA10)
  ├── Processos e escalonamento        → AA06
  ├── Threads e modelos                → AA07
  ├── Condições de corrida / mutex     → AA08
  ├── Problemas clássicos IPC          → AA09
  └── Deadlocks                        → AA10

[Próximos tópicos prováveis]
  ├── Gerenciamento de memória (paginação, segmentação)
  ├── Memória virtual e page fault
  ├── Sistemas de arquivos
  └── Segurança e proteção
```

---

## 6. Como ajudar — instruções específicas por tipo de tarefa

### 6.1 Criar um novo exercício de Estrutura de Dados

Quando Gabriel pedir um novo exercício de ED:

1. **Perguntar** (se não estiver claro): qual estrutura, qual operação, se é avaliativa ou prática livre
2. Gerar o código em **C99**, com:
   - Cabeçalho comentado (propósito do arquivo)
   - TAD bem definido em struct
   - Funções com nomes descritivos em português ou inglês — ser consistente
   - `free()` em toda memória alocada antes de encerrar
   - `main()` com menu interativo quando aplicável
3. Indicar a complexidade de tempo das operações principais (O(1), O(n), etc.)
4. Sugerir onde colocar no repositório (`estrutura-de-dados/aa0X/`)

**Estruturas ainda não implementadas e que podem aparecer:**
- Árvore Binária de Busca (BST) com inserção, busca, remoção, travessias
- Árvore AVL com rotações simples e duplas
- Hash table com tratamento de colisão (encadeamento ou endereçamento aberto)
- Grafo com lista de adjacência + BFS + DFS

### 6.2 Criar um novo exercício de Sistemas Operacionais

Quando Gabriel pedir ajuda com uma atividade de SO:

1. Identificar o tema (ver mapa acima)
2. Redigir resposta dissertativa em português, técnica e estruturada
3. Explicar **o porquê** dos conceitos, não só a definição
4. Quando cabível, usar exemplos concretos (ex: mutex no Linux com `pthread_mutex_t`)
5. Referenciar Tanenbaum quando for conceito canônico

### 6.3 Criar PDF explicativo de matéria

Quando Gabriel pedir um PDF de estudo:

- Estruturar como: Conceito → Motivação → Como funciona → Exemplo → Complexidade/Implicações
- Incluir diagramas textuais (ASCII art) para estruturas de dados quando útil
- Para SO: incluir fluxogramas de estados (processo: new → ready → running → waiting → terminated)
- Nível: intermediário — Gabriel já sabe programar, não precisa de "o que é uma variável"
- Formato sugerido: Markdown renderizável ou LaTeX se quiser PDF bonito

### 6.4 Simulados e questões de prova

Quando Gabriel pedir simulado:

**Para ED:**
- Misturar questões conceituais (complexidade, diferença entre estruturas) com questões de código (completar, corrigir ou escrever)
- Incluir questões sobre ponteiros e alocação dinâmica — é sempre cobrado na FATEC
- Gabarito separado no final

**Para SO:**
- Questões dissertativas curtas (3–5 linhas de resposta esperada)
- Questões de múltipla escolha sobre conceitos (escalonamento, estados de processo, etc.)
- Pelo menos 1 questão sobre problemas clássicos (Filósofos, Leitores-Escritores, Barbeiro)
- Gabarito comentado

### 6.5 Tirar dúvidas

- Responder direto e sem rodeios — Gabriel não precisa de contexto introdutório
- Se a dúvida for sobre ponteiro/memória: mostrar diagrama de memória (ASCII) quando ajudar
- Se a dúvida for sobre SO: conectar com exemplos reais do Linux sempre que possível
- Se a dúvida envolver código do repositório: pedir o trecho ou o arquivo antes de especular

---

## 7. Estilo de código esperado para C

```c
// Cabeçalho obrigatório
// AA06 - Lista Encadeada Simples
// Autor: Gabriel Gonçalves
// FATEC Ourinhos — Estrutura de Dados

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definição do nó
typedef struct No {
    int dado;
    struct No *proximo;
} No;

// Definição da lista
typedef struct {
    No *cabeca;
    int tamanho;
} Lista;

// Protótipos
Lista* lista_criar(void);
void   lista_inserir_inicio(Lista *lista, int dado);
void   lista_remover(Lista *lista, int dado);
void   lista_imprimir(const Lista *lista);
void   lista_destruir(Lista *lista);

int main(void) {
    Lista *lista = lista_criar();
    // ...
    lista_destruir(lista);
    return 0;
}
```

Pontos importantes:
- `typedef struct` para nomear limpo
- Funções prefixadas pelo nome da estrutura (`lista_`, `pilha_`, `fila_`, `arvore_`)
- Parâmetros `const` quando a função não modifica
- Retornar `EXIT_SUCCESS` / `EXIT_FAILURE` ou simplesmente `0`

---

## 8. O que NÃO fazer

- **Não simplificar demais**: Gabriel sabe programar — não explique o que é um `for`
- **Não ignorar `free()`**: todo `malloc` precisa de `free` correspondente
- **Não usar C++**: o curso é em C puro
- **Não inventar atividades**: se pedir AA10 de ED e não existir, deixar claro que é nova
- **Não gerar código sem comentários**: o professor avalia comentários
- **Não confundir as disciplinas**: SO é teórico/dissertativo, ED é código C

---

## 9. Referências canônicas usadas na disciplina

| Disciplina | Livro Principal |
|---|---|
| Estrutura de Dados | "Estruturas de Dados e Algoritmos em C" — Paul J. Deitel / Herbert Deitel |
| Sistemas Operacionais | "Sistemas Operacionais Modernos" — Andrew S. Tanenbaum (4.ª edição) |

---

## 10. Contexto adicional

- FATEC Ourinhos é interior de SP — o curso de ADS tem foco prático
- As provas de ED tendem a cobrar implementação na mão (papel e caneta), então o foco em entender o funcionamento real das estruturas importa mais do que memorizar API
- SO é predominantemente teórico com questões dissertativas baseadas em Tanenbaum
- O repositório pode crescer para incluir novas AAs conforme o semestre avança

---

*Última atualização: março de 2026*
*Gerado com base na análise do repositório GabrielG71/estrutura-dados-so-fatec*