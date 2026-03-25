#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    char dado;
    struct No* proximo;
} No;

typedef struct {
    No* inicio;
    No* fim;
} Lista;

void criar_lista(Lista* lista) {
    lista->inicio = NULL;
    lista->fim = NULL;
}

int esta_vazia(Lista* lista) {
    return lista->inicio == NULL;
}

// Insere no final da lista
void inserir(Lista* lista, char c) {
    No* novo = (No*) malloc(sizeof(No));
    novo->dado = c;
    novo->proximo = NULL;

    if (esta_vazia(lista)) {
        lista->inicio = novo;
        lista->fim = novo;
    } else {
        lista->fim->proximo = novo;
        lista->fim = novo;
    }
}

// Pesquisa um caractere, imprime Encontrado ou Nao Encontrado
void pesquisar(Lista* lista, char c) {
    No* atual = lista->inicio;
    while (atual != NULL) {
        if (atual->dado == c) {
            printf("Pesquisa '%c': Encontrado\n", c);
            return;
        }
        atual = atual->proximo;
    }
    printf("Pesquisa '%c': Nao Encontrado\n", c);
}

// Remove o primeiro elemento da lista
void remover_primeiro(Lista* lista) {
    if (esta_vazia(lista)) {
        printf("Lista vazia, nada a remover.\n");
        return;
    }
    No* temp = lista->inicio;
    lista->inicio = lista->inicio->proximo;
    if (lista->inicio == NULL)
        lista->fim = NULL;
    free(temp);
}

// Remove a primeira ocorrencia do caractere informado
void remover(Lista* lista, char c) {
    if (esta_vazia(lista)) return;

    // Caso o elemento esteja no inicio
    if (lista->inicio->dado == c) {
        remover_primeiro(lista);
        return;
    }

    No* anterior = lista->inicio;
    No* atual = lista->inicio->proximo;
    while (atual != NULL) {
        if (atual->dado == c) {
            anterior->proximo = atual->proximo;
            if (atual == lista->fim)
                lista->fim = anterior;
            free(atual);
            return;
        }
        anterior = atual;
        atual = atual->proximo;
    }
}

void imprimir(Lista* lista) {
    if (esta_vazia(lista)) {
        printf("A lista esta vazia!\n");
        return;
    }
    No* atual = lista->inicio;
    while (atual != NULL) {
        printf("%c", atual->dado);
        if (atual->proximo != NULL)
            printf(" -> ");
        atual = atual->proximo;
    }
    printf("\n");
}

// Libera todos os nos da lista
void destruir(Lista* lista) {
    No* atual = lista->inicio;
    while (atual != NULL) {
        No* temp = atual;
        atual = atual->proximo;
        free(temp);
    }
    lista->inicio = NULL;
    lista->fim = NULL;
}

int main() {
    Lista lista;

    criar_lista(&lista);

    // Lista vazia
    imprimir(&lista);

    // Inserindo caracteres do nome
    char nome[] = "Wellington";
    for (int i = 0; nome[i] != '\0'; i++)
        inserir(&lista, nome[i]);

    // Lista completa
    imprimir(&lista);

    // Pesquisa
    pesquisar(&lista, 'W');
    pesquisar(&lista, 'z');

    // Remove o primeiro elemento
    remover_primeiro(&lista);
    imprimir(&lista);

    // Remove vogais
    char vogais[] = {'a', 'e', 'i', 'o', 'u'};
    for (int i = 0; i < 5; i++)
        remover(&lista, vogais[i]);
    imprimir(&lista);

    destruir(&lista);

    return 0;
}