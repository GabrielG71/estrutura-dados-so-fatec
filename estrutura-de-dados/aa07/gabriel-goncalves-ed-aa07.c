#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int dado;
    struct No *proximo;
} No;

typedef struct Fila {
    No *inicio;
    No *fim;
    int tamanho;
} Fila;

Fila *criarFila(void) {
    Fila *fila = (Fila *)malloc(sizeof(Fila));
    if (fila == NULL) return NULL;
    fila->inicio  = NULL;
    fila->fim     = NULL;
    fila->tamanho = 0;
    return fila;
}

int filaVazia(Fila *fila) {
    return (fila->inicio == NULL);
}

void enfileirar(Fila *fila, int valor) {
    No *novoNo = (No *)malloc(sizeof(No));
    if (novoNo == NULL) return;

    novoNo->dado    = valor;
    novoNo->proximo = NULL;

    if (filaVazia(fila)) {
        fila->inicio = novoNo;
        fila->fim    = novoNo;
    } else {
        fila->fim->proximo = novoNo;
        fila->fim          = novoNo;
    }

    fila->tamanho++;
}

int desenfileirar(Fila *fila) {
    if (filaVazia(fila)) return -1;

    No *noRemovido    = fila->inicio;
    int valorRemovido = noRemovido->dado;

    fila->inicio = fila->inicio->proximo;
    if (fila->inicio == NULL) fila->fim = NULL;

    free(noRemovido);
    fila->tamanho--;

    return valorRemovido;
}

void exibirFila(Fila *fila) {
    if (filaVazia(fila)) {
        printf("Fila vazia.\n");
        return;
    }

    No *atual = fila->inicio;
    while (atual != NULL) {
        printf("%d", atual->dado);
        if (atual->proximo != NULL) printf(" -> ");
        atual = atual->proximo;
    }
    printf("\n");
}

void liberarFila(Fila *fila) {
    No *atual = fila->inicio;
    while (atual != NULL) {
        No *proximo = atual->proximo;
        free(atual);
        atual = proximo;
    }
    free(fila);
}

int main(void) {
    Fila *fila = criarFila();

    enfileirar(fila, 10);
    enfileirar(fila, 20);
    enfileirar(fila, 30);
    enfileirar(fila, 40);
    enfileirar(fila, 50);

    exibirFila(fila);

    printf("Removido: %d\n", desenfileirar(fila));
    printf("Removido: %d\n", desenfileirar(fila));

    exibirFila(fila);

    liberarFila(fila);
    return EXIT_SUCCESS;
}