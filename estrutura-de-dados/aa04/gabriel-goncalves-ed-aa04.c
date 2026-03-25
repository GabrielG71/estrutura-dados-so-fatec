#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

// Tipo personalizado: duploLong (dois long para representar número de 10 dígitos)
typedef struct {
    long parte1;
    long parte2;
} duploLong;

// Estrutura do Produto
typedef struct {
    duploLong codigo;
    double preco;
} Produto;

// Estrutura do Item de Estoque
typedef struct {
    Produto produto;
    int quantidade;
    int quantidadeMinima;
} ItemEstoque;

// Função: verifica se o item está acabando
bool itemAcabando(ItemEstoque item) {
    return item.quantidade <= item.quantidadeMinima;
}

// Função: verifica se o estoque está vazio
bool estoqueVazio(ItemEstoque inventario[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        if (inventario[i].quantidade > 0) {
            return false;
        }
    }
    return true;
}

// Função auxiliar para imprimir o código duploLong
void imprimirCodigo(duploLong codigo) {
    printf("%ld%ld", codigo.parte1, codigo.parte2);
}

int main() {
    srand(time(NULL));

    // Vetor de itens de estoque (até 5 itens)
    ItemEstoque inventario[5];

    // Produto 1
    Produto prod1;
    prod1.codigo.parte1 = 11111;
    prod1.codigo.parte2 = 11111;
    prod1.preco = 10.01;
    inventario[0].produto = prod1;
    inventario[0].quantidade = (rand() % 10) + 1;       // entre 1 e 10
    inventario[0].quantidadeMinima = (rand() % 5) + 1;  // entre 1 e 5

    // Produto 2
    Produto prod2;
    prod2.codigo.parte1 = 22222;
    prod2.codigo.parte2 = 22222;
    prod2.preco = 22.22;
    inventario[1].produto = prod2;
    inventario[1].quantidade = 32;
    inventario[1].quantidadeMinima = 16;

    // Produto 3
    Produto prod3;
    prod3.codigo.parte1 = 12345;
    prod3.codigo.parte2 = 67890;
    prod3.preco = 98.76;
    inventario[2].produto = prod3;
    inventario[2].quantidade = 333;
    inventario[2].quantidadeMinima = 333;

    int totalItens = 3;

    // Verifica se o estoque está vazio antes de imprimir
    if (estoqueVazio(inventario, totalItens)) {
        printf("Estoque vazio!\n");
        return 0;
    }

    // Impressão do inventário
    for (int i = 0; i < totalItens; i++) {
        printf("Produto: ");
        imprimirCodigo(inventario[i].produto.codigo);
        printf(" (R$ %.2f) Estoque: %3d.", inventario[i].produto.preco, inventario[i].quantidade);
        if (itemAcabando(inventario[i])) {
            printf(" [ESTA ACABANDO]");
        }
        printf("\n");
    }

    return 0;
}