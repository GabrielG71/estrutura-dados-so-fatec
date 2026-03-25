#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct No {
    char dado[3];
    struct No *proximo;
} No;

typedef struct Pilha {
    No *topo;
    int tamanho;
} Pilha;

Pilha *criarPilha(void) {
    Pilha *pilha = (Pilha *)malloc(sizeof(Pilha));
    if (pilha == NULL) return NULL;
    pilha->topo    = NULL;
    pilha->tamanho = 0;
    return pilha;
}

int pilhaVazia(Pilha *pilha) {
    return (pilha->topo == NULL);
}

void Push(Pilha *pilha, const char *uf) {
    No *novoNo = (No *)malloc(sizeof(No));
    if (novoNo == NULL) return;

    strncpy(novoNo->dado, uf, 2);
    novoNo->dado[2]  = '\0';
    novoNo->proximo  = pilha->topo;
    pilha->topo      = novoNo;
    pilha->tamanho++;
}

char *Pop(Pilha *pilha) {
    if (pilhaVazia(pilha)) return NULL;

    No *noRemovido = pilha->topo;
    static char valor[3];
    strncpy(valor, noRemovido->dado, 3);

    pilha->topo = pilha->topo->proximo;
    free(noRemovido);
    pilha->tamanho--;

    return valor;
}

char *Top(Pilha *pilha) {
    if (pilhaVazia(pilha)) return NULL;
    return pilha->topo->dado;
}

void liberarPilha(Pilha *pilha) {
    while (!pilhaVazia(pilha)) Pop(pilha);
    free(pilha);
}

int main(void) {
    Pilha *pilha = criarPilha();

    Push(pilha, "MS");
    Push(pilha, "DF");
    Push(pilha, "RJ");
    Push(pilha, "PR");
    Top(pilha);
    Push(pilha, Pop(pilha));
    Push(pilha, "SP");
    Push(pilha, Top(pilha));
    Pop(pilha);
    Pop(pilha);

    printf("O elemento no topo da pilha: %s\n", Top(pilha));

    liberarPilha(pilha);
    return EXIT_SUCCESS;
}