# Referência — Estrutura de Dados (FATEC Ourinhos)

Livro base: *Estruturas de Dados e Algoritmos em C* — Deitel & Deitel

## Tópicos implementados (AA01–AA09)

| AA   | Tópico                          | Pontos cobrados em prova                                     |
|------|---------------------------------|--------------------------------------------------------------|
| AA01 | Menu interativo / I/O           | `scanf`/`printf`, `switch`, laços, funções                  |
| AA02 | Vetores, média e variância      | Arrays, ponteiros, aritmética de ponteiros                   |
| AA03 | Aleatoriedade / sorteio         | `rand()`, `srand(time(NULL))`, modulo bias                  |
| AA04 | Structs / estoque               | `typedef struct`, acesso `.` e `->`, structs aninhadas      |
| AA05 | Recursão / potência             | Caso base, caso recursivo, pilha de chamadas, tail recursion |
| AA06 | Lista encadeada simples         | Nó, inserção início/fim/meio, remoção, busca, O(n)          |
| AA07 | Fila (FIFO)                     | Enqueue, dequeue, front, rear, fila circular                |
| AA08 | Pilha (LIFO)                    | Push, pop, peek, underflow, overflow                         |
| AA09 | Lista duplamente enc. circular  | Ponteiro anterior + próximo, remoção O(1) com nó em mão     |

## Tópicos prováveis (próximas AAs)

### Árvore Binária de Busca (BST)

**Invariante:** `esquerda < raiz < direita` em toda subárvore.

**Operações:**
- `inserir(raiz, valor)` — O(log n) médio, O(n) pior caso (árvore degenerada)
- `buscar(raiz, valor)` — O(log n) médio
- `remover(raiz, valor)` — 3 casos: sem filhos, 1 filho, 2 filhos (substitui pelo sucessor in-order)
- Travessias: **in-order** (crescente), **pre-order** (raiz primeiro), **post-order** (raiz por último)

**Código padrão (estrutura):**
```c
typedef struct No {
    int dado;
    struct No *esquerda;
    struct No *direita;
} No;

No* arvore_inserir(No *raiz, int dado);
No* arvore_remover(No *raiz, int dado);
No* arvore_buscar(No *raiz, int dado);
void arvore_in_order(No *raiz);
void arvore_destruir(No *raiz);  // post-order free
```

### Árvore AVL

- BST com rebalanceamento automático
- **Fator de balanceamento** (FB) = altura(direita) - altura(esquerda), deve ser {-1, 0, 1}
- **4 rotações:** Simples Direita (SD), Simples Esquerda (SE), Dupla Direita-Esquerda (DRE), Dupla Esquerda-Direita (DER)
- Inserção/busca/remoção: O(log n) **garantido**

### Hash Table

- Função hash mapeia chave → índice no array
- **Colisão:** duas chaves mapeiam para o mesmo índice
- **Tratamento por encadeamento:** cada posição é uma lista ligada
- **Endereçamento aberto:** sondagem linear, quadrática, hash duplo
- Fator de carga α = n/m; recomendado α < 0.75

### Grafos

- **Representações:** matriz de adjacência O(V²), lista de adjacência O(V+E)
- **BFS:** fila, visita por nível, menor caminho não-ponderado
- **DFS:** pilha (ou recursão), detecta ciclos, componentes conectados

## Padrões de questão de prova FATEC

1. "Escreva a função `lista_remover` para uma lista encadeada simples"
2. "Trace a execução de inserção X na BST abaixo e desenhe o estado final"
3. "Qual a complexidade de busca em lista encadeada? E em BST balanceada?"
4. "Identifique o bug no código abaixo (ponteiro não liberado / acesso a NULL)"
5. "Converta este código iterativo para recursivo"
6. "Qual estrutura usar para implementar desfazer (Ctrl+Z)? Por quê?"
