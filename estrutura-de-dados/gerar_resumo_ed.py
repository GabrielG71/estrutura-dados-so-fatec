#!/usr/bin/env python3
"""
Gera PDF de resumo completo de Estrutura de Dados — FATEC Ourinhos
Cobre AA01–AA09 com foco nas estruturas lineares dinamicas e simulado de prova
"""
import sys
sys.path.insert(0, '.claude/skills/fatec-estudo-pdf/scripts')
from gerar_pdf import gerar_pdf

dados = {
  "topico": "Resumo Completo para Prova",
  "disciplina": "Estrutura de Dados",
  "data": "Marco 2026",

  "secoes": [

    # ────────────────────────────────────────────────────────────
    # SECAO 1 — Fundamentos: Ponteiros e Alocacao Dinamica
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "1. Ponteiros e Alocacao Dinamica em C",
      "conteudo": [
        {"tipo": "texto", "body":
          "Ponteiro e uma variavel que armazena um endereco de memoria. E o mecanismo "
          "central de todas as estruturas dinamicas em C: sem ponteiros nao ha listas "
          "encadeadas, filas, pilhas ou arvores. Dominar ponteiros significa entender "
          "o modelo de memoria — stack vs. heap — e o ciclo malloc/free."},

        {"tipo": "subtitulo", "body": "Stack vs. Heap"},
        {"tipo": "diagrama", "body":
          "  Stack (automatico)          Heap (dinamico)\n"
          "  +-------------------+       +-------------------+\n"
          "  | int x = 10;       |       | malloc(sizeof(No))|  <-- voce gerencia\n"
          "  | char buf[64];     |       | calloc(n, size)   |\n"
          "  | No *ptr;  (8 B)   |------>| No { dado, *prox }|\n"
          "  +-------------------+       +-------------------+\n"
          "  Liberado ao sair            Liberado SOMENTE via free()\n"
          "  da funcao (automatico)      Vazamento se esquecer!",
          "legenda": "Figura 1 — Stack (local/automatico) vs. Heap (dinamico, controlado pelo programador)"},

        {"tipo": "subtitulo", "body": "Operacoes essenciais com ponteiros"},
        {"tipo": "codigo", "body":
          "int valor = 42;\n"
          "int *ptr = &valor;       // & = endereco de\n"
          "printf(\"%d\\n\", *ptr); // * = desreferenciar (acessar o valor)\n\n"
          "// Alocacao dinamica\n"
          "typedef struct No {\n"
          "    int dado;\n"
          "    struct No *proximo;\n"
          "} No;\n\n"
          "No *novo = malloc(sizeof(No));  // aloca no heap\n"
          "if (novo == NULL) { /* sem memoria */ exit(1); }\n"
          "novo->dado    = 10;             // -> eh (*novo).dado\n"
          "novo->proximo = NULL;\n"
          "free(novo);                     // devolve ao SO — OBRIGATORIO",
          "legenda": "Codigo 1 — Ponteiro, dereferenciamento e ciclo malloc/free"},

        {"tipo": "dica", "body":
          "Regra de ouro: todo malloc tem um free correspondente. "
          "Ponteiro apos free deve ser setado a NULL para evitar uso acidental (dangling pointer). "
          "Acesso a NULL gera segfault — valide sempre o retorno do malloc."},

        {"tipo": "subtitulo", "body": "Complexidade das estruturas — visao geral"},
        {"tipo": "tabela",
         "cabecalho": ["Estrutura", "Acesso", "Busca", "Insercao (inicio)", "Insercao (fim)", "Remocao"],
         "linhas": [
           ["Array estatico",      "O(1)", "O(n)", "O(n) shift", "O(1) amortizado", "O(n) shift"],
           ["Lista encadeada",     "O(n)", "O(n)", "O(1)",       "O(1) c/ ptr fim", "O(n) busca + O(1)"],
           ["Fila (FIFO)",         "O(n)", "O(n)", "N/A",        "O(1) enqueue",    "O(1) dequeue"],
           ["Pilha (LIFO)",        "O(n)", "O(n)", "O(1) push",  "N/A",             "O(1) pop"],
           ["Lista dupla circular","O(n)", "O(n)", "O(1)",       "O(1)",            "O(1) com no em maos"],
           ["BST (media)",         "O(n)", "O(log n)", "O(log n)", "O(log n)",      "O(log n)"],
         ]},
      ]
    },

    # ────────────────────────────────────────────────────────────
    # SECAO 2 — Lista Encadeada Simples (AA06)
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "2. Lista Encadeada Simples (AA06)",
      "conteudo": [
        {"tipo": "texto", "body":
          "Lista encadeada simples e uma sequencia de nos onde cada no contem um dado e "
          "um ponteiro para o proximo no. O ultimo no aponta para NULL. Diferente do array, "
          "os elementos nao ficam em posicoes contiguas de memoria — a conexao e feita pelos "
          "ponteiros. Isso torna insercao e remocao O(1) quando se tem o no anterior, "
          "mas busca O(n) pois nao ha acesso direto por indice."},

        {"tipo": "diagrama", "body":
          "  inicio                              fim\n"
          "    |                                  |\n"
          "    v                                  v\n"
          "  +------+------+   +------+------+   +------+------+\n"
          "  | 'W'  |  *---+-->| 'e'  |  *---+-->| 'l'  | NULL |\n"
          "  +------+------+   +------+------+   +------+------+\n"
          "    No              No                No",
          "legenda": "Figura 2 — Lista encadeada simples com ponteiros inicio e fim"},

        {"tipo": "subtitulo", "body": "Implementacao: insercao no final"},
        {"tipo": "codigo", "body":
          "void inserir(Lista *lista, char c) {\n"
          "    No *novo = malloc(sizeof(No));\n"
          "    novo->dado    = c;\n"
          "    novo->proximo = NULL;\n\n"
          "    if (lista->inicio == NULL) {   // lista vazia\n"
          "        lista->inicio = novo;\n"
          "        lista->fim    = novo;\n"
          "    } else {\n"
          "        lista->fim->proximo = novo; // encadeia no fim\n"
          "        lista->fim          = novo; // atualiza ponteiro fim\n"
          "    }\n"
          "}",
          "legenda": "Codigo 2 — Insercao no final: O(1) porque guardamos ponteiro para o fim"},

        {"tipo": "subtitulo", "body": "Implementacao: remocao de elemento especifico"},
        {"tipo": "codigo", "body":
          "void remover(Lista *lista, char c) {\n"
          "    if (lista->inicio == NULL) return;\n\n"
          "    // Caso especial: elemento esta no inicio\n"
          "    if (lista->inicio->dado == c) {\n"
          "        No *temp      = lista->inicio;\n"
          "        lista->inicio = lista->inicio->proximo;\n"
          "        if (lista->inicio == NULL) lista->fim = NULL;\n"
          "        free(temp);\n"
          "        return;\n"
          "    }\n\n"
          "    // Percorre buscando o anterior ao alvo\n"
          "    No *anterior = lista->inicio;\n"
          "    No *atual    = lista->inicio->proximo;\n"
          "    while (atual != NULL) {\n"
          "        if (atual->dado == c) {\n"
          "            anterior->proximo = atual->proximo;  // desencadeia\n"
          "            if (atual == lista->fim) lista->fim = anterior;\n"
          "            free(atual);                         // libera\n"
          "            return;\n"
          "        }\n"
          "        anterior = atual;\n"
          "        atual    = atual->proximo;\n"
          "    }\n"
          "}",
          "legenda": "Codigo 3 — Remocao por valor: O(n) busca + O(1) desencadeamento"},

        {"tipo": "dica", "body":
          "Ponto critico da remocao: voce precisa do NO ANTERIOR para ajustar o ponteiro "
          "proximo. Por isso percorre com dois ponteiros (anterior + atual). "
          "Trate sempre o caso especial do primeiro elemento separadamente."},
      ]
    },

    # ────────────────────────────────────────────────────────────
    # SECAO 3 — Fila FIFO (AA07)
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "3. Fila — FIFO (AA07)",
      "conteudo": [
        {"tipo": "texto", "body":
          "Fila e uma estrutura FIFO (First-In, First-Out): o primeiro elemento a entrar "
          "e o primeiro a sair. Analogia real: fila de banco, fila de impressao, BFS em grafos. "
          "Duas operacoes fundamentais: enqueue (inserir no fim) e dequeue (remover do inicio). "
          "Ambas sao O(1) quando se mantem ponteiros para inicio e fim."},

        {"tipo": "diagrama", "body":
          "  ENQUEUE (entrada)               DEQUEUE (saida)\n"
          "        |                              |\n"
          "        v                              v\n"
          "  fim -->[50]->[40]->[30]->[20]->[10]<-- inicio\n\n"
          "  Estado apos enqueue(60):\n"
          "  fim -->[60]->[50]->[40]->[30]->[20]->[10]<-- inicio\n\n"
          "  Estado apos dequeue() retorna 10:\n"
          "  fim -->[60]->[50]->[40]->[30]->[20]<-- inicio",
          "legenda": "Figura 3 — Fila: entrada pelo fim, saida pelo inicio"},

        {"tipo": "subtitulo", "body": "Implementacao"},
        {"tipo": "codigo", "body":
          "typedef struct No   { int dado; struct No *proximo; } No;\n"
          "typedef struct Fila { No *inicio; No *fim; int tamanho; } Fila;\n\n"
          "// Enqueue: O(1)\n"
          "void enfileirar(Fila *fila, int valor) {\n"
          "    No *novo = malloc(sizeof(No));\n"
          "    novo->dado    = valor;\n"
          "    novo->proximo = NULL;\n"
          "    if (fila->inicio == NULL) { fila->inicio = novo; fila->fim = novo; }\n"
          "    else { fila->fim->proximo = novo; fila->fim = novo; }\n"
          "    fila->tamanho++;\n"
          "}\n\n"
          "// Dequeue: O(1)\n"
          "int desenfileirar(Fila *fila) {\n"
          "    if (fila->inicio == NULL) return -1;  // fila vazia\n"
          "    No  *removido = fila->inicio;\n"
          "    int  valor    = removido->dado;\n"
          "    fila->inicio  = fila->inicio->proximo;\n"
          "    if (fila->inicio == NULL) fila->fim = NULL;\n"
          "    free(removido);\n"
          "    fila->tamanho--;\n"
          "    return valor;\n"
          "}",
          "legenda": "Codigo 4 — Fila com lista encadeada: enqueue e dequeue O(1)"},

        {"tipo": "subtitulo", "body": "Quando usar Fila?"},
        {"tipo": "lista", "items": [
          "BFS (Busca em Largura) em grafos: processa vizinhos nivel por nivel",
          "Escalonamento de processos Round-Robin: fila de prontos",
          "Buffer de impressao, requisicoes de rede: ordem de chegada",
          "Simulacao de filas de atendimento (bancos, call centers)",
        ]},
      ]
    },

    # ────────────────────────────────────────────────────────────
    # SECAO 4 — Pilha LIFO (AA08)
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "4. Pilha — LIFO (AA08)",
      "conteudo": [
        {"tipo": "texto", "body":
          "Pilha e uma estrutura LIFO (Last-In, First-Out): o ultimo elemento inserido "
          "e o primeiro a ser removido. Analogia: pilha de pratos, pilha de chamadas "
          "de funcoes (call stack). Operacoes: push (empilhar no topo), pop (desempilhar "
          "do topo), peek/top (consultar topo sem remover). Todas O(1)."},

        {"tipo": "diagrama", "body":
          "  PUSH 'SP'   PUSH 'RJ'   PUSH 'MG'   POP         PEEK\n"
          "  +---------+ +---------+ +---------+ +---------+ +---------+\n"
          "  | topo    | | topo    | | topo    | | topo    | | topo    |\n"
          "  |  [SP]   | |  [RJ]   | |  [MG]<--| |  [RJ]<--| |  [RJ]  |\n"
          "  |         | |  [SP]   | |  [RJ]   | |  [SP]   | |  [SP]   |\n"
          "  |         | |         | |  [SP]   | |         | |         |\n"
          "  +---------+ +---------+ +---------+ +---------+ +---------+\n"
          "                                        retorna MG  retorna RJ\n"
          "                                        sem remover",
          "legenda": "Figura 4 — Estado da pilha apos push/pop/peek"},

        {"tipo": "subtitulo", "body": "Implementacao"},
        {"tipo": "codigo", "body":
          "typedef struct No   { char dado[3]; struct No *proximo; } No;\n"
          "typedef struct Pilha { No *topo; int tamanho; } Pilha;\n\n"
          "// Push: O(1) — insere como novo topo\n"
          "void Push(Pilha *pilha, const char *uf) {\n"
          "    No *novo = malloc(sizeof(No));\n"
          "    strncpy(novo->dado, uf, 2);\n"
          "    novo->dado[2]  = '\\0';\n"
          "    novo->proximo  = pilha->topo;  // aponta para o topo atual\n"
          "    pilha->topo    = novo;          // novo vira o topo\n"
          "    pilha->tamanho++;\n"
          "}\n\n"
          "// Pop: O(1) — remove e retorna o topo\n"
          "char *Pop(Pilha *pilha) {\n"
          "    if (pilha->topo == NULL) return NULL;  // underflow\n"
          "    No   *removido = pilha->topo;\n"
          "    static char valor[3];\n"
          "    strncpy(valor, removido->dado, 3);\n"
          "    pilha->topo = pilha->topo->proximo;\n"
          "    free(removido);\n"
          "    pilha->tamanho--;\n"
          "    return valor;\n"
          "}",
          "legenda": "Codigo 5 — Pilha com lista encadeada: push e pop O(1)"},

        {"tipo": "subtitulo", "body": "Quando usar Pilha?"},
        {"tipo": "lista", "items": [
          "Ctrl+Z (desfazer): operacoes empilhadas, desfeitas na ordem inversa",
          "Avaliacao de expressoes aritmeticas (notacao polonesa reversa — RPN)",
          "DFS (Busca em Profundidade) em grafos: pilha explicita ou recursao (call stack implicita)",
          "Verificacao de parenteses balanceados: push '(', pop ao encontrar ')'",
          "Chamadas de funcao recursivas: o proprio processador usa a call stack",
        ]},

        {"tipo": "dica", "body":
          "Diferenca chave Pilha vs. Fila: pilha inverte a ordem (LIFO), fila preserva (FIFO). "
          "Para implementar 'desfazer', use pilha. Para processar por ordem de chegada, use fila."},
      ]
    },

    # ────────────────────────────────────────────────────────────
    # SECAO 5 — Lista Duplamente Encadeada Circular (AA09)
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "5. Lista Duplamente Encadeada Circular (AA09)",
      "conteudo": [
        {"tipo": "texto", "body":
          "Cada no possui dois ponteiros: proximo (avanca) e anterior (retrocede). "
          "O ultimo no aponta de volta para o primeiro (circular), formando um anel. "
          "Isso permite: travessia nos dois sentidos, remocao em O(1) quando se tem o no "
          "alvo (sem precisar do anterior), e acesso eficiente ao fim sem percorrer a lista."},

        {"tipo": "diagrama", "body":
          "  inicio                                        fim\n"
          "    |                                             |\n"
          "    v                                             v\n"
          "  +----------+    +----------+    +----------+\n"
          "  | ant | P1 |    | ant | P2 |    | ant | P3 |\n"
          "  | dat |    |    | dat |    |    | dat |    |\n"
          "  | prx |  --+--> | prx |  --+--> | prx |  --+-->\n"
          "  +----------+    +----------+    +----------+   |\n"
          "  ^    ^                                ^         |\n"
          "  |    +---<---<---<---<---<---<---<---<+         |\n"
          "  +---<---<---<---<---<---<---<---<---<-----------+\n"
          "  (fim->proximo aponta para inicio, inicio->anterior aponta para fim)",
          "legenda": "Figura 5 — Lista duplamente encadeada circular"},

        {"tipo": "subtitulo", "body": "Vantagem: remocao O(1) com o no em maos"},
        {"tipo": "codigo", "body":
          "// Com o ponteiro 'alvo' em maos, remocao e O(1):\n"
          "void removerNo(Lista *lista, No *alvo) {\n"
          "    if (lista->tamanho == 1) {\n"
          "        lista->inicio = NULL;\n"
          "        lista->fim    = NULL;\n"
          "    } else {\n"
          "        alvo->anterior->proximo = alvo->proximo;\n"
          "        alvo->proximo->anterior = alvo->anterior;\n"
          "        if (alvo == lista->inicio) lista->inicio = alvo->proximo;\n"
          "        if (alvo == lista->fim)    lista->fim    = alvo->anterior;\n"
          "    }\n"
          "    free(alvo);\n"
          "    lista->tamanho--;\n"
          "}",
          "legenda": "Codigo 6 — Remocao O(1): ajusta os 4 ponteiros vizinhos"},

        {"tipo": "subtitulo", "body": "Insercao na lista circular"},
        {"tipo": "codigo", "body":
          "void inserirElemento(Lista *lista, int cod, float desconto) {\n"
          "    No *novo = malloc(sizeof(No));\n"
          "    novo->dado.cod_produto = cod;\n"
          "    novo->dado.desconto    = desconto;\n\n"
          "    if (lista->inicio == NULL) {          // primeiro no\n"
          "        novo->proximo  = novo;            // aponta para si mesmo\n"
          "        novo->anterior = novo;\n"
          "        lista->inicio  = novo;\n"
          "        lista->fim     = novo;\n"
          "    } else {                              // encadeia antes do inicio\n"
          "        novo->anterior          = lista->fim;\n"
          "        novo->proximo           = lista->inicio;\n"
          "        lista->fim->proximo     = novo;\n"
          "        lista->inicio->anterior = novo;\n"
          "        lista->fim              = novo;\n"
          "    }\n"
          "    lista->tamanho++;\n"
          "}",
          "legenda": "Codigo 7 — Insercao: ajuste dos 4 links circulares"},

        {"tipo": "subtitulo", "body": "Travessia circular: cuidado com o loop"},
        {"tipo": "codigo", "body":
          "// Percorre usando do-while para incluir o inicio\n"
          "void imprimirLista(Lista *lista) {\n"
          "    if (lista->inicio == NULL) return;\n"
          "    No *atual = lista->inicio;\n"
          "    do {\n"
          "        printf(\"Cod: %d | %.2f%%\\n\",\n"
          "               atual->dado.cod_produto,\n"
          "               atual->dado.desconto);\n"
          "        atual = atual->proximo;\n"
          "    } while (atual != lista->inicio);  // para quando volta ao inicio\n"
          "}",
          "legenda": "Codigo 8 — Travessia circular com do-while"},

        {"tipo": "tabela",
         "cabecalho": ["Operacao", "Lista Simples", "Lista Dupla Circular"],
         "linhas": [
           ["Insercao no inicio", "O(1)", "O(1)"],
           ["Insercao no fim", "O(1) com ptr fim", "O(1) com ptr fim"],
           ["Remocao com no em maos", "O(n) — precisa do anterior", "O(1) — tem ponteiro anterior"],
           ["Remocao por valor", "O(n)", "O(n) busca + O(1) remocao"],
           ["Travessia invertida", "Impossivel", "O(n) — percorre via anterior"],
           ["Memoria por no", "dado + 1 ponteiro", "dado + 2 ponteiros"],
         ]},
      ]
    },

    # ────────────────────────────────────────────────────────────
    # SECAO 6 — Recursao (AA05)
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "6. Recursao e a Pilha de Chamadas",
      "conteudo": [
        {"tipo": "texto", "body":
          "Uma funcao recursiva e aquela que chama a si mesma para resolver um subproblema "
          "menor. Toda funcao recursiva precisa de: (1) caso base — condicao de parada que "
          "nao faz chamada recursiva; (2) caso recursivo — reduz o problema e chama a funcao "
          "com parametro menor. Sem caso base, a recursao nunca para (stack overflow)."},

        {"tipo": "codigo", "body":
          "// Potencia recursiva: base^exp\n"
          "long long potencia(long long base, int exp) {\n"
          "    if (exp == 0) return 1;               // caso base\n"
          "    return base * potencia(base, exp - 1); // caso recursivo\n"
          "}\n\n"
          "// Trace de potencia(2, 4):\n"
          "// potencia(2,4) = 2 * potencia(2,3)\n"
          "//               = 2 * 2 * potencia(2,2)\n"
          "//               = 2 * 2 * 2 * potencia(2,1)\n"
          "//               = 2 * 2 * 2 * 2 * potencia(2,0)\n"
          "//               = 2 * 2 * 2 * 2 * 1 = 16",
          "legenda": "Codigo 9 — Potencia recursiva e trace de execucao"},

        {"tipo": "subtitulo", "body": "A Call Stack durante recursao"},
        {"tipo": "diagrama", "body":
          "  Chamada potencia(2, 3):\n\n"
          "  +--------------------+  <- topo da stack\n"
          "  | potencia(2, 0)     |  retorna 1\n"
          "  +--------------------+\n"
          "  | potencia(2, 1)     |  aguarda, calcula 2*1=2\n"
          "  +--------------------+\n"
          "  | potencia(2, 2)     |  aguarda, calcula 2*2=4\n"
          "  +--------------------+\n"
          "  | potencia(2, 3)     |  aguarda, calcula 2*4=8\n"
          "  +--------------------+  <- frame original\n"
          "  | main()             |\n"
          "  +--------------------+",
          "legenda": "Figura 6 — Pilha de chamadas (call stack) durante recursao"},

        {"tipo": "dica", "body":
          "Recursao de cauda (tail recursion): quando a chamada recursiva e a ULTIMA "
          "operacao da funcao (sem multiplicar ou somar o resultado). Compiladores otimizam "
          "tail recursion eliminando frames da stack (tail call optimization — TCO). "
          "GCC com -O2 faz isso. A potencia acima NAO e tail recursion pois multiplica apos retornar."},
      ]
    },

    # ────────────────────────────────────────────────────────────
    # SECAO 7 — Arvore Binaria de Busca (proximo topico)
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "7. Arvore Binaria de Busca — BST (Proximo Topico)",
      "conteudo": [
        {"tipo": "texto", "body":
          "BST e uma arvore binaria com a invariante: para todo no, todos os valores "
          "na subarvore esquerda sao menores e todos na direita sao maiores. "
          "Isso permite busca O(log n) no caso medio — mas O(n) no pior caso "
          "(arvore degenerada, inserida em ordem). Arvores AVL e Rubro-Negras "
          "garantem O(log n) no pior caso com rebalanceamento automatico."},

        {"tipo": "diagrama", "body":
          "  Insercao de 50, 30, 70, 20, 40, 60, 80:\n\n"
          "              [50]          <- raiz\n"
          "             /    \\\n"
          "          [30]    [70]\n"
          "          /  \\    /  \\\n"
          "        [20][40][60][80]\n\n"
          "  Invariante: esquerda < no < direita\n"
          "  Travessia in-order: 20 30 40 50 60 70 80 (ordem crescente!)",
          "legenda": "Figura 7 — BST balanceada com 7 nos"},

        {"tipo": "subtitulo", "body": "Estrutura e operacoes em C"},
        {"tipo": "codigo", "body":
          "typedef struct No {\n"
          "    int dado;\n"
          "    struct No *esquerda;\n"
          "    struct No *direita;\n"
          "} No;\n\n"
          "// Insercao: O(log n) medio\n"
          "No* arvore_inserir(No *raiz, int dado) {\n"
          "    if (raiz == NULL) {                     // posicao encontrada\n"
          "        No *novo     = malloc(sizeof(No));\n"
          "        novo->dado      = dado;\n"
          "        novo->esquerda  = NULL;\n"
          "        novo->direita   = NULL;\n"
          "        return novo;\n"
          "    }\n"
          "    if (dado < raiz->dado)\n"
          "        raiz->esquerda = arvore_inserir(raiz->esquerda, dado);\n"
          "    else if (dado > raiz->dado)\n"
          "        raiz->direita  = arvore_inserir(raiz->direita, dado);\n"
          "    // igual: ignorar (sem duplicatas)\n"
          "    return raiz;\n"
          "}\n\n"
          "// Travessia in-order (esq -> raiz -> dir) = ordem crescente\n"
          "void arvore_in_order(No *raiz) {\n"
          "    if (raiz == NULL) return;\n"
          "    arvore_in_order(raiz->esquerda);\n"
          "    printf(\"%d \", raiz->dado);\n"
          "    arvore_in_order(raiz->direita);\n"
          "}\n\n"
          "// Destruir: post-order (libera filhos antes da raiz)\n"
          "void arvore_destruir(No *raiz) {\n"
          "    if (raiz == NULL) return;\n"
          "    arvore_destruir(raiz->esquerda);\n"
          "    arvore_destruir(raiz->direita);\n"
          "    free(raiz);\n"
          "}",
          "legenda": "Codigo 10 — BST: insercao recursiva e travessias"},

        {"tipo": "subtitulo", "body": "As tres travessias"},
        {"tipo": "tabela",
         "cabecalho": ["Travessia", "Ordem de visita", "Resultado na BST do diagrama", "Uso tipico"],
         "linhas": [
           ["In-order",   "Esq -> Raiz -> Dir", "20 30 40 50 60 70 80", "Listar em ordem crescente"],
           ["Pre-order",  "Raiz -> Esq -> Dir", "50 30 20 40 70 60 80", "Serializar/clonar arvore"],
           ["Post-order", "Esq -> Dir -> Raiz", "20 40 30 60 80 70 50", "Destruir arvore (free)"],
         ]},
      ]
    },

    # ────────────────────────────────────────────────────────────
    # SECAO 8 — Comparativo Final
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "8. Guia de Escolha de Estrutura",
      "conteudo": [
        {"tipo": "texto", "body":
          "A escolha da estrutura de dados certa e uma das decisoes de design mais importantes. "
          "Use a tabela abaixo como guia rapido para questoes de prova e situacoes reais."},

        {"tipo": "tabela",
         "cabecalho": ["Cenario / Problema", "Estrutura Ideal", "Justificativa"],
         "linhas": [
           ["Implementar Ctrl+Z (desfazer)", "Pilha (LIFO)", "Operacoes empilhadas, desfeitas na ordem inversa"],
           ["Fila de impressao / atendimento", "Fila (FIFO)", "Ordem de chegada preservada, enqueue/dequeue O(1)"],
           ["Navegar historico do browser (voltar/avancar)", "Lista dupla", "Navegacao em ambos os sentidos O(1)"],
           ["Playlist circular de musicas", "Lista dupla circular", "Volta ao inicio automaticamente"],
           ["Busca rapida por valor", "BST / Hash", "O(log n) BST, O(1) amortizado Hash"],
           ["Remover elemento frequentemente (posicao conhecida)", "Lista dupla", "Remocao O(1) com ponteiro no no"],
           ["Acesso por indice (arr[i])", "Array", "O(1) acesso direto — listas sao O(n)"],
           ["BFS em grafo", "Fila", "Processa nos nivel por nivel"],
           ["DFS em grafo / expressoes", "Pilha", "Profundidade primeiro, LIFO"],
         ]},

        {"tipo": "dica", "body":
          "Questao classica de prova: 'qual estrutura para implementar Ctrl+Z?' Resposta: PILHA. "
          "Cada acao e empilhada (push). Desfazer = pop. Refazer = segunda pilha. "
          "Nunca use array para isso — insercao/remocao no meio e O(n) shift."},
      ]
    },

  ],  # fim secoes

  # ────────────────────────────────────────────────────────────
  # SIMULADO
  # ────────────────────────────────────────────────────────────
  "simulado": [

    {
      "numero": 1,
      "tipo": "conceitual",
      "enunciado":
        "Explique a diferenca entre alocacao de memoria na stack e no heap em C. "
        "Por que estruturas de dados dinamicas (listas, arvores) usam heap e nao stack? "
        "O que acontece se voce esquecer de chamar free() em um no alocado com malloc()?",
      "gabarito":
        "Stack: memoria alocada automaticamente para variaveis locais, liberada ao sair do "
        "escopo da funcao. Tamanho fixo e limitado (~1-8 MB tipicamente). Heap: alocacao manual "
        "via malloc/calloc, persiste alem do escopo da funcao, tamanho limitado pela memoria "
        "disponivel. Estruturas dinamicas precisam de heap porque: (1) tamanho nao e conhecido "
        "em tempo de compilacao; (2) nos precisam sobreviver alem da funcao que os criou; "
        "(3) a lista pode crescer/encolher em runtime. Sem free(): memory leak — o SO nunca "
        "recupera a memoria ate o processo terminar. Em programas longos, isso exaure a RAM."
    },

    {
      "numero": 2,
      "tipo": "codigo",
      "enunciado":
        "O codigo abaixo contem um bug grave envolvendo ponteiros. Identifique o problema "
        "e reescreva a funcao corretamente.\n\n"
        "No* criar_no(int valor) {\n"
        "    No no;              // declarado na stack!\n"
        "    no.dado    = valor;\n"
        "    no.proximo = NULL;\n"
        "    return &no;         // retorna endereco de variavel local\n"
        "}\n\n"
        "// Chamada: No *novo = criar_no(42);\n"
        "//          novo->dado = ???   // comportamento indefinido",
      "gabarito":
        "Bug: a funcao retorna o endereco de uma variavel local (no stack). Ao retornar, "
        "o frame da funcao e destruido e aquela memoria pode ser sobrescrita a qualquer momento. "
        "Acessar novo->dado e comportamento indefinido (undefined behavior) — o programa pode "
        "parecer funcionar ou crashar aleatoriamente. Correcao:\n"
        "No* criar_no(int valor) {\n"
        "    No *no = malloc(sizeof(No));  // aloca no heap\n"
        "    if (no == NULL) return NULL;\n"
        "    no->dado    = valor;\n"
        "    no->proximo = NULL;\n"
        "    return no;  // retorna ponteiro para memoria persistente\n"
        "}"
    },

    {
      "numero": 3,
      "tipo": "conceitual",
      "enunciado":
        "Qual a complexidade de tempo das operacoes abaixo em cada estrutura? "
        "Justifique cada resposta.\n\n"
        "a) Busca de um elemento em lista encadeada simples com N nos.\n"
        "b) Insercao no inicio de uma lista encadeada simples.\n"
        "c) Remocao do primeiro elemento de uma fila com ponteiro de inicio.\n"
        "d) Pop do topo de uma pilha.\n"
        "e) Remocao de um no especifico em lista duplamente encadeada, dado o ponteiro para o no.",
      "gabarito":
        "a) O(n): no pior caso, percorre todos os N nos ate encontrar ou chegar ao NULL. "
        "Nao ha acesso aleatorio (diferente de array). "
        "b) O(1): basta criar o novo no, apontar seu proximo para o inicio atual, e atualizar "
        "o ponteiro de inicio. Nenhum percurso necessario. "
        "c) O(1): o ponteiro inicio ja aponta para o primeiro no. Basta salvar o valor, "
        "avancas o inicio para o proximo, e liberar o no removido. "
        "d) O(1): o ponteiro topo ja aponta para o elemento a remover. "
        "e) O(1): com o ponteiro no no, ajusta-se apenas os 4 ponteiros vizinhos "
        "(anterior->proximo e proximo->anterior). Sem necessidade de percurso."
    },

    {
      "numero": 4,
      "tipo": "raciocinio",
      "enunciado":
        "Trace a execucao da funcao potencia(3, 3) mostrando o estado da call stack "
        "em cada chamada recursiva. Qual e o valor retornado? "
        "Identifique o caso base e o caso recursivo na funcao abaixo:\n\n"
        "long long potencia(long long base, int exp) {\n"
        "    if (exp == 0) return 1;\n"
        "    return base * potencia(base, exp - 1);\n"
        "}",
      "gabarito":
        "Caso base: exp == 0, retorna 1 (sem chamada recursiva). "
        "Caso recursivo: retorna base * potencia(base, exp-1). "
        "Trace de potencia(3, 3): "
        "potencia(3,3) -> 3 * potencia(3,2) "
        "potencia(3,2) -> 3 * potencia(3,1) "
        "potencia(3,1) -> 3 * potencia(3,0) "
        "potencia(3,0) -> retorna 1 (caso base). "
        "Desfazendo: potencia(3,1)=3*1=3; potencia(3,2)=3*3=9; potencia(3,3)=3*9=27. "
        "Resultado final: 27. A call stack cresce 4 frames (potencia 3,2,1,0) e depois "
        "desempilha retornando o resultado acumulado."
    },

    {
      "numero": 5,
      "tipo": "codigo",
      "enunciado":
        "Implemente a funcao lista_buscar para uma lista encadeada simples de inteiros. "
        "A funcao deve retornar o ponteiro para o no que contem o valor buscado, ou NULL "
        "se nao encontrar. Use a struct abaixo:\n\n"
        "typedef struct No { int dado; struct No *proximo; } No;\n"
        "typedef struct   { No *inicio; } Lista;\n\n"
        "No* lista_buscar(Lista *lista, int valor);",
      "gabarito":
        "No* lista_buscar(Lista *lista, int valor) {\n"
        "    No *atual = lista->inicio;\n"
        "    while (atual != NULL) {\n"
        "        if (atual->dado == valor) return atual;  // encontrou\n"
        "        atual = atual->proximo;\n"
        "    }\n"
        "    return NULL;  // nao encontrado\n"
        "}\n"
        "Complexidade: O(n) — percorre no maximo N nos. Nao ha como fazer melhor em "
        "lista encadeada pois nao ha acesso por indice (diferente de array, onde busca binaria "
        "seria O(log n))."
    },

    {
      "numero": 6,
      "tipo": "conceitual",
      "enunciado":
        "Qual estrutura de dados voce usaria para cada cenario abaixo? Justifique.\n\n"
        "a) Sistema de desfazer/refazer (Ctrl+Z / Ctrl+Y) de um editor de texto.\n"
        "b) Fila de processos prontos no escalonador Round-Robin de um SO.\n"
        "c) Armazenar o historico de paginas de um browser com navegacao voltar/avancar.\n"
        "d) Verificar se uma expressao '({[]})' tem parenteses balanceados.",
      "gabarito":
        "a) Duas pilhas (LIFO): uma para acoes feitas (Ctrl+Z faz pop), outra para desfeitas "
        "(Ctrl+Y faz pop da segunda e push na primeira). LIFO e natural pois desfazemos na "
        "ordem inversa de execucao. "
        "b) Fila circular (FIFO): cada processo entra no fim e sai do inicio. Apos usar seu "
        "quantum, volta ao fim. FIFO garante fairness (ordem de chegada). "
        "c) Lista duplamente encadeada: botao Voltar = anterior, botao Avancar = proximo. "
        "Insercao de nova pagina = inserir apos posicao atual e descartar o resto. "
        "d) Pilha: para cada abre-parentese push; para cada fecha-parentese, pop e verifica "
        "se corresponde. Ao final, pilha deve estar vazia. O(n) tempo, O(n) espaco."
    },

    {
      "numero": 7,
      "tipo": "multipla",
      "enunciado":
        "Sobre lista encadeada simples versus array de tamanho fixo, qual afirmativa e CORRETA?\n\n"
        "a) Array tem insercao no inicio O(1) pois basta atualizar um indice.\n"
        "b) Lista encadeada tem acesso ao elemento do meio em O(1) via aritmetica de ponteiros.\n"
        "c) Array ocupa menos memoria por elemento pois nao armazena ponteiros.\n"
        "d) Lista encadeada e mais eficiente que array para acesso sequencial em todos os casos.\n"
        "e) Remover o ultimo elemento de uma lista encadeada simples e O(1) com ponteiro para o fim.",
      "gabarito":
        "Alternativa CORRETA: c. Array armazena apenas os dados, sem overhead de ponteiros. "
        "Lista encadeada armazena dado + 1 ponteiro (simples) ou dado + 2 ponteiros (dupla) por no. "
        "a) ERRADA: insercao no inicio de array e O(n) pois requer shift de todos os elementos. "
        "b) ERRADA: lista encadeada e O(n) para acessar elemento do meio — sem aritmetica de ponteiros. "
        "d) ERRADA: array tem melhor localidade de cache para acesso sequencial (elementos contiguos na RAM). "
        "e) ERRADA: remover o ultimo numa lista simples e O(n) — precisa percorrer ate o penultimo "
        "para atualizar o ponteiro fim (sem ponteiro anterior disponivel)."
    },

    {
      "numero": 8,
      "tipo": "raciocinio",
      "enunciado":
        "Dado o codigo abaixo que opera sobre uma pilha, qual o valor impresso pelo printf final? "
        "Trace a execucao passo a passo mostrando o estado da pilha apos cada operacao.\n\n"
        "Pilha *p = criarPilha();\n"
        "Push(p, \"MS\");\n"
        "Push(p, \"DF\");\n"
        "Push(p, \"RJ\");\n"
        "Push(p, \"PR\");\n"
        "char *t = Top(p);\n"
        "Push(p, Pop(p));\n"
        "Push(p, \"SP\");\n"
        "Push(p, Top(p));\n"
        "Pop(p);\n"
        "Pop(p);\n"
        "printf(\"%s\\n\", Top(p));",
      "gabarito":
        "Trace passo a passo: "
        "Push MS -> [MS]. "
        "Push DF -> [DF, MS]. "
        "Push RJ -> [RJ, DF, MS]. "
        "Push PR -> [PR, RJ, DF, MS]. "
        "Top(p) = PR (nao remove). "
        "Pop(p) = PR, depois Push(PR) -> [PR, RJ, DF, MS] (estado inalterado). "
        "Push SP -> [SP, PR, RJ, DF, MS]. "
        "Top(p) = SP, Push(SP) -> [SP, SP, PR, RJ, DF, MS]. "
        "Pop(p) remove SP -> [SP, PR, RJ, DF, MS]. "
        "Pop(p) remove SP -> [PR, RJ, DF, MS]. "
        "Top(p) = PR. "
        "printf imprime: PR"
    },

  ]  # fim simulado
}  # fim dados


if __name__ == "__main__":
    caminho = gerar_pdf(dados, "estrutura-de-dados/resumo-prova-ed.pdf")
    print(f"PDF gerado: {caminho}")