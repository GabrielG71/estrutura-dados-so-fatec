#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TOTAL_NUMEROS 15
#define MIN 1
#define MAX 25

// Função que gera um número aleatório no intervalo [MIN, MAX].
int gerarNumeroAleatorio() {
    return (rand() % (MAX - MIN + 1)) + MIN;
}

// Função que mostra na telinha o vetor com os números sorteados.
void imprimirVetor(int v[], int n) {
    int i;

    printf("Sorteio Lotofácil\n");

    for (i = 0; i < n; i++) {
        // Formata com 2 dígitos (01, 02, 03...) pra ficar com vibe de loteria tlgd?.
        printf("%02d", v[i]);

        if (i < n - 1) {
            printf(" - ");
        } // Enfeite
    }
}

int main() {
    int sorteio[TOTAL_NUMEROS];
    int i, j;
    int numero;
    int repetido;

    // Seed do rand: sem isso, ele só tende a repetir a mesma sequência.
    srand((unsigned)time(NULL));

    // Preenche o vetor com 15 números aleatórios sem repetir.
    i = 0;
    while (i < TOTAL_NUMEROS) {
        numero = gerarNumeroAleatorio();

        // Checa se esse número já existe no vetor.
        repetido = 0;
        for (j = 0; j < i; j++) {
            if (sorteio[j] == numero) {
                repetido = 1;
                break;
            }
        }

        // Se não for repetido, coloca no vetor e avança.
        if (!repetido) {
            sorteio[i] = numero;
            i++;
        }
        // Se for repetido, ignora e gera outro (como se a bola já tivesse saído).
    }

    // Resultado final do sorteio.
    imprimirVetor(sorteio, TOTAL_NUMEROS);

    return 0;
}