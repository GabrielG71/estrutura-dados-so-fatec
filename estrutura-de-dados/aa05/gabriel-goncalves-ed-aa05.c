#include <stdio.h>

// Calcula base elevado ao expoente de forma recursiva
unsigned long potencia(unsigned long base, unsigned long expoente) {
    // Caso base: qualquer número elevado a 0 é 1
    if (expoente == 0) {
        return 1;
    }
    return base * potencia(base, expoente - 1);
}

int main() {
    unsigned long base, expoente, resultado;

    printf("Informe a base (inteiro positivo): ");
    scanf("%lu", &base);

    printf("Informe o expoente (inteiro positivo): ");
    scanf("%lu", &expoente);

    resultado = potencia(base, expoente);

    printf("\nResultado: %lu^%lu = %lu\n", base, expoente, resultado);

    return 0;
}