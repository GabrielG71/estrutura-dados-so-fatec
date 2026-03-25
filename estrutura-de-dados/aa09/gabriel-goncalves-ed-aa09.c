#include <stdio.h>
#include <stdlib.h>

typedef struct promocao {
    int   cod_produto;
    float desconto;
} Promo;

typedef struct no {
    Promo       dado;
    struct no  *anterior;
    struct no  *proximo;
} No;

typedef struct {
    No  *inicio;
    No  *fim;
    int  tamanho;
} Lista;

Lista *criarLista() {
    Lista *lista   = malloc(sizeof(Lista));
    lista->inicio  = NULL;
    lista->fim     = NULL;
    lista->tamanho = 0;
    return lista;
}

int estaVazia(Lista *lista) {
    return lista->inicio == NULL;
}

No *criarNo(int cod, float desconto) {
    No *novo               = malloc(sizeof(No));
    novo->dado.cod_produto = cod;
    novo->dado.desconto    = desconto;
    novo->anterior         = NULL;
    novo->proximo          = NULL;
    return novo;
}

void inserirElemento(Lista *lista, int cod, float desconto) {
    No *novo = criarNo(cod, desconto);

    if (estaVazia(lista)) {
        novo->proximo   = novo;
        novo->anterior  = novo;
        lista->inicio   = novo;
        lista->fim      = novo;
    } else {
        novo->anterior          = lista->fim;
        novo->proximo           = lista->inicio;
        lista->fim->proximo     = novo;
        lista->inicio->anterior = novo;
        lista->fim              = novo;
    }

    lista->tamanho++;
    printf("Produto %d inserido (desconto: %.2f%%)\n", cod, desconto);
}

No *pesquisarElemento(Lista *lista, int cod) {
    if (estaVazia(lista)) return NULL;

    No *atual = lista->inicio;
    do {
        if (atual->dado.cod_produto == cod) return atual;
        atual = atual->proximo;
    } while (atual != lista->inicio);

    return NULL;
}

void removerElemento(Lista *lista, int cod) {
    No *alvo = pesquisarElemento(lista, cod);

    if (alvo == NULL) {
        printf("Produto %d nao encontrado.\n", cod);
        return;
    }

    if (lista->tamanho == 1) {
        lista->inicio = NULL;
        lista->fim    = NULL;
    } else {
        alvo->anterior->proximo = alvo->proximo;
        alvo->proximo->anterior = alvo->anterior;
        if (alvo == lista->inicio) lista->inicio = alvo->proximo;
        if (alvo == lista->fim)    lista->fim    = alvo->anterior;
    }

    printf("Produto %d removido.\n", alvo->dado.cod_produto);
    free(alvo);
    lista->tamanho--;
}

void imprimirLista(Lista *lista) {
    if (estaVazia(lista)) {
        printf("Lista vazia.\n");
        return;
    }

    printf("Lista (inicio -> fim):\n");
    No *atual = lista->inicio;
    do {
        printf("Cod: %d | Desconto: %.2f%%\n",
               atual->dado.cod_produto,
               atual->dado.desconto);
        atual = atual->proximo;
    } while (atual != lista->inicio);
}

void imprimirListaInversa(Lista *lista) {
    if (estaVazia(lista)) {
        printf("Lista vazia.\n");
        return;
    }

    printf("Lista (fim -> inicio):\n");
    No *atual = lista->fim;
    do {
        printf("Cod: %d | Desconto: %.2f%%\n",
               atual->dado.cod_produto,
               atual->dado.desconto);
        atual = atual->anterior;
    } while (atual != lista->fim);
}

No *buscarMaiorDesconto(Lista *lista) {
    if (estaVazia(lista)) return NULL;

    No *maior = lista->inicio;
    No *atual = lista->inicio->proximo;

    while (atual != lista->inicio) {
        if (atual->dado.desconto > maior->dado.desconto) maior = atual;
        atual = atual->proximo;
    }

    return maior;
}

No *buscarMenorDesconto(Lista *lista) {
    if (estaVazia(lista)) return NULL;

    No *menor = lista->inicio;
    No *atual = lista->inicio->proximo;

    while (atual != lista->inicio) {
        if (atual->dado.desconto < menor->dado.desconto) menor = atual;
        atual = atual->proximo;
    }

    return menor;
}

void destruirLista(Lista *lista) {
    if (estaVazia(lista)) {
        free(lista);
        return;
    }

    No *atual     = lista->inicio;
    No *proximo;
    lista->fim->proximo = NULL;

    while (atual != NULL) {
        proximo = atual->proximo;
        free(atual);
        atual = proximo;
    }

    free(lista);
    printf("Lista destruida.\n");
}

void exibirResultadoPesquisa(No *no, int cod) {
    if (no != NULL)
        printf("Encontrado -> Cod: %d | Desconto: %.2f%%\n",
               no->dado.cod_produto, no->dado.desconto);
    else
        printf("Produto %d nao encontrado.\n", cod);
}

void exibirMenuOpcoes() {
    printf("\n1. Inserir produto\n");
    printf("2. Pesquisar produto\n");
    printf("3. Remover produto\n");
    printf("4. Imprimir lista\n");
    printf("5. Imprimir lista inversa\n");
    printf("6. Verificar se esta vazia\n");
    printf("7. Maior desconto\n");
    printf("8. Menor desconto\n");
    printf("9. Destruir lista\n");
    printf("0. Sair\n");
    printf("Opcao: ");
}

int main() {
    Lista *lista = criarLista();
    int    opcao, cod;
    float  desconto;

    do {
        exibirMenuOpcoes();
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Codigo do produto: ");
                scanf("%d", &cod);
                printf("Desconto (%%): ");
                scanf("%f", &desconto);
                inserirElemento(lista, cod, desconto);
                break;

            case 2:
                printf("Codigo do produto: ");
                scanf("%d", &cod);
                exibirResultadoPesquisa(pesquisarElemento(lista, cod), cod);
                break;

            case 3:
                printf("Codigo do produto: ");
                scanf("%d", &cod);
                removerElemento(lista, cod);
                break;

            case 4:
                imprimirLista(lista);
                break;

            case 5:
                imprimirListaInversa(lista);
                break;

            case 6:
                printf(estaVazia(lista) ? "Lista esta vazia.\n" : "Lista possui elementos.\n");
                break;

            case 7: {
                No *maior = buscarMaiorDesconto(lista);
                if (maior) printf("Maior desconto -> Cod: %d | %.2f%%\n",
                                  maior->dado.cod_produto, maior->dado.desconto);
                else       printf("Lista vazia.\n");
                break;
            }

            case 8: {
                No *menor = buscarMenorDesconto(lista);
                if (menor) printf("Menor desconto -> Cod: %d | %.2f%%\n",
                                  menor->dado.cod_produto, menor->dado.desconto);
                else       printf("Lista vazia.\n");
                break;
            }

            case 9:
                destruirLista(lista);
                lista = criarLista();
                break;

            case 0:
                destruirLista(lista);
                printf("Encerrando.\n");
                break;

            default:
                printf("Opcao invalida.\n");
        }

    } while (opcao != 0);

    return 0;
}