#include <stdio.h>
#include <locale.h>

#define MIN_N 8
#define MAX_N 100

// Função que mostra o menu sempre antes de pedir uma opção.
void menu() {
    printf("Seja bem-vindo ao sistema de Média & Variância!\n");
    printf("Escolha uma das opções abaixo:\n");
    printf("1. Informar números\n");
    printf("2. Calcular média e variância\n");
    printf("0. Sair do programa\n");
}

// Lê N números reais e armazena no vetor.
// Retorna 1 se deu certo, 0 se o usuário digitou um N inválido.
int informarNumeros(double v[], int *n) {
    int i;

    printf("\nQuantos números você quer em? (mínimo %d, máximo %d): ", MIN_N, MAX_N);
    scanf("%d", n);

    if (*n < MIN_N || *n > MAX_N) {
        printf("Quantidade inválida. Escolha entre %d e %d.\n", MIN_N, MAX_N);
        return 0;
    }

    printf("Boa! Agora digite %d números reais (pode usar decimal tipo 2.5):\n", *n);

    for (i = 0; i < *n; i++) {
        printf("Número %d: ", i + 1);
        scanf("%lf", &v[i]);
    }

    printf("Boa! Números armazenados com sucesso.\n");
    return 1;
}

// Calcula a média do vetor.
double calcularMedia(double v[], int n) {
    int i;
    double soma = 0.0;

    for (i = 0; i < n; i++) {
        soma += v[i];
    }

    return soma / n;
}

// Calcula a variância populacional do vetor:
double calcularVariancia(double v[], int n, double media) {
    int i;
    double somaQuadrados = 0.0;
    double diff;

    for (i = 0; i < n; i++) {
        diff = v[i] - media;
        somaQuadrados += diff * diff;
    }

    return somaQuadrados / n;
}

// Apenas para exibir os números que estão sendo usados nas conta.
void mostrarVetor(double v[], int n) {
    int i;
    printf("Números atuais no vetor: ");
    for (i = 0; i < n; i++) {
        printf("%.2f", v[i]);
        if (i < n - 1) printf(", ");
    }
    printf("\n");
}

int main() {
    setlocale(LC_ALL, ""); // Para ter acentos.

    double numeros[MAX_N]; // Vetor para guardar os números.
    int n = 0;             // Quantos números falou que vai usar.
    int opcao = -1;        // Opção do menu.
    int jaTemNumeros = 0;  // Flag para saber se o usuário já informou números.

    while (opcao != 0) { // O programa roda até ele escolher sair.
        menu();

        printf("Digite a opção que você quer: ");
        scanf("%d", &opcao);

        if (opcao == 1) {
            // Opção 1: Informar números
            jaTemNumeros = informarNumeros(numeros, &n);

        } else if (opcao == 2) {
            // Opção 2: Calcular média e variância
            if (!jaTemNumeros) {
                printf("\nCalma lá! Antes de calcular, você precisa informar os números (opção 1).\n");
            } else {
                double media = calcularMedia(numeros, n);
                double variancia = calcularVariancia(numeros, n, media);

                printf("\nResultados:\n");
                mostrarVetor(numeros, n);
                printf("Média: %.4f\n", media);
                printf("Variância: %.4f\n", variancia);
            }

        } else if (opcao == 0) {
            // Opção 0: Sair
            printf("\nSaindo do programa... valeu!\n");

        } else {
            // Qualquer outra coisa: inválido
            printf("\nOpção inválida! Tente 0, 1 ou 2.\n");
        }
    }

    return 0;
}